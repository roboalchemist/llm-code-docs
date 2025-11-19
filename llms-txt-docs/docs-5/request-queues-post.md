# Source: https://docs.apify.com/api/v2/request-queues-post.md

# Create request queue


```
POST 
https://api.apify.com/v2/request-queues
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClientAsync#get_or_createhttps://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient#getOrCreateCreates a request queue and returns its object. Keep in mind that requests stored under unnamed queue follows https://docs.apify.com/platform/storage#data-retention.

It creates a queue of given name if the parameter name is used. If a queue with the given name already exists then the endpoint returns its object.

## Request

## Responses

* 201

**Response Headers**

* **Location**
