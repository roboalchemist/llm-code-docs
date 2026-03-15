# Source: https://docs.akeyless.io/reference/updatesecretval.md

# /update-secret-val

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
    "/update-secret-val": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateSecretVal",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateSecretVal"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateSecretValResponse"
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
      "updateSecretValResponse": {
        "description": "updateSecretValResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UpdateSecretValOutput"
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
      "UpdateSecretValOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateSecretVal": {
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
          "custom-field": {
            "description": "For Password Management use, additional fields",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "CustomFields"
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
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the\naccount default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "last-version": {
            "description": "The last version number before the update",
            "type": "integer",
            "format": "int32",
            "x-go-name": "LastVersion"
          },
          "multiline": {
            "description": "The provided value is a multiline value (separated by '\\n')",
            "type": "boolean",
            "x-go-name": "MultilineValue"
          },
          "name": {
            "description": "Secret name",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "new-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "NewVersion"
          },
          "password": {
            "description": "For Password Management use, additional fields",
            "type": "string",
            "x-go-name": "Password"
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