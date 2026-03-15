# Source: https://posthog.com/docs/open-api-spec/mcp_server_installations_list.md

# mcp_server_installations_list

## OpenAPI

```json GET /api/environments/{project_id}/mcp_server_installations/
{
  "paths": {
    "/api/environments/{project_id}/mcp_server_installations/": {
      "get": {
        "operationId": "mcp_server_installations_list",
        "parameters": [
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
          }
        ],
        "tags": [
          "mcp_store",
          "mcp_server_installations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedMCPServerInstallationList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "mcp_store"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedMCPServerInstallationList": {
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
              "$ref": "#/components/schemas/MCPServerInstallation"
            }
          }
        }
      },
      "MCPServerInstallation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "server_id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "display_name": {
            "type": "string",
            "maxLength": 200
          },
          "url": {
            "type": "string",
            "format": "uri",
            "maxLength": 2048
          },
          "description": {
            "type": "string"
          },
          "auth_type": {
            "$ref": "#/components/schemas/MCPServerInstallationAuthTypeEnum"
          },
          "is_enabled": {
            "type": "boolean"
          },
          "needs_reauth": {
            "type": "boolean",
            "readOnly": true
          },
          "pending_oauth": {
            "type": "boolean",
            "readOnly": true
          },
          "proxy_url": {
            "type": "string",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "id",
          "name",
          "needs_reauth",
          "pending_oauth",
          "proxy_url",
          "server_id",
          "updated_at"
        ]
      },
      "MCPServerInstallationAuthTypeEnum": {
        "enum": [
          "api_key",
          "oauth"
        ],
        "type": "string",
        "description": "* `api_key` - API Key\n* `oauth` - OAuth"
      }
    }
  }
}
```
