# Source: https://configcat.com/docs/api/reference/update-setting-value-v-2.md

# Update value

Copy page

This endpoint updates the value of a Feature Flag or Setting with a collection of [JSON Patch](https://jsonpatch.com) operations in a specified Environment.

Only the `defaultValue`, `targetingRules`, and `percentageEvaluationAttribute` fields are modifiable by this endpoint.

The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change. It supports collection reordering, so it also can be used for reordering the targeting rules of a Feature Flag or Setting.

For example: We have the following resource of a Feature Flag.

```json
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

If we send an update request body as below:

```json
[
  {
    "op": "replace",
    "path": "/targetingRules/0/value/boolValue",
    "value": true
  }
]

```

Only the first Targeting Rule's `value` is going to be set to `false` and all the other fields are remaining unchanged.

So we get a response like this:

```json
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
        "boolValue": false
      }
    }
  ]
}

```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 204
* 400
* 404
* 429

When the patch was successful.

When no change applied on the resource.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
