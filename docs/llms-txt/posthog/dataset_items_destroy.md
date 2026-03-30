# Source: https://posthog.com/docs/open-api-spec/dataset_items_destroy.md

# dataset_items_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/dataset_items/{id}/
{
  "paths": {
    "/api/projects/{project_id}/dataset_items/{id}/": {
      "delete": {
        "operationId": "dataset_items_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this dataset item.",
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
          "llm_analytics",
          "dataset_items"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "dataset:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "llm_analytics"
        ]
      }
    }
  }
}
```
