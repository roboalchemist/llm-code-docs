# Source: https://docs.apify.com/api/v2/actor-task-input-put.md

# Update task input


```
PUT 
https://api.apify.com/v2/actor-tasks/:actorTaskId/input
```


Clientshttps://docs.apify.com/api/client/python/reference/class/TaskClientAsync#update_inputhttps://docs.apify.com/api/client/js/reference/class/TaskClient#updateInputUpdates the input of a task using values specified by an object passed as JSON in the PUT payload.

If the object does not define a specific property, its value is not updated.

The response is the full task input as returned by the  endpoint.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 200

**Response Headers**

