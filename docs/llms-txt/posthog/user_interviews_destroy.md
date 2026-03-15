# Source: https://posthog.com/docs/open-api-spec/user_interviews_destroy.md

# user_interviews_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/user_interviews/{id}/
{
  "paths": {
    "/api/environments/{project_id}/user_interviews/{id}/": {
      "delete": {
        "operationId": "user_interviews_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this user interview.",
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
          "user_interviews",
          "user_interviews"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user_interview_DO_NOT_USE:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "user_interviews"
        ]
      }
    }
  }
}
```
