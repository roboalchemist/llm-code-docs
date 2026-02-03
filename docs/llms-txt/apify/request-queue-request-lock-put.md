# Source: https://docs.apify.com/api/v2/request-queue-request-lock-put.md

# Prolong request lock


```
PUT 
https://api.apify.com/v2/request-queues/:queueId/requests/:requestId/lock
```


Prolongs request lock. The request lock can be prolonged only by the client that has locked it using .

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
