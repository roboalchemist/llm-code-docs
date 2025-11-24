# Source: https://docs.apify.com/api/v2/request-queue-requests-post.md

# Add request


```
POST 
https://api.apify.com/v2/request-queues/:queueId/requests
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync#add_requesthttps://docs.apify.com/api/client/js/reference/class/RequestQueueClient#addRequestAdds request to the queue. Response contains ID of the request and info if request was already present in the queue or handled.

If request with same `uniqueKey` was already present in the queue then returns an ID of existing request.

## Request

## Responses

* 201

**Response Headers**

