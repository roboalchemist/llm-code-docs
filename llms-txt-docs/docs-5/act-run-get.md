# Source: https://docs.apify.com/api/v2/act-run-get.md

# Get run


```
GET 
https://api.apify.com/v2/acts/:actorId/runs/:runId
```


deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

**\[DEPRECATED]** API endpoints related to run of the Actor were moved under new namespace .

Gets an object that contains all the details about a specific run of an Actor.

By passing the optional `waitForFinish` parameter the API endpoint will synchronously wait for the run to finish. This is useful to avoid periodic polling when waiting for Actor run to complete.

This endpoint does not require the authentication token. Instead, calls are authenticated using a hard-to-guess ID of the run. However, if you access the endpoint without the token, certain attributes, such as `usageUsd` and `usageTotalUsd`, will be hidden.

## Request

## Responses

* 200

**Response Headers**

