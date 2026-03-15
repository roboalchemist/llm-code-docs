# Source: https://docs.akeyless.io/reference/createsecret.md

# /create-secret

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
    "/create-secret": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createSecret",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createSecret"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createSecretResponse"
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
      "createSecretResponse": {
        "description": "createSecretResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateSecretOutput"
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
      "CreateSecretOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
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
      "createSecret": {
        "type": "object",
        "required": [
          "value",
          "name"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "change-event": {
            "description": "Trigger an event when a secret value changed [true/false] (Relevant only for Static Secret)",
            "type": "string",
            "x-go-name": "NotifyOnChangeEvent"
          },
          "custom-field": {
            "description": "For Password Management use, additional fields",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "CustomFields"
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
          "format": {
            "description": "Secret format [text/json/key-value] (relevant only for type 'generic')",
            "type": "string",
            "default": "text",
            "x-go-name": "Format"
          },
          "inject-url": {
            "description": "For Password Management use, reflect the website context",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Websites"
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
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "multiline_value": {
            "description": "The provided value is a multiline value (separated by '\\n')",
            "type": "boolean",
            "x-go-name": "MultilineValue"
          },
          "name": {
            "description": "Secret name",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "password": {
            "description": "For Password Management use, additional fields",
            "type": "string",
            "x-go-name": "Password"
          },
          "protection_key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the\naccount default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
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
          "secure-access-gateway": {
            "type": "string",
            "x-go-name": "SecureAccessGwUrl"
          },
          "secure-access-host": {
            "description": "Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessHost"
          },
          "secure-access-rdp-user": {
            "description": "Remote Desktop Username",
            "type": "string",
            "x-go-name": "SecureAccessOverrideUser"
          },
          "secure-access-ssh-creds": {
            "description": "Static-Secret values contains SSH Credentials, either Private Key or Password [password/private-key]",
            "type": "string",
            "x-go-name": "SecureAccessSSHCategory"
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
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "The secret sub type [generic/password]",
            "type": "string",
            "default": "generic",
            "x-go-name": "SecretType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "username": {
            "description": "For Password Management use",
            "type": "string",
            "x-go-name": "Username"
          },
          "value": {
            "description": "The secret value (relevant only for type 'generic')",
            "type": "string",
            "x-go-name": "Value"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```