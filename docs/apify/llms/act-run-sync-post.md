# Source: https://docs.apify.com/api/v2/act-run-sync-post.md

# Run Actor synchronously with input and return output


```
POST 
https://api.apify.com/v2/acts/:actorId/run-sync
```


Runs a specific Actor and returns its output.

The POST payload including its `Content-Type` header is passed as `INPUT` to the Actor (usually `application/json`). The HTTP response contains Actors `OUTPUT` record from its default key-value store.

The Actor is started with the default options; you can override them using various URL query parameters. If the Actor run exceeds 300 seconds, the HTTP response will have status 408 (Request Timeout).

Beware that it might be impossible to maintain an idle HTTP connection for a long period of time, due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout. If the connection breaks, you will not receive any information about the run and its status.

To run the Actor asynchronously, use the  API endpoint instead.

## Request

## Responses

* 201
* 400
* 408

**Response Headers**



**Response Headers**



**Response Headers**

