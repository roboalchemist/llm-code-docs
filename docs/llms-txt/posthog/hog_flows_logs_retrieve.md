# Source: https://posthog.com/docs/open-api-spec/hog_flows_logs_retrieve.md

# hog_flows_logs_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/hog_flows/{id}/logs/
{
  "paths": {
    "/api/projects/{project_id}/hog_flows/{id}/logs/": {
      "get": {
        "operationId": "hog_flows_logs_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this hog flow.",
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
          "workflows",
          "hog_flows"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "workflows"
        ]
      }
    }
  }
}
```
