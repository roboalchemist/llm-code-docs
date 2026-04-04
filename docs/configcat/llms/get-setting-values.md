# Source: https://configcat.com/docs/api/reference/get-setting-values.md

# Get values

Copy page

This endpoint returns the value of a specified Config's Feature Flags or Settings identified by the `configId` parameter in a specified Environment identified by the `environmentId` parameter.

The most important attributes in the response are the `value`, `rolloutRules` and `percentageRules`. The `value` represents what the clients will get when the evaluation requests of our SDKs are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.

The `rolloutRules` and `percentageRules` attributes are representing the current Targeting and Percentage Rules configuration of the actual Feature Flag or Setting in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/targeting/targeting-overview.md).

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
