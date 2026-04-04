# Source: https://posthog.com/docs/open-api-spec/logs_alerts_destroy.md

# logs_alerts_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/logs/alerts/{id}/
{
  "paths": {
    "/api/projects/{project_id}/logs/alerts/{id}/": {
      "delete": {
        "operationId": "logs_alerts_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this logs alert configuration.",
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
          "logs",
          "logs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
