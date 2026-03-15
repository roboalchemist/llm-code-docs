# Source: https://posthog.com/docs/open-api-spec/batch_exports_runs_retry_create.md

# batch_exports_runs_retry_create

## OpenAPI

```json POST /api/projects/{project_id}/batch_exports/{batch_export_id}/runs/{id}/retry/
{
  "paths": {
    "/api/projects/{project_id}/batch_exports/{batch_export_id}/runs/{id}/retry/": {
      "post": {
        "operationId": "batch_exports_runs_retry_create",
        "description": "Retry a batch export run.\n\nWe use the same underlying mechanism as when backfilling a batch export, as retrying\na run is the same as backfilling one run.",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportRun"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportRun"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/BatchExportRun"
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
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "BatchExportRun": {
        "type": "object",
        "description": "Serializer for a BatchExportRun model.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/BatchExportRunStatusEnum"
              }
            ],
            "description": "The status of this run.\n\n* `Cancelled` - Cancelled\n* `Completed` - Completed\n* `ContinuedAsNew` - Continued As New\n* `Failed` - Failed\n* `FailedRetryable` - Failed Retryable\n* `FailedBilling` - Failed Billing\n* `Terminated` - Terminated\n* `TimedOut` - Timedout\n* `Running` - Running\n* `Starting` - Starting"
          },
          "records_completed": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true,
            "description": "The number of records that have been exported."
          },
          "latest_error": {
            "type": "string",
            "nullable": true,
            "description": "The latest error that occurred during this run."
          },
          "data_interval_start": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The start of the data interval."
          },
          "data_interval_end": {
            "type": "string",
            "format": "date-time",
            "description": "The end of the data interval."
          },
          "cursor": {
            "type": "string",
            "nullable": true,
            "description": "An opaque cursor that may be used to resume."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "The timestamp at which this BatchExportRun was created."
          },
          "finished_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "The timestamp at which this BatchExportRun finished, successfully or not."
          },
          "last_updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "The timestamp at which this BatchExportRun was last updated."
          },
          "records_total_count": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true,
            "description": "The total count of records that should be exported in this BatchExportRun."
          },
          "bytes_exported": {
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "format": "int64",
            "nullable": true,
            "description": "The number of bytes that have been exported in this BatchExportRun."
          },
          "batch_export": {
            "type": "string",
            "format": "uuid",
            "readOnly": true,
            "description": "The BatchExport this run belongs to."
          },
          "backfill": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "The backfill this run belongs to."
          }
        },
        "required": [
          "batch_export",
          "created_at",
          "data_interval_end",
          "id",
          "last_updated_at",
          "status"
        ]
      },
      "BatchExportRunStatusEnum": {
        "enum": [
          "Cancelled",
          "Completed",
          "ContinuedAsNew",
          "Failed",
          "FailedRetryable",
          "FailedBilling",
          "Terminated",
          "TimedOut",
          "Running",
          "Starting"
        ],
        "type": "string",
        "description": "* `Cancelled` - Cancelled\n* `Completed` - Completed\n* `ContinuedAsNew` - Continued As New\n* `Failed` - Failed\n* `FailedRetryable` - Failed Retryable\n* `FailedBilling` - Failed Billing\n* `Terminated` - Terminated\n* `TimedOut` - Timedout\n* `Running` - Running\n* `Starting` - Starting"
      }
    }
  }
}
```
