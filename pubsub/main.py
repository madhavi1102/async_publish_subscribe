import asyncio
from hub import Hub
from publisher import Publisher
from subscriber import Subscriber

NUM_SUBSCRIBERS = 5
ITERATIONS = 10


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    hub = Hub()
    pub = Publisher(hub)
    readers = [Subscriber.read(Subscriber(hub, i)) for i in range(NUM_SUBSCRIBERS)]
    loop.run_until_complete(asyncio.gather(pub.publish(ITERATIONS), *readers))
