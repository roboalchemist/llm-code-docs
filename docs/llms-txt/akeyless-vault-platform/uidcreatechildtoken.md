# Source: https://docs.akeyless.io/reference/uidcreatechildtoken.md

# /uid-create-child-token

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/uid-create-child-token": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uidCreateChildToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uidCreateChildToken"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uidCreateChildTokenResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "uidCreateChildTokenResponse": {
        "description": "uidCreateChildTokenResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/uidCreateChildTokenOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "uidCreateChildToken": {
        "description": "uidCreateChildToken is a command that creates a new child token using\nAkeyless Universal Identity.",
        "type": "object",
        "properties": {
          "auth-method-name": {
            "description": "The universal identity auth method name, required only when uid-token is not provided",
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "child-deny-inheritance": {
            "description": "Deny from new child to create their own children",
            "type": "boolean",
            "x-go-name": "ChildDenyInheritance"
          },
          "child-deny-rotate": {
            "description": "Deny from new child to rotate",
            "type": "boolean",
            "x-go-name": "ChildDenyRotate"
          },
          "child-ttl": {
            "description": "New child token ttl",
            "type": "integer",
            "format": "int32",
            "x-go-name": "ChildTTL"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "uid-token-id": {
            "description": "The ID of the uid-token, required only when uid-token is not provided",
            "type": "string",
            "x-go-name": "UIDTokenId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "uidCreateChildTokenOutput": {
        "type": "object",
        "properties": {
          "token": {
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```