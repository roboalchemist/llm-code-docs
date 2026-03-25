# Source: https://posthog.com/docs/open-api-spec/conversations_tickets_destroy.md

# conversations_tickets_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/conversations/tickets/{id}/
{
  "paths": {
    "/api/projects/{project_id}/conversations/tickets/{id}/": {
      "delete": {
        "operationId": "conversations_tickets_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this ticket.",
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
          "conversations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "ticket:write"
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
