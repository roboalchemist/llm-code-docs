# Source: https://posthog.com/docs/open-api-spec/session_group_summaries_destroy.md

# session_group_summaries_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/session_group_summaries/{id}/
{
  "paths": {
    "/api/projects/{project_id}/session_group_summaries/{id}/": {
      "delete": {
        "operationId": "session_group_summaries_destroy",
        "description": "API for retrieving and managing stored group session summaries.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this session group summary.",
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
          "session_group_summaries"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording:write"
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
