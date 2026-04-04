# Source: https://docs.apify.com/api/v2/act-run-sync-get.md

# Without input


```
GET 
https://api.apify.com/v2/acts/:actorId/run-sync
```


Runs a specific Actor and returns its output. The run must finish in 300 seconds otherwise the API endpoint returns a timeout error. The Actor is not passed any input.

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

