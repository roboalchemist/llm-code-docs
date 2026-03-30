# Source: https://posthog.com/docs/open-api-spec/notebooks_activity_retrieve_2.md

# notebooks_activity_retrieve_2

## OpenAPI

```json GET /api/projects/{project_id}/notebooks/{short_id}/activity/
{
  "paths": {
    "/api/projects/{project_id}/notebooks/{short_id}/activity/": {
      "get": {
        "operationId": "notebooks_activity_retrieve_2",
        "description": "The API for interacting with Notebooks. This feature is in early access and the API can have breaking changes without announcement.",
        "parameters": [
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
            "name": "short_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "notebooks"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "activity_log:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "notebooks"
        ]
      }
    }
  }
}
```
