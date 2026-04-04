# Source: https://posthog.com/docs/open-api-spec/surveys_archived_response_uuids_retrieve.md

# surveys_archived_response_uuids_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/surveys/{id}/archived-response-uuids/
{
  "paths": {
    "/api/projects/{project_id}/surveys/{id}/archived-response-uuids/": {
      "get": {
        "operationId": "surveys_archived_response_uuids_retrieve",
        "description": "Get list of archived response UUIDs for HogQL filtering.\n\nReturns list of UUIDs that the frontend can use to filter out archived responses\nin HogQL queries.",
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
              "survey:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
