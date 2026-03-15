# Source: https://posthog.com/docs/open-api-spec/live_debugger_breakpoints_retrieve.md

# live_debugger_breakpoints_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/live_debugger_breakpoints/{id}/
{
  "paths": {
    "/api/projects/{project_id}/live_debugger_breakpoints/{id}/": {
      "get": {
        "operationId": "live_debugger_breakpoints_retrieve",
        "description": "Create, Read, Update and Delete breakpoints for live debugging.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this live debugger breakpoint.",
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
          "live_debugger_breakpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "live_debugger:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LiveDebuggerBreakpoint"
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
      "LiveDebuggerBreakpoint": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "repository": {
            "type": "string",
            "nullable": true
          },
          "filename": {
            "type": "string"
          },
          "line_number": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "enabled": {
            "type": "boolean"
          },
          "condition": {
            "type": "string",
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
          "filename",
          "id",
          "line_number",
          "updated_at"
        ]
      }
    }
  }
}
```
