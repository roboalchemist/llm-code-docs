# Source: https://docs.akeyless.io/reference/gatewaycreatemigration.md

# /gateway-create-migration

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
    "/gateway-create-migration": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayCreateMigration",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayCreateMigration"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayMigrationCreateResponse"
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
      "gatewayMigrationCreateResponse": {
        "description": "gatewayMigrationCreateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewayMigrationCreateOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GatewayMigrationCreateOutput": {
        "type": "object",
        "properties": {
          "migration_name": {
            "type": "string",
            "x-go-name": "MigrationName"
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
      "gatewayCreateMigration": {
        "description": "gatewayCreateMigration is a command that create migration",
        "type": "object",
        "required": [
          "si-target-name",
          "si-users-path-template",
          "hosts",
          "name",
          "target-location"
        ],
        "properties": {
          "ServiceAccountKeyDecoded": {
            "type": "string"
          },
          "ad-auto-rotate": {
            "description": "Enable/Disable automatic/recurrent rotation for migrated secrets. Default is false: only manual rotation is allowed for migrated secrets. If set to true, this command should be combined with --ad-rotation-interval and --ad-rotation-hour parameters (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdAutoRotateV2"
          },
          "ad-cert-expiration-event-in": {
            "description": "How many days before the expiration of discovered certificates would you like to be notified (Relevant only for Active Directory migration with certificate discovery enabled)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AdCertificatesExpirationEventsInDays"
          },
          "ad-certificates-path-template": {
            "description": "Path location template for migrating certificates e.g.: /Certificates/{{COMMON_NAME}} (Relevant only for Active Directory migration with certificate discovery enabled)",
            "type": "string",
            "x-go-name": "AdCertificatesPathTemplate"
          },
          "ad-computer-base-dn": {
            "description": "Distinguished Name of Computer objects (servers) to search in Active Directory e.g.: CN=Computers,DC=example,DC=com (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdComputerBaseDNV2"
          },
          "ad-discover-iis-app": {
            "description": "Enable/Disable discovery of IIS application from each domain server as part of the SSH/Windows Rotated Secrets. Default is false. (Relevant only for Active Directory migration)",
            "type": "string",
            "default": "false",
            "x-go-name": "AdDiscoverIISApp"
          },
          "ad-discover-services": {
            "description": "Enable/Disable discovery of Windows services from each domain server as part of the SSH/Windows Rotated Secrets. Default is false. (Relevant only for Active Directory migration)",
            "type": "string",
            "default": "false",
            "x-go-name": "AdDiscoverServices"
          },
          "ad-discovery-types": {
            "description": "Set migration discovery types (domain-users, computers, local-users). (Relevant only for Active Directory migration)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AdDiscoverTypes"
          },
          "ad-domain-name": {
            "description": "Active Directory Domain Name (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdDomainNameV2"
          },
          "ad-domain-users-path-template": {
            "description": "Path location template for migrating domain users as Rotated Secrets e.g.: .../DomainUsers/{{USERNAME}} (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdDomainUsersPathTemplateV2"
          },
          "ad-local-users-ignore": {
            "description": "Comma-separated list of Local Users which should not be migrated (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdLocalUsersIgnoreV2"
          },
          "ad-local-users-path-template": {
            "description": "Path location template for migrating domain users as Rotated Secrets e.g.: .../LocalUsers/{{COMPUTER_NAME}}/{{USERNAME}} (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdLocalUsersPathTemplateV2"
          },
          "ad-os-filter": {
            "description": "Filter by Operating System to run the migration, can be used with wildcards, e.g. SRV20* (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdOsFilter"
          },
          "ad-rotation-hour": {
            "description": "The hour of the scheduled rotation in UTC (Relevant only for Active Directory migration)",
            "type": "integer",
            "format": "int32",
            "x-go-name": "AdRotationHourV2"
          },
          "ad-rotation-interval": {
            "description": "The number of days to wait between every automatic rotation [1-365] (Relevant only for Active Directory migration)",
            "type": "integer",
            "format": "int32",
            "x-go-name": "AdRotationIntervalV2"
          },
          "ad-sra-enable-rdp": {
            "description": "Enable/Disable RDP Secure Remote Access for the migrated local users rotated secrets. Default is false: rotated secrets will not be created with SRA (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdSRAEnableRDPV2"
          },
          "ad-ssh-port": {
            "description": "Set the SSH Port for further connection to the domain servers. Default is port 22 (Relevant only for Active Directory migration)",
            "type": "string",
            "default": "22",
            "x-go-name": "AdSshPort"
          },
          "ad-target-format": {
            "description": "Relevant only for ad-discovery-types=computers. For linked, all computers will be migrated into a linked target(s). if set with regular, the migration will create a target for each computer.",
            "type": "string",
            "default": "linked",
            "x-go-name": "AdTargetFormat"
          },
          "ad-target-name": {
            "description": "Active Directory LDAP Target Name. Server type should be Active Directory (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdTargetNameV2"
          },
          "ad-targets-path-template": {
            "description": "Path location template for migrating domain servers as SSH/Windows Targets e.g.: .../Servers/{{COMPUTER_NAME}} (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdTargetsPathTemplateV2"
          },
          "ad-targets-type": {
            "description": "Set the target type of the domain servers [ssh/windows](Relevant only for Active Directory migration)",
            "type": "string",
            "default": "windows",
            "x-go-name": "TargetsType"
          },
          "ad-user-base-dn": {
            "description": "Distinguished Name of User objects to search in Active Directory, e.g.: CN=Users,DC=example,DC=com (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdUserBaseDNV2"
          },
          "ad-user-groups": {
            "description": "Comma-separated list of domain groups from which privileged domain users will be migrated. If empty, migrate all users based on the --ad-user-base-dn (Relevant only for Active Directory migration)",
            "type": "string",
            "x-go-name": "AdUserGroupsV2"
          },
          "ad-winrm-over-http": {
            "description": "Use WinRM over HTTP, by default runs over HTTPS",
            "type": "string",
            "default": "false",
            "x-go-name": "AdWinrmOverHttp"
          },
          "ad-winrm-port": {
            "description": "Set the WinRM Port for further connection to the domain servers. Default is 5986 (Relevant only for Active Directory migration)",
            "type": "string",
            "default": "5986",
            "x-go-name": "AdWinrmPort"
          },
          "ad_discover_local_users": {
            "description": "Enable/Disable discovery of local users from each domain server and migrate them as SSH/Windows Rotated Secrets. Default is false: only domain users will be migrated. Discovery of local users might require further installation of SSH on the servers, based on the supplied computer base DN. This will be implemented automatically as part of the migration process (Relevant only for Active Directory migration)\nDeprecated: use AdDiscoverTypes",
            "type": "string",
            "x-go-name": "AdDiscoverLocalUsersDeprecated"
          },
          "ai-certificate-discovery": {
            "description": "Enable AI-assisted certificate discovery (only when AI Insight is enabled on the Gateway)",
            "type": "string",
            "x-go-name": "AdUseAI"
          },
          "aws-key": {
            "description": "AWS Secret Access Key (relevant only for AWS migration)",
            "type": "string",
            "x-go-name": "AwsSecret"
          },
          "aws-key-id": {
            "description": "AWS Access Key ID with sufficient permissions to get all secrets, e.g. 'arn:aws:secretsmanager:[Region]:[AccountId]:secret:[/path/to/secrets/*]' (relevant only for AWS migration)",
            "type": "string",
            "x-go-name": "AwsKey"
          },
          "aws-region": {
            "description": "AWS region of the required Secrets Manager (relevant only for AWS migration)",
            "type": "string",
            "default": "us-east-2",
            "x-go-name": "AwsRegion"
          },
          "azure-client-id": {
            "description": "Azure Key Vault Access client ID, should be Azure AD App with a service principal (relevant only for Azure Key Vault migration)",
            "type": "string",
            "x-go-name": "AzureClient"
          },
          "azure-kv-name": {
            "description": "Azure Key Vault Name (relevant only for Azure Key Vault migration)",
            "type": "string",
            "x-go-name": "AzureName"
          },
          "azure-secret": {
            "description": "Azure Key Vault secret (relevant only for Azure Key Vault migration)",
            "type": "string",
            "x-go-name": "AzureSecret"
          },
          "azure-tenant-id": {
            "description": "Azure Key Vault Access tenant ID (relevant only for Azure Key Vault migration)",
            "type": "string",
            "x-go-name": "AzureTenant"
          },
          "conjur-account": {
            "description": "Conjur account name set on your Conjur server (relevant only for Conjur migration).",
            "type": "string",
            "x-go-name": "ConjurAccount"
          },
          "conjur-api-key": {
            "description": "Conjur API Key for the specified user (relevant only for Conjur migration).",
            "type": "string",
            "x-go-name": "ConjurApiKey"
          },
          "conjur-url": {
            "description": "Conjur server base URL (relevant only for Conjur migration).\nIf conjur-url is HTTPS and Conjur uses a private CA/self-signed certificate,\nmake the CA bundle available on the Gateway and set CONJUR_SSL_CERT_PATH to its path.",
            "type": "string",
            "x-go-name": "ConjurURL"
          },
          "conjur-username": {
            "description": "Conjur username used to authenticate (relevant only for Conjur migration).",
            "type": "string",
            "x-go-name": "ConjurUsername"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "gcp-key": {
            "description": "Base64-encoded GCP Service Account private key text with sufficient permissions to Secrets Manager, Minimum required permission is Secret Manager Secret Accessor, e.g. 'roles/secretmanager.secretAccessor' (relevant only for GCP migration)",
            "type": "string",
            "x-go-name": "ServiceAccountKey"
          },
          "gcp-project-id": {
            "description": "GCP Project ID (cross-project override)",
            "type": "string",
            "x-go-name": "GcpProjectId"
          },
          "hashi-json": {
            "description": "Import secret key as json value or independent secrets (relevant only for HasiCorp Vault migration) [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "HashiImportAsJson"
          },
          "hashi-ns": {
            "description": "HashiCorp Vault Namespaces is a comma-separated list of namespaces which need to be imported into Akeyless Vault. For every provided namespace, all its child namespaces are imported as well, e.g. nmsp/subnmsp1/subnmsp2,nmsp/anothernmsp. By default, import all namespaces (relevant only for HasiCorp Vault migration)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "HashiNamespaces"
          },
          "hashi-token": {
            "description": "HashiCorp Vault access token with sufficient permissions to preform list & read operations on secrets objects (relevant only for HasiCorp Vault migration)",
            "type": "string",
            "x-go-name": "HashiToken"
          },
          "hashi-url": {
            "description": "HashiCorp Vault API URL, e.g. https://vault-mgr01:8200 (relevant only for HasiCorp Vault migration)",
            "type": "string",
            "x-go-name": "HashiUrl"
          },
          "hosts": {
            "description": "A comma separated list of IPs, CIDR ranges, or DNS names to scan",
            "type": "string",
            "x-go-name": "Hosts"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "k8s-ca-certificate": {
            "description": "For Certificate Authentication method\nK8s Cluster CA certificate (relevant only for K8s migration with Certificate Authentication method)",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "K8SCA"
          },
          "k8s-client-certificate": {
            "description": "K8s Client certificate with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Certificate Authentication method)",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "K8SClientCert"
          },
          "k8s-client-key": {
            "description": "K8s Client key (relevant only for K8s migration with Certificate Authentication method)",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "K8SClientKey"
          },
          "k8s-namespace": {
            "description": "K8s Namespace, Use this field to import secrets from a particular namespace only. By default, the secrets are imported from all namespaces (relevant only for K8s migration)",
            "type": "string",
            "x-go-name": "K8SNamespace"
          },
          "k8s-password": {
            "description": "K8s Client password (relevant only for K8s migration with Password Authentication method)",
            "type": "string",
            "x-go-name": "K8SPassword"
          },
          "k8s-skip-system": {
            "description": "K8s Skip Control Plane Secrets, This option allows to avoid importing secrets from system namespaces (relevant only for K8s migration)",
            "type": "boolean",
            "x-go-name": "K8SSkipSystem"
          },
          "k8s-token": {
            "description": "For Token Authentication method\nK8s Bearer Token with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Token Authentication method)",
            "type": "string",
            "x-go-name": "K8SToken"
          },
          "k8s-url": {
            "description": "K8s API Server URL, e.g. https://k8s-api.mycompany.com:6443 (relevant only for K8s migration)",
            "type": "string",
            "x-go-name": "K8SServer"
          },
          "k8s-username": {
            "description": "For Password Authentication method\nK8s Client username with sufficient permission to list and get secrets in the namespace(s) you selected (relevant only for K8s migration with Password Authentication method)",
            "type": "string",
            "x-go-name": "K8SUsername"
          },
          "name": {
            "description": "Migration name",
            "type": "string",
            "x-go-name": "MigrationName"
          },
          "port-ranges": {
            "description": "A comma separated list of port ranges\nExamples: \"80,443\" or \"80,443,8080-8090\" or \"443\"",
            "type": "string",
            "default": "443",
            "x-go-name": "PortRanges"
          },
          "protection-key": {
            "description": "The name of the key that protects the classic key value (if empty, the account default key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "si-auto-rotate": {
            "description": "Enable/Disable automatic/recurrent rotation for migrated secrets. Default is false: only manual rotation is allowed for migrated secrets. If set to true, this command should be combined with --si-rotation-interval and --si-rotation-hour parameters (Relevant only for Server Inventory migration)",
            "type": "string",
            "x-go-name": "SiAutoRotate"
          },
          "si-rotation-hour": {
            "description": "The hour of the scheduled rotation in UTC (Relevant only for Server Inventory migration)",
            "type": "integer",
            "format": "int32",
            "x-go-name": "SiRotationHour"
          },
          "si-rotation-interval": {
            "description": "The number of days to wait between every automatic rotation [1-365] (Relevant only for Server Inventory migration)",
            "type": "integer",
            "format": "int32",
            "x-go-name": "SiRotationInterval"
          },
          "si-sra-enable-rdp": {
            "description": "Enable/Disable RDP Secure Remote Access for the migrated local users rotated secrets. Default is false: rotated secrets will not be created with SRA (Relevant only for Server Inventory migration)",
            "type": "string",
            "default": "false",
            "x-go-name": "SiSRAEnableRDP"
          },
          "si-target-name": {
            "description": "SSH, Windows or Linked Target Name. (Relevant only for Server Inventory migration)",
            "type": "string",
            "x-go-name": "SiTargetName"
          },
          "si-user-groups": {
            "description": "Comma-separated list of groups to migrate users from. If empty, all users from all groups will be migrated (Relevant only for Server Inventory migration)",
            "type": "string",
            "x-go-name": "SiUserGroups"
          },
          "si-users-ignore": {
            "description": "Comma-separated list of Local Users which should not be migrated (Relevant only for Server Inventory migration)",
            "type": "string",
            "x-go-name": "SiLocalUsersIgnore"
          },
          "si-users-path-template": {
            "description": "Path location template for migrating users as Rotated Secrets e.g.: .../Users/{{COMPUTER_NAME}}/{{USERNAME}} (Relevant only for Server Inventory migration)",
            "type": "string",
            "x-go-name": "SiUsersPathTemplate"
          },
          "target-location": {
            "description": "Target location in Akeyless for imported secrets",
            "type": "string",
            "x-go-name": "TargetLocation"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Migration type (hashi/aws/gcp/k8s/azure_kv/conjur/active_directory/server_inventory/certificate)",
            "type": "string",
            "x-go-name": "MigrationType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "use-gw-cloud-identity": {
            "description": "Use the GW's Cloud IAM",
            "type": "boolean",
            "x-go-name": "GCPUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```