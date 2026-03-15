# Source: https://posthog.com/docs/open-api-spec/datasets_destroy.md

# datasets_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/datasets/{id}/
{
  "paths": {
    "/api/projects/{project_id}/datasets/{id}/": {
      "delete": {
        "operationId": "datasets_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this dataset.",
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
          "datasets"
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
