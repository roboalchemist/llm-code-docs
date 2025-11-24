# Source: https://configcat.com/docs/api/reference/replace-setting-value-by-sdkkey.md

# Replace value

```
PUT 
/v1/settings/:settingKeyOrId/value
```

This endpoint replaces the value of a Feature Flag or Setting in a specified Environment identified by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` header.

Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.

**Important:** As this endpoint is doing a complete replace, it's important to set every other attribute that you don't want to change to its original state. Not listing one means it will reset.

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

If we send a replace request body as below:

```
{
  "value": true
}
```

Then besides that the default served value is set to `true`, all the Percentage Rules are deleted. So we get a response like this:

```
{
  "rolloutPercentageItems": [],
  "rolloutRules": [],
  "value": true
}
```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
