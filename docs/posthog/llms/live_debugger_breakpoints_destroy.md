# Source: https://posthog.com/docs/open-api-spec/live_debugger_breakpoints_destroy.md

# live_debugger_breakpoints_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/live_debugger_breakpoints/{id}/
{
  "paths": {
    "/api/projects/{project_id}/live_debugger_breakpoints/{id}/": {
      "delete": {
        "operationId": "live_debugger_breakpoints_destroy",
        "description": "Create, Read, Update and Delete breakpoints for live debugging.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this live debugger breakpoint.",
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
          "live_debugger_breakpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "live_debugger:write"
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
