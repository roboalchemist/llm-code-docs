# Source: https://docs.apify.com/api/v2/act-version-put.md

# Update version


```
PUT 
https://api.apify.com/v2/acts/:actorId/versions/:versionNumber
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ActorVersionClientAsync#updateUpdates Actor version using values specified by a  passed as JSON in the POST payload.

If the object does not define a specific property, its value will not be updated.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

The response is the  as returned by the  endpoint.

## Request

## Responses

* 200

**Response Headers**

