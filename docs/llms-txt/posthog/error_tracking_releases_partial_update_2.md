# Source: https://posthog.com/docs/open-api-spec/error_tracking_releases_partial_update_2.md

# error_tracking_releases_partial_update_2

## OpenAPI

```json PATCH /api/projects/{project_id}/error_tracking/releases/{id}/
{
  "paths": {
    "/api/projects/{project_id}/error_tracking/releases/{id}/": {
      "patch": {
        "operationId": "error_tracking_releases_partial_update_2",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking release.",
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
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingRelease"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingRelease"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingRelease"
              }
            }
          }
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
                  "$ref": "#/components/schemas/ErrorTrackingRelease"
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
      "PatchedErrorTrackingRelease": {
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
