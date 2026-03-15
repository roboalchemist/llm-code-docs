# Source: https://posthog.com/docs/open-api-spec/flag_value_values_retrieve.md

# flag_value_values_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/flag_value/values/
{
  "paths": {
    "/api/projects/{project_id}/flag_value/values/": {
      "get": {
        "operationId": "flag_value_values_retrieve",
        "description": "Get possible values for a feature flag.\n\nQuery parameters:\n- key: The flag ID (required)\nReturns:\n\n- Array of objects with 'name' field containing possible values",
        "parameters": [
          {
            "in": "query",
            "name": "key",
            "schema": {
              "type": "string"
            },
            "description": "The flag ID"
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
          "flag_value"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FlagValueResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Unspecified response body"
                }
              }
            },
            "description": ""
          },
          "404": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Unspecified response body"
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
      "FlagValueResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FlagValueItem"
            }
          },
          "refreshing": {
            "type": "boolean"
          }
        },
        "required": [
          "refreshing",
          "results"
        ]
      },
      "FlagValueItem": {
        "type": "object",
        "properties": {
          "name": {}
        },
        "required": [
          "name"
        ]
      }
    }
  }
}
```
