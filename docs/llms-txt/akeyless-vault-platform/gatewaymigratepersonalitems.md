# Source: https://docs.akeyless.io/reference/gatewaymigratepersonalitems.md

# /gateway-migrate-personal-items

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
    "/gateway-migrate-personal-items": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayMigratePersonalItems",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayMigratePersonalItems"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayMigratePersonalItemsResponse"
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
      "gatewayMigratePersonalItemsResponse": {
        "description": "gatewayMigratePersonalItemsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayMigratePersonalItemsOutput"
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
      "MigrationItems": {
        "type": "object",
        "properties": {
          "failed": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Failed"
          },
          "migrated": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Migrated"
          },
          "skipped": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Skipped"
          },
          "total": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Total"
          },
          "updated": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/importer/report"
      },
      "gatewayMigratePersonalItems": {
        "description": "gatewayMigratePersonalItems is a command that migrate personal items from external vault",
        "type": "object",
        "properties": {
          "1password-email": {
            "description": "1Password user email to connect to the API",
            "type": "string",
            "x-go-name": "OpEmail"
          },
          "1password-password": {
            "description": "1Password user password to connect to the API",
            "type": "string",
            "x-go-name": "OpPassword"
          },
          "1password-secret-key": {
            "description": "1Password user secret key to connect to the API",
            "type": "string",
            "x-go-name": "OpSecretKey"
          },
          "1password-url": {
            "description": "1Password api container url",
            "type": "string",
            "x-go-name": "OpUrl"
          },
          "1password-vaults": {
            "description": "1Password list of vault to get the items from",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Vaults"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "protection-key": {
            "description": "The name of a key that used to encrypt the secret value",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "target-location": {
            "description": "Target location in your Akeyless personal folder for migrated secrets",
            "type": "string",
            "x-go-name": "TargetLocation"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Migration type for now only 1password.",
            "type": "string",
            "default": "1password",
            "x-go-name": "MigrationType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "gatewayMigratePersonalItemsOutput": {
        "type": "object",
        "properties": {
          "migration_items": {
            "$ref": "#/components/schemas/MigrationItems"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```