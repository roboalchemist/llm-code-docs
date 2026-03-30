# Source: https://posthog.com/docs/open-api-spec/llm_prompts_resolve_name_retrieve.md

# llm_prompts_resolve_name_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/llm_prompts/resolve/name/{prompt_name}/
{
  "paths": {
    "/api/environments/{project_id}/llm_prompts/resolve/name/{prompt_name}/": {
      "get": {
        "operationId": "llm_prompts_resolve_name_retrieve",
        "parameters": [
          {
            "in": "query",
            "name": "before_version",
            "schema": {
              "type": "integer",
              "minimum": 1
            },
            "description": "Return versions older than this version number. Mutually exclusive with offset."
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "maximum": 100,
              "minimum": 1,
              "default": 50
            },
            "description": "Maximum number of versions to return per page (1-100)."
          },
          {
            "in": "query",
            "name": "offset",
            "schema": {
              "type": "integer",
              "minimum": 0
            },
            "description": "Zero-based offset into version history for pagination. Mutually exclusive with before_version."
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
            "in": "path",
            "name": "prompt_name",
            "schema": {
              "type": "string",
              "pattern": "^[^/]+$"
            },
            "required": true
          },
          {
            "in": "query",
            "name": "version",
            "schema": {
              "type": "integer",
              "minimum": 1
            },
            "description": "Specific prompt version to fetch. If omitted, the latest version is returned."
          },
          {
            "in": "query",
            "name": "version_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "Exact prompt version UUID to resolve. Can be used together with version for extra safety."
          }
        ],
        "tags": [
          "llm_analytics",
          "llm_prompts"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "llm_prompt:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LLMPromptResolveResponse"
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
      "LLMPromptResolveResponse": {
        "type": "object",
        "properties": {
          "prompt": {
            "$ref": "#/components/schemas/LLMPrompt"
          },
          "versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LLMPromptVersionSummary"
            }
          },
          "has_more": {
            "type": "boolean"
          }
        },
        "required": [
          "has_more",
          "prompt",
          "versions"
        ]
      },
      "LLMPrompt": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "description": "Unique prompt name using letters, numbers, hyphens, and underscores only.",
            "maxLength": 255
          },
          "prompt": {
            "description": "Prompt payload as JSON or string data."
          },
          "version": {
            "type": "integer",
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
          "deleted": {
            "type": "boolean",
            "readOnly": true
          },
          "is_latest": {
            "type": "boolean",
            "readOnly": true
          },
          "latest_version": {
            "type": "integer",
            "readOnly": true
          },
          "version_count": {
            "type": "integer",
            "readOnly": true
          },
          "first_version_created_at": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "deleted",
          "first_version_created_at",
          "id",
          "is_latest",
          "latest_version",
          "name",
          "prompt",
          "updated_at",
          "version",
          "version_count"
        ]
      },
      "LLMPromptVersionSummary": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "version": {
            "type": "integer",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "is_latest": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "id",
          "is_latest",
          "version"
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
