# Source: https://configcat.com/docs/api/scim/configcat-user-provisioning-scim-api.md

Version: v1

# ConfigCat User Provisioning (SCIM) API

Copy page

The purpose of this API is to allow user and group synchronization from your Identity Provider into a ConfigCat Organization via the SCIM protocol.

[Here](https://configcat.com/docs/advanced/team-management/scim/scim-overview/) you can read more about the user provisioning process.

**Base API URL**: `https://scim-api.configcat.com`

## OpenAPI Specification[​](#openapi-specification "Direct link to OpenAPI Specification")

The complete specification is publicly available in the following formats:

* [OpenAPI v3](https://scim-api.configcat.com/openapi/v1/openapi.json)

## Throttling and rate limits[​](#throttling-and-rate-limits "Direct link to Throttling and rate limits")

All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:

| Header                 | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. |
| X-Rate-Limit-Reset     | The time when the current rate limit period resets.                        |

When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header.

## Authentication[​](#authentication "Direct link to Authentication")

* HTTP: Bearer Auth

To authenticate with the API you have to fill the `Authorization` HTTP request header with your SCIM token.

You can retrieve your credentials on the [Authentication & Provisioning page](https://app.configcat.com/organization/authentication). Example: `Bearer 12345abcdef`

| Security Scheme Type:      | http   |
| -------------------------- | ------ |
| HTTP Authorization Scheme: | bearer |

### Contact

ConfigCat: <support@configcat.com>

URL: <https://configcat.com>

### Terms of Service

<https://configcat.com/policies>
