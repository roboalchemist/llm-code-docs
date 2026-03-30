# Source: https://posthog.com/docs/open-api-spec/hog_functions_icons_retrieve.md

# hog_functions_icons_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/hog_functions/icons/
{
  "paths": {
    "/api/projects/{project_id}/hog_functions/icons/": {
      "get": {
        "operationId": "hog_functions_icons_retrieve",
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
          "hog_functions",
          "hog_functions"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  }
}
```
