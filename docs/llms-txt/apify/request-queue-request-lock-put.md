# Source: https://docs.apify.com/api/v2/request-queue-request-lock-put.md

# Prolong request lock


```
PUT 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId/lock
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#prolong_request_lockhttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#prolongRequestLockProlongs request lock. The request lock can be prolonged only by the client that has locked it using .

## Request

## Responses

* 200

**Response Headers**

