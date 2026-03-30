# Source: https://docs.akeyless.io/reference/gatewaystatusmigration.md

# /gateway-migration-status

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
    "/gateway-migration-status": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayStatusMigration",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayStatusMigration"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayMigrationStatusResponse"
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
      "gatewayMigrationStatusResponse": {
        "description": "gatewayMigrationStatusResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/MigrationStatusReplyObj"
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
      "MigrationStatusReplyObj": {
        "type": "object",
        "properties": {
          "certificates": {
            "$ref": "#/components/schemas/MigrationItems"
          },
          "computers": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Computers"
          },
          "duration_time": {
            "type": "string",
            "x-go-name": "DurationTime"
          },
          "error": {
            "type": "string",
            "x-go-name": "Error"
          },
          "last_status_message": {
            "type": "string",
            "x-go-name": "LastMessage"
          },
          "max_name_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxNameLength"
          },
          "max_value_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxValueLength"
          },
          "migration_id": {
            "type": "string",
            "x-go-name": "MigrationID"
          },
          "migration_items": {
            "$ref": "#/components/schemas/MigrationItems"
          },
          "migration_name": {
            "type": "string",
            "x-go-name": "MigrationName"
          },
          "migration_state": {
            "type": "string",
            "x-go-name": "MigrationState"
          },
          "migration_type": {
            "type": "string",
            "x-go-name": "MigrationType"
          },
          "migration_type_name": {
            "type": "string",
            "x-go-name": "MigrationTypeName"
          },
          "rotated_secrets": {
            "$ref": "#/components/schemas/MigrationItems"
          },
          "start_time": {
            "type": "string",
            "x-go-name": "StartTime"
          },
          "targets": {
            "$ref": "#/components/schemas/MigrationItems"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "gatewayStatusMigration": {
        "description": "gatewayStatusMigration is a command that get migration status",
        "type": "object",
        "properties": {
          "id": {
            "description": "Migration ID",
            "type": "string",
            "x-go-name": "MigrationID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Migration name to display",
            "type": "string",
            "x-go-name": "MigrationName"
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
      }
    }
  }
}
```