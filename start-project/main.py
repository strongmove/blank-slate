import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypedDict

from groupers import group_items
from parsers import parse_items
from queue_item import QueueItem
from queue_runner import QueueRunner
from runnable import ShellRunnable
from ui.planner import get_user_selection_with_ui
from ui.selection import Selection

cwd = Path(__file__).parent

PACKAGE_EXECUTABLE = "bun"


@dataclass
class ManifestShellCommandItem:
    shell_statement: str
    type: Literal["SHELL_COMMAND"] = "SHELL_COMMAND"
    name: str = ""
    description: str = ""
    enable_by_default: bool = False


class ManifestShellCommandItemData(TypedDict):
    type: Literal["SHELL_COMMAND"]
    name: str
    description: str
    shell_statement: str
    enable_by_default: bool


ManifestType = TypedDict(
    "ManifestType",
    {"items": list[ManifestShellCommandItemData] | str},
)


def main():
    with open(cwd / "manifest.json", "r") as f:

        def standardize_manifest_items(items):
            res = []
            for item in items:
                if isinstance(item, str):
                    item = ManifestShellCommandItemData(
                        **{
                            "type": "SHELL_COMMAND",
                            "name": item,
                            "description": "",
                            "shell_statement": item,
                            "enable_by_default": False,
                        }
                    )
                res.append(item)
            return res

        manifest: ManifestType = json.load(f)
        manifest["items"] = standardize_manifest_items(manifest["items"])

    items = [ManifestShellCommandItem(**item) for item in manifest["items"]]
    available_selections = [
        Selection(
            name=item.name,
            description=item.description,
            item=item.shell_statement,
            default=item.enable_by_default,
        )
        for item in items
    ]
    selections = get_user_selection_with_ui(available_selections)
    matches = parse_items([s.item for s in selections if s.selected])
    groups = group_items(matches)
    runner = QueueRunner()
    for group_name, items in groups.items():
        if group_name == "PNPM_ADD":
            args = " ".join([item.args for item in items])
            cmd = f"{PACKAGE_EXECUTABLE} add {args}"
            runner.add(QueueItem(ShellRunnable(cmd)))
        elif group_name == "PNPM_ADD_DEV":
            args = " ".join([item.args for item in items])
            cmd = f"{PACKAGE_EXECUTABLE} add -D {args}"
            runner.add(QueueItem(ShellRunnable(cmd)))
        elif group_name == "BUN_ADD":
            args = " ".join([item.args for item in items])
            cmd = f"{PACKAGE_EXECUTABLE} add {args}"
            runner.add(QueueItem(ShellRunnable(cmd)))
        elif group_name == "BUN_ADD_DEV":
            args = " ".join([item.args for item in items])
            cmd = f"{PACKAGE_EXECUTABLE} add -D {args}"
            runner.add(QueueItem(ShellRunnable(cmd)))
        else:
            for item in items:
                cmd = item.shell_command
                runner.add(QueueItem(ShellRunnable(cmd)))
    runner.run()


if __name__ == "__main__":
    main()
