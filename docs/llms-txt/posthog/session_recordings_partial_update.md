# Source: https://posthog.com/docs/open-api-spec/session_recordings_partial_update.md

# session_recordings_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/session_recordings/{id}/
{
  "paths": {
    "/api/projects/{project_id}/session_recordings/{id}/": {
      "patch": {
        "operationId": "session_recordings_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this session recording.",
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
          "replay",
          "session_recordings"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecording"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecording"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecording"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SessionRecording"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedSessionRecording": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "viewed": {
            "type": "boolean",
            "readOnly": true
          },
          "viewers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "recording_duration": {
            "type": "integer",
            "readOnly": true
          },
          "active_seconds": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "inactive_seconds": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "start_time": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "end_time": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "click_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "keypress_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "mouse_activity_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_log_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_warn_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_error_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "start_url": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "person": {
            "$ref": "#/components/schemas/MinimalPerson"
          },
          "retention_period_days": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "expiry_time": {
            "type": "string",
            "readOnly": true
          },
          "recording_ttl": {
            "type": "string",
            "readOnly": true
          },
          "snapshot_source": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "snapshot_library": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "ongoing": {
            "type": "boolean",
            "readOnly": true
          },
          "activity_score": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "readOnly": true
          },
          "external_references": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Load external references (linked issues) for this recording",
            "readOnly": true
          }
        }
      },
      "SessionRecording": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "viewed": {
            "type": "boolean",
            "readOnly": true
          },
          "viewers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "recording_duration": {
            "type": "integer",
            "readOnly": true
          },
          "active_seconds": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "inactive_seconds": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "start_time": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "end_time": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "click_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "keypress_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "mouse_activity_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_log_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_warn_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "console_error_count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "start_url": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "person": {
            "$ref": "#/components/schemas/MinimalPerson"
          },
          "retention_period_days": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "expiry_time": {
            "type": "string",
            "readOnly": true
          },
          "recording_ttl": {
            "type": "string",
            "readOnly": true
          },
          "snapshot_source": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "snapshot_library": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "ongoing": {
            "type": "boolean",
            "readOnly": true
          },
          "activity_score": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "readOnly": true
          },
          "external_references": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Load external references (linked issues) for this recording",
            "readOnly": true
          }
        },
        "required": [
          "active_seconds",
          "activity_score",
          "click_count",
          "console_error_count",
          "console_log_count",
          "console_warn_count",
          "distinct_id",
          "end_time",
          "expiry_time",
          "external_references",
          "id",
          "inactive_seconds",
          "keypress_count",
          "mouse_activity_count",
          "ongoing",
          "recording_duration",
          "recording_ttl",
          "retention_period_days",
          "snapshot_library",
          "snapshot_source",
          "start_time",
          "start_url",
          "viewed",
          "viewers"
        ]
      },
      "MinimalPerson": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "distinct_ids": {
            "type": "string",
            "readOnly": true
          },
          "properties": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "last_seen_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "distinct_ids",
          "id",
          "last_seen_at",
          "name",
          "uuid"
        ]
      }
    }
  }
}
```
