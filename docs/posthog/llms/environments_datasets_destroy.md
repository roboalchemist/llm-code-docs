# Source: https://posthog.com/docs/open-api-spec/environments_datasets_destroy.md

# environments_datasets_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/datasets/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/datasets/{id}/": {
      "delete": {
        "operationId": "environments_datasets_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this dataset.",
            "required": true
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
        "deprecated": true,
        "x-explicit-tags": [
          "llm_analytics"
        ]
      }
    }
  }
}
```
