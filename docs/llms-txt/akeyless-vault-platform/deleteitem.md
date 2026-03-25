# Source: https://docs.akeyless.io/reference/deleteitem.md

# /delete-item

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
    "/delete-item": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "deleteItem",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/deleteItem"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/deleteItemResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        },
        "x-generate-protobuf": "true"
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
      "deleteItemResponse": {
        "description": "deleteItemResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/DeleteItemOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
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
      "deleteItem": {
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "delete-immediately": {
            "description": "When delete-in-days=-1, must be set",
            "type": "boolean",
            "default": false,
            "x-go-name": "DeleteImmediately"
          },
          "delete-in-days": {
            "description": "The number of days to wait before deleting the item (relevant for keys\nonly)",
            "type": "integer",
            "format": "int64",
            "default": 7,
            "x-go-name": "DeleteInDays"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Item name",
            "type": "string",
            "x-go-name": "ItemName"
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
            "description": "The specific version you want to delete - 0=last version, -1=entire item\nwith all versions (default)",
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