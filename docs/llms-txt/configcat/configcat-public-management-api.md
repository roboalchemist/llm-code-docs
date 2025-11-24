# Source: https://configcat.com/docs/api/reference/configcat-public-management-api.md

Version: v1

# ConfigCat Public Management API

The purpose of this API is to access the ConfigCat platform programmatically. You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.

**Base API URL**: <https://api.configcat.com>

If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).

The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON format.

**Important:** Do not use this API for accessing and evaluating feature flag values. Use the [SDKs](https://configcat.com/docs/docs/sdk-reference/overview/.md) or the [ConfigCat Proxy](https://configcat.com/docs/docs/advanced/proxy/proxy-overview/.md) instead.

## OpenAPI Specification[​](#openapi-specification "Direct link to OpenAPI Specification")

The complete specification is publicly available in the following formats:

* [OpenAPI v3](https://api.configcat.com/docs/v1/swagger.json)
* [Swagger v2](https://api.configcat.com/docs/v1/swagger.v2.json)

You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.

## Throttling and rate limits[​](#throttling-and-rate-limits "Direct link to Throttling and rate limits")

All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:

| Header                 | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. |
| X-Rate-Limit-Reset     | The time when the current rate limit period resets.                        |

When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header.

## Authentication[​](#authentication "Direct link to Authentication")

* HTTP: Basic Auth

To authenticate with the API you have to fill the `Authorization` HTTP request header with your Public API credentials.

You can create your credentials on the [Public API credentials management page](https://app.configcat.com/my-account/public-api-credentials).

| Security Scheme Type:      | http  |
| -------------------------- | ----- |
| HTTP Authorization Scheme: | basic |

### Contact

ConfigCat: <support@configcat.com>

URL: <https://configcat.com>

### Terms of Service

<https://configcat.com/policies>
