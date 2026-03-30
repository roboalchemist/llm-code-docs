# Source: https://docs.akeyless.io/reference/gatewaygetconfig.md

# /gateway-get-config

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
    "/gateway-get-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetConfigResponse"
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
      "gatewayGetConfigResponse": {
        "description": "gatewayGetConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AkeylessGatewayConfig"
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
      "AccessPermission": {
        "type": "string",
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
      "AdminsConfigPart": {
        "type": "object",
        "properties": {
          "admins_migration_status": {
            "$ref": "#/components/schemas/AdminsMigrationStatus"
          },
          "allowed_access": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/AllowedAccessOld"
            },
            "x-go-name": "Allowed"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AdminsMigrationStatus": {
        "type": "integer",
        "format": "int64",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AiInsightsConfigPart": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "model": {
            "type": "string",
            "x-go-name": "Model"
          },
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetId"
          },
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AkeylessGatewayConfig": {
        "type": "object",
        "properties": {
          "admins": {
            "$ref": "#/components/schemas/AdminsConfigPart"
          },
          "ai_insights": {
            "$ref": "#/components/schemas/AiInsightsConfigPart"
          },
          "ca_certificates": {
            "$ref": "#/components/schemas/CaCertificatesConfigPart"
          },
          "cache": {
            "$ref": "#/components/schemas/CacheConfigPart"
          },
          "cf": {
            "$ref": "#/components/schemas/CFConfigPart"
          },
          "config_protection_key_name": {
            "type": "string",
            "x-go-name": "ConfigProtectionKeyName"
          },
          "general": {
            "$ref": "#/components/schemas/GeneralConfigPart"
          },
          "k8s_auths": {
            "$ref": "#/components/schemas/K8SAuthsConfigPart"
          },
          "kerberos": {
            "$ref": "#/components/schemas/KerberosConfigPart"
          },
          "kmip_clients": {
            "$ref": "#/components/schemas/KMIPConfigPart"
          },
          "ldap": {
            "$ref": "#/components/schemas/LdapConfigPart"
          },
          "leadership": {
            "$ref": "#/components/schemas/LeadershipConfigPart"
          },
          "log_forwarding": {
            "$ref": "#/components/schemas/LogForwardingConfigPart"
          },
          "message_queue_info": {
            "$ref": "#/components/schemas/GatewayMessageQueueInfo"
          },
          "migrations": {
            "$ref": "#/components/schemas/MigrationsConfigPart"
          },
          "producers": {
            "$ref": "#/components/schemas/ProducersConfigPart"
          },
          "rotators": {
            "$ref": "#/components/schemas/RotatorsConfigPart"
          },
          "saml": {
            "$ref": "#/components/schemas/DefaultConfigPart"
          },
          "version": {
            "type": "integer",
            "format": "uint64",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AllowedAccessOld": {
        "description": "Deprecated: AllowedAccessOld please use Gator allowed_access API structs such as AllowedAccessInput/AllowedAccess",
        "type": "object",
        "properties": {
          "acc_id": {
            "type": "string",
            "x-go-name": "AccId"
          },
          "access_permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AccessPermission"
            },
            "x-go-name": "AccessPermissions"
          },
          "access_rules_type": {
            "type": "string",
            "x-go-name": "AccessRulesType"
          },
          "allowed_api": {
            "type": "boolean",
            "x-go-name": "AllowedApi"
          },
          "alloweds_login": {
            "type": "boolean",
            "x-go-name": "AllowedsLogin"
          },
          "editable": {
            "type": "boolean",
            "x-go-name": "Editable"
          },
          "err_msg": {
            "type": "string",
            "x-go-name": "ErrMsg"
          },
          "hash": {
            "type": "string",
            "x-go-name": "Hash"
          },
          "is_valid": {
            "type": "boolean",
            "x-go-name": "IsValid"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "SubClaims"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AwsAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/log"
      },
      "AwsS3LogForwardingConfig": {
        "type": "object",
        "properties": {
          "aws_access_id": {
            "type": "string",
            "x-go-name": "AwsAccessId"
          },
          "aws_access_key": {
            "type": "string",
            "x-go-name": "AwsAccessKey"
          },
          "aws_auth_type": {
            "$ref": "#/components/schemas/AwsAuthType"
          },
          "aws_region": {
            "type": "string",
            "x-go-name": "AwsRegion"
          },
          "aws_role_arn": {
            "type": "string",
            "x-go-name": "AwsRoleARN"
          },
          "aws_use_gateway_cloud_identity": {
            "description": "deprecated",
            "type": "boolean",
            "x-go-name": "AwsUseGatewayCloudIdentity"
          },
          "bucket_name": {
            "type": "string",
            "x-go-name": "BucketName"
          },
          "log_folder": {
            "type": "string",
            "x-go-name": "LogFolder"
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
      "AzureLogAnalyticsForwardingConfig": {
        "type": "object",
        "properties": {
          "azure_enable_batch": {
            "type": "string",
            "x-go-name": "AzureEnableBatch"
          },
          "azure_workspace_id": {
            "type": "string",
            "x-go-name": "AzureWorkspaceId"
          },
          "azure_workspace_key": {
            "type": "string",
            "x-go-name": "AzureWorkspaceKey"
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
      "CFConfigPart": {
        "type": "object",
        "properties": {
          "customer_fragements": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "CFragments"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "CaCertificatesConfigPart": {
        "type": "object",
        "properties": {
          "certificate_store": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateStore"
            },
            "x-go-name": "Certificate_store"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "CacheConfigPart": {
        "type": "object",
        "properties": {
          "cache_enable": {
            "type": "boolean",
            "x-go-name": "CacheEnable"
          },
          "cache_encryption_key": {
            "type": "string",
            "x-go-name": "CacheEncryptionKey"
          },
          "cache_ttl": {
            "type": "string",
            "x-go-name": "CacheTTL"
          },
          "new_proactive_cache_enable": {
            "type": "boolean",
            "x-go-name": "NewProActiveCacheEnable"
          },
          "proactive_cache_dump_interval": {
            "type": "string",
            "x-go-name": "ProActiveCacheDumpInterval"
          },
          "proactive_cache_enable": {
            "type": "boolean",
            "x-go-name": "ProActiveCacheEnable"
          },
          "proactive_cache_minimum_fetching_time": {
            "type": "string",
            "x-go-name": "ProActiveCacheMinimumFetchingTime"
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
      "CertificateStore": {
        "type": "object",
        "properties": {
          "certificate_pem": {
            "type": "string",
            "x-go-name": "CertificatePem"
          },
          "common_name": {
            "type": "string",
            "x-go-name": "CommonName"
          },
          "expiration_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ExpirationDate"
          },
          "expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "ExpirationEvents"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ClusterApiType": {
        "description": "ClusterApiType defines types of API access to cluster",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "DatadogForwardingConfig": {
        "type": "object",
        "properties": {
          "datadog_api_key": {
            "type": "string",
            "x-go-name": "DatadogApiKey"
          },
          "datadog_host": {
            "type": "string",
            "x-go-name": "DatadogHost"
          },
          "datadog_log_service": {
            "type": "string",
            "x-go-name": "DatadogLogService"
          },
          "datadog_log_source": {
            "type": "string",
            "x-go-name": "DatadogLogSource"
          },
          "datadog_log_tags": {
            "type": "string",
            "x-go-name": "DatadogLogTags"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "DefaultConfigPart": {
        "type": "object",
        "properties": {
          "certificate_access_id": {
            "type": "string",
            "x-go-name": "CertificateAccessId"
          },
          "default_protection_key_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ProtectionKeyID"
          },
          "default_secret_location": {
            "type": "string",
            "x-go-name": "SecretLocation"
          },
          "oidc_access_id": {
            "type": "string",
            "x-go-name": "OIDCAccessId"
          },
          "saml_access_id": {
            "type": "string",
            "x-go-name": "SamlAccessId"
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
      "ElasticsearchLogForwardingConfig": {
        "type": "object",
        "properties": {
          "elasticsearch_api_key": {
            "type": "string",
            "x-go-name": "ElasticsearchApiKey"
          },
          "elasticsearch_auth_type": {
            "type": "string",
            "x-go-name": "ElasticsearchAuthType"
          },
          "elasticsearch_cloud_id": {
            "type": "string",
            "x-go-name": "ElasticsearchCloudId"
          },
          "elasticsearch_enable_tls": {
            "type": "boolean",
            "x-go-name": "ElasticsearchEnableTLS"
          },
          "elasticsearch_index": {
            "type": "string",
            "x-go-name": "ElasticsearchIndex"
          },
          "elasticsearch_nodes": {
            "type": "string",
            "x-go-name": "ElasticsearchNodes"
          },
          "elasticsearch_password": {
            "type": "string",
            "x-go-name": "ElasticsearchPassword"
          },
          "elasticsearch_server_type": {
            "type": "string",
            "x-go-name": "ElasticsearchServerType"
          },
          "elasticsearch_tls_certificate": {
            "type": "string",
            "x-go-name": "ElasticsearchTlsCertificate"
          },
          "elasticsearch_user_name": {
            "type": "string",
            "x-go-name": "ElasticsearchUserName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "GatewayMessageQueueInfo": {
        "type": "object",
        "properties": {
          "broadcast_queue_name_a": {
            "type": "string",
            "x-go-name": "BroadcastQueueName"
          },
          "mq_type": {
            "type": "string",
            "x-go-name": "MQType"
          },
          "queue_name": {
            "type": "string",
            "x-go-name": "QueueName"
          },
          "queue_url": {
            "type": "string",
            "x-go-name": "QueueURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "GeneralConfigPart": {
        "type": "object",
        "properties": {
          "akeyless_url": {
            "description": "AkeylessUrl is here for BC only. Gator will still return it if it exists in\nthe configuration, but new clients (>=2.34.0) will ignore it and override it with what exists in\ntheir local file.\nIt will no longer be sent to Gator for update, so new clusters will only have\nthe default value saved in the DB.",
            "type": "string",
            "x-go-name": "AkeylessUrl"
          },
          "api_token_ttl": {
            "type": "string",
            "x-go-name": "ApiTokenTtl"
          },
          "display_name": {
            "type": "string",
            "x-go-name": "DisplayName"
          },
          "enable_sni_proxy": {
            "type": "boolean",
            "x-go-name": "EnableSniProxy"
          },
          "enable_tls": {
            "type": "boolean",
            "x-go-name": "EnableTLS"
          },
          "enable_tls_configure": {
            "type": "boolean",
            "x-go-name": "EnableTLSConfig"
          },
          "enable_tls_curl": {
            "type": "boolean",
            "x-go-name": "EnableTLSCurl"
          },
          "enable_tls_hvp": {
            "type": "boolean",
            "x-go-name": "EnableTLSHpv"
          },
          "gw_cluster_url": {
            "type": "string",
            "x-go-name": "GwClusterUrl"
          },
          "hvp_route_version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "HvpRouteVersion"
          },
          "notify_on_status_change": {
            "type": "boolean",
            "x-go-name": "NotifyOnStatusChange"
          },
          "tcp_port": {
            "type": "string",
            "x-go-name": "TcpPort"
          },
          "tls_cert": {
            "type": "string",
            "x-go-name": "TLSCert"
          },
          "tls_cert_common_name": {
            "type": "string",
            "x-go-name": "TlsCertCommonName"
          },
          "tls_cert_expiration_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "TlsCertExpirationDate"
          },
          "tls_cert_expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "TlsCertExpirationEvents"
          },
          "tls_key": {
            "type": "string",
            "x-go-name": "TLSKey"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "GoogleChronicleForwardingConfig": {
        "type": "object",
        "properties": {
          "customer_id": {
            "type": "string",
            "x-go-name": "CustomerID"
          },
          "log_type": {
            "type": "string",
            "x-go-name": "LogType"
          },
          "region": {
            "type": "string",
            "x-go-name": "Region"
          },
          "service_account_key": {
            "type": "string",
            "x-go-name": "ServiceAccountKey"
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
      "K8SAuth": {
        "type": "object",
        "properties": {
          "am_token_expiration": {
            "description": "AuthMethodTokenExpiration is time in seconds of expiration of the Akeyless Kube Auth Method token",
            "type": "integer",
            "format": "int64",
            "x-go-name": "AuthMethodTokenExpiration"
          },
          "auth_method_access_id": {
            "description": "AuthMethodAccessId of the Kubernetes auth method",
            "type": "string",
            "x-go-name": "AuthMethodAccessId"
          },
          "auth_method_prv_key_pem": {
            "description": "AuthMethodSigningKey is the private key (in base64 of the PEM format) associated with the public key defined in the\nKubernetes auth method, that used to sign the internal token for the Akeyless Kubernetes Auth Method",
            "type": "string",
            "x-go-name": "AuthMethodSigningKey"
          },
          "cluster_api_type": {
            "$ref": "#/components/schemas/ClusterApiType"
          },
          "disable_iss_validation": {
            "description": "DisableISSValidation is optional parameter to disable ISS validation",
            "type": "boolean",
            "x-go-name": "DisableISSValidation"
          },
          "id": {
            "type": "string",
            "x-go-name": "Id"
          },
          "k8s_auth_type": {
            "$ref": "#/components/schemas/NativeK8sAuthType"
          },
          "k8s_ca_cert": {
            "description": "K8SCACert is the CA Cert to use to call into the kubernetes API",
            "type": "string",
            "x-go-name": "K8SCACert"
          },
          "k8s_client_cert_data": {
            "description": "K8sClientCertData is the client certificate for k8s client certificate authentication",
            "type": "string",
            "x-go-name": "K8sClientCertData"
          },
          "k8s_client_key_data": {
            "description": "K8sClientKeyData is the client key for k8s client certificate authentication",
            "type": "string",
            "x-go-name": "K8sClientKeyData"
          },
          "k8s_host": {
            "description": "K8SHost is the url string for the kubernetes API",
            "type": "string",
            "x-go-name": "K8SHost"
          },
          "k8s_issuer": {
            "description": "K8SIssuer is the claim that specifies who issued the Kubernetes token",
            "type": "string",
            "x-go-name": "K8SIssuer"
          },
          "k8s_pub_keys_pem": {
            "description": "K8SPublicKeysPEM is the list of public key in PEM format",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "K8SPublicKeysPEM"
          },
          "k8s_token_reviewer_jwt": {
            "description": "K8STokenReviewerJWT is the bearer for clusterApiTypeK8s, used during TokenReview API call",
            "type": "string",
            "x-go-name": "K8STokenReviewerJWT"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "rancher_api_key": {
            "description": "RancherApiKey the bear token for clusterApiTypeRancher",
            "type": "string",
            "x-go-name": "RancherApiKey"
          },
          "rancher_cluster_id": {
            "description": "RancherClusterId cluster id as define in rancher (in case of clusterApiTypeRancher)",
            "type": "string",
            "x-go-name": "RancherClusterId"
          },
          "use_local_ca_jwt": {
            "description": "UseLocalCAJwt is an optional parameter to set defaulting to using\nthe local service account when running in a Kubernetes pod",
            "type": "boolean",
            "x-go-name": "UseLocalCAJwt"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "K8SAuthsConfigPart": {
        "type": "object",
        "properties": {
          "k8s_auths": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/K8SAuth"
            },
            "x-go-name": "K8SAuths"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "KMIPClient": {
        "type": "object",
        "properties": {
          "activate_keys_on_creation": {
            "type": "boolean",
            "x-go-name": "ActivateKeysOnCreation"
          },
          "certificate_issue_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CertificateIssueDate"
          },
          "certificate_ttl_in_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateTTLInSeconds"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "rules": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PathRule"
            },
            "x-go-name": "Rules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "KMIPConfigPart": {
        "type": "object",
        "properties": {
          "clients": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/KMIPClient"
            },
            "x-go-name": "Clients"
          },
          "key_enc": {
            "description": "Saves the private key of the cert issuer in encypted form",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "KeyEnc"
          },
          "server": {
            "$ref": "#/components/schemas/KMIPServer"
          },
          "server_enc": {
            "description": "Saved for backward compatibility\nTODO: remove this after all clients upgrade",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "ServerEnc"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "KMIPServer": {
        "type": "object",
        "properties": {
          "active": {
            "type": "boolean",
            "x-go-name": "Active"
          },
          "ca": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "CA"
          },
          "certificate": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "Certificate"
          },
          "certificate_issue_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CertificateIssueDate"
          },
          "certificate_ttl_in_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateTTLInSeconds"
          },
          "hostname": {
            "type": "string",
            "x-go-name": "Hostname"
          },
          "root": {
            "type": "string",
            "x-go-name": "Root"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "KerberosConfigPart": {
        "type": "object",
        "properties": {
          "kerberos_access_id": {
            "type": "string",
            "x-go-name": "KerberosAccessId"
          },
          "kerberos_keytab": {
            "type": "string",
            "x-go-name": "KerberosKeytab"
          },
          "kerberos_krb_5_conf": {
            "type": "string",
            "x-go-name": "KerberosKrb5Conf"
          },
          "kerberos_private_key": {
            "type": "string",
            "x-go-name": "KerberosPrivateKey"
          },
          "ldap_anonymous_search": {
            "type": "boolean",
            "x-go-name": "LdapAnonymousSearch"
          },
          "ldap_bind_dn": {
            "type": "string",
            "x-go-name": "LdapBindDn"
          },
          "ldap_bind_password": {
            "type": "string",
            "x-go-name": "LdapBindPassword"
          },
          "ldap_cert": {
            "type": "string",
            "x-go-name": "LdapCertificate"
          },
          "ldap_group_attr": {
            "type": "string",
            "x-go-name": "LdapGroupAttr"
          },
          "ldap_group_dn": {
            "type": "string",
            "x-go-name": "LdapGroupDn"
          },
          "ldap_group_filter": {
            "type": "string",
            "x-go-name": "LdapGroupFilter"
          },
          "ldap_url": {
            "type": "string",
            "x-go-name": "LdapUrlAddress"
          },
          "ldap_user_attr": {
            "type": "string",
            "x-go-name": "LdapUserAttr"
          },
          "ldap_user_dn": {
            "type": "string",
            "x-go-name": "LdapUserDn"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LdapConfigPart": {
        "type": "object",
        "properties": {
          "ldap_access_id": {
            "type": "string",
            "x-go-name": "LdapAccessId"
          },
          "ldap_anonymous_search": {
            "type": "boolean",
            "x-go-name": "LdapAnonymousSearch"
          },
          "ldap_bind_dn": {
            "type": "string",
            "x-go-name": "LdapBindDn"
          },
          "ldap_bind_password": {
            "type": "string",
            "x-go-name": "LdapBindPassword"
          },
          "ldap_cert": {
            "type": "string",
            "x-go-name": "LdapCertificate"
          },
          "ldap_enable": {
            "type": "boolean",
            "x-go-name": "LdapEnable"
          },
          "ldap_group_attr": {
            "type": "string",
            "x-go-name": "LdapGroupAttr"
          },
          "ldap_group_dn": {
            "type": "string",
            "x-go-name": "LdapGroupDn"
          },
          "ldap_group_filter": {
            "type": "string",
            "x-go-name": "LdapGroupFilter"
          },
          "ldap_private_key": {
            "type": "string",
            "x-go-name": "LdapPrivateKey"
          },
          "ldap_token_expiration": {
            "type": "string",
            "x-go-name": "LdapTokenExpiration"
          },
          "ldap_url": {
            "type": "string",
            "x-go-name": "LdapUrlAddress"
          },
          "ldap_user_attr": {
            "type": "string",
            "x-go-name": "LdapUserAttr"
          },
          "ldap_user_dn": {
            "type": "string",
            "x-go-name": "LdapUserDn"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LeadershipConfigPart": {
        "type": "object",
        "properties": {
          "open_leadership": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint32"
            },
            "x-go-name": "OpenLeadership"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LogForwardingConfigPart": {
        "type": "object",
        "properties": {
          "aws_s3_config": {
            "$ref": "#/components/schemas/AwsS3LogForwardingConfig"
          },
          "azure_analytics_config": {
            "$ref": "#/components/schemas/AzureLogAnalyticsForwardingConfig"
          },
          "datadog_config": {
            "$ref": "#/components/schemas/DatadogForwardingConfig"
          },
          "elasticsearch_config": {
            "$ref": "#/components/schemas/ElasticsearchLogForwardingConfig"
          },
          "google_chronicle_config": {
            "$ref": "#/components/schemas/GoogleChronicleForwardingConfig"
          },
          "json_output": {
            "type": "boolean",
            "x-go-name": "JsonOutput"
          },
          "logan_enable": {
            "type": "boolean",
            "x-go-name": "LoganEnable"
          },
          "logan_url": {
            "type": "string",
            "x-go-name": "LoganURLConfig"
          },
          "logstash_config": {
            "$ref": "#/components/schemas/LogstashLogForwardingConfig"
          },
          "logz_io_config": {
            "$ref": "#/components/schemas/LogzIoLogForwardingConfig"
          },
          "pull_interval_sec": {
            "type": "string",
            "x-go-name": "PullIntervalSec"
          },
          "splunk_config": {
            "$ref": "#/components/schemas/SplunkLogForwardingConfig"
          },
          "sumo_logic_config": {
            "$ref": "#/components/schemas/SumologicLogForwardingConfig"
          },
          "syslog_config": {
            "$ref": "#/components/schemas/SyslogLogForwardingConfig"
          },
          "target_log_type": {
            "type": "string",
            "x-go-name": "TargetLogType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LogstashLogForwardingConfig": {
        "type": "object",
        "properties": {
          "logstash_dns": {
            "type": "string",
            "x-go-name": "LogstashDns"
          },
          "logstash_enable_tls": {
            "type": "boolean",
            "x-go-name": "LogstashEnableTLS"
          },
          "logstash_protocol": {
            "type": "string",
            "x-go-name": "LogstashProtocol"
          },
          "logstash_tls_certificate": {
            "type": "string",
            "x-go-name": "LogstashTlsCertificate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "LogzIoLogForwardingConfig": {
        "type": "object",
        "properties": {
          "target_logz_io_protocol": {
            "type": "string",
            "x-go-name": "TargetLogzIoProtocol"
          },
          "target_logz_io_token": {
            "type": "string",
            "x-go-name": "TargetLogzIoToken"
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
      "NativeK8sAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "PathRule": {
        "type": "object",
        "title": "PathRule is a single rule used in AKEYLESS RBAC.",
        "properties": {
          "assigners": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RuleAssigner"
            },
            "x-go-name": "Assigners"
          },
          "capabilities": {
            "description": "The approved/denied capabilities in the path",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Capabilities"
          },
          "cb": {
            "type": "integer",
            "format": "uint64",
            "x-go-name": "CapabilitiesBitmap"
          },
          "is_limit_access": {
            "description": "flag that indicate that this rule is allowed to be access RemainingAccess of times.",
            "type": "boolean",
            "x-go-name": "IsLimitAccess"
          },
          "item_id": {
            "description": "The item id this rule directly refers to (when applicable)",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "number_of_access_used": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAccessUsed"
          },
          "number_of_allowed_access": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAllowedAccess"
          },
          "path": {
            "description": "The path the rule refers to",
            "type": "string",
            "x-go-name": "Path"
          },
          "start_time": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "StartTime"
          },
          "ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          },
          "type": {
            "$ref": "#/components/schemas/PathRuleType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PathRuleType": {
        "type": "string",
        "title": "PathRuleType defines a kind of every PathRule assigned to a Role.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Producer": {
        "type": "object",
        "properties": {
          "active": {
            "type": "boolean",
            "x-go-name": "Active"
          },
          "failure_message": {
            "type": "string",
            "x-go-name": "FailureMessage"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Id"
          },
          "init": {
            "type": "boolean",
            "x-go-name": "Init"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "ProducersConfigPart": {
        "type": "object",
        "properties": {
          "producers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Producer"
            },
            "x-go-name": "Producers"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "Rotator": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Id"
          },
          "last_error": {
            "type": "string",
            "x-go-name": "LastError"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "rotation_interval": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "RotationInterval"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "RotatorsConfigPart": {
        "type": "object",
        "properties": {
          "rotators": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Rotator"
            },
            "x-go-name": "Rotators"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "RuleAssigner": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "unique_id": {
            "type": "string",
            "x-go-name": "UniqueId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "SplunkLogForwardingConfig": {
        "type": "object",
        "properties": {
          "splunk_enable_batch": {
            "type": "string",
            "x-go-name": "SplunkEnableBatch"
          },
          "splunk_enable_tls": {
            "type": "boolean",
            "x-go-name": "SplunkEnableTLS"
          },
          "splunk_index": {
            "type": "string",
            "x-go-name": "SplunkIndex"
          },
          "splunk_source": {
            "type": "string",
            "x-go-name": "SplunkSource"
          },
          "splunk_sourcetype": {
            "type": "string",
            "x-go-name": "SplunkSourcetype"
          },
          "splunk_tls_certificate": {
            "type": "string",
            "x-go-name": "SplunkTlsCertificate"
          },
          "splunk_token": {
            "type": "string",
            "x-go-name": "SplunkToken"
          },
          "splunk_url": {
            "type": "string",
            "x-go-name": "SplunkUrl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SumologicLogForwardingConfig": {
        "type": "object",
        "properties": {
          "sumo_logic_endpoint": {
            "type": "string",
            "x-go-name": "SumologicEndPointURL"
          },
          "sumo_logic_host": {
            "type": "string",
            "x-go-name": "SumologicHost"
          },
          "sumo_logic_tags": {
            "type": "string",
            "x-go-name": "SumologicTags"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "SyslogLogForwardingConfig": {
        "type": "object",
        "properties": {
          "syslog_enable_tls": {
            "type": "boolean",
            "x-go-name": "SyslogEnableTLS"
          },
          "syslog_formatter": {
            "type": "string",
            "x-go-name": "SyslogFormatter"
          },
          "syslog_host": {
            "type": "string",
            "x-go-name": "SyslogHost"
          },
          "syslog_network": {
            "type": "string",
            "x-go-name": "SyslogNetwork"
          },
          "syslog_target_tag": {
            "type": "string",
            "x-go-name": "SyslogTargetTag"
          },
          "syslog_tls_certificate": {
            "type": "string",
            "x-go-name": "SyslogTlsCertificate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "TargetFormatType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "gatewayGetConfig": {
        "description": "gatewayGetConfig is a command that returns gateway configuration",
        "type": "object",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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