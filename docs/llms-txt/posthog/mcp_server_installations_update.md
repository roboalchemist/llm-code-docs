# Source: https://posthog.com/docs/open-api-spec/mcp_server_installations_update.md

# mcp_server_installations_update

## OpenAPI

```json PUT /api/environments/{project_id}/mcp_server_installations/{id}/
{
  "paths": {
    "/api/environments/{project_id}/mcp_server_installations/{id}/": {
      "put": {
        "operationId": "mcp_server_installations_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this mcp server installation.",
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
          "mcp_store",
          "mcp_server_installations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MCPServerInstallation"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/MCPServerInstallation"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/MCPServerInstallation"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MCPServerInstallation"
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
