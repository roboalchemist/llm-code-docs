# Source: https://help.cloudsmith.io/reference/user_tokens_refresh.md

# Refresh the specified API key for the user that is currently authenticated.

Refresh the specified API key for the user that is currently authenticated.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/user/tokens/{slug_perm}/refresh/": {
      "put": {
        "operationId": "user_tokens_refresh",
        "summary": "Refresh the specified API key for the user that is currently authenticated.",
        "description": "Refresh the specified API key for the user that is currently authenticated.",
        "responses": {
          "200": {
            "description": "Successfully refreshed the API key.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserAuthenticationToken"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "The specified API key cannot be found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "user"
        ]
      },
      "parameters": [
        {
          "name": "slug_perm",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "UserAuthenticationToken": {
        "type": "object",
        "properties": {
          "created": {
            "title": "Created",
            "description": "The time at which the API key was created.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "key": {
            "title": "Key",
            "description": "The unique API key used for authentication. This will be obfuscated on read-only HTTP methods.",
            "type": "string",
            "readOnly": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "description": "The slug_perm for token.",
            "type": "string",
            "readOnly": true
          }
        }
      }
    }
  }
}
```