# Source: https://posthog.com/docs/open-api-spec/batch_exports_runs_logs_retrieve.md

# batch_exports_runs_logs_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/batch_exports/{batch_export_id}/runs/{id}/logs/
{
  "paths": {
    "/api/projects/{project_id}/batch_exports/{batch_export_id}/runs/{id}/logs/": {
      "get": {
        "operationId": "batch_exports_runs_logs_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "batch_export_id",
            "schema": {
              "type": "string",
              "format": "uuid",
              "description": "The BatchExport this run belongs to."
            },
            "required": true
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this batch export run.",
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
          "batch_exports",
          "batch_exports"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
