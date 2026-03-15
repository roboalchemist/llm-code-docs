# Source: https://posthog.com/docs/open-api-spec/product_tours_generate_create.md

# product_tours_generate_create

## OpenAPI

```json POST /api/projects/{project_id}/product_tours/{id}/generate/
{
  "paths": {
    "/api/projects/{project_id}/product_tours/{id}/generate/": {
      "post": {
        "operationId": "product_tours_generate_create",
        "description": "Generate tour step content using AI.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this product tour.",
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
          "product_tours"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GenerateRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/GenerateRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/GenerateRequest"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "product_tour:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GenerateResponse"
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
      "GenerateRequest": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "default": ""
          },
          "goal": {
            "type": "string",
            "default": ""
          },
          "steps": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          }
        }
      },
      "GenerateResponse": {
        "type": "object",
        "properties": {
          "steps": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GenerateStepResponse"
            }
          }
        },
        "required": [
          "steps"
        ]
      },
      "GenerateStepResponse": {
        "type": "object",
        "properties": {
          "step_id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "description",
          "step_id",
          "title"
        ]
      }
    }
  }
}
```
