# Source: https://docs.akeyless.io/reference/rotatedsecretdelete.md

# /rotated-secret-delete

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
    "/rotated-secret-delete": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretDelete",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretDelete"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretDeleteResponse"
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
      "rotatedSecretDeleteResponse": {
        "description": "rotatedSecretDeleteResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/DeleteItemOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "DeleteItemOutput": {
        "type": "object",
        "title": "DeleteItemOutput defines output of DeleteItem operation.",
        "properties": {
          "deletion_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "DeletionDate"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "item_name": {
            "type": "string",
            "x-go-name": "ItemName"
          },
          "version_deleted": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "VersionDeleted"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
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
      "rotatedSecretDelete": {
        "description": "rotatedSecretDelete is a command that deletes a rotated secret",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Rotated secret name",
            "type": "string",
            "x-go-name": "RsName"
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
          "version": {
            "description": "The specific version you want to delete, -1=entire item with all versions (default)",
            "type": "integer",
            "format": "int32",
            "default": -1,
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```