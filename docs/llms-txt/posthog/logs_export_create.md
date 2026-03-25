# Source: https://posthog.com/docs/open-api-spec/logs_export_create.md

# logs_export_create

## OpenAPI

```json POST /api/projects/{project_id}/logs/export/
{
  "paths": {
    "/api/projects/{project_id}/logs/export/": {
      "post": {
        "operationId": "logs_export_create",
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
