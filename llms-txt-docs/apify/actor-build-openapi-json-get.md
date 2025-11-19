# Source: https://docs.apify.com/api/v2/actor-build-openapi-json-get.md

# Get OpenAPI definition


```
GET 
https://api.apify.com/v2/actor-builds/:buildId/openapi.json
```


Clientshttps://docs.apify.com/api/client/python/reference/class/BuildClient#get_open_api_definitionhttps://docs.apify.com/api/client/js/reference/class/BuildClient#getOpenApiDefinitionGet the OpenAPI definition for Actor builds. Two similar endpoints are available:

* https://docs.apify.com/api/v2/act-openapi-json-get.md: Requires both `actorId` and `buildId`. Use `default` as the `buildId` to get the OpenAPI schema for the default Actor build.
* https://docs.apify.com/api/v2/actor-build-openapi-json-get.md: Requires only `buildId`.

Get the OpenAPI definition for a specific Actor build. Authentication is based on the build's unique ID. No authentication token is required.

note

You can also use the https://docs.apify.com/api/v2/act-openapi-json-get.md endpoint to get the OpenAPI definition for a build.

## Request

## Responses

* 200

**Response Headers**

