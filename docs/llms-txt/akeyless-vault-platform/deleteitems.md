# Source: https://docs.akeyless.io/reference/deleteitems.md

# /delete-items

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
    "/delete-items": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "deleteItems",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/deleteItems"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/deleteItemsResponse"
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
      "deleteItemsResponse": {
        "description": "deleteItemsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/deleteItemsOutput"
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
      "deleteItems": {
        "type": "object",
        "title": "deleteItems is a command that deletes multiple items from a given path.",
        "properties": {
          "item": {
            "description": "A list of items to delete, To specify multiple items use argument multiple times",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Items"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "path": {
            "description": "Path to delete the items from",
            "type": "string",
            "x-go-name": "Path"
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
      },
      "deleteItemsOutput": {
        "type": "object",
        "properties": {
          "deleted_items": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DeletedItems"
          },
          "failed_deleted_items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "FailedDeletedItems"
          },
          "path": {
            "type": "string",
            "x-go-name": "Path"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```