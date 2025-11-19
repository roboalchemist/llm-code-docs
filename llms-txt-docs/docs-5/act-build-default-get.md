# Source: https://docs.apify.com/api/v2/act-build-default-get.md

# Get default build


```
GET 
https://api.apify.com/v2/acts/:actorId/builds/default
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ActorClient#default_buildhttps://docs.apify.com/api/client/js/reference/class/ActorClient#defaultBuildGet the default build for an Actor.

Use the optional `waitForFinish` parameter to synchronously wait for the build to finish. This avoids the need for periodic polling when waiting for the build to complete.

This endpoint does not require an authentication token. Instead, calls are authenticated using the Actor's unique ID. However, if you access the endpoint without a token, certain attributes (e.g., `usageUsd` and `usageTotalUsd`) will be hidden.

## Request

## Responses

* 200

**Response Headers**

