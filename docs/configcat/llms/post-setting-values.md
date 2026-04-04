# Source: https://configcat.com/docs/api/reference/post-setting-values.md

# Post values

Copy page

This endpoint replaces the values of a specified Config's Feature Flags or Settings identified by the `configId` parameter in a specified Environment identified by the `environmentId` parameter.

Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.

**Important:** As this endpoint is doing a complete replace, it's important to set every other attribute that you don't want to change in its original state. Not listing one means it will reset.

For example: We have the following resource.

```json
{
  "settingValues": [
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
      "value": false,
      "settingId": 1
    }
  ]
}

```

If we send a replace request body as below:

```json
{ 
  "settingValues": [
    {
      "value": true,
      "settingId": 1
    }
  ]
}

```

Then besides that the default value is set to `true`, all the Percentage Rules are deleted. So we get a response like this:

```json
{
  "settingValues": [
    {
      "rolloutPercentageItems": [],
      "rolloutRules": [],
      "value": true,
      "setting": 
      {
        "settingId": 1
      }
    }
  ]
}

```

The `rolloutRules` property describes two types of rules:

* **Targeting rules**: When you want to add or update a targeting rule, the `comparator`, `comparisonAttribute`, and `comparisonValue` members are required.
* **Segment rules**: When you want to add add or update a segment rule, the `segmentId` which identifies the desired segment and the `segmentComparator` members are required.

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
