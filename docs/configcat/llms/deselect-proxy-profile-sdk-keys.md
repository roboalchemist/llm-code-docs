# Source: https://configcat.com/docs/api/reference/deselect-proxy-profile-sdk-keys.md

# Deselect SDK keys

Copy page

This endpoint removes the given list of Config / Environment pairs' SDK Keys from a Proxy Profile identified by the `proxyProfileId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 404
* 429

When the deselection was successful.

Bad request.

Forbidden. When selection rules are applied to the Proxy Profile.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
