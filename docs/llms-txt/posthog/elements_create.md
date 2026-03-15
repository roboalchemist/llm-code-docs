# Source: https://posthog.com/docs/open-api-spec/elements_create.md

# elements_create

## OpenAPI

```json POST /api/projects/{project_id}/elements/
{
  "paths": {
    "/api/projects/{project_id}/elements/": {
      "post": {
        "operationId": "elements_create",
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
          "product_analytics",
          "elements"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Element"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Element"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Element"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "element:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Element"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "product_analytics"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Element": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string",
            "nullable": true,
            "maxLength": 10000
          },
          "tag_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 1000
          },
          "attr_class": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 200
            },
            "nullable": true
          },
          "href": {
            "type": "string",
            "nullable": true,
            "maxLength": 10000
          },
          "attr_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 10000
          },
          "nth_child": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "nth_of_type": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "attributes": {},
          "order": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          }
        }
      }
    }
  }
}
```
