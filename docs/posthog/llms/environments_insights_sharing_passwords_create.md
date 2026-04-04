# Source: https://posthog.com/docs/open-api-spec/environments_insights_sharing_passwords_create.md

# environments_insights_sharing_passwords_create

## OpenAPI

```json POST /api/environments/{environment_id}/insights/{insight_id}/sharing/passwords/
{
  "paths": {
    "/api/environments/{environment_id}/insights/{insight_id}/sharing/passwords/": {
      "post": {
        "operationId": "environments_insights_sharing_passwords_create",
        "description": "Create a new password for the sharing configuration.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "insight_id",
            "schema": {
              "type": "integer"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "insights"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "sharing_configuration:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SharingConfiguration"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "SharingConfiguration": {
        "type": "object",
        "properties": {
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "enabled": {
            "type": "boolean"
          },
          "access_token": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "settings": {
            "nullable": true
          },
          "password_required": {
            "type": "boolean"
          },
          "share_passwords": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "access_token",
          "created_at",
          "share_passwords"
        ]
      }
    }
  }
}
```
