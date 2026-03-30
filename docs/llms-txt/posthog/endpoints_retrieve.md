# Source: https://posthog.com/docs/open-api-spec/endpoints_retrieve.md

# endpoints_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/": {
      "get": {
        "operationId": "endpoints_retrieve",
        "description": "List all endpoints for the team.",
        "parameters": [
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
          "endpoints",
          "endpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  }
}
```
