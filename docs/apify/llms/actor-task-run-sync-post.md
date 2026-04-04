# Source: https://docs.apify.com/api/v2/actor-task-run-sync-post.md

# Run task synchronously


```
POST 
https://api.apify.com/v2/actor-tasks/:actorTaskId/run-sync
```


Runs an Actor task and synchronously returns its output.

The run must finish in 300 seconds otherwise the HTTP request fails with a timeout error (this won't abort the run itself).

Optionally, you can override the Actor input configuration by passing a JSON object as the POST payload and setting the `Content-Type: application/json` HTTP header.

Note that if the object in the POST payload does not define a particular input property, the Actor run uses the default value defined by the task (or Actor's input schema if not defined by the task).

Beware that it might be impossible to maintain an idle HTTP connection for an extended period, due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.

If the connection breaks, you will not receive any information about the run and its status.

Input fields from Actor task configuration can be overloaded with values passed as the POST payload.

Just make sure to specify `Content-Type` header to be `application/json` and input to be an object.

To run the task asynchronously, use the  API endpoint instead.

## Request

## Responses

* 201
* 400

**Response Headers**



**Response Headers**

