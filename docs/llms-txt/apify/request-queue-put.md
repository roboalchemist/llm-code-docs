# Source: https://docs.apify.com/api/v2/request-queue-put.md

# Update request queue


```
PUT 
https://api.apify.com/v2/request-queues/:queueId
```


Updates a request queue's name and general resource access level using a value specified by a JSON object passed in the PUT payload.

The response is the updated request queue object, as returned by the  API endpoint.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
