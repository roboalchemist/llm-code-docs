# Source: https://docs.apify.com/api/v2/request-queue-request-put.md

# Update request


```
PUT 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#updatehttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#updateUpdates a request in a queue. Mark request as handled by setting `request.handledAt = new Date()`. If `handledAt` is set, the request will be removed from head of the queue (and unlocked, if applicable).

## Request

## Responses

* 200

**Response Headers**

