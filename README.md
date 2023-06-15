## async_publish_subscribe

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
