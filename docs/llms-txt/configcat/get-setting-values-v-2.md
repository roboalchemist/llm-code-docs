# Source: https://configcat.com/docs/api/reference/get-setting-values-v-2.md

# Get values

Copy page

This endpoint returns all Feature Flag and Setting values of a Config identified by the `configId` parameter in a specified Environment identified by the `environmentId` parameter.

The most important fields in the response are the `defaultValue`, `targetingRules`. The `defaultValue` represents what the clients will get when the evaluation requests of our SDKs are not matching to any of the defined Targeting Rules, or when there are no additional rules to evaluate.

The `targetingRules` represents the current Targeting Rule configuration of the actual Feature Flag or Setting in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/targeting/targeting-overview.md).

The `percentageEvaluationAttribute` represents the custom [User Object](https://configcat.com/docs/targeting/user-object.md) attribute that must be used for [percentage evaluation](https://configcat.com/docs/targeting/percentage-options.md) of the Feature Flag or Setting.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the setting values returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
