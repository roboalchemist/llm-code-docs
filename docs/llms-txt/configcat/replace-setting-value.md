# Source: https://configcat.com/docs/api/reference/replace-setting-value.md

# Replace value

```
PUT 
/v1/environments/:environmentId/settings/:settingId/value
```

This endpoint replaces the whole value of a Feature Flag or Setting in a specified Environment.

Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.

**Important:** As this endpoint is doing a complete replace, it's important to set every other attribute that you don't want to change in its original state. Not listing one means it will reset.

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

Then besides that the default value is set to `true`, all the Percentage Rules are deleted. So we get a response like this:

```
{
  "rolloutPercentageItems": [],
  "rolloutRules": [],
  "value": true
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

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
