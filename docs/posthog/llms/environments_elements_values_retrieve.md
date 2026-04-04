# Source: https://posthog.com/docs/open-api-spec/environments_elements_values_retrieve.md

# environments_elements_values_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/elements/values/
{
  "paths": {
    "/api/environments/{environment_id}/elements/values/": {
      "get": {
        "operationId": "environments_elements_values_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "product_analytics",
          "elements"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "element:read"
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
          "product_analytics"
        ]
      }
    }
  }
}
```
