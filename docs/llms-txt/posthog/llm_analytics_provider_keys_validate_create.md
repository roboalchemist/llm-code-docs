# Source: https://posthog.com/docs/open-api-spec/llm_analytics_provider_keys_validate_create.md

# llm_analytics_provider_keys_validate_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/provider_keys/{id}/validate/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/provider_keys/{id}/validate/": {
      "post": {
        "operationId": "llm_analytics_provider_keys_validate_create",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this llm provider key.",
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
          "llm_analytics"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LLMProviderKey"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/LLMProviderKey"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/LLMProviderKey"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LLMProviderKey"
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
