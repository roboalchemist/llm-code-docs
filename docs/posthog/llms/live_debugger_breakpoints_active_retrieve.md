# Source: https://posthog.com/docs/open-api-spec/live_debugger_breakpoints_active_retrieve.md

# live_debugger_breakpoints_active_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/live_debugger_breakpoints/active/
{
  "paths": {
    "/api/projects/{project_id}/live_debugger_breakpoints/active/": {
      "get": {
        "operationId": "live_debugger_breakpoints_active_retrieve",
        "description": "External API endpoint for client applications to fetch active breakpoints using Project API key. This endpoint allows external client applications (like Python scripts, Node.js apps, etc.) to fetch the list of active breakpoints so they can instrument their code accordingly. \n\nAuthentication: Requires a Project API Key in the Authorization header: `Authorization: Bearer phs_<your-project-api-key>`. You can find your Project API Key in PostHog at: Settings → Project → Project API Key",
        "summary": "Get active breakpoints (External API)",
        "parameters": [
          {
            "in": "query",
            "name": "enabled",
            "schema": {
              "type": "boolean"
            },
            "description": "Only return enabled breakpoints"
          },
          {
            "in": "query",
            "name": "filename",
            "schema": {
              "type": "string"
            },
            "description": "Filter breakpoints for a specific file"
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
            },
            "description": "Filter breakpoints for a specific repository (e.g., 'PostHog/posthog')"
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
                  "$ref": "#/components/schemas/ActiveBreakpointsResponse"
                }
              }
            },
            "description": "List of breakpoints for client consumption"
          },
          "400": {
            "description": "Invalid query parameters"
          },
          "401": {
            "description": "Invalid or missing Project API key"
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
      "ActiveBreakpointsResponse": {
        "type": "object",
        "description": "Response schema for active breakpoints endpoint",
        "properties": {
          "breakpoints": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ActiveBreakpoint"
            },
            "description": "List of active breakpoints"
          }
        },
        "required": [
          "breakpoints"
        ]
      },
      "ActiveBreakpoint": {
        "type": "object",
        "description": "Schema for a single active breakpoint",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Unique identifier for the breakpoint"
          },
          "repository": {
            "type": "string",
            "nullable": true,
            "description": "Repository identifier (e.g., 'PostHog/posthog')"
          },
          "filename": {
            "type": "string",
            "description": "File path where the breakpoint is set"
          },
          "line_number": {
            "type": "integer",
            "description": "Line number of the breakpoint"
          },
          "enabled": {
            "type": "boolean",
            "description": "Whether the breakpoint is enabled"
          },
          "condition": {
            "type": "string",
            "nullable": true,
            "description": "Optional condition for the breakpoint"
          }
        },
        "required": [
          "enabled",
          "filename",
          "id",
          "line_number"
        ]
      }
    }
  }
}
```
