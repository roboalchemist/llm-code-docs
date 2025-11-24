# Source: https://docs.apify.com/api/v2/actor-build-get.md

# Get build


```
GET 
https://api.apify.com/v2/actor-builds/:buildId
```


Clientshttps://docs.apify.com/api/client/python/reference/class/BuildClientAsync#gethttps://docs.apify.com/api/client/js/reference/class/BuildClient#getGets an object that contains all the details about a specific build of an Actor.

By passing the optional `waitForFinish` parameter the API endpoint will synchronously wait for the build to finish. This is useful to avoid periodic polling when waiting for an Actor build to finish.

This endpoint does not require the authentication token. Instead, calls are authenticated using a hard-to-guess ID of the build. However, if you access the endpoint without the token, certain attributes, such as `usageUsd` and `usageTotalUsd`, will be hidden.

## Request

## Responses

* 200

**Response Headers**

