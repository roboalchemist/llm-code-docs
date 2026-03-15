# Source: https://posthog.com/docs/open-api-spec/web_experiments_create.md

# web_experiments_create

## OpenAPI

```json POST /api/projects/{project_id}/web_experiments/
{
  "paths": {
    "/api/projects/{project_id}/web_experiments/": {
      "post": {
        "operationId": "web_experiments_create",
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
          "web_experiments"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WebExperimentsAPI"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/WebExperimentsAPI"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/WebExperimentsAPI"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:write"
            ]
          }
        ],
        "responses": {
          "201": {
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
