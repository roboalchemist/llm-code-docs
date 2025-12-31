# Source: https://configcat.com/docs/api/scim/get-service-provider-config.md

# Get Service Provider Config

```
GET 
/v2/:organizationId/ServiceProviderConfig
```

This endpoint returns the service provider config.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 401
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
