"""
Publisher publishes to all subscribers synchronously
However, it is asynchronous such that upon resting, other tasks can be completed before the next iteration
The publisher sends n notifications.
"""
import asyncio


class Publisher:

    def __init__(self, hub):
        self.hub = hub

    async def publish(self, count_notifications):
        message = "THIS IS EVENT"
        for i in range(count_notifications):
            print(f"Publisher has {len(self.hub.subscriptions)} subscribers")
            self.hub.push(f"{message}-{i}")
            await asyncio.sleep(4)
        self.hub.push("TERMINATE")
