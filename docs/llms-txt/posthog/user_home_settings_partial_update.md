# Source: https://posthog.com/docs/open-api-spec/user_home_settings_partial_update.md

# user_home_settings_partial_update

## OpenAPI

```json PATCH /api/user_home_settings/{uuid}/
{
  "paths": {
    "/api/user_home_settings/{uuid}/": {
      "patch": {
        "operationId": "user_home_settings_partial_update",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedPinnedSceneTabs"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedPinnedSceneTabs"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedPinnedSceneTabs"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user:write"
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
      "PatchedPinnedSceneTabs": {
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
