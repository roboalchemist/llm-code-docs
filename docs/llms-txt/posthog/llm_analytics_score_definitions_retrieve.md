# Source: https://posthog.com/docs/open-api-spec/llm_analytics_score_definitions_retrieve.md

# llm_analytics_score_definitions_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/llm_analytics/score_definitions/{id}/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/score_definitions/{id}/": {
      "get": {
        "operationId": "llm_analytics_score_definitions_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this score definition.",
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
          "llm_analytics",
          "llm_analytics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "llm_analytics:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ScoreDefinition"
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
      "ScoreDefinition": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "description": {
            "type": "string",
            "readOnly": true
          },
          "kind": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Kind01eEnum"
              }
            ],
            "readOnly": true
          },
          "archived": {
            "type": "boolean",
            "readOnly": true
          },
          "current_version": {
            "type": "integer",
            "readOnly": true,
            "description": "Current immutable configuration version number."
          },
          "config": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ScoreDefinitionConfig"
              }
            ],
            "readOnly": true,
            "description": "Current immutable scorer configuration."
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true,
            "nullable": true,
            "description": "User who created the scorer."
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
          },
          "team": {
            "type": "integer",
            "readOnly": true
          }
        },
        "required": [
          "archived",
          "config",
          "created_at",
          "created_by",
          "current_version",
          "description",
          "id",
          "kind",
          "name",
          "team",
          "updated_at"
        ]
      },
      "Kind01eEnum": {
        "enum": [
          "categorical",
          "numeric",
          "boolean"
        ],
        "type": "string",
        "description": "* `categorical` - categorical\n* `numeric` - numeric\n* `boolean` - boolean"
      },
      "ScoreDefinitionConfig": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/CategoricalScoreDefinitionConfig"
          },
          {
            "$ref": "#/components/schemas/NumericScoreDefinitionConfig"
          },
          {
            "$ref": "#/components/schemas/BooleanScoreDefinitionConfig"
          }
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
      "CategoricalScoreDefinitionConfig": {
        "type": "object",
        "properties": {
          "options": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CategoricalScoreOption"
            },
            "description": "Ordered categorical options available to the scorer."
          },
          "selection_mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SelectionModeEnum"
              }
            ],
            "description": "Whether reviewers can select one option or multiple options. Defaults to `single`.\n\n* `single` - single\n* `multiple` - multiple"
          },
          "min_selections": {
            "type": "integer",
            "minimum": 1,
            "nullable": true,
            "description": "Optional minimum number of options that can be selected when `selection_mode` is `multiple`."
          },
          "max_selections": {
            "type": "integer",
            "minimum": 1,
            "nullable": true,
            "description": "Optional maximum number of options that can be selected when `selection_mode` is `multiple`."
          }
        },
        "required": [
          "options"
        ]
      },
      "NumericScoreDefinitionConfig": {
        "type": "object",
        "properties": {
          "min": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Optional inclusive minimum score."
          },
          "max": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Optional inclusive maximum score."
          },
          "step": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Optional increment step for numeric input, for example 1 or 0.5."
          }
        }
      },
      "BooleanScoreDefinitionConfig": {
        "type": "object",
        "properties": {
          "true_label": {
            "type": "string",
            "description": "Optional label for a true value."
          },
          "false_label": {
            "type": "string",
            "description": "Optional label for a false value."
          }
        }
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
      },
      "CategoricalScoreOption": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Stable option key. Use lowercase letters, numbers, underscores, or hyphens.",
            "maxLength": 128
          },
          "label": {
            "type": "string",
            "description": "Human-readable option label.",
            "maxLength": 256
          }
        },
        "required": [
          "key",
          "label"
        ]
      },
      "SelectionModeEnum": {
        "enum": [
          "single",
          "multiple"
        ],
        "type": "string",
        "description": "* `single` - single\n* `multiple` - multiple"
      }
    }
  }
}
```
