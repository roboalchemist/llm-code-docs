# Source: https://posthog.com/docs/open-api-spec/elements_destroy.md

# elements_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/elements/{id}/
{
  "paths": {
    "/api/projects/{project_id}/elements/{id}/": {
      "delete": {
        "operationId": "elements_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this element.",
            "required": true
          },
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
              "element:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
