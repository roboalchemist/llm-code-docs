# Source: https://docs.apify.com/api/v2/request-queue-requests-batch-delete.md

# Delete requests


```
DELETE 
https://api.apify.com/v2/request-queues/:queueId/requests/batch
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#batch_delete_requestshttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#batchDeleteRequestsBatch-deletes given requests from the queue. The number of requests in a batch is limited to 25. The response contains an array of unprocessed and processed requests. If any delete operation fails because the request queue rate limit is exceeded or an internal failure occurs, the failed request is returned in the `unprocessedRequests` response parameter. You can re-send these delete requests. It is recommended to use an exponential backoff algorithm for these retries. Each request is identified by its ID or uniqueKey parameter. You can use either of them to identify the request.

## Request

## Responses

* 204

**Response Headers**

