# Source: https://docs.apify.com/api/v2/request-queue-requests-unlock-post.md

# Unlock requests


```
POST 
https://api.apify.com/v2/request-queues/:queueId/requests/unlock
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#unlock_requestshttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#unlockRequestsUnlocks requests in the queue that are currently locked by the client.

* If the client is within an Actor run, it unlocks all requests locked by that specific run plus all requests locked by the same clientKey.
* If the client is outside of an Actor run, it unlocks all requests locked using the same clientKey.

## Request

## Responses

* 200

Number of requests that were unlocked
