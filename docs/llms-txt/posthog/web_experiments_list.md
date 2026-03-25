# Source: https://posthog.com/docs/open-api-spec/web_experiments_list.md

# web_experiments_list

## OpenAPI

```json GET /api/projects/{project_id}/web_experiments/
{
  "paths": {
    "/api/projects/{project_id}/web_experiments/": {
      "get": {
        "operationId": "web_experiments_list",
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
          "web_experiments"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedWebExperimentsAPIList"
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
      "PaginatedWebExperimentsAPIList": {
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
              "$ref": "#/components/schemas/WebExperimentsAPI"
            }
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
