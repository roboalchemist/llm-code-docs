# Source: https://configcat.com/docs/api/reference/post-setting-values-v-2.md

# Post values

Copy page

This endpoint batch updates the Feature Flags and Settings of a Config identified by the `configId` parameter in a specified Environment identified by the `environmentId` parameter.

Only those Feature Flags and Settings are updated which are part of the request, all the others are left untouched.

**Important:** As this endpoint is doing a complete replace on those Feature Flags and Settings, which are set in the request. It's important to set every other field that you don't want to change in its original state. Not listing a field means that it will reset.

For example: We have the following resource of a Feature Flag.

```json
{
  "settingFormulas": [
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
      ],
      "settingId": 1
    }
  ]
}

```

If we send a batch replace request body as below:

```json
{ 
  "updateFormulas": [
    {
      "defaultValue": {
        "boolValue": false
      },
      "settingId": 1
    }
  ]
}

```

Then besides that the default value is set to `true`, all Targeting Rules of the related Feature Flag are deleted. So we get a response like this:

```json
{
  "settingFormulas": [
    {
      "defaultValue": {
        "boolValue": false
      },
      "targetingRules": [],
      "setting": 
      {
        "settingId": 1
      }
    }
  ]
}

```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the updated setting values returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
