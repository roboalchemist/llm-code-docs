# Source: https://posthog.com/docs/open-api-spec/live_debugger_breakpoints_list.md

# live_debugger_breakpoints_list

## OpenAPI

```json GET /api/projects/{project_id}/live_debugger_breakpoints/
{
  "paths": {
    "/api/projects/{project_id}/live_debugger_breakpoints/": {
      "get": {
        "operationId": "live_debugger_breakpoints_list",
        "description": "Create, Read, Update and Delete breakpoints for live debugging.",
        "parameters": [
          {
            "in": "query",
            "name": "filename",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
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
          },
          {
            "in": "query",
            "name": "repository",
            "schema": {
              "type": "string"
            }
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
                  "$ref": "#/components/schemas/PaginatedLiveDebuggerBreakpointList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "live_debugger"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedLiveDebuggerBreakpointList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LiveDebuggerBreakpoint"
            }
          }
        }
      },
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
