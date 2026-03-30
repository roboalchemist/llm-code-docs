# Source: https://posthog.com/docs/open-api-spec/error_tracking_symbol_sets_list.md

# error_tracking_symbol_sets_list

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/symbol_sets/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/symbol_sets/": {
      "get": {
        "operationId": "error_tracking_symbol_sets_list",
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
          "error_tracking",
          "error_tracking"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "error_tracking:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedErrorTrackingSymbolSetList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "error_tracking"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedErrorTrackingSymbolSetList": {
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
              "$ref": "#/components/schemas/ErrorTrackingSymbolSet"
            }
          }
        }
      },
      "ErrorTrackingSymbolSet": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "ref": {
            "type": "string"
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "last_used": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "storage_ptr": {
            "type": "string",
            "nullable": true
          },
          "failure_reason": {
            "type": "string",
            "nullable": true
          },
          "release": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "id",
          "ref",
          "release",
          "team_id"
        ]
      }
    }
  }
}
```
