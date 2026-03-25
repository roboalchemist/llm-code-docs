# Source: https://posthog.com/docs/open-api-spec/environments_hog_functions_destroy.md

# environments_hog_functions_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/hog_functions/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/hog_functions/{id}/": {
      "delete": {
        "operationId": "environments_hog_functions_destroy",
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
            "description": "A UUID string identifying this hog function.",
            "required": true
          }
        ],
        "tags": [
          "hog_functions",
          "hog_functions"
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  }
}
```
