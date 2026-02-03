# Source: https://docs.apify.com/api/v2/request-queue-requests-batch-post.md

# Add requests


```
POST 
https://api.apify.com/v2/request-queues/:queueId/requests/batch
```


Adds requests to the queue in batch. The maximum requests in batch is limit to 25. The response contains an array of unprocessed and processed requests. If any add operation fails because the request queue rate limit is exceeded or an internal failure occurs, the failed request is returned in the unprocessedRequests response parameter. You can resend these requests to add. It is recommended to use exponential backoff algorithm for these retries. If a request with the same `uniqueKey` was already present in the queue, then it returns an ID of the existing request.

## Request

## Responses

* 201
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
