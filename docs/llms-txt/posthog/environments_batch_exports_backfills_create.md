# Source: https://posthog.com/docs/open-api-spec/environments_batch_exports_backfills_create.md

# environments_batch_exports_backfills_create

## OpenAPI

```json POST /api/environments/{environment_id}/batch_exports/{batch_export_id}/backfills/
{
  "paths": {
    "/api/environments/{environment_id}/batch_exports/{batch_export_id}/backfills/": {
      "post": {
        "operationId": "environments_batch_exports_backfills_create",
        "description": "Create a new backfill for a BatchExport.",
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
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "batch_exports"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportBackfill"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportBackfill"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportBackfill"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "batch_export:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BatchExportBackfill"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
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
