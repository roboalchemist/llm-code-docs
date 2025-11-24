# Source: https://docs.apify.com/api/v2/actor-tasks-post.md

# Create task


```
POST 
https://api.apify.com/v2/actor-tasks
```


Clientshttps://docs.apify.com/api/client/python/reference/class/TaskCollectionClientAsync#createhttps://docs.apify.com/api/client/js/reference/class/TaskCollectionClient#createCreate a new task with settings specified by the object passed as JSON in the POST payload.

The response is the full task object as returned by the  endpoint.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 201

**Response Headers**

* **Location**
