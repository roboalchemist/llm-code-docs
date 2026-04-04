# Source: https://posthog.com/docs/open-api-spec/product_tours_destroy.md

# product_tours_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/product_tours/{id}/
{
  "paths": {
    "/api/projects/{project_id}/product_tours/{id}/": {
      "delete": {
        "operationId": "product_tours_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this product tour.",
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
          "product_tours"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "product_tour:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
