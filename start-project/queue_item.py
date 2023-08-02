class QueueItem:
    def __init__(self, item):
        self.item = item
        self.priority = 0

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        print(f"QueueItem(priority={self.priority}, item={self.item})")

    def __repr__(self):
        print(f"QueueItem(priority={self.priority}, item={self.item})")
