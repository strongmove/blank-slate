import re
from collections import namedtuple

Item = namedtuple("Item", ["type", "args", "shell_command"])

default_parsers = {}


def register_parser(parser):
    def _register(func):
        default_parsers[parser] = func
        return func

    return _register


# Register parser in the order of specificity


@register_parser("PNPM_DLX")
def parse_pnpm_dlx(string: str):
    pattern = re.compile(r"pnpm (dlx) (?P<args>.*$)")
    item_type = "PNPM_DLX"
    if match := pattern.match(string):
        return Item(item_type, match.group("args"), f"pnpm dlx {match.group('args')}")


@register_parser("PNPM_CREATE")
def parse_pnpm_create(string: str):
    pattern = re.compile(r"pnpm (create) (?P<args>.*$)")
    item_type = "PNPM_CREATE"
    if match := pattern.match(string):
        return Item(
            item_type, match.group("args"), f"pnpm create {match.group('args')}"
        )


# PNPM_ADD_DEV is more specific than PNPM_ADD
@register_parser("PNPM_ADD_DEV")
def parse_pnpm_add_dev(string: str):
    pattern = re.compile(r"pnpm (add) (-D) (?P<args>.*$)")
    item_type = "PNPM_ADD_DEV"
    if match := pattern.match(string):
        return Item(item_type, match.group("args"), None)


@register_parser("PNPM_ADD")
def parse_pnpm_add(string: str):
    pattern = re.compile(r"pnpm (add) (?P<args>.*$)")
    item_type = "PNPM_ADD"
    if match := pattern.match(string):
        return Item(item_type, match.group("args"), None)


def match_first_valid(string: str, parsers=default_parsers):
    for _, parse in parsers.items():
        if match := parse(string):
            return match


def parse_items(items, parsers=default_parsers):
    parsed_items = []
    for item in items:
        if match := match_first_valid(item, parsers):
            parsed_items.append(match)
    return parsed_items


def parse_manifest(manifest, parsers=default_parsers):
    items = manifest["items"]
    return parse_items(items, parsers)
