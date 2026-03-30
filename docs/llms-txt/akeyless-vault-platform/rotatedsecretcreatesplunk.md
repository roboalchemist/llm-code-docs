# Source: https://docs.akeyless.io/reference/rotatedsecretcreatesplunk.md

# /rotated-secret-create-splunk

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
    "/rotated-secret-create-splunk": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretCreateSplunk",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretCreateSplunk"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretCreateSplunkResponse"
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
      "rotatedSecretCreateSplunkResponse": {
        "description": "rotatedSecretCreateSplunkResponse wraps response body.",
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
      "rotatedSecretCreateOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "rotatedSecretCreateSplunk": {
        "description": "rotatedSecretCreateSplunk is a command that creates a rotated secret for a\nSplunk target. Currently we support target-rotator behavior (rotate\ncredentials on the target itself).",
        "type": "object",
        "title": "Splunk",
        "required": [
          "name",
          "target-name",
          "rotator-type"
        ],
        "properties": {
          "audience": {
            "description": "Token audience for Splunk token creation (required for rotator-type=token)",
            "type": "string",
            "x-go-name": "Audience"
          },
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
          "expiration-date": {
            "description": "Token expiration date in YYYY-MM-DD format (required for rotator-type=token when manual rotation is selected and no existing token is provided). Time will be set to 00:00 UTC.",
            "type": "string",
            "x-go-name": "ExpirationDate"
          },
          "hec-token": {
            "description": "Current Splunk HEC token value to store (relevant only for rotator-type=hec-token). If not provided, a new HEC input will be created in Splunk.",
            "type": "string",
            "x-go-name": "HecToken"
          },
          "hec-token-name": {
            "description": "Splunk HEC input name to manage  (required for rotator-type=hec-token)",
            "type": "string",
            "x-go-name": "HecTokenName"
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
          "rotated-password": {
            "description": "rotated-username password (relevant only for rotator-type=password)",
            "type": "string",
            "x-go-name": "RotatedPassword"
          },
          "rotated-username": {
            "description": "username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it's own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type=password)",
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
            "description": "The rotator type. options: [target/password/token/hec-token]",
            "type": "string",
            "x-go-name": "RotatorType"
          },
          "splunk-token": {
            "description": "Current Splunk authentication token to store (relevant only for rotator-type=token). If not provided, a new token will be created in Splunk.",
            "type": "string",
            "x-go-name": "SplunkToken"
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
          "token-owner": {
            "description": "Splunk token owner username (relevant only for rotator-type=token)",
            "type": "string",
            "x-go-name": "TokenOwner"
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