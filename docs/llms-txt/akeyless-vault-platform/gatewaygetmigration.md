# Source: https://docs.akeyless.io/reference/gatewaygetmigration.md

# /gateway-get-migration

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
    "/gateway-get-migration": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetMigration",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetMigration"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayMigrationGetResponse"
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
      "gatewayMigrationGetResponse": {
        "description": "gatewayMigrationGetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayMigrationGetOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AWSPayload": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "x-go-name": "Key"
          },
          "region": {
            "type": "string",
            "x-go-name": "Region"
          },
          "secret": {
            "type": "string",
            "x-go-name": "Secret"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AWSSecretsMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/AWSPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ActiveDirectoryMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/ActiveDirectoryPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ActiveDirectoryPayload": {
        "type": "object",
        "properties": {
          "active_directory_target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ActiveDirectoryTargetID"
          },
          "ai_certificate_discovery": {
            "type": "boolean",
            "x-go-name": "UseAI"
          },
          "auto_rotate": {
            "type": "boolean",
            "x-go-name": "AutoRotate"
          },
          "auto_rotate_interval_in_days": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "AutoRotateIntervalInDays"
          },
          "auto_rotate_rotation_hour": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "AutoRotateRotationHour"
          },
          "certificates_expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "CertificatesExpirationEvents"
          },
          "certificates_path_template": {
            "type": "string",
            "x-go-name": "CertificatesPathTemplate"
          },
          "computer_base_dn": {
            "type": "string",
            "x-go-name": "ComputerBaseDN"
          },
          "discover_iis_apps": {
            "type": "boolean",
            "x-go-name": "DiscoverIISApps"
          },
          "discover_local_users": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "DiscoverLocalUsers"
          },
          "discover_services": {
            "type": "boolean",
            "x-go-name": "DiscoverServices"
          },
          "discovery_types": {
            "$ref": "#/components/schemas/DiscoveryTypes"
          },
          "domain_name": {
            "type": "string",
            "x-go-name": "DomainName"
          },
          "domain_server_targets_path_template": {
            "type": "string",
            "x-go-name": "DomainServerTargetsPathTemplate"
          },
          "domain_users_rotated_secrets_path_template": {
            "type": "string",
            "x-go-name": "DomainUsersRotatedSecretsPathTemplate"
          },
          "enable_rdp_sra": {
            "type": "boolean",
            "x-go-name": "EnableRdpSRA"
          },
          "local_users_ignore_list": {
            "type": "object",
            "additionalProperties": {
              "type": "boolean"
            },
            "x-go-name": "LocalUsersIgnoreList"
          },
          "local_users_rotated_secrets_path_template": {
            "type": "string",
            "x-go-name": "LocalUsersRotatedSecretsPathTemplate"
          },
          "os_filter": {
            "type": "string",
            "x-go-name": "OsFilter"
          },
          "ssh_port": {
            "type": "string",
            "x-go-name": "SshPort"
          },
          "target_format": {
            "$ref": "#/components/schemas/TargetFormatType"
          },
          "targets_type": {
            "type": "string",
            "x-go-name": "TargetsType"
          },
          "user_base_dn": {
            "type": "string",
            "x-go-name": "UserBaseDN"
          },
          "user_groups": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserGroups"
          },
          "winrm_over_http": {
            "type": "boolean",
            "x-go-name": "WinrmOverHttp"
          },
          "winrm_port": {
            "type": "string",
            "x-go-name": "WinrmPort"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AzureKeyVaultMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/AzurePayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AzurePayload": {
        "type": "object",
        "properties": {
          "client": {
            "type": "string",
            "x-go-name": "Client"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "secret": {
            "type": "string",
            "x-go-name": "Secret"
          },
          "tenant": {
            "type": "string",
            "x-go-name": "Tenant"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "CertificateExpirationEvent": {
        "type": "object",
        "properties": {
          "seconds_before": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "SecondsBefore"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/CertificatePayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "CertificatePayload": {
        "type": "object",
        "properties": {
          "expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "ExpirationEvents"
          },
          "folder": {
            "type": "string",
            "x-go-name": "Folder"
          },
          "max_dial_timeout": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxDialTimeout"
          },
          "max_scan_duration": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxScanDuration"
          },
          "max_workers": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxWorkers"
          },
          "port_ranges": {
            "type": "string",
            "x-go-name": "PortRanges"
          },
          "targets": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateScanTarget"
            },
            "x-go-name": "Targets"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "CertificateScanTarget": {
        "type": "object",
        "properties": {
          "host": {
            "type": "string",
            "x-go-name": "Host"
          },
          "portRanges": {
            "type": "string",
            "x-go-name": "PortRanges"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ConjurMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/ConjurPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ConjurPayload": {
        "type": "object",
        "properties": {
          "conjur_account": {
            "type": "string",
            "x-go-name": "ConjurAccount"
          },
          "conjur_api_key": {
            "type": "string",
            "x-go-name": "ConjurApiKey"
          },
          "conjur_url": {
            "type": "string",
            "x-go-name": "ConjurURL"
          },
          "conjur_username": {
            "type": "string",
            "x-go-name": "ConjurUsername"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "DiscoveryType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DiscoveryTypes": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/DiscoveryType"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GCPPayload": {
        "type": "object",
        "properties": {
          "gcp_credentials_json": {
            "type": "string",
            "x-go-name": "Key"
          },
          "project_id": {
            "type": "string",
            "x-go-name": "ProjectId"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "UseGwCloudIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "GCPSecretsMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/GCPPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "HashiMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/HashiPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "HashiPayload": {
        "type": "object",
        "properties": {
          "import_as_json": {
            "type": "boolean",
            "x-go-name": "ImportAsJson"
          },
          "namespaces": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Namespaces"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          },
          "url": {
            "type": "string",
            "x-go-name": "Url"
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
      "K8SMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/K8SPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "K8SPayload": {
        "type": "object",
        "properties": {
          "ca": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "CA"
          },
          "client_cert": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "ClientCert"
          },
          "client_key": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "ClientKey"
          },
          "namespace": {
            "type": "string",
            "x-go-name": "Namespace"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "server": {
            "type": "string",
            "x-go-name": "Server"
          },
          "skip_system": {
            "type": "boolean",
            "x-go-name": "SkipSystem"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MigrationGeneral": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "x-go-name": "Id"
          },
          "last_migration": {
            "type": "string",
            "x-go-name": "LastMigrationTime"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "new_name": {
            "type": "string",
            "x-go-name": "NewName"
          },
          "prefix": {
            "type": "string",
            "x-go-name": "Prefix"
          },
          "protection_key": {
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "status": {
            "type": "string",
            "x-go-name": "Status"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MigrationsConfigPart": {
        "type": "object",
        "properties": {
          "active_directory_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ActiveDirectoryMigration"
            },
            "x-go-name": "ActiveDirectoryMigrations"
          },
          "aws_secrets_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AWSSecretsMigration"
            },
            "x-go-name": "AWSSecretsMigrations"
          },
          "azure_kv_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AzureKeyVaultMigration"
            },
            "x-go-name": "AzureKVMigrations"
          },
          "certificate_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateMigration"
            },
            "x-go-name": "CertificateMigrations"
          },
          "conjur_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConjurMigration"
            },
            "x-go-name": "ConjurMigrations"
          },
          "gcp_secrets_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GCPSecretsMigration"
            },
            "x-go-name": "GCPSecretsMigrations"
          },
          "hashi_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HashiMigration"
            },
            "x-go-name": "HashiMigrations"
          },
          "k8s_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/K8SMigration"
            },
            "x-go-name": "K8SMigrations"
          },
          "mock_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MockMigration"
            },
            "x-go-name": "MockMigrations"
          },
          "one_password_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OnePasswordMigration"
            },
            "x-go-name": "OnePasswordMigrations"
          },
          "server_inventory_migrations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ServerInventoryMigration"
            },
            "x-go-name": "ServerInventoryMigrations"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MockMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/MockPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "MockPayload": {
        "type": "object",
        "properties": {
          "vaults": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Vaults"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "OnePasswordMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/OnePasswordPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "OnePasswordPayload": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "x-go-name": "Email"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "secret_key": {
            "type": "string",
            "x-go-name": "SecretKey"
          },
          "url": {
            "type": "string",
            "x-go-name": "AccountUrl"
          },
          "vaults": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Vaults"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ServerInventoryMigration": {
        "type": "object",
        "properties": {
          "general": {
            "$ref": "#/components/schemas/MigrationGeneral"
          },
          "payload": {
            "$ref": "#/components/schemas/ServerInventoryPayload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ServerInventoryPayload": {
        "type": "object",
        "properties": {
          "auto_rotate": {
            "type": "boolean",
            "x-go-name": "AutoRotate"
          },
          "auto_rotate_interval_in_days": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "AutoRotateIntervalInDays"
          },
          "auto_rotate_rotation_hour": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "AutoRotateRotationHour"
          },
          "enable_rdp_sra": {
            "type": "boolean",
            "x-go-name": "EnableRdpSRA"
          },
          "migration_target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MigrationTargetID"
          },
          "server_targets_path_template": {
            "type": "string",
            "x-go-name": "ServerTargetsPathTemplate"
          },
          "user_groups": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserGroups"
          },
          "users_ignore_list": {
            "type": "object",
            "additionalProperties": {
              "type": "boolean"
            },
            "x-go-name": "UsersIgnoreList"
          },
          "users_rotated_secrets_path_template": {
            "type": "string",
            "x-go-name": "UsersRotatedSecretsPathTemplate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "TargetFormatType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "gatewayGetMigration": {
        "description": "gatewayGetMigration is a command that get migration",
        "type": "object",
        "properties": {
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
      },
      "gatewayMigrationGetOutput": {
        "type": "object",
        "properties": {
          "body": {
            "$ref": "#/components/schemas/MigrationsConfigPart"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```