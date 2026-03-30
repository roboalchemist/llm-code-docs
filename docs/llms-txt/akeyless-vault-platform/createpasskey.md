# Source: https://docs.akeyless.io/reference/createpasskey.md

# /create-passkey

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
    "/create-passkey": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "CreatePasskey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreatePasskey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/CreatePasskeyResponse"
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
      "CreatePasskeyResponse": {
        "description": "CreatePasskeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreatePasskeyOutput"
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
      "ClassicKeyType": {
        "type": "string",
        "title": "ClassicKeyType defines types of keys that can be managed by ClassicKey supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CreatePasskey": {
        "description": "CreatePasskey is a command that creates a new passkey",
        "type": "object",
        "required": [
          "name",
          "alg"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "alg": {
            "description": "Passkey type; options: [EC256, EC384, EC512]",
            "type": "string",
            "default": "EC256",
            "x-go-name": "Alg"
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
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "ClassicKey name",
            "type": "string",
            "x-go-name": "ClassicKeyName"
          },
          "origin-url": {
            "description": "Originating websites for this passkey",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Websites"
          },
          "protection-key-name": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
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
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "username": {
            "description": "For Password Management use",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "CreatePasskeyOutput": {
        "type": "object",
        "properties": {
          "classic_key_id": {
            "type": "string",
            "x-go-name": "ClassicKeyId"
          },
          "classic_key_name": {
            "type": "string",
            "x-go-name": "ClassicKeyName"
          },
          "classic_key_type": {
            "$ref": "#/components/schemas/ClassicKeyType"
          },
          "public_key": {
            "type": "string",
            "x-go-name": "PublicKey"
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
      }
    }
  }
}
```