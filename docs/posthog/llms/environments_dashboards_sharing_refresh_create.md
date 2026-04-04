# Source: https://posthog.com/docs/open-api-spec/environments_dashboards_sharing_refresh_create.md

# environments_dashboards_sharing_refresh_create

## OpenAPI

```json POST /api/environments/{environment_id}/dashboards/{dashboard_id}/sharing/refresh/
{
  "paths": {
    "/api/environments/{environment_id}/dashboards/{dashboard_id}/sharing/refresh/": {
      "post": {
        "operationId": "environments_dashboards_sharing_refresh_create",
        "parameters": [
          {
            "in": "path",
            "name": "dashboard_id",
            "schema": {
              "type": "integer"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "core",
          "dashboards"
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
