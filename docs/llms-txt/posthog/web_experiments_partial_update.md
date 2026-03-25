# Source: https://posthog.com/docs/open-api-spec/web_experiments_partial_update.md

# web_experiments_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/web_experiments/{id}/
{
  "paths": {
    "/api/projects/{project_id}/web_experiments/{id}/": {
      "patch": {
        "operationId": "web_experiments_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this web experiment.",
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
          "web_experiments"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedWebExperimentsAPI"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedWebExperimentsAPI"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedWebExperimentsAPI"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WebExperimentsAPI"
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
      "PatchedWebExperimentsAPI": {
        "type": "object",
        "description": "Serializer for the exposed /api/web_experiments endpoint, to be used in posthog-js and for headless APIs.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "feature_flag_key": {
            "type": "string",
            "readOnly": true
          },
          "variants": {
            "description": "Variants for the web experiment. Example:\n\n        {\n            \"control\": {\n                \"transforms\": [\n                    {\n                        \"text\": \"Here comes Superman!\",\n                        \"html\": \"\",\n                        \"selector\": \"#page > #body > .header h1\"\n                    }\n                ],\n                \"conditions\": \"None\",\n                \"rollout_percentage\": 50\n            },\n        }"
          }
        }
      },
      "WebExperimentsAPI": {
        "type": "object",
        "description": "Serializer for the exposed /api/web_experiments endpoint, to be used in posthog-js and for headless APIs.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "feature_flag_key": {
            "type": "string",
            "readOnly": true
          },
          "variants": {
            "description": "Variants for the web experiment. Example:\n\n        {\n            \"control\": {\n                \"transforms\": [\n                    {\n                        \"text\": \"Here comes Superman!\",\n                        \"html\": \"\",\n                        \"selector\": \"#page > #body > .header h1\"\n                    }\n                ],\n                \"conditions\": \"None\",\n                \"rollout_percentage\": 50\n            },\n        }"
          }
        },
        "required": [
          "feature_flag_key",
          "id",
          "name",
          "variants"
        ]
      }
    }
  }
}
```
