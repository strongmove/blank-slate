# python (wget -qO - https://raw.githubusercontent.com/strongmove/blank-slate/main/create-next-app.py | psub)

from subprocess import run

DEFI = {
    "nextjs": {
        "prompt": {"type": "confirm", "name": "nextjs", "default": "y"},
        "actions": [lambda: "pnpm create next-app --ts ."],
    },
    "xstate": {
        "prompt": {"type": "confirm", "name": "xstate", "default": "y"},
        "actions": [lambda: "pnpm add xstate @xstate/react"],
    },
    "shadcn-ui@latest": {
        "prompt": {"type": "confirm", "name": "shadcn-ui@latest", "default": "y"},
        "actions": [
            lambda: "pnpm dlx shadcn-ui@latest init",
            lambda: "pnpm dlx shadcn-ui@latest add",
        ],
    },
    "sass": {
        "prompt": {"type": "confirm", "name": "sass", "default": "y"},
        "actions": [lambda: "pnpm add -D sass"],
    },
    "zod": {
        "prompt": {"type": "confirm", "name": "zod", "default": "y"},
        "actions": [lambda: "pnpm add zod"],
    },
    "react-icons": {
        "prompt": {"type": "confirm", "name": "react-icons", "default": "y"},
        "actions": [lambda: "pnpm add react-icons"],
    },
    "rxjs": {
        "prompt": {"type": "confirm", "name": "rxjs", "default": "y"},
        "actions": [lambda: "pnpm add rxjs"],
    },
    "markdown": {
        "prompt": {"type": "confirm", "name": "markdown", "default": "y"},
        "actions": [
            lambda: "pnpm add react-markdown",
            lambda: "pnpm add rehype-highlight",
        ],
    },
    "trpc": {
        "prompt": {"type": "confirm", "name": "markdown", "default": "y"},
        "actions": [
            lambda: "pnpm add @trpc/server @trpc/client",
        ],
    },
}


def run_actions(actions):
    for action in actions:
        if type(action) == list:
            run_actions(action)
        else:
            run(action(), shell=True)


def main():
    actions = []
    for name, defi in DEFI.items():
        choice = input(f"{name} (Y/n): ")
        if not choice:
            choice = defi["prompt"]["default"]
        if choice.lower() == "y":
            actions += [defi["actions"]]
    run_actions(actions)


main()
