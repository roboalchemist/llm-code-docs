# Source: https://docs.apify.com/api/v2/request-queue-request-lock-delete.md

# Delete request lock


```
DELETE 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId/lock
```


Deletes a request lock. The request lock can be deleted only by the client that has locked it using .

## Request

## Responses

* 204
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
