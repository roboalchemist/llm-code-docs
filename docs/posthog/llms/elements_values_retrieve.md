# Source: https://posthog.com/docs/open-api-spec/elements_values_retrieve.md

# elements_values_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/elements/values/
{
  "paths": {
    "/api/projects/{project_id}/elements/values/": {
      "get": {
        "operationId": "elements_values_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": [
          "product_analytics"
        ]
      }
    }
  }
}
```
