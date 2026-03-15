# Source: https://posthog.com/docs/open-api-spec/evaluations_list.md

# evaluations_list

## OpenAPI

```json GET /api/environments/{project_id}/evaluations/
{
  "paths": {
    "/api/environments/{project_id}/evaluations/": {
      "get": {
        "operationId": "evaluations_list",
        "parameters": [
          {
            "in": "query",
            "name": "enabled",
            "schema": {
              "type": "boolean"
            },
            "description": "Filter by enabled status"
          },
          {
            "in": "query",
            "name": "id__in",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "format": "uuid"
              }
            },
            "description": "Multiple values may be separated by commas.",
            "explode": false,
            "style": "form"
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
            "in": "query",
            "name": "order_by",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "-created_at",
                  "-name",
                  "-updated_at",
                  "created_at",
                  "name",
                  "updated_at"
                ]
              }
            },
            "description": "Ordering\n\n* `created_at` - Created At\n* `-created_at` - Created At (descending)\n* `updated_at` - Updated At\n* `-updated_at` - Updated At (descending)\n* `name` - Name\n* `-name` - Name (descending)",
            "explode": false,
            "style": "form"
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
            "name": "search",
            "schema": {
              "type": "string"
            },
            "description": "Search in name or description"
          }
        ],
        "tags": [
          "evaluations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "evaluation:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedEvaluationList"
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
      "PaginatedEvaluationList": {
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
              "$ref": "#/components/schemas/Evaluation"
            }
          }
        }
      },
      "Evaluation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "description": {
            "type": "string"
          },
          "enabled": {
            "type": "boolean"
          },
          "evaluation_type": {
            "$ref": "#/components/schemas/EvaluationTypeEnum"
          },
          "evaluation_config": {},
          "output_type": {
            "$ref": "#/components/schemas/OutputTypeEnum"
          },
          "output_config": {},
          "conditions": {},
          "model_configuration": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ModelConfiguration"
              }
            ],
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
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "deleted": {
            "type": "boolean"
          }
        },
        "required": [
          "created_at",
          "created_by",
          "evaluation_type",
          "id",
          "name",
          "output_type",
          "updated_at"
        ]
      },
      "EvaluationTypeEnum": {
        "enum": [
          "llm_judge",
          "hog"
        ],
        "type": "string",
        "description": "* `llm_judge` - LLM as a judge\n* `hog` - Hog"
      },
      "OutputTypeEnum": {
        "enum": [
          "boolean"
        ],
        "type": "string",
        "description": "* `boolean` - Boolean (Pass/Fail)"
      },
      "ModelConfiguration": {
        "type": "object",
        "description": "Nested serializer for model configuration.",
        "properties": {
          "provider": {
            "$ref": "#/components/schemas/ProviderEnum"
          },
          "model": {
            "type": "string",
            "maxLength": 100
          },
          "provider_key_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "provider_key_name": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "required": [
          "model",
          "provider",
          "provider_key_name"
        ]
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
