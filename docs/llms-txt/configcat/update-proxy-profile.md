# Source: https://configcat.com/docs/api/reference/update-proxy-profile.md

# Update Proxy Profile

```
PATCH 
/v1/proxy-profiles/:proxyProfileId
```

This endpoint updates a Proxy Profile identified by the `proxyProfileId` parameter with a collection of [JSON Patch](https://jsonpatch.com) operations.

The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change.

For example: We have the following resource.

```
{
  "proxyProfileId": "4ebe288d-6415-44a8-85c8-7b9f78316a86",
  "name": "production",
  "description": "profile for production environments",
  "lastAccessedAt": "2019-08-24T14:15:22Z",
  "connectionPreferences": {
    "sdkPollInterval": 60,
    "webhookNotification": null
  },
  "sdkKeySelectionRules": []
}
```

If we send an update request body as below (it changes the `sdkPollInterval` field and adds a new Proxy Webhook URL):

```
[
  {
    "op": "replace", 
    "path": "/connectionPreferences/sdkPollInterval", 
    "value": 120
  }, 
  {
    "op": "add",
    "path": "/connectionPreferences/webhookNotification",
    "value": {
      "webhookProxyUrl": "https://my-proxy-url.com"
    }
  }
]
```

Only the `sdkPollInterval` and `webhookProxyUrl` are updated and all the other attributes remain unchanged. So we get a response like this:

```
{
  "proxyProfileId": "4ebe288d-6415-44a8-85c8-7b9f78316a86",
  "name": "production",
  "description": "profile for production environments",
  "lastAccessedAt": "2019-08-24T14:15:22Z",
  "connectionPreferences": {
    "sdkPollInterval": 120,
    "webhookNotification": {
      "webhookProxyUrl": "https://my-proxy-url.com",
      "signingKey1": "<generated-signing-key>",
      "signingKey2": null
    }
  },
  "sdkKeySelectionRules": []
}
```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
