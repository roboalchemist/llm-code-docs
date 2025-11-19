# Source: https://docs.apify.com/api/v2/request-queue-request-lock-delete.md

# Delete request lock


```
DELETE 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId/lock
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#delete_request_lockhttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#deleteRequestLockDeletes a request lock. The request lock can be deleted only by the client that has locked it using .

## Request

## Responses

* 204

**Response Headers**

