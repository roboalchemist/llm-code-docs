# Source: https://docs.apify.com/api/v2/request-queue-requests-unlock-post.md

# Unlock requests


```
POST 
https://api.apify.com/v2/request-queues/:queueId/requests/unlock
```


Unlocks requests in the queue that are currently locked by the client.

* If the client is within an Actor run, it unlocks all requests locked by that specific run plus all requests locked by the same clientKey.
* If the client is outside of an Actor run, it unlocks all requests locked using the same clientKey.

## Request

## Responses

* 200
* 400

Number of requests that were unlocked

Bad request - invalid input parameters or request body.
