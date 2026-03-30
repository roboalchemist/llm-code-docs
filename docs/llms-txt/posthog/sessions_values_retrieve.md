# Source: https://posthog.com/docs/open-api-spec/sessions_values_retrieve.md

# sessions_values_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/sessions/values/
{
  "paths": {
    "/api/projects/{project_id}/sessions/values/": {
      "get": {
        "operationId": "sessions_values_retrieve",
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
          "sessions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
