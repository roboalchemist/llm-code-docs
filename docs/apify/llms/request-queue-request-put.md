# Source: https://docs.apify.com/api/v2/request-queue-request-put.md

# Update request


```
PUT 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId
```


Updates a request in a queue. Mark request as handled by setting `request.handledAt = new Date()`. If `handledAt` is set, the request will be removed from head of the queue (and unlocked, if applicable).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
