# Source: https://docs.apify.com/api/v2/actor-task-put.md

# Update task


```
PUT 
https://api.apify.com/v2/actor-tasks/:actorTaskId
```


Clientshttps://docs.apify.com/api/client/python/reference/class/TaskClientAsync#updatehttps://docs.apify.com/api/client/js/reference/class/TaskClient#updateUpdate settings of a task using values specified by an object passed as JSON in the POST payload.

If the object does not define a specific property, its value is not updated.

The response is the full task object as returned by the  endpoint.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 200

**Response Headers**

