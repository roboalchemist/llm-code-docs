# Source: https://posthog.com/docs/open-api-spec/error_tracking_releases_list_2.md

# error_tracking_releases_list_2

## OpenAPI

```json GET /api/projects/{project_id}/error_tracking/releases/
{
  "paths": {
    "/api/projects/{project_id}/error_tracking/releases/": {
      "get": {
        "operationId": "error_tracking_releases_list_2",
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
                  "$ref": "#/components/schemas/PaginatedErrorTrackingReleaseList"
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
      "PaginatedErrorTrackingReleaseList": {
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
              "$ref": "#/components/schemas/ErrorTrackingRelease"
            }
          }
        }
      },
      "ErrorTrackingRelease": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "hash_id": {
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
          "metadata": {
            "nullable": true
          },
          "version": {
            "type": "string"
          },
          "project": {
            "type": "string"
          }
        },
        "required": [
          "created_at",
          "hash_id",
          "id",
          "project",
          "team_id",
          "version"
        ]
      }
    }
  }
}
```
