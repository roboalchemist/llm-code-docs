# Source: https://docs.apify.com/api/v2/request-queue-head-get.md

# Get head


```
GET 
https://api.apify.com/v2/request-queues/:queueId/head
```


Returns given number of first requests from the queue.

The response contains the `hadMultipleClients` boolean field which indicates that the queue was accessed by more than one client (with unique or empty `clientKey`). This field is used by [Apify SDK](https://sdk.apify.com) to determine whether the local cache is consistent with the request queue, and thus optimize performance of certain operations.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
