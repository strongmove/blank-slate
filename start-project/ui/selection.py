class Selection:
    def __init__(self, name, description, item=None, default=False):
        self.name = name
        self.description = description
        self.selected = default
        self.item = item

    def toggle(self):
        self.selected = not self.selected

    def __str__(self):
        return f"{self.name}"


class Selections:
    def __init__(self, selections):
        self.selections = selections

    def selected(self):
        return [s for s in self.selections if s.selected]

    def __iter__(self):
        return iter(self.selections)

    def __getitem__(self, index):
        return self.selections[index]

    def __len__(self):
        return len(self.selections)

    def __str__(self):
        return "\n".join([str(s) for s in self.selections])
