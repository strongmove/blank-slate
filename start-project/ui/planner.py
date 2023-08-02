import curses
from curses import wrapper

from .selection import Selection, Selections

CHOICE_INDEXES = list("123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ")


def show_options(definition, s, r, c):
    for key, item in definition.items():
        if isinstance(item, Selection):
            color = curses.color_pair(4) if item.selected else curses.color_pair(1)
            s.addstr(r, c, f"{key}) {item}", color)
            r += 1
    s.addstr(
        r,
        c,
        "Press the choice key to toggle a selection, Enter to confirm, q to quit: ",
    )
    s.refresh()


def get_user_selection_with_ui(manifest):
    def _do(s):
        curses.noecho()
        s.clear()
        s.refresh()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        definition = {
            CHOICE_INDEXES[index]: item for index, item in enumerate(manifest)
        }
        counter_win = curses.newwin(20, 100, 0, 1)
        counter_win.clear()
        while True:
            counter_win.refresh()
            show_options(definition, counter_win, 0, 0)

            char = s.getkey()
            if char in definition:
                definition[char].toggle()
            elif char == curses.KEY_ENTER or char == "\n":
                break
            elif char == "q":
                definition = {}
                break

        curses.endwin()
        return Selections(definition.values())

    return wrapper(_do)
