# Source: https://posthog.com/docs/open-api-spec/desktop_recordings_update.md

# desktop_recordings_update

## OpenAPI

```json PUT /api/environments/{project_id}/desktop_recordings/{id}/
{
  "paths": {
    "/api/environments/{project_id}/desktop_recordings/{id}/": {
      "put": {
        "operationId": "desktop_recordings_update",
        "description": "RESTful API for managing desktop meeting recordings.\n\nStandard CRUD operations plus transcript management as a subresource.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this desktop recording.",
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
          "desktop_recordings",
          "desktop_recordings"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DesktopRecording"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/DesktopRecording"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/DesktopRecording"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "desktop_recording:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "desktop_recording:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DesktopRecording"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "desktop_recordings"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "DesktopRecording": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "team": {
            "type": "integer",
            "readOnly": true
          },
          "created_by": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "sdk_upload_id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "recall_recording_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "platform": {
            "$ref": "#/components/schemas/Platform9aaEnum"
          },
          "meeting_title": {
            "type": "string",
            "nullable": true,
            "maxLength": 255
          },
          "meeting_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "maxLength": 200
          },
          "duration_seconds": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "status": {
            "$ref": "#/components/schemas/Status292Enum"
          },
          "notes": {
            "type": "string",
            "nullable": true
          },
          "error_message": {
            "type": "string",
            "nullable": true
          },
          "video_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "maxLength": 200
          },
          "video_size_bytes": {
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "format": "int64",
            "nullable": true
          },
          "participants": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of participant names"
          },
          "transcript_text": {
            "type": "string",
            "readOnly": true
          },
          "transcript_segments": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TranscriptSegment"
            },
            "description": "Transcript segments with timestamps"
          },
          "summary": {
            "type": "string",
            "nullable": true
          },
          "extracted_tasks": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Task"
            },
            "description": "AI-extracted tasks from transcript"
          },
          "tasks_generated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "summary_generated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "started_at": {
            "type": "string",
            "format": "date-time"
          },
          "completed_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "id",
          "platform",
          "sdk_upload_id",
          "team",
          "transcript_text",
          "updated_at"
        ]
      },
      "Platform9aaEnum": {
        "enum": [
          "zoom",
          "teams",
          "meet",
          "desktop_audio",
          "slack"
        ],
        "type": "string",
        "description": "* `zoom` - Zoom\n* `teams` - Microsoft Teams\n* `meet` - Google Meet\n* `desktop_audio` - Desktop audio\n* `slack` - Slack huddle"
      },
      "Status292Enum": {
        "enum": [
          "recording",
          "uploading",
          "processing",
          "ready",
          "error"
        ],
        "type": "string",
        "description": "* `recording` - Recording\n* `uploading` - Uploading\n* `processing` - Processing\n* `ready` - Ready\n* `error` - Error"
      },
      "TranscriptSegment": {
        "type": "object",
        "description": "Serializer for individual transcript segments from AssemblyAI",
        "properties": {
          "timestamp": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Milliseconds from recording start"
          },
          "speaker": {
            "type": "string",
            "nullable": true
          },
          "text": {
            "type": "string"
          },
          "confidence": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Transcription confidence score"
          },
          "is_final": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether this is the final version"
          }
        },
        "required": [
          "text"
        ]
      },
      "Task": {
        "type": "object",
        "description": "Serializer for extracted tasks",
        "properties": {
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "assignee": {
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "title"
        ]
      }
    }
  }
}
```
