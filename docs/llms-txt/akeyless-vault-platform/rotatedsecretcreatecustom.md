# Source: https://docs.akeyless.io/reference/rotatedsecretcreatecustom.md

# /rotated-secret-create-custom

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
    "/rotated-secret-create-custom": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretCreateCustom",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretCreateCustom"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretCreateCustomResponse"
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
      "rotatedSecretCreateCustomResponse": {
        "description": "rotatedSecretCreateCustomResponse wraps response body.",
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
      "rotatedSecretCreateCustom": {
        "type": "object",
        "title": "rotatedSecretCreateCustom is a command that creates a rotated secret.",
        "required": [
          "name",
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
          "custom-payload": {
            "description": "Secret payload to be sent with rotation request",
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
            "x-go-name": "Description"
          },
          "enable-password-policy": {
            "description": "Enable password policy",
            "type": "string",
            "x-go-name": "EnablePasswordPolicy"
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
          "secure-access-allow-external-user": {
            "description": "Allow providing external user for a domain users",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessAllowProvidingExternalUser"
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
          "secure-access-host": {
            "description": "Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessHost"
          },
          "secure-access-rdp-domain": {
            "description": "Default domain name server. i.e. microsoft.com",
            "type": "string",
            "x-go-name": "SecureAccessDomain"
          },
          "secure-access-rdp-user": {
            "description": "Override the RDP Domain username",
            "type": "string",
            "x-go-name": "SecureAccessOverrideUser"
          },
          "secure-access-ssh-user": {
            "description": "Override the SSH username as indicated in SSH Certificate Issuer",
            "type": "string",
            "x-go-name": "SecureAccessSSHUser"
          },
          "secure-access-url": {
            "description": "Destination URL to inject secrets",
            "type": "string",
            "x-go-name": "SecureAccessURL"
          },
          "secure-access-web": {
            "description": "Enable Web Secure Remote Access",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessWebCategory"
          },
          "secure-access-web-browsing": {
            "description": "Secure browser via Akeyless's Secure Remote Access (SRA)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessIsolated"
          },
          "secure-access-web-proxy": {
            "description": "Web-Proxy via Akeyless's Secure Remote Access (SRA)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessWebProxy"
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
          "timeout-sec": {
            "description": "Maximum allowed time in seconds for the custom rotator to return the results",
            "type": "integer",
            "format": "int64",
            "default": 40,
            "x-go-name": "TimeoutSeconds"
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
          "use-capital-letters": {
            "description": "Password must contain capital letters [true/false]",
            "type": "string",
            "x-go-name": "UseCapitalLettersV2"
          },
          "use-lower-letters": {
            "description": "Password must contain lower case letters [true/false]",
            "type": "string",
            "x-go-name": "UseLowerLetters"
          },
          "use-numbers": {
            "description": "Password must contain numbers [true/false]",
            "type": "string",
            "x-go-name": "UseNumbers"
          },
          "use-special-characters": {
            "description": "Password must contain special characters [true/false]",
            "type": "string",
            "x-go-name": "UseSpecialCharacters"
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