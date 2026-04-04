# Source: https://posthog.com/docs/open-api-spec/error_tracking_symbol_sets_update.md

# error_tracking_symbol_sets_update

## OpenAPI

```json PUT /api/environments/{project_id}/error_tracking/symbol_sets/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/symbol_sets/{id}/": {
      "put": {
        "operationId": "error_tracking_symbol_sets_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking symbol set.",
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
          "error_tracking",
          "error_tracking"
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingSymbolSet"
              }
            },
            "*/*": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingSymbolSet"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "error_tracking:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorTrackingSymbolSet"
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
