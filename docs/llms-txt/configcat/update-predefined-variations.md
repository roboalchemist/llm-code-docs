# Source: https://configcat.com/docs/api/reference/update-predefined-variations.md

# Update predefined variations (Beta)

```
PUT 
/v1/settings/:settingId/predefined-variations
```

This endpoint updates the predefined variations for a Feature Flag or Setting identified by the `settingId` parameter.

**Important:** You can only update a predefined variation's value if it is not used anywhere in your feature flags.

**Beta feature:** The feature is currently in closed beta state and cannot be used.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
