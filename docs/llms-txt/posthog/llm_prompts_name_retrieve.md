# Source: https://posthog.com/docs/open-api-spec/llm_prompts_name_retrieve.md

# llm_prompts_name_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/llm_prompts/name/{prompt_name}/
{
  "paths": {
    "/api/environments/{project_id}/llm_prompts/name/{prompt_name}/": {
      "get": {
        "operationId": "llm_prompts_name_retrieve",
        "parameters": [
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
                  "$ref": "#/components/schemas/LLMPromptPublic"
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
      "LLMPromptPublic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "name": {
            "type": "string"
          },
          "prompt": {},
          "version": {
            "type": "integer"
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time"
          },
          "deleted": {
            "type": "boolean"
          },
          "is_latest": {
            "type": "boolean"
          },
          "latest_version": {
            "type": "integer"
          },
          "version_count": {
            "type": "integer"
          },
          "first_version_created_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "created_at",
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
      }
    }
  }
}
```
