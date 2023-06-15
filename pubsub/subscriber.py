"""
Each subscriber maintains an async queue which holds messages being published.
It registers itself to the hub.
Reading from queue is asynchronous so that while the subscriber is waiting for message to be available,
other tasks can be picked up.
Reading loop is running until receives the  message 'TERMINATE'.
Once terminated, it removes its queue from hub
"""

import asyncio
import random


class Subscriber:

    def __init__(self, hub, sub_id):
        self.hub = hub
        self.id = sub_id
        self.queue = asyncio.Queue()

    @property
    def subscribe(self):
        self.hub.subscriptions.add(self.queue)
        return self.queue

    def unsubscribe(self):
        self.hub.subscriptions.discard(self.queue)

    @staticmethod
    async def read(self):
        queue = self.subscribe
        await asyncio.sleep(random.random() * 12)
        print(f"Subscriber{self.id} is ready now to read")
        message = ""
        while message != "TERMINATE":
            message = await queue.get()
            print(f"Subscriber{self.id} got message: {message}")

            if random.random() < 0.1:
                print(f"Subscriber{self.id} has enough reading!")
                break
        print(f"Subscriber{self.id} is terminating!")
        self.unsubscribe()

