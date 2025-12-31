# Source: https://configcat.com/docs/api/reference/update-setting-value-by-sdkkey.md

# Update value

```
PATCH 
/v1/settings/:settingKeyOrId/value
```

This endpoint updates the value of a Feature Flag or Setting with a collection of [JSON Patch](https://jsonpatch.com) operations in a specified Environment identified by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` header.

Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.

The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change. It supports collection reordering, so it also can be used for reordering the targeting rules of a Feature Flag or Setting.

For example: We have the following resource.

```
{
  "rolloutPercentageItems": [
    {
      "percentage": 30,
      "value": true
    },
    {
      "percentage": 70,
      "value": false
    }
  ],
  "rolloutRules": [],
  "value": false
}
```

If we send an update request body as below:

```
[
  {
    "op": "replace",
    "path": "/value",
    "value": true
  }
]
```

Only the default served value is going to be set to `true` and all the Percentage Rules are remaining unchanged. So we get a response like this:

```
{
  "rolloutPercentageItems": [
    {
      "percentage": 30,
      "value": true
    },
    {
      "percentage": 70,
      "value": false
    }
  ],
  "rolloutRules": [],
  "value": true
}
```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 204
* 400
* 404
* 429

When no change applied on the resource.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
