# Source: https://posthog.com/docs/open-api-spec/environments_hog_functions_icons_retrieve.md

# environments_hog_functions_icons_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/hog_functions/icons/
{
  "paths": {
    "/api/environments/{environment_id}/hog_functions/icons/": {
      "get": {
        "operationId": "environments_hog_functions_icons_retrieve",
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
          "hog_functions",
          "hog_functions"
        ],
        "responses": {
          "200": {
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
