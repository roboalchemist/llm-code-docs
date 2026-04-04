# Source: https://posthog.com/docs/open-api-spec/endpoints_run_retrieve.md

# endpoints_run_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/{name}/run/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/{name}/run/": {
      "get": {
        "operationId": "endpoints_run_retrieve",
        "description": "Execute endpoint with optional materialization. Supports version parameter, runs latest version if not set.",
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
