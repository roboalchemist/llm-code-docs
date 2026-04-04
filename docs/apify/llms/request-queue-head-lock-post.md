# Source: https://docs.apify.com/api/v2/request-queue-head-lock-post.md

# Get head and lock


```
POST 
https://api.apify.com/v2/request-queues/:queueId/head/lock
```


Returns the given number of first requests from the queue and locks them for the given time.

If this endpoint locks the request, no other client or run will be able to get and lock these requests.

The response contains the `hadMultipleClients` boolean field which indicates that the queue was accessed by more than one client (with unique or empty `clientKey`).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
