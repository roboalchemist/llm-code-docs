# Source: https://posthog.com/docs/open-api-spec/error_tracking_fingerprints_retrieve.md

# error_tracking_fingerprints_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/fingerprints/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/fingerprints/{id}/": {
      "get": {
        "operationId": "error_tracking_fingerprints_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking issue fingerprint v2.",
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
                  "$ref": "#/components/schemas/ErrorTrackingFingerprint"
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
      "ErrorTrackingFingerprint": {
        "type": "object",
        "properties": {
          "fingerprint": {
            "type": "string"
          },
          "issue_id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "fingerprint",
          "issue_id"
        ]
      }
    }
  }
}
```
