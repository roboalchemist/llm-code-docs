# Source: https://docs.akeyless.io/reference/rotatedsecretcreategcp.md

# /rotated-secret-create-gcp

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
    "/rotated-secret-create-gcp": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretCreateGcp",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretCreateGcp"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretCreateGcpResponse"
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
      "rotatedSecretCreateGcpResponse": {
        "description": "rotatedSecretCreateGcpResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/rotatedSecretCreateOutput"
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
      "rotatedSecretCreateGcp": {
        "type": "object",
        "title": "rotatedSecretCreateGcp is a command that creates a rotated secret.",
        "required": [
          "name",
          "rotator-type",
          "target-name"
        ],
        "properties": {
          "authentication-credentials": {
            "description": "The credentials to connect with use-user-creds/use-target-creds",
            "type": "string",
            "default": "use-user-creds",
            "x-go-name": "RotatorCredsType"
          },
          "auto-rotate": {
            "description": "Whether to automatically rotate every --rotation-interval days, or disable existing automatic rotation [true/false]",
            "type": "string",
            "x-go-name": "AutoRotate"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
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
            "description": "Enable graceful rotation (keep both versions temporarily). When enabled, a new secret version is created while the previous version is kept for the grace period, so both versions exist for a limited time. [true/false]",
            "type": "string",
            "x-go-name": "GraceRotation"
          },
          "grace-rotation-hour": {
            "description": "The Hour of the grace rotation in UTC",
            "type": "integer",
            "format": "int32",
            "x-go-name": "GraceRotationHour"
          },
          "grace-rotation-interval": {
            "description": "The number of days to wait before deleting the old key (must be bigger than rotation-interval)",
            "type": "string",
            "x-go-name": "GraceRotationInterval"
          },
          "grace-rotation-timing": {
            "description": "When to create the new version relative to the rotation date [after/before]",
            "type": "string",
            "x-go-name": "GraceRotationTiming"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "name": {
            "description": "Rotated secret name",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "password-length": {
            "description": "The length of the password to be generated",
            "type": "string",
            "x-go-name": "PasswordLengthInput"
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
            "description": "The Hour of the rotation in UTC",
            "type": "integer",
            "format": "int32",
            "x-go-name": "RotationHour"
          },
          "rotation-interval": {
            "description": "The number of days to wait between every automatic key rotation (1-365)",
            "type": "string",
            "x-go-name": "RotationInterval"
          },
          "rotator-type": {
            "description": "The rotator type. options: [target/service-account-rotator]",
            "type": "string",
            "x-go-name": "RotatorType"
          },
          "tags": {
            "description": "Add tags attached to this object",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "target-name": {
            "description": "The target name to associate",
            "type": "string",
            "x-go-name": "TargetName"
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
      "rotatedSecretCreateOutput": {
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