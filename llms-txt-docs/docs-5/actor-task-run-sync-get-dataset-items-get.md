# Source: https://docs.apify.com/api/v2/actor-task-run-sync-get-dataset-items-get.md

# Run task synchronously and get dataset items


```
GET 
https://api.apify.com/v2/actor-tasks/:actorTaskId/run-sync-get-dataset-items
```


Run a specific task and return its dataset items.

The run must finish in 300 seconds otherwise the HTTP request fails with a timeout error (this won't abort the run itself).

You can send all the same options in parameters as the  API endpoint.

Beware that it might be impossible to maintain an idle HTTP connection for an extended period, due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.

If the connection breaks, you will not receive any information about the run and its status.

To run the Task asynchronously, use the  endpoint instead.

## Request

## Responses

* 201
* 400
* 408

**Response Headers**

* **X-Apify-Pagination-Offset**

  **X-Apify-Pagination-Limit**

  **X-Apify-Pagination-Count**

  **X-Apify-Pagination-Total**

**Response Headers**



Request Timeout: the HTTP request exceeded the 300 second limit

**Response Headers**

