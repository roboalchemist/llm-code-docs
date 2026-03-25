# Source: https://posthog.com/docs/open-api-spec/logs_values_retrieve.md

# logs_values_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/logs/values/
{
  "paths": {
    "/api/projects/{project_id}/logs/values/": {
      "get": {
        "operationId": "logs_values_retrieve",
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
          "logs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "logs"
        ]
      }
    }
  }
}
```
