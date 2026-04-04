# Source: https://posthog.com/docs/open-api-spec/signal_source_configs_destroy.md

# signal_source_configs_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/signal_source_configs/{id}/
{
  "paths": {
    "/api/projects/{project_id}/signal_source_configs/{id}/": {
      "delete": {
        "operationId": "signal_source_configs_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this signal source config.",
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
          "signal_source_configs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:write"
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
