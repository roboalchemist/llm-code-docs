# Source: https://configcat.com/docs/api/reference/select-proxy-profile-sdk-keys.md

# Select SDK keys

Copy page

This endpoint adds the given list of Config / Environment pairs' SDK Keys to a Proxy Profile identified by the `proxyProfileId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 404
* 429

When the selection was successful.

Bad request.

Forbidden. When selection rules are applied to the Proxy Profile.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
