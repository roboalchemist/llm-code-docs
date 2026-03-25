# Source: https://posthog.com/docs/open-api-spec/batch_exports_backfills_list.md

# batch_exports_backfills_list

## OpenAPI

```json GET /api/projects/{project_id}/batch_exports/{batch_export_id}/backfills/
{
  "paths": {
    "/api/projects/{project_id}/batch_exports/{batch_export_id}/backfills/": {
      "get": {
        "operationId": "batch_exports_backfills_list",
        "description": "ViewSet for BatchExportBackfill models.\n\nAllows creating and reading backfills, but not updating or deleting them.",
        "parameters": [
          {
            "in": "path",
            "name": "batch_export_id",
            "schema": {
              "type": "string",
              "format": "uuid",
              "description": "The BatchExport this backfill belongs to."
            },
            "required": true
          },
          {
            "name": "cursor",
            "required": false,
            "in": "query",
            "description": "The pagination cursor value.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ordering",
            "required": false,
            "in": "query",
            "description": "Which field to use when ordering the results.",
            "schema": {
              "type": "string"
            }
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
          "batch_exports"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "batch_export:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedBatchExportBackfillList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedBatchExportBackfillList": {
        "type": "object",
        "required": [
          "results"
        ],
        "properties": {
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?cursor=cD00ODY%3D\""
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?cursor=cj0xJnA9NDg3"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BatchExportBackfill"
            }
          }
        }
      },
      "BatchExportBackfill": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "progress": {
            "type": "string",
            "readOnly": true
          },
          "start_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The start of the data interval."
          },
          "end_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The end of the data interval."
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/BatchExportBackfillStatusEnum"
              }
            ],
            "description": "The status of this backfill.\n\n* `Cancelled` - Cancelled\n* `Completed` - Completed\n* `ContinuedAsNew` - Continued As New\n* `Failed` - Failed\n* `FailedRetryable` - Failed Retryable\n* `Terminated` - Terminated\n* `TimedOut` - Timedout\n* `Running` - Running\n* `Starting` - Starting"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "The timestamp at which this BatchExportBackfill was created."
          },
          "finished_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The timestamp at which this BatchExportBackfill finished, successfully or not."
          },
          "last_updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "The timestamp at which this BatchExportBackfill was last updated."
          },
          "total_records_count": {
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "format": "int64",
            "nullable": true,
            "description": "The total number of records to export. Initially estimated, updated with actual count after completion."
          },
          "adjusted_start_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The actual start time after adjustment for earliest available data. May differ from start_at if user requested a date before data exists."
          },
          "team": {
            "type": "integer",
            "description": "The team this belongs to."
          },
          "batch_export": {
            "type": "string",
            "format": "uuid",
            "description": "The BatchExport this backfill belongs to."
          }
        },
        "required": [
          "batch_export",
          "created_at",
          "id",
          "last_updated_at",
          "progress",
          "status",
          "team"
        ]
      },
      "BatchExportBackfillStatusEnum": {
        "enum": [
          "Cancelled",
          "Completed",
          "ContinuedAsNew",
          "Failed",
          "FailedRetryable",
          "Terminated",
          "TimedOut",
          "Running",
          "Starting"
        ],
        "type": "string",
        "description": "* `Cancelled` - Cancelled\n* `Completed` - Completed\n* `ContinuedAsNew` - Continued As New\n* `Failed` - Failed\n* `FailedRetryable` - Failed Retryable\n* `Terminated` - Terminated\n* `TimedOut` - Timedout\n* `Running` - Running\n* `Starting` - Starting"
      }
    }
  }
}
```
