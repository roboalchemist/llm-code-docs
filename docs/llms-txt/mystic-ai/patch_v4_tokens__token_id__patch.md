# Source: https://docs.mystic.ai/reference/patch_v4_tokens__token_id__patch.md

# Patch

Update selected fields of an API Bearer token for an authenticated user.

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
    "/v4/tokens/{token_id}": {
      "patch": {
        "tags": [
          "Tokens"
        ],
        "summary": "Patch",
        "description": "Update selected fields of an API Bearer token for an authenticated user.",
        "operationId": "patch_v4_tokens__token_id__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Token Id"
            },
            "name": "token_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TokenPatch"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TokenGet"
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
      "TokenGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "title": "Updated At"
          },
          "value": {
            "type": "string",
            "title": "Value"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "title": "Expires At"
          },
          "last_used": {
            "type": "string",
            "format": "date-time",
            "title": "Last Used"
          },
          "is_active": {
            "type": "boolean",
            "title": "Is Active"
          },
          "is_enabled": {
            "type": "boolean",
            "title": "Is Enabled"
          },
          "team_id": {
            "type": "string",
            "title": "Team Id"
          }
        },
        "type": "object",
        "required": [
          "id",
          "created_at",
          "updated_at",
          "value",
          "name",
          "is_active",
          "is_enabled"
        ],
        "title": "TokenGet",
        "description": "API token representation when returned from an API call."
      },
      "TokenPatch": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "is_enabled": {
            "type": "boolean",
            "title": "Is Enabled"
          }
        },
        "additionalProperties": false,
        "type": "object",
        "title": "TokenPatch",
        "description": "Model for patching an API token"
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