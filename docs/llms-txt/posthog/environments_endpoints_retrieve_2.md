# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_retrieve_2.md

# environments_endpoints_retrieve_2

## OpenAPI

```json GET /api/environments/{environment_id}/endpoints/{name}/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/": {
      "get": {
        "operationId": "environments_endpoints_retrieve_2",
        "description": "Retrieve an endpoint, or a specific endpoint version.",
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
