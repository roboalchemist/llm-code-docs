# Source: https://docs.mystic.ai/reference/get_user_public_profile_v4_users__username__get.md

# Get User Public Profile

Retrieve a user's public profile

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
    "/v4/users/{username}": {
      "get": {
        "tags": [
          "Users"
        ],
        "summary": "Get User Public Profile",
        "description": "Retrieve a user's public profile",
        "operationId": "get_user_public_profile_v4_users__username__get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "pattern": "[a-z0-9][a-z0-9-_]{1,22}[a-z0-9]",
              "title": "Username"
            },
            "name": "username",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserPublicGet"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "UserPublicGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "username": {
            "type": "string",
            "title": "Username"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "avatar_colour": {
            "type": "string",
            "title": "Avatar Colour"
          }
        },
        "type": "object",
        "required": [
          "id",
          "username",
          "created_at"
        ],
        "title": "UserPublicGet",
        "description": "Base model for schemas."
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
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