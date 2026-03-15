# Source: https://posthog.com/docs/open-api-spec/surveys_destroy.md

# surveys_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/surveys/{id}/
{
  "paths": {
    "/api/projects/{project_id}/surveys/{id}/": {
      "delete": {
        "operationId": "surveys_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this survey.",
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
          "surveys",
          "surveys"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "survey:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "surveys"
        ]
      }
    }
  }
}
```
