# Source: https://posthog.com/docs/open-api-spec/llm_analytics_provider_keys_list.md

# llm_analytics_provider_keys_list

## OpenAPI

```json GET /api/environments/{project_id}/llm_analytics/provider_keys/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/provider_keys/": {
      "get": {
        "operationId": "llm_analytics_provider_keys_list",
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
          "llm_analytics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "llm_provider_key:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedLLMProviderKeyList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "llm_analytics"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedLLMProviderKeyList": {
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
              "$ref": "#/components/schemas/LLMProviderKey"
            }
          }
        }
      },
      "LLMProviderKey": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "provider": {
            "$ref": "#/components/schemas/ProviderEnum"
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/LLMProviderKeyStateEnum"
              }
            ],
            "readOnly": true
          },
          "error_message": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "api_key": {
            "type": "string",
            "writeOnly": true
          },
          "api_key_masked": {
            "type": "string",
            "readOnly": true
          },
          "set_as_active": {
            "type": "boolean",
            "writeOnly": true,
            "default": false
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "last_used_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "api_key_masked",
          "created_at",
          "created_by",
          "error_message",
          "id",
          "last_used_at",
          "name",
          "provider",
          "state"
        ]
      },
      "ProviderEnum": {
        "enum": [
          "openai",
          "anthropic",
          "gemini",
          "openrouter",
          "fireworks"
        ],
        "type": "string",
        "description": "* `openai` - Openai\n* `anthropic` - Anthropic\n* `gemini` - Gemini\n* `openrouter` - Openrouter\n* `fireworks` - Fireworks"
      },
      "LLMProviderKeyStateEnum": {
        "enum": [
          "unknown",
          "ok",
          "invalid",
          "error"
        ],
        "type": "string",
        "description": "* `unknown` - Unknown\n* `ok` - Ok\n* `invalid` - Invalid\n* `error` - Error"
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
