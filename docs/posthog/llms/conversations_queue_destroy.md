# Source: https://posthog.com/docs/open-api-spec/conversations_queue_destroy.md

# conversations_queue_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/conversations/{conversation}/queue/{queue_id}/
{
  "paths": {
    "/api/environments/{project_id}/conversations/{conversation}/queue/{queue_id}/": {
      "delete": {
        "operationId": "conversations_queue_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "conversation",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this conversation.",
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
          },
          {
            "in": "path",
            "name": "queue_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "max",
          "conversations"
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "max"
        ]
      }
    }
  }
}
```
