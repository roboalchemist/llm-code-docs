# Source: https://posthog.com/docs/open-api-spec/alerts_destroy.md

# alerts_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/alerts/{id}/
{
  "paths": {
    "/api/projects/{project_id}/alerts/{id}/": {
      "delete": {
        "operationId": "alerts_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this alert configuration.",
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
          "alerts"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "alert:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
