# Source: https://posthog.com/docs/open-api-spec/mcp_server_installations_install_custom_create.md

# mcp_server_installations_install_custom_create

## OpenAPI

```json POST /api/environments/{project_id}/mcp_server_installations/install_custom/
{
  "paths": {
    "/api/environments/{project_id}/mcp_server_installations/install_custom/": {
      "post": {
        "operationId": "mcp_server_installations_install_custom_create",
        "parameters": [
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
                "$ref": "#/components/schemas/InstallCustom"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/InstallCustom"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/InstallCustom"
              }
            }
          },
          "required": true
        },
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
                  "$ref": "#/components/schemas/OAuthRedirectResponse"
                }
              }
            },
            "description": ""
          },
          "201": {
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
      "InstallCustom": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "maxLength": 200
          },
          "url": {
            "type": "string",
            "format": "uri",
            "maxLength": 2048
          },
          "auth_type": {
            "$ref": "#/components/schemas/InstallCustomAuthTypeEnum"
          },
          "api_key": {
            "type": "string",
            "default": ""
          },
          "description": {
            "type": "string",
            "default": ""
          },
          "oauth_provider_kind": {
            "type": "string",
            "default": ""
          },
          "install_source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InstallSourceEnum"
              }
            ],
            "default": "posthog"
          },
          "posthog_code_callback_url": {
            "type": "string",
            "default": ""
          }
        },
        "required": [
          "auth_type",
          "name",
          "url"
        ]
      },
      "OAuthRedirectResponse": {
        "type": "object",
        "properties": {
          "redirect_url": {
            "type": "string",
            "format": "uri"
          }
        },
        "required": [
          "redirect_url"
        ]
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
      "InstallCustomAuthTypeEnum": {
        "enum": [
          "api_key",
          "oauth"
        ],
        "type": "string",
        "description": "* `api_key` - api_key\n* `oauth` - oauth"
      },
      "InstallSourceEnum": {
        "enum": [
          "posthog",
          "posthog-code"
        ],
        "type": "string",
        "description": "* `posthog` - posthog\n* `posthog-code` - posthog-code"
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
