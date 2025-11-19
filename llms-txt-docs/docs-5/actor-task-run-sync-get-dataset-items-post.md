# Source: https://docs.apify.com/api/v2/actor-task-run-sync-get-dataset-items-post.md

# Run task synchronously and get dataset items


```
POST 
https://api.apify.com/v2/actor-tasks/:actorTaskId/run-sync-get-dataset-items
```


Runs an Actor task and synchronously returns its dataset items.

The run must finish in 300 seconds otherwise the HTTP request fails with a timeout error (this won't abort the run itself).

Optionally, you can override the Actor input configuration by passing a JSON object as the POST payload and setting the `Content-Type: application/json` HTTP header.

Note that if the object in the POST payload does not define a particular input property, the Actor run uses the default value defined by the task (or the Actor's input schema if not defined by the task).

You can send all the same options in parameters as the  API endpoint.

Beware that it might be impossible to maintain an idle HTTP connection for an extended period, due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.

If the connection breaks, you will not receive any information about the run and its status.

Input fields from Actor task configuration can be overloaded with values passed as the POST payload.

Just make sure to specify the `Content-Type` header as `application/json` and that the input is an object.

To run the task asynchronously, use the  API endpoint instead.

## Request

## Responses

* 201
* 400

**Response Headers**

* **X-Apify-Pagination-Offset**

  **X-Apify-Pagination-Limit**

  **X-Apify-Pagination-Count**

  **X-Apify-Pagination-Total**

**Response Headers**

