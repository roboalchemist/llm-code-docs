# Source: https://docs.akeyless.io/reference/importpasswords.md

# /import-passwords

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
    "/import-passwords": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "importPasswords",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/importPasswords"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/importPasswordsResponse"
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
      "importPasswordsResponse": {
        "description": "importPasswordsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ImportPasswordsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ImportPasswordsOutput": {
        "type": "object",
        "properties": {
          "imported": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "Imported"
          },
          "passwords_in_file": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "PasswordsInFile"
          },
          "successfully_parsed": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "SuccessfullyParsed"
          },
          "updated": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "Updated"
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
      "UpdateModeType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "importPasswords": {
        "description": "importPasswords is a command that import passwords",
        "type": "object",
        "required": [
          "import-path"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "personal",
            "x-go-name": "ItemAccessibilityString"
          },
          "format": {
            "description": "Password format type [LastPass/Chrome/Firefox/1password/keeper/bitwarden/dashlane]",
            "type": "string",
            "default": "LastPass",
            "x-go-name": "Format"
          },
          "import-path": {
            "description": "File path",
            "type": "string",
            "x-go-name": "FilePath"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "protection_key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "target-folder": {
            "description": "Target folder for imported passwords",
            "type": "string",
            "default": "/",
            "x-go-name": "TargetFolder"
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
          "update-mode": {
            "$ref": "#/components/schemas/UpdateModeType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```