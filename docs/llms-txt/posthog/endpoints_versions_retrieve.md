# Source: https://posthog.com/docs/open-api-spec/endpoints_versions_retrieve.md

# endpoints_versions_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/{name}/versions/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/{name}/versions/": {
      "get": {
        "operationId": "endpoints_versions_retrieve",
        "description": "List all versions for an endpoint.",
        "parameters": [
          {
            "in": "path",
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
            },
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
