# Source: https://configcat.com/docs/api/reference/get-setting-value-by-sdkkey-v-2.md

# Get value

Copy page

This endpoint returns the value of a Feature Flag or Setting in a specified Environment identified by the [SDK key](https://app.configcat.com/sdkkey) passed in the `X-CONFIGCAT-SDKKEY` header.

The most important fields in the response are the `defaultValue`, `targetingRules`. The `defaultValue` represents what the clients will get when the evaluation requests of our SDKs are not matching to any of the defined Targeting Rules, or when there are no additional rules to evaluate.

The `targetingRules` represents the current Targeting Rule configuration of the actual Feature Flag or Setting in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/targeting/targeting-overview.md).

The `percentageEvaluationAttribute` represents the custom [User Object](https://configcat.com/docs/targeting/user-object.md) attribute that must be used at the [percentage evaluation](https://configcat.com/docs/targeting/percentage-options.md) of the Feature Flag or Setting.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
