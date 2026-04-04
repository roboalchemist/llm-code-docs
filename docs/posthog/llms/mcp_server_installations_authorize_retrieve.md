# Source: https://posthog.com/docs/open-api-spec/mcp_server_installations_authorize_retrieve.md

# mcp_server_installations_authorize_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/mcp_server_installations/authorize/
{
  "paths": {
    "/api/environments/{project_id}/mcp_server_installations/authorize/": {
      "get": {
        "operationId": "mcp_server_installations_authorize_retrieve",
        "parameters": [
          {
            "in": "query",
            "name": "install_source",
            "schema": {
              "enum": [
                "posthog",
                "posthog-code"
              ],
              "type": "string",
              "default": "posthog",
              "minLength": 1
            },
            "description": "* `posthog` - posthog\n* `posthog-code` - posthog-code"
          },
          {
            "in": "query",
            "name": "posthog_code_callback_url",
            "schema": {
              "type": "string",
              "default": ""
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
            "name": "server_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
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
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "mcp_store"
        ]
      }
    }
  }
}
```
