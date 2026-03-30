# Source: https://docs.mystic.ai/reference/owned_or_used_v4_pipelines_owned_or_used_get.md

# Owned Or Used

Get a lean list of pipelines that the user has either used or owns.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/pipelines/owned-or-used": {
      "get": {
        "tags": [
          "Pipelines"
        ],
        "summary": "Owned Or Used",
        "description": "Get a lean list of pipelines that the user has either used or owns.",
        "operationId": "owned_or_used_v4_pipelines_owned_or_used_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/GetLean"
                  },
                  "type": "array",
                  "title": "Response Owned Or Used V4 Pipelines Owned Or Used Get"
                }
              }
            }
          }
        },
        "security": [
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "GetLean": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "pointers": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Pointers"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "image_url": {
            "type": "string",
            "title": "Image Url"
          }
        },
        "type": "object",
        "required": [
          "id",
          "name",
          "pointers"
        ],
        "title": "GetLean",
        "description": "Base model for schemas."
      }
    },
    "securitySchemes": {
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```