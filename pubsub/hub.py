"""
Hub is a central point that maintains a set of subscribers,
thus decouples publisher from subscribers
Hub does job of pushing message to each subscriber when publisher publishes
"""


class Hub:

    def __init__(self):
        self.subscriptions = set()

    def push(self, message):
        for queue in self.subscriptions:
            queue.put_nowait(message)
