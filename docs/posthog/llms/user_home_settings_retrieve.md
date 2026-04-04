# Source: https://posthog.com/docs/open-api-spec/user_home_settings_retrieve.md

# user_home_settings_retrieve

## OpenAPI

```json GET /api/user_home_settings/{uuid}/
{
  "paths": {
    "/api/user_home_settings/{uuid}/": {
      "get": {
        "operationId": "user_home_settings_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "user_home_settings",
          "user_home_settings"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PinnedSceneTabs"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "user_home_settings"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PinnedSceneTabs": {
        "type": "object",
        "properties": {
          "tabs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PinnedSceneTab"
            }
          },
          "homepage": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PinnedSceneTab"
              }
            ],
            "nullable": true
          }
        }
      },
      "PinnedSceneTab": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "pathname": {
            "type": "string"
          },
          "search": {
            "type": "string"
          },
          "hash": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "customTitle": {
            "type": "string",
            "nullable": true
          },
          "iconType": {
            "type": "string"
          },
          "sceneId": {
            "type": "string",
            "nullable": true
          },
          "sceneKey": {
            "type": "string",
            "nullable": true
          },
          "sceneParams": {},
          "pinned": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
