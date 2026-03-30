# Source: https://docs.akeyless.io/reference/folderget.md

# /folder-get

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
    "/folder-get": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "folderGet",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/folderGet"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/folderGetResponse"
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
      "folderGetResponse": {
        "description": "folderGetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/folderGetOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "FolderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GetFolderOutput": {
        "description": "GetFolderOutput is the result of the getFolder operation",
        "type": "object",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "accessibility": {
            "$ref": "#/components/schemas/ItemAccessibility"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "delete_protection": {
            "type": "boolean",
            "x-go-name": "DeleteProtection"
          },
          "folder_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "FolderID"
          },
          "folder_name": {
            "type": "string",
            "x-go-name": "FolderName"
          },
          "metadata": {
            "type": "string",
            "x-go-name": "Metadata"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemAccessibility": {
        "type": "integer",
        "format": "int64",
        "title": "ItemAccessibility defines types supported by AKEYLESS.",
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
      "folderGet": {
        "description": "folderGet is a command that get folder",
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
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Folder name",
            "type": "string",
            "x-go-name": "FolderName"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "$ref": "#/components/schemas/FolderType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "folderGetOutput": {
        "type": "object",
        "properties": {
          "folder": {
            "$ref": "#/components/schemas/GetFolderOutput"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```