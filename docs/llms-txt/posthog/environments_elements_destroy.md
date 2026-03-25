# Source: https://posthog.com/docs/open-api-spec/environments_elements_destroy.md

# environments_elements_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/elements/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/elements/{id}/": {
      "delete": {
        "operationId": "environments_elements_destroy",
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
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this element.",
            "required": true
          }
        ],
        "tags": [
          "product_analytics",
          "elements"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "element:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
