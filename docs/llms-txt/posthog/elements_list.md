# Source: https://posthog.com/docs/open-api-spec/elements_list.md

# elements_list

## OpenAPI

```json GET /api/projects/{project_id}/elements/
{
  "paths": {
    "/api/projects/{project_id}/elements/": {
      "get": {
        "operationId": "elements_list",
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
                  "$ref": "#/components/schemas/PaginatedElementList"
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
      "PaginatedElementList": {
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
              "$ref": "#/components/schemas/Element"
            }
          }
        }
      },
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
