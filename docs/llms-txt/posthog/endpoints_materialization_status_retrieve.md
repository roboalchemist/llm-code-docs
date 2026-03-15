# Source: https://posthog.com/docs/open-api-spec/endpoints_materialization_status_retrieve.md

# endpoints_materialization_status_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/{name}/materialization_status/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/{name}/materialization_status/": {
      "get": {
        "operationId": "endpoints_materialization_status_retrieve",
        "description": "Get materialization status for an endpoint. Supports ?version=N query param.",
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
