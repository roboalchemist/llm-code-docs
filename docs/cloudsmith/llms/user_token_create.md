# Source: https://help.cloudsmith.io/reference/user_token_create.md

# Create or retrieve API token for a user.

Handles both:
- Users authenticating with basic credentials to get a token
- Two-factor authentication flow

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
    "/user/token/": {
      "post": {
        "operationId": "user_token_create",
        "summary": "Create or retrieve API token for a user.",
        "description": "Handles both:\n- Users authenticating with basic credentials to get a token\n- Two-factor authentication flow",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserAuthTokenRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Retrieved/created user API token/key.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserAuthToken"
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
          "403": {
            "description": "Locked out.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Failed to authenticate.",
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
        ],
        "security": [
          {
            "basic": []
          }
        ]
      },
      "parameters": []
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
      "UserAuthTokenRequest": {
        "type": "object",
        "properties": {
          "email": {
            "title": "Email",
            "description": "Email address to authenticate with",
            "type": "string",
            "format": "email",
            "minLength": 1
          },
          "password": {
            "title": "Password",
            "description": "Password to authenticate with",
            "type": "string",
            "minLength": 1
          },
          "totp_token": {
            "title": "Two-factor code",
            "description": "Two-factor authentication code",
            "type": "string",
            "minLength": 1
          }
        }
      },
      "UserAuthToken": {
        "type": "object",
        "properties": {
          "token": {
            "title": "Token",
            "description": "API token for the authenticated user",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "two_factor_required": {
            "title": "Two factor required",
            "description": "Flag indicating whether a 2FA code is required to complete authentication",
            "type": "boolean",
            "readOnly": true
          },
          "two_factor_token": {
            "title": "Two factor token",
            "description": "Token to use when providing 2FA code",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          }
        }
      }
    }
  }
}
```