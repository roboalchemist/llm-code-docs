# Source: https://posthog.com/docs/open-api-spec/environments_saved_destroy.md

# environments_saved_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/saved/{short_id}/
{
  "paths": {
    "/api/environments/{environment_id}/saved/{short_id}/": {
      "delete": {
        "operationId": "environments_saved_destroy",
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
            "name": "short_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "saved"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "heatmap:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
