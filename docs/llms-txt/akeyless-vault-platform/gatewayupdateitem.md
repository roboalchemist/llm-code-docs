# Source: https://docs.akeyless.io/reference/gatewayupdateitem.md

# /gateway-update-item

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
    "/gateway-update-item": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateItem",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateItem"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayUpdateItemResponse"
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
      "gatewayUpdateItemResponse": {
        "description": "gatewayUpdateItemResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateItemOutput"
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
      "gatewayUpdateItem": {
        "description": "gatewayUpdateItem is a command that updates classic key",
        "type": "object",
        "required": [
          "name",
          "type"
        ],
        "properties": {
          "add-tag": {
            "description": "List of the new tags that will be attached to this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AddTags"
          },
          "api-id": {
            "description": "API ID to rotate (relevant only for rotator-type=api-key)",
            "type": "string",
            "x-go-name": "ApiId"
          },
          "api-key": {
            "description": "API key to rotate (relevant only for rotator-type=api-key)",
            "type": "string",
            "x-go-name": "ApiKey"
          },
          "app-id": {
            "description": "ApplicationId (used in azure)",
            "type": "string",
            "x-go-name": "ApplicationId"
          },
          "auto-rotate": {
            "description": "Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]",
            "type": "string",
            "x-go-name": "AutoRotate"
          },
          "custom-payload": {
            "description": "Secret payload to be sent with rotation request (relevant only for rotator-type=custom)",
            "type": "string",
            "x-go-name": "Payload"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "default": "default_metadata",
            "x-go-name": "Description"
          },
          "gcp-key": {
            "description": "Base64-encoded service account private key text",
            "type": "string",
            "x-go-name": "ServiceAccountKey"
          },
          "gcp-service-account-email": {
            "description": "The email of the gcp service account to rotate",
            "type": "string",
            "x-go-name": "GcpServiceAccountEmail"
          },
          "gcp-service-account-key-id": {
            "description": "The key id of the gcp service account to rotate",
            "type": "string",
            "x-go-name": "GcpServiceAccountKeyId"
          },
          "grace-rotation": {
            "description": "Create a new access key without deleting the old key from AWS for backup (relevant only for AWS) [true/false]",
            "type": "string",
            "x-go-name": "GraceRotation"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. (relevant only for --type=rotated-secret). If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "name": {
            "description": "Item name",
            "type": "string",
            "x-go-name": "ItemName"
          },
          "new-metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "default": "default_metadata",
            "x-go-name": "NewMetadata"
          },
          "new-name": {
            "description": "New item name",
            "type": "string",
            "x-go-name": "NewName"
          },
          "new-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "NewVersion"
          },
          "password-length": {
            "description": "The length of the password to be generated",
            "type": "string",
            "x-go-name": "PasswordLengthInput"
          },
          "rm-tag": {
            "description": "List of the existent tags that will be removed from this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RemoveTags"
          },
          "rotated-password": {
            "description": "rotated-username password (relevant only for rotator-type=password)",
            "type": "string",
            "x-go-name": "RotatedPassword"
          },
          "rotated-username": {
            "description": "username to be rotated, if selected \\\"use-self-creds\\\" at rotator-creds-type, this username will try to rotate it's own password, if \\\"use-target-creds\\\" is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type=password)",
            "type": "string",
            "x-go-name": "RotatedUser"
          },
          "rotation-event-in": {
            "description": "How many days before the rotation of the item would you like to be notified",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RotationEventsInDays"
          },
          "rotation-hour": {
            "description": "The Rotation Hour",
            "type": "integer",
            "format": "int32",
            "default": 0,
            "x-go-name": "RotationHour"
          },
          "rotation-interval": {
            "description": "The number of days to wait between every automatic key rotation (1-365)",
            "type": "string",
            "x-go-name": "RotationInterval"
          },
          "rotator-creds-type": {
            "description": "The rotation credentials type",
            "type": "string",
            "default": "use-self-creds",
            "x-go-name": "RotatorCredsType"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Item type",
            "type": "string",
            "x-go-name": "ItemType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "gatewayUpdateItemOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```