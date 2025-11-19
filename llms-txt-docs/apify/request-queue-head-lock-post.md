# Source: https://docs.apify.com/api/v2/request-queue-head-lock-post.md

# Get head and lock


```
POST 
https://api.apify.com/v2/request-queues/:queueId/head/lock
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#list_and_lock_headhttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#listAndLockHeadReturns the given number of first requests from the queue and locks them for the given time.

If this endpoint locks the request, no other client or run will be able to get and lock these requests.

The response contains the `hadMultipleClients` boolean field which indicates that the queue was accessed by more than one client (with unique or empty `clientKey`).

## Request

## Responses

* 200

**Response Headers**

