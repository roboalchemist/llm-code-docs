# Source: https://docs.akeyless.io/reference/gatewaydeletek8sauthconfig.md

# /gateway-delete-k8s-auth-config

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
    "/gateway-delete-k8s-auth-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayDeleteK8SAuthConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayDeleteK8SAuthConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayDeleteK8SAuthConfigResponse"
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
      "gatewayDeleteK8SAuthConfigResponse": {
        "description": "gatewayDeleteK8SAuthConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayDeleteK8SAuthConfigOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ConfigChange": {
        "type": "object",
        "properties": {
          "config_hash": {
            "$ref": "#/components/schemas/ConfigHash"
          },
          "last_change": {
            "$ref": "#/components/schemas/LastConfigChange"
          },
          "last_status": {
            "$ref": "#/components/schemas/LastStatusInfo"
          },
          "required_activity": {
            "$ref": "#/components/schemas/RequiredActivity"
          },
          "update_stamp": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "UpdateStamp"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ConfigHash": {
        "type": "object",
        "properties": {
          "admins": {
            "type": "string",
            "x-go-name": "Admins"
          },
          "ai_insights": {
            "type": "string",
            "x-go-name": "AiInsights"
          },
          "cache": {
            "type": "string",
            "x-go-name": "Cache"
          },
          "customer_fragements": {
            "type": "string",
            "x-go-name": "CFragements"
          },
          "general": {
            "type": "string",
            "x-go-name": "General"
          },
          "k8s_auths": {
            "type": "string",
            "x-go-name": "K8SAuths"
          },
          "kmip": {
            "type": "string",
            "x-go-name": "KMIP"
          },
          "ldap": {
            "type": "string",
            "x-go-name": "Ldap"
          },
          "leadership": {
            "type": "string",
            "x-go-name": "Leadership"
          },
          "log_forwarding": {
            "type": "string",
            "x-go-name": "LogForwarding"
          },
          "m_queue": {
            "type": "string",
            "x-go-name": "MQueue"
          },
          "migration_status": {
            "type": "string",
            "x-go-name": "MigrationStatus"
          },
          "migrations": {
            "type": "string",
            "x-go-name": "Migrations"
          },
          "producers": {
            "x-go-name": "Producers"
          },
          "producers_status": {
            "type": "string",
            "x-go-name": "ProducersStatus"
          },
          "rotators": {
            "x-go-name": "Rotators"
          },
          "saml": {
            "type": "string",
            "x-go-name": "Default"
          },
          "universal_identity": {
            "type": "string",
            "x-go-name": "UIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "K8SAuthsConfigLastChange": {
        "type": "object",
        "properties": {
          "changed_k8s_auths_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ChangedK8SAuthsIDs"
          },
          "created_k8s_auths_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CreatedK8SAuthsIDs"
          },
          "deleted_k8s_auths_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DeletedK8SAuthsIDs"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LastConfigChange": {
        "type": "object",
        "properties": {
          "last_k8s_auths_change": {
            "$ref": "#/components/schemas/K8SAuthsConfigLastChange"
          },
          "last_migrations_change": {
            "$ref": "#/components/schemas/MigrationsConfigLastChange"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LastStatusInfo": {
        "type": "object",
        "properties": {
          "migrations_status": {
            "$ref": "#/components/schemas/MigrationStatus"
          },
          "producers_errors": {
            "x-go-name": "Producers"
          },
          "was_migrations_copied_to_new_table": {
            "description": "flag to indicate migrationStatus copied to new table",
            "type": "boolean",
            "x-go-name": "WasMigrationsCopiedToNewTable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MigrationStatus": {
        "type": "object",
        "properties": {
          "last_messages": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "LastMessages"
          },
          "last_reports": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "LastReports"
          },
          "last_statuses": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "LastStatuses"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MigrationsConfigLastChange": {
        "type": "object",
        "properties": {
          "changed_migrations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ChangedMigrations"
          },
          "created_migrations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CreatedMigrations"
          },
          "deleted_migrations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DeletedMigrations"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "RequiredActivity": {
        "type": "object",
        "properties": {
          "migrations_required_activity": {
            "type": "object",
            "additionalProperties": {
              "type": "boolean"
            },
            "x-go-name": "Migrations"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "gatewayDeleteK8SAuthConfig": {
        "description": "gatewayDeleteK8SAuth is a command that deletes k8s auth config",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "K8S Auth config name",
            "type": "string",
            "x-go-name": "K8SAuthConfigName"
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
      "gatewayDeleteK8SAuthConfigOutput": {
        "type": "object",
        "properties": {
          "cluster_id": {
            "type": "string",
            "x-go-name": "ClusterId"
          },
          "parts_change": {
            "$ref": "#/components/schemas/ConfigChange"
          },
          "total_hash": {
            "type": "string",
            "x-go-name": "TotalHash"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```