# Source: https://posthog.com/docs/open-api-spec/mcp_servers_list.md

# mcp_servers_list

## OpenAPI

```json GET /api/environments/{project_id}/mcp_servers/
{
  "paths": {
    "/api/environments/{project_id}/mcp_servers/": {
      "get": {
        "operationId": "mcp_servers_list",
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
          "mcp_servers"
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
                  "$ref": "#/components/schemas/PaginatedRecommendedServerList"
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
      "PaginatedRecommendedServerList": {
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
              "$ref": "#/components/schemas/RecommendedServer"
            }
          }
        }
      },
      "RecommendedServer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "url": {
            "type": "string",
            "format": "uri"
          },
          "description": {
            "type": "string"
          },
          "auth_type": {
            "$ref": "#/components/schemas/RecommendedServerAuthTypeEnum"
          },
          "oauth_provider_kind": {
            "type": "string",
            "default": ""
          }
        },
        "required": [
          "auth_type",
          "description",
          "name",
          "url"
        ]
      },
      "RecommendedServerAuthTypeEnum": {
        "enum": [
          "none",
          "api_key",
          "oauth"
        ],
        "type": "string",
        "description": "* `none` - none\n* `api_key` - api_key\n* `oauth` - oauth"
      }
    }
  }
}
```
