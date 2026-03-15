# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_openapi.json_retrieve.md

# environments_endpoints_openapi.json_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/endpoints/{name}/openapi.json/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/openapi.json/": {
      "get": {
        "operationId": "environments_endpoints_openapi.json_retrieve",
        "description": "Get OpenAPI 3.0 specification for this endpoint. Use this to generate typed SDK clients.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
            },
            "required": true
          }
        ],
        "tags": [
          "endpoints",
          "endpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  }
}
```
