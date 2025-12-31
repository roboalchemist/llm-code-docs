# Source: https://configcat.com/docs/api/reference/replace-setting-value-by-sdkkey-v-2.md

# Replace value

```
PUT 
/v2/settings/:settingKeyOrId/value
```

This endpoint replaces the value and the Targeting Rules of a Feature Flag or Setting in a specified Environment identified by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` header.

Only the `defaultValue`, `targetingRules`, and `percentageEvaluationAttribute` fields are modifiable by this endpoint.

**Important:** As this endpoint is doing a complete replace, it's important to set every other field that you don't want to change to its original state. Not listing one means it will reset.

For example: We have the following resource of a Feature Flag.

```
{
  "defaultValue": {
    "boolValue": false
  },
  "targetingRules": [
    {
      "conditions": [
        {
          "userCondition": {
            "comparisonAttribute": "Email",
            "comparator": "sensitiveTextEquals",
            "comparisonValue": {
              "stringValue": "test@example.com"
            }
          }
        }
      ],
      "percentageOptions": [],
      "value": {
        "boolValue": true
      }
    }
  ]
}
```

If we send a replace request body as below:

```
{
  "defaultValue": {
    "boolValue": true
  }
}
```

Then besides that the default served value is set to `true`, all the Targeting Rules are deleted. So we get a response like this:

```
{
  "defaultValue": {
    "boolValue": true
  },
  "targetingRules": []
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
