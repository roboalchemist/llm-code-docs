# Source: https://posthog.com/docs/open-api-spec/elements_retrieve.md

# elements_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/elements/{id}/
{
  "paths": {
    "/api/projects/{project_id}/elements/{id}/": {
      "get": {
        "operationId": "elements_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this element.",
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
          "product_analytics",
          "elements"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "element:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
