# Source: https://posthog.com/docs/open-api-spec/environments_query_retrieve.md

# environments_query_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/query/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/query/{id}/": {
      "get": {
        "operationId": "environments_query_retrieve",
        "description": "(Experimental)",
        "parameters": [
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
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "query"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/QueryStatusResponse"
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
      "QueryStatusResponse": {
        "additionalProperties": false,
        "properties": {
          "query_status": {
            "$ref": "#/components/schemas/QueryStatus"
          }
        },
        "required": [
          "query_status"
        ],
        "title": "QueryStatusResponse",
        "type": "object"
      },
      "QueryStatus": {
        "additionalProperties": false,
        "properties": {
          "complete": {
            "default": false,
            "description": "Whether the query is still running. Will be true if the query is complete, even if it errored. Either result or error will be set.",
            "title": "Complete",
            "type": "boolean",
            "nullable": true
          },
          "dashboard_id": {
            "default": null,
            "title": "Dashboard Id",
            "type": "integer",
            "nullable": true
          },
          "end_time": {
            "default": null,
            "description": "When did the query execution task finish (whether successfully or not).",
            "title": "End Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "error": {
            "default": false,
            "description": "If the query failed, this will be set to true. More information can be found in the error_message field.",
            "title": "Error",
            "type": "boolean",
            "nullable": true
          },
          "error_message": {
            "default": null,
            "title": "Error Message",
            "type": "string",
            "nullable": true
          },
          "expiration_time": {
            "default": null,
            "title": "Expiration Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "insight_id": {
            "default": null,
            "title": "Insight Id",
            "type": "integer",
            "nullable": true
          },
          "labels": {
            "default": null,
            "title": "Labels",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "pickup_time": {
            "default": null,
            "description": "When was the query execution task picked up by a worker.",
            "title": "Pickup Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "query_async": {
            "default": true,
            "description": "ONLY async queries use QueryStatus.",
            "title": "Query Async",
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "query_progress": {
            "default": null,
            "$ref": "#/components/schemas/ClickhouseQueryProgress",
            "nullable": true
          },
          "results": {
            "default": null,
            "title": "Results",
            "nullable": true
          },
          "start_time": {
            "default": null,
            "description": "When was query execution task enqueued.",
            "title": "Start Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "task_id": {
            "default": null,
            "title": "Task Id",
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "title": "Team Id",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "team_id"
        ],
        "title": "QueryStatus",
        "type": "object"
      },
      "ClickhouseQueryProgress": {
        "additionalProperties": false,
        "properties": {
          "active_cpu_time": {
            "title": "Active Cpu Time",
            "type": "integer"
          },
          "bytes_read": {
            "title": "Bytes Read",
            "type": "integer"
          },
          "estimated_rows_total": {
            "title": "Estimated Rows Total",
            "type": "integer"
          },
          "rows_read": {
            "title": "Rows Read",
            "type": "integer"
          },
          "time_elapsed": {
            "title": "Time Elapsed",
            "type": "integer"
          }
        },
        "required": [
          "active_cpu_time",
          "bytes_read",
          "estimated_rows_total",
          "rows_read",
          "time_elapsed"
        ],
        "title": "ClickhouseQueryProgress",
        "type": "object"
      }
    }
  }
}
```
