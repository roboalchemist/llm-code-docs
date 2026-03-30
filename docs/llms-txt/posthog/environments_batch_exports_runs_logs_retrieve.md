# Source: https://posthog.com/docs/open-api-spec/environments_batch_exports_runs_logs_retrieve.md

# environments_batch_exports_runs_logs_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/batch_exports/{batch_export_id}/runs/{id}/logs/
{
  "paths": {
    "/api/environments/{environment_id}/batch_exports/{batch_export_id}/runs/{id}/logs/": {
      "get": {
        "operationId": "environments_batch_exports_runs_logs_retrieve",
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
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
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
        "deprecated": true,
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
