## Asynchronous Publish-Subscribe With Python

### KEY FEATURES

* Implemented an asynchronous publish-subscribe application using ```asyncio``` package with 
  pure ```python```. 
* Publisher and Subscribers are decoupled thus publisher does not maintain track of subscribers.
* This demonstrates how broadcasting of notifications to multiple subscribed users works asynchronously 
  with leveraging asyncio in python.

```Asyncio``` enables concurrent programming in python, it makes world of multiple subscribers reading the same notification
simultaneously. Performance of this asynchronous publish-subscriptions model is overall always much higher than sequential model.

Here, publisher and subscribers are decoupled with introducing a middle layer 'hub' which does task of maintaining subscribers and 
publishing to them. This way publisher need not take extra job to maintain subscribers, keeping publisher's main job to publish.


### Requirements
```
python >= 3.7
```

### How To Run

```  
python main.py
 ```
 
 ### OUTPUT

```
Publisher has 0 subscribers
Subscriber0 is ready now to read
Subscriber2 is ready now to read
Publisher has 5 subscribers
Subscriber0 got message: THIS IS EVENT-1
Subscriber2 got message: THIS IS EVENT-1
Subscriber3 is ready now to read
Subscriber3 got message: THIS IS EVENT-1
Subscriber1 is ready now to read
Subscriber1 got message: THIS IS EVENT-1
Publisher has 5 subscribers
Subscriber3 got message: THIS IS EVENT-2
Subscriber0 got message: THIS IS EVENT-2
Subscriber1 got message: THIS IS EVENT-2
Subscriber2 got message: THIS IS EVENT-2
Subscriber4 is ready now to read
Subscriber4 got message: THIS IS EVENT-1
Subscriber4 got message: THIS IS EVENT-2
Publisher has 5 subscribers
Subscriber3 got message: THIS IS EVENT-3
Subscriber0 got message: THIS IS EVENT-3
Subscriber1 got message: THIS IS EVENT-3
Subscriber1 has enough reading!
Subscriber1 is terminating!
Subscriber4 got message: THIS IS EVENT-3
Subscriber2 got message: THIS IS EVENT-3
Publisher has 4 subscribers
Subscriber3 got message: THIS IS EVENT-4
Subscriber0 got message: THIS IS EVENT-4
Subscriber4 got message: THIS IS EVENT-4
Subscriber2 got message: THIS IS EVENT-4
Publisher has 4 subscribers
Subscriber3 got message: THIS IS EVENT-5
Subscriber0 got message: THIS IS EVENT-5
Subscriber4 got message: THIS IS EVENT-5
Subscriber2 got message: THIS IS EVENT-5
Publisher has 4 subscribers
Subscriber3 got message: THIS IS EVENT-6
Subscriber0 got message: THIS IS EVENT-6
Subscriber4 got message: THIS IS EVENT-6
Subscriber2 got message: THIS IS EVENT-6
Publisher has 4 subscribers
Subscriber3 got message: THIS IS EVENT-7
Subscriber3 has enough reading!
Subscriber3 is terminating!
Subscriber0 got message: THIS IS EVENT-7
Subscriber4 got message: THIS IS EVENT-7
Subscriber2 got message: THIS IS EVENT-7
Publisher has 3 subscribers
Subscriber0 got message: THIS IS EVENT-8
Subscriber0 has enough reading!
Subscriber0 is terminating!
Subscriber4 got message: THIS IS EVENT-8
Subscriber2 got message: THIS IS EVENT-8
Publisher has 2 subscribers
Subscriber4 got message: THIS IS EVENT-9
Subscriber2 got message: THIS IS EVENT-9
Subscriber4 got message: TERMINATE
Subscriber4 is terminating!
Subscriber2 got message: TERMINATE
Subscriber2 has enough reading!
Subscriber2 is terminating!

```
