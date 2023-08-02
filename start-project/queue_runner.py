from collections import deque


class QueueRunner:
    def __init__(self):
        self.queue = deque([])
        self.running = False

    def add(self, item):
        self.queue.append(item)

    def run(self):
        self.running = True
        while self.running:
            try:
                queue_item = self.queue.popleft()
                print("queue item is ", queue_item.item)
                queue_item.item.run()
            except IndexError:
                self.stop()

    def sort(self):
        self.queue = deque(sorted(self.queue, reverse=True))

    def stop(self):
        self.running = False

    def print_items(self):
        for item in self.queue:
            print(f"Item {item} with priority of {item.priority}")
