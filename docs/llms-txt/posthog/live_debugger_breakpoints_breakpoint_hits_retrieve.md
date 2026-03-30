# Source: https://posthog.com/docs/open-api-spec/live_debugger_breakpoints_breakpoint_hits_retrieve.md

# live_debugger_breakpoints_breakpoint_hits_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/live_debugger_breakpoints/breakpoint_hits/
{
  "paths": {
    "/api/projects/{project_id}/live_debugger_breakpoints/breakpoint_hits/": {
      "get": {
        "operationId": "live_debugger_breakpoints_breakpoint_hits_retrieve",
        "description": "Retrieve breakpoint hit events from ClickHouse with optional filtering and pagination. Returns hit events containing stack traces, local variables, and execution context from your application's runtime. \n\nSecurity: Breakpoint IDs are filtered to only include those belonging to the current team.",
        "summary": "Get breakpoint hits",
        "parameters": [
          {
            "in": "query",
            "name": "breakpoint_ids",
            "schema": {
              "type": "string"
            },
            "description": "Filter hits for specific breakpoints (repeat parameter for multiple IDs, e.g., ?breakpoint_ids=uuid1&breakpoint_ids=uuid2)"
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer"
            },
            "description": "Number of hits to return (default: 100, max: 1000)"
          },
          {
            "in": "query",
            "name": "offset",
            "schema": {
              "type": "integer"
            },
            "description": "Pagination offset for retrieving additional results (default: 0)"
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
                  "$ref": "#/components/schemas/BreakpointHitsResponse"
                }
              }
            },
            "description": "List of breakpoint hits with pagination info"
          },
          "400": {
            "description": "Invalid query parameters (invalid UUID, limit out of range, etc.)"
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
      "BreakpointHitsResponse": {
        "type": "object",
        "description": "Response schema for breakpoint hits endpoint",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BreakpointHit"
            },
            "description": "List of breakpoint hit events"
          },
          "count": {
            "type": "integer",
            "description": "Number of results returned"
          },
          "has_more": {
            "type": "boolean",
            "description": "Whether there are more results available"
          }
        },
        "required": [
          "count",
          "has_more",
          "results"
        ]
      },
      "BreakpointHit": {
        "type": "object",
        "description": "Schema for a single breakpoint hit event",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Unique identifier for the hit event"
          },
          "lineNumber": {
            "type": "integer",
            "description": "Line number where the breakpoint was hit"
          },
          "functionName": {
            "type": "string",
            "description": "Name of the function where breakpoint was hit"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "When the breakpoint was hit"
          },
          "variables": {
            "type": "object",
            "additionalProperties": {},
            "description": "Local variables at the time of the hit"
          },
          "stackTrace": {
            "type": "array",
            "items": {},
            "description": "Stack trace at the time of the hit"
          },
          "breakpoint_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of the breakpoint that was hit"
          },
          "filename": {
            "type": "string",
            "description": "Filename where the breakpoint was hit"
          }
        },
        "required": [
          "breakpoint_id",
          "filename",
          "functionName",
          "id",
          "lineNumber",
          "stackTrace",
          "timestamp",
          "variables"
        ]
      }
    }
  }
}
```
