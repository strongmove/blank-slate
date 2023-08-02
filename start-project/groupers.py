from collections import namedtuple

Group = namedtuple("Group", ["name", "items"])

DEFAULT_GROUPS = {
    "PNPM_ADD_DEV": {"priority": 0},
    "PNPM_ADD": {"priority": 1000},
    "NO_GROUP": {"priority": 2000},
}


def group_items(items, groups=DEFAULT_GROUPS):
    """
    Group items by their group name
    """
    res = {}
    for item in items:
        item_type = item.type
        group_name = item_type if item_type in groups else "NO_GROUP"
        if group_name not in res:
            res[group_name] = []
        res[group_name].append(item)
    res = dict(
        sorted(tuple(res.items()), key=lambda x: groups[x[0]]["priority"], reverse=True)
    )
    return res
