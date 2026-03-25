# Source: https://posthog.com/docs/open-api-spec/evaluations_create.md

# evaluations_create

## OpenAPI

```json POST /api/environments/{project_id}/evaluations/
{
  "paths": {
    "/api/environments/{project_id}/evaluations/": {
      "post": {
        "operationId": "evaluations_create",
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
          "evaluations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Evaluation"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Evaluation"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Evaluation"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "evaluation:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Evaluation"
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
