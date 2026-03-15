# Source: https://docs.akeyless.io/reference/uidlistchildren.md

# /uid-list-children

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
    "/uid-list-children": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uidListChildren",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uidListChildren"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uidListChildrenResponse"
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
      "uidListChildrenResponse": {
        "description": "uidListChildrenResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UniversalIdentityDetails"
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
      "UIDTokenDetails": {
        "type": "object",
        "title": "UIDTokenDetails Universal identity type.",
        "properties": {
          "children": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/UIDTokenDetails"
            },
            "x-go-name": "Children"
          },
          "comment": {
            "type": "string",
            "x-go-name": "Comment"
          },
          "deny_inheritance": {
            "type": "boolean",
            "x-go-name": "DenyInheritance"
          },
          "deny_rotate": {
            "type": "boolean",
            "x-go-name": "DenyRotate"
          },
          "depth": {
            "type": "integer",
            "format": "uint16",
            "x-go-name": "Depth"
          },
          "expired_date": {
            "type": "string",
            "x-go-name": "ExpiredDate"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "last_rotate": {
            "type": "string",
            "x-go-name": "LastRotate"
          },
          "revoked": {
            "type": "boolean",
            "x-go-name": "Revoked"
          },
          "ttl": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "TTL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "UniversalIdentityDetails": {
        "type": "object",
        "title": "UniversalIdentityDetails Universal identity type.",
        "properties": {
          "max_depth": {
            "type": "integer",
            "format": "uint16",
            "x-go-name": "MaxDepth"
          },
          "number_of_tokens": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfTokens"
          },
          "root": {
            "$ref": "#/components/schemas/UIDTokenDetails"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "uidListChildren": {
        "description": "uidListChildren is a command that lists child token ids of Akeyless\nUniversal Identity.",
        "type": "object",
        "properties": {
          "auth-method-name": {
            "description": "The universal identity auth method name, required only when uid-token is not provided",
            "type": "string",
            "x-go-name": "AuthMethodName"
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
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```