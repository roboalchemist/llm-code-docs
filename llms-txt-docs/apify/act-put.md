# Source: https://docs.apify.com/api/v2/act-put.md

# Update Actor


```
PUT 
https://api.apify.com/v2/acts/:actorId
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ActorClientAsync#updatehttps://docs.apify.com/api/client/js/reference/class/ActorClient#updateUpdates settings of an Actor using values specified by an Actor object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

The response is the full Actor object as returned by the  endpoint.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

If you want to make your Actor https://docs.apify.com/platform/actors/publishing using `isPublic: true`, you will need to provide the Actor's `title` and the `categories` under which that Actor will be classified in Apify Store. For this, it's best to use the https://github.com/apify/apify-shared-js/blob/2d43ebc41ece9ad31cd6525bd523fb86939bf860/packages/consts/src/consts.ts#L452-L471.

## Request

## Responses

* 200

**Response Headers**

