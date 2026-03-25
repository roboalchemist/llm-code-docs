# Source: https://docs.akeyless.io/reference/rotatedsecretcreateaws.md

# /rotated-secret-create-aws

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
    "/rotated-secret-create-aws": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretCreateAws",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretCreateAws"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretCreateAwsResponse"
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
      "rotatedSecretCreateAwsResponse": {
        "description": "rotatedSecretCreateAwsResponse wraps response body.",
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
      "rotatedSecretCreateAws": {
        "type": "object",
        "title": "rotatedSecretCreateAws is a command that creates a rotated secret.",
        "required": [
          "name",
          "rotator-type",
          "target-name"
        ],
        "properties": {
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
          "aws-region": {
            "description": "Aws Region",
            "type": "string",
            "default": "us-east-2",
            "x-go-name": "AwsRegion"
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
          "rotate-after-disconnect": {
            "description": "Rotate the value of the secret after SRA session ends [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "RotateAfterDisconnect"
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
            "description": "The rotator type. options: [target/api-key]",
            "type": "string",
            "x-go-name": "RotatorType"
          },
          "secure-access-aws-account-id": {
            "description": "The AWS account id",
            "type": "string",
            "x-go-name": "SecureAccessAccountId"
          },
          "secure-access-aws-native-cli": {
            "description": "The AWS native cli",
            "type": "boolean",
            "x-go-name": "SecureAccessAwsNativeCli"
          },
          "secure-access-bastion-issuer": {
            "description": "Deprecated. use secure-access-certificate-issuer",
            "type": "string",
            "x-go-name": "SecureAccessBastionIssuer"
          },
          "secure-access-certificate-issuer": {
            "description": "Path to the SSH Certificate Issuer for your Akeyless Secure Access",
            "type": "string",
            "x-go-name": "SecureAccessCertIssuer"
          },
          "secure-access-enable": {
            "description": "Enable/Disable secure remote access [true/false]",
            "type": "string",
            "x-go-name": "SecureAccessEnabled"
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