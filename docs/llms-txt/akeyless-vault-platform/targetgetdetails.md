# Source: https://docs.akeyless.io/reference/targetgetdetails.md

# /target-get-details

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
    "/target-get-details": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetGetDetails",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetGetDetails"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/targetGetDetailsResponse"
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
      "targetGetDetailsResponse": {
        "description": "targetGetDetailsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetTargetDetailsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ACMEChallengeType": {
        "description": "ACMEChallengeType defines ACME challenge type for Let's Encrypt",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ACMEEnvironment": {
        "description": "ACMEEnvironment defines Let's Encrypt ACME directory environment",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AWSGatewayCloudIdentityExternalIdOpt": {
        "type": "object",
        "title": "AWSGatewayCloudIdentityExternalIdOpt ...",
        "properties": {
          "generated_external_id": {
            "type": "string",
            "x-go-name": "GeneratedExternalId"
          },
          "is_enabled": {
            "type": "boolean",
            "x-go-name": "IsEnabled"
          },
          "role_arn": {
            "type": "string",
            "x-go-name": "RoleARN"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AWSTargetDetails": {
        "type": "object",
        "title": "AWSTargetDetails ...",
        "properties": {
          "aws_access_key_id": {
            "type": "string",
            "x-go-name": "AWSAccessKeyID"
          },
          "aws_region": {
            "type": "string",
            "x-go-name": "AWSRegion"
          },
          "aws_secret_access_key": {
            "type": "string",
            "x-go-name": "AWSSecretAccessKey"
          },
          "aws_session_token": {
            "type": "string",
            "x-go-name": "AWSSessionToken"
          },
          "gw_cloud_identity_external_id_opt": {
            "$ref": "#/components/schemas/AWSGatewayCloudIdentityExternalIdOpt"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "AWSUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ArtifactoryTargetDetails": {
        "type": "object",
        "title": "ArtifactoryTargetDetails ...",
        "properties": {
          "artifactory_admin_apikey": {
            "type": "string",
            "x-go-name": "ArtifactoryAdminApiKey"
          },
          "artifactory_admin_username": {
            "type": "string",
            "x-go-name": "ArtifactoryAdminUsername"
          },
          "artifactory_base_url": {
            "type": "string",
            "x-go-name": "ArtifactoryBaseURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AssocRelationship": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AzureTargetDetails": {
        "type": "object",
        "title": "AzureTargetDetails ..",
        "properties": {
          "azure_client_id": {
            "type": "string",
            "x-go-name": "AzureClientID"
          },
          "azure_client_secret": {
            "type": "string",
            "x-go-name": "AzureClientSecret"
          },
          "azure_cloud": {
            "type": "string",
            "x-go-name": "AzureCloud"
          },
          "azure_resource_group_name": {
            "type": "string",
            "x-go-name": "AzureResourceGroupName"
          },
          "azure_resource_name": {
            "type": "string",
            "x-go-name": "AzureResourceName"
          },
          "azure_subscription_id": {
            "type": "string",
            "x-go-name": "AzureSubscriptionId"
          },
          "azure_tenant_id": {
            "type": "string",
            "x-go-name": "AzureTenantID"
          },
          "azure_username": {
            "type": "string",
            "x-go-name": "AzureUsername"
          },
          "connection_type": {
            "$ref": "#/components/schemas/TargetAuthType"
          },
          "expiration_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ExpirationDate"
          },
          "grace_rotated_secret_key": {
            "type": "string",
            "x-go-name": "GraceRotatedSecretKey"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "AzureUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateVersionInfo": {
        "type": "object",
        "properties": {
          "not_after": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotAfter"
          },
          "not_before": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotBefore"
          },
          "status": {
            "$ref": "#/components/schemas/CertificateStatus"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ChefTargetDetails": {
        "description": "ChefTargetDetails",
        "type": "object",
        "properties": {
          "chef_server_host_name": {
            "type": "string",
            "x-go-name": "ChefServerHostName"
          },
          "chef_server_key": {
            "type": "string",
            "x-go-name": "ChefServerKey"
          },
          "chef_server_port": {
            "type": "string",
            "x-go-name": "ChefServerPort"
          },
          "chef_server_url": {
            "type": "string",
            "x-go-name": "ChefServerURL"
          },
          "chef_server_username": {
            "type": "string",
            "x-go-name": "ChefServerUsername"
          },
          "chef_skip_ssl": {
            "type": "boolean",
            "x-go-name": "ChefSkipSSL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CustomTargetDetails": {
        "type": "object",
        "properties": {
          "payload": {
            "type": "string",
            "x-go-name": "Payload"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DbTargetDetails": {
        "description": "DbTargetDetails",
        "type": "object",
        "properties": {
          "cloud_service_provider": {
            "type": "string",
            "x-go-name": "CloudServiceProvider"
          },
          "cluster_mode": {
            "type": "boolean",
            "x-go-name": "ClusterMode"
          },
          "connection_type": {
            "$ref": "#/components/schemas/TargetAuthType"
          },
          "db_client_id": {
            "type": "string",
            "x-go-name": "MssqlAzureClientID"
          },
          "db_client_secret": {
            "type": "string",
            "x-go-name": "MssqlAzureClientSecret"
          },
          "db_host_name": {
            "type": "string",
            "x-go-name": "DbHostName"
          },
          "db_name": {
            "type": "string",
            "x-go-name": "DbName"
          },
          "db_port": {
            "type": "string",
            "x-go-name": "DbPort"
          },
          "db_private_key": {
            "description": "(Optional) Private Key in PEM format",
            "type": "string",
            "x-go-name": "DbPrivateKey"
          },
          "db_private_key_passphrase": {
            "type": "string",
            "x-go-name": "DbPrivateKeyPassphrase"
          },
          "db_pwd": {
            "type": "string",
            "x-go-name": "DbPwd"
          },
          "db_server_certificates": {
            "description": "(Optional) DBServerCertificates defines the set of root certificate authorities\nthat clients use when verifying server certificates.\nIf DBServerCertificates is empty, TLS uses the host's root CA set.",
            "type": "string",
            "x-go-name": "DBServerCertificates"
          },
          "db_server_name": {
            "description": "(Optional) ServerName is used to verify the hostname on the returned\ncertificates unless InsecureSkipVerify is given. It is also included\nin the client's handshake to support virtual hosting unless it is\nan IP address.",
            "type": "string",
            "x-go-name": "DBServerName"
          },
          "db_tenant_id": {
            "type": "string",
            "x-go-name": "MssqlAzureTenantID"
          },
          "db_user_name": {
            "type": "string",
            "x-go-name": "DbUserName"
          },
          "oracle_wallet_details": {
            "$ref": "#/components/schemas/WalletDetails"
          },
          "sf_account": {
            "type": "string",
            "x-go-name": "SnowflakeAccountName"
          },
          "ssl_connection_certificate": {
            "description": "(Optional) SSLConnectionCertificate defines the certificate for SSL connection. Must be base64 certificate loaded by UI using file loader field",
            "type": "string",
            "x-go-name": "SSLConnectionCertificate"
          },
          "ssl_connection_mode": {
            "description": "(Optional) SSLConnectionMode defines if SSL mode will be used to connect to DB",
            "type": "boolean",
            "x-go-name": "SSLConnectionMode"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DockerhubTargetDetails": {
        "description": "DockerhubTargetDetails",
        "type": "object",
        "properties": {
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "user_name": {
            "type": "string",
            "x-go-name": "UserName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Duration": {
        "description": "A Duration represents the elapsed time between two instants\nas an int64 nanosecond count. The representation limits the\nlargest representable duration to approximately 290 years.",
        "type": "integer",
        "format": "int64",
        "x-go-package": "time"
      },
      "EKSTargetDetails": {
        "description": "EKSTargetDetails defines details related to connecting to\na EKS (Elastic Container Service) target",
        "type": "object",
        "properties": {
          "eks_access_key_id": {
            "type": "string",
            "x-go-name": "EKSAccessID"
          },
          "eks_cluster_ca_certificate": {
            "type": "string",
            "x-go-name": "EKSClusterCACertificate"
          },
          "eks_cluster_endpoint": {
            "type": "string",
            "x-go-name": "EKSClusterEndpoint"
          },
          "eks_cluster_name": {
            "type": "string",
            "x-go-name": "EKSClusterName"
          },
          "eks_region": {
            "type": "string",
            "x-go-name": "EKSRegion"
          },
          "eks_secret_access_key": {
            "type": "string",
            "x-go-name": "EKSSecretAccessKey"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "EKSUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GKETargetDetails": {
        "description": "GKETargetDetails defines details related to connecting to\na GKE (Google Kubernetes Engine) target",
        "type": "object",
        "properties": {
          "gke_cluster_ca_certificate": {
            "type": "string",
            "x-go-name": "GKEClusterCACertificate"
          },
          "gke_cluster_endpoint": {
            "type": "string",
            "x-go-name": "GKEClusterEndpoint"
          },
          "gke_cluster_name": {
            "type": "string",
            "x-go-name": "GKEClusterName"
          },
          "gke_service_account_key": {
            "type": "string",
            "x-go-name": "GKEServiceAccountKey"
          },
          "gke_service_account_name": {
            "type": "string",
            "x-go-name": "GKEServiceAccountName"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "GKEUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GcpTargetDetails": {
        "type": "object",
        "title": "GcpTargetDetails ...",
        "properties": {
          "gcp_service_account_email": {
            "type": "string",
            "x-go-name": "GCPServiceAccountEmail"
          },
          "gcp_service_account_key": {
            "type": "string",
            "x-go-name": "GCPServiceAccountKey"
          },
          "gcp_service_account_key_base64": {
            "type": "string",
            "x-go-name": "GCPServiceAccountKeyBase64"
          },
          "gcp_service_account_key_id": {
            "type": "string",
            "x-go-name": "GCPServiceAccountKeyId"
          },
          "grace_rotated_secret_key": {
            "type": "string",
            "x-go-name": "GraceRotatedSecretKey"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "GCPUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GeminiTargetDetails": {
        "description": "GeminiTargetDetails defines details related to connecting to a Google Gemini provider",
        "type": "object",
        "properties": {
          "api_key": {
            "type": "string",
            "x-go-name": "ApiKey"
          },
          "gemini_url": {
            "type": "string",
            "x-go-name": "BaseURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GetTargetDetailsOutput": {
        "type": "object",
        "title": "GetTargetDetailsOutput defines output of GetTargetDetails operation.",
        "properties": {
          "target": {
            "$ref": "#/components/schemas/Target"
          },
          "value": {
            "$ref": "#/components/schemas/TargetTypeDetailsInput"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GithubTargetDetails": {
        "type": "object",
        "title": "GithubTargetDetails ...",
        "properties": {
          "github_app_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GithubAppId"
          },
          "github_app_private_key": {
            "type": "string",
            "x-go-name": "GithubAppPrivateKey"
          },
          "github_base_url": {
            "type": "string",
            "x-go-name": "GithubBaseURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GitlabTargetDetails": {
        "description": "GitlabTargetDetails",
        "type": "object",
        "properties": {
          "gitlab_access_token": {
            "type": "string",
            "x-go-name": "GitlabAccessToken"
          },
          "gitlab_certificate": {
            "type": "string",
            "x-go-name": "GitlabCertificate"
          },
          "gitlab_url": {
            "type": "string",
            "x-go-name": "GitlabURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GlobalSignAtlasTargetDetails": {
        "description": "GlobalSignAtlasTargetDetails",
        "type": "object",
        "properties": {
          "api_key": {
            "type": "string",
            "x-go-name": "APIKey"
          },
          "api_secret": {
            "type": "string",
            "x-go-name": "APISecret"
          },
          "mtls_cert": {
            "type": "string",
            "x-go-name": "MutualTLSCert"
          },
          "mtls_key": {
            "type": "string",
            "x-go-name": "MutualTLSKey"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GlobalSignGCCTargetDetails": {
        "description": "GlobalSignGCCTargetDetails",
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "x-go-name": "ContactEmail"
          },
          "first_name": {
            "description": "Contact Info - GlobalSign requires this to be sent with every certificate creation request",
            "type": "string",
            "x-go-name": "ContactFirstName"
          },
          "last_name": {
            "type": "string",
            "x-go-name": "ContactLastName"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "phone": {
            "type": "string",
            "x-go-name": "ContactPhone"
          },
          "profile_id": {
            "type": "string",
            "x-go-name": "ProfileID"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GodaddyTargetDetails": {
        "description": "GodaddyTargetDetails",
        "type": "object",
        "properties": {
          "imap_fqdn": {
            "type": "string",
            "x-go-name": "FQDN"
          },
          "imap_password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "imap_port": {
            "type": "string",
            "x-go-name": "Port"
          },
          "imap_user": {
            "type": "string",
            "x-go-name": "User"
          },
          "key": {
            "type": "string",
            "x-go-name": "Key"
          },
          "secret": {
            "type": "string",
            "x-go-name": "Secret"
          },
          "shopper_id": {
            "description": "Optional, used to find the certificate ID in GoDaddy's API",
            "type": "string",
            "x-go-name": "ShopperID"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          },
          "validation_email": {
            "type": "string",
            "x-go-name": "ValidationEmail"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "HashiVaultTargetDetails": {
        "description": "HashiVaultTargetDetails",
        "type": "object",
        "properties": {
          "vault_namespaces": {
            "type": "string",
            "x-go-name": "VaultNamespaces"
          },
          "vault_token": {
            "type": "string",
            "x-go-name": "VaultToken"
          },
          "vault_url": {
            "type": "string",
            "x-go-name": "VaultURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemState": {
        "description": "ItemState defines the different states an Item can be in",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemType": {
        "type": "string",
        "title": "ItemType defines types supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemVersion": {
        "type": "object",
        "title": "ItemVersion describes an item version in AKEYLESS.",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "certificate_version_info": {
            "$ref": "#/components/schemas/CertificateVersionInfo"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "customer_fragment_id": {
            "type": "string",
            "x-go-name": "CustomerFragmentId"
          },
          "deletion_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "DeletionDate"
          },
          "item_version_state": {
            "$ref": "#/components/schemas/ItemState"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "unique_identifier": {
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          },
          "version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "LdapTargetDetails": {
        "description": "LdapTargetDetails",
        "type": "object",
        "properties": {
          "implementation_type": {
            "type": "string",
            "x-go-name": "ImplementationType"
          },
          "ldap_audience": {
            "type": "string",
            "x-go-name": "Audience"
          },
          "ldap_bind_dn": {
            "type": "string",
            "x-go-name": "BindDn"
          },
          "ldap_bind_password": {
            "type": "string",
            "x-go-name": "BindPass"
          },
          "ldap_certificate": {
            "type": "string",
            "x-go-name": "Certificate"
          },
          "ldap_token_expiration": {
            "type": "string",
            "x-go-name": "TokenExpirationInSec"
          },
          "ldap_url": {
            "type": "string",
            "x-go-name": "Url"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "LetsEncryptTargetDetails": {
        "description": "LetsEncryptTargetDetails defines configuration for Let's Encrypt ACME target",
        "type": "object",
        "properties": {
          "account_key_pem": {
            "description": "ACME Account Private Key (PEM-encoded)\nSupports ECDSA (P-256, P-384, P-521), RSA (2048+), and Ed25519\nAuto-generated as ECDSA P-256 on first certificate issuance if not provided\nStored encrypted, required for certificate operations and revocation",
            "type": "string",
            "x-go-name": "AccountKeyPEM"
          },
          "account_url": {
            "description": "ACME Account URL (returned after registration with Let's Encrypt)\nUsed to retrieve existing account instead of re-registering",
            "type": "string",
            "x-go-name": "AccountURL"
          },
          "acme_environment": {
            "$ref": "#/components/schemas/ACMEEnvironment"
          },
          "challenge_type": {
            "$ref": "#/components/schemas/ACMEChallengeType"
          },
          "dns_target_name": {
            "description": "Name of DNS target (transient field - not stored in DB)\nUsed by CLI to pass DNS target name to SDK for creating target_object_assoc\nRetrieved from target_object_assoc when reading target\nRequired when ChallengeType is \"dns\"",
            "type": "string",
            "x-go-name": "DNSTargetName"
          },
          "dns_target_type": {
            "$ref": "#/components/schemas/TargetType"
          },
          "email": {
            "description": "Email address for ACME account registration\nRequired",
            "type": "string",
            "x-go-name": "Email"
          },
          "gcp_project": {
            "description": "GCP Cloud DNS: Project ID\nOptional - can be derived from service account",
            "type": "string",
            "x-go-name": "GCPProject"
          },
          "hosted_zone": {
            "description": "AWS Route53: Hosted zone ID\nRequired when DNSTargetType is AWS",
            "type": "string",
            "x-go-name": "HostedZone"
          },
          "resource_group": {
            "description": "Azure DNS: Resource group name\nRequired when DNSTargetType is Azure",
            "type": "string",
            "x-go-name": "ResourceGroup"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "LinkedTargetDetails": {
        "description": "LinkedTargetDetails",
        "type": "object",
        "properties": {
          "hosts": {
            "description": "key hostname, value description",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Hosts"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "LoginType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types/oracle"
      },
      "MongoDBTargetDetails": {
        "type": "object",
        "title": "MongoDBTargetDetails ...",
        "properties": {
          "mongodb_atlas_api_private_key": {
            "type": "string",
            "x-go-name": "MongoDBAtlasAPIPrivateKey"
          },
          "mongodb_atlas_api_public_key": {
            "type": "string",
            "x-go-name": "MongoDBAtlasAPIPublicKey"
          },
          "mongodb_atlas_project_id": {
            "description": "mongodb atlas fields",
            "type": "string",
            "x-go-name": "MongoDBAtlasProjectID"
          },
          "mongodb_db_name": {
            "description": "common fields",
            "type": "string",
            "x-go-name": "MongoDBName"
          },
          "mongodb_default_auth_db": {
            "type": "string",
            "x-go-name": "MongoDBDefaultAuthDB"
          },
          "mongodb_host_port": {
            "type": "string",
            "x-go-name": "MongoDBHostAndPort"
          },
          "mongodb_is_atlas": {
            "type": "boolean",
            "x-go-name": "MongoDBAtlas"
          },
          "mongodb_password": {
            "type": "string",
            "x-go-name": "MongoDBPassword"
          },
          "mongodb_uri_connection": {
            "description": "mongodb fields",
            "type": "string",
            "x-go-name": "MongoDBServerURI"
          },
          "mongodb_uri_options": {
            "type": "string",
            "x-go-name": "MongoDBURIOptions"
          },
          "mongodb_username": {
            "type": "string",
            "x-go-name": "MongoDBUsername"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NativeK8sAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NativeK8sTargetDetails": {
        "type": "object",
        "title": "NativeK8sTargetDetails ...",
        "properties": {
          "k8s_auth_type": {
            "$ref": "#/components/schemas/NativeK8sAuthType"
          },
          "k8s_bearer_token": {
            "type": "string",
            "x-go-name": "K8sBearerToken"
          },
          "k8s_client_cert_data": {
            "description": "For K8s Client certificates authentication",
            "type": "string",
            "x-go-name": "K8sClientCertData"
          },
          "k8s_client_key_data": {
            "type": "string",
            "x-go-name": "K8sClientKeyData"
          },
          "k8s_cluster_ca_certificate": {
            "type": "string",
            "x-go-name": "K8sClusterCACertificate"
          },
          "k8s_cluster_endpoint": {
            "type": "string",
            "x-go-name": "K8sClusterEndpoint"
          },
          "k8s_cluster_name": {
            "type": "string",
            "x-go-name": "K8sClusterName"
          },
          "use_gw_service_account": {
            "type": "boolean",
            "x-go-name": "K8sUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OpenAITargetDetails": {
        "description": "OpenAITargetDetails defines details related to connecting to an OpenAI provider",
        "type": "object",
        "properties": {
          "api_key": {
            "type": "string",
            "x-go-name": "ApiKey"
          },
          "api_key_id": {
            "type": "string",
            "x-go-name": "ApiKeyID"
          },
          "openai_url": {
            "type": "string",
            "x-go-name": "BaseURL"
          },
          "organization_id": {
            "type": "string",
            "x-go-name": "OrganizationID"
          },
          "project_id": {
            "type": "string",
            "x-go-name": "ProjectId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PingTargetDetails": {
        "description": "PingTargetDetails",
        "type": "object",
        "properties": {
          "administrative_port": {
            "type": "string",
            "x-go-name": "AdministrativePort"
          },
          "authorization_port": {
            "type": "string",
            "x-go-name": "AuthorizationPort"
          },
          "ping_url": {
            "type": "string",
            "x-go-name": "PingURL"
          },
          "privileged_user": {
            "type": "string",
            "x-go-name": "PrivilegedUser"
          },
          "user_password": {
            "type": "string",
            "x-go-name": "UserPassword"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RabbitMQTargetDetails": {
        "type": "object",
        "title": "RabbitMQTargetDetails ...",
        "properties": {
          "rabbitmq_server_password": {
            "type": "string",
            "x-go-name": "RabbitmqServerPassword"
          },
          "rabbitmq_server_uri": {
            "type": "string",
            "x-go-name": "RabbitmqServerURI"
          },
          "rabbitmq_server_user": {
            "type": "string",
            "x-go-name": "RabbitmqServerUser"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SSHTargetDetails": {
        "type": "object",
        "title": "SSHTargetDetails ...",
        "properties": {
          "host": {
            "type": "string",
            "x-go-name": "HostName"
          },
          "password": {
            "type": "string",
            "x-go-name": "AdminPwd"
          },
          "port": {
            "type": "string",
            "x-go-name": "HostPort"
          },
          "private_key": {
            "type": "string",
            "x-go-name": "SshPrivateKey"
          },
          "private_key_password": {
            "type": "string",
            "x-go-name": "SshPrivateKeyPassword"
          },
          "username": {
            "type": "string",
            "x-go-name": "AdminName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SalesforceTargetDetails": {
        "description": "SalesforceTargetDetails",
        "type": "object",
        "properties": {
          "app_private_key": {
            "description": "params needed for jwt auth\nAppPrivateKey is the rsa private key in PEM format",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "AppPrivateKey"
          },
          "auth_flow": {
            "type": "string",
            "x-go-name": "AuthFlow"
          },
          "ca_cert_data": {
            "description": "CACertData is the rsa 4096 certificate data in PEM format",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "CACertData"
          },
          "ca_cert_name": {
            "description": "CACertName is the name of the certificate in SalesForce tenant",
            "type": "string",
            "x-go-name": "CACertName"
          },
          "client_id": {
            "type": "string",
            "x-go-name": "ClientId"
          },
          "client_secret": {
            "description": "params needed for password auth",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "security_token": {
            "type": "string",
            "x-go-name": "SecurityToken"
          },
          "tenant_url": {
            "type": "string",
            "x-go-name": "TenantUrl"
          },
          "user_name": {
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SectigoTargetDetails": {
        "description": "SectigoTargetDetails",
        "type": "object",
        "properties": {
          "certificate_profile_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateProfileID"
          },
          "customer_uri": {
            "type": "string",
            "x-go-name": "CustomerUri"
          },
          "external_requester": {
            "type": "string",
            "x-go-name": "ExternalRequester"
          },
          "org_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "OrgId"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SplunkPayload": {
        "type": "object",
        "properties": {
          "audience": {
            "type": "string",
            "x-go-name": "Audience"
          },
          "expiration_date": {
            "type": "string",
            "x-go-name": "ExpirationDate"
          },
          "hec_token_name": {
            "type": "string",
            "x-go-name": "HecTokenName"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          },
          "token_id": {
            "type": "string",
            "x-go-name": "TokenID"
          },
          "token_owner": {
            "type": "string",
            "x-go-name": "TokenOwner"
          },
          "validity_period_days": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ValidityPeriodDays"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SplunkTargetDetails": {
        "description": "SplunkTargetDetails defines details related to connecting to a Splunk server",
        "type": "object",
        "properties": {
          "audience": {
            "description": "Token audience",
            "type": "string",
            "x-go-name": "Audience"
          },
          "auth_mode": {
            "description": "Authentication mode: \"username\" or \"token\"",
            "type": "string",
            "x-go-name": "AuthMode"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "splunk_payload": {
            "$ref": "#/components/schemas/SplunkPayload"
          },
          "splunk_url": {
            "description": "Splunk server URL",
            "type": "string",
            "x-go-name": "SplunkURL"
          },
          "token": {
            "description": "Token is used when AuthMode == \"token\"",
            "type": "string",
            "x-go-name": "Token"
          },
          "token_owner": {
            "description": "Token owner (the Splunk user who owns the token, required for token rotation)",
            "type": "string",
            "x-go-name": "TokenOwner"
          },
          "use_tls": {
            "description": "Use TLS certificate verification when connecting to the Splunk management API.",
            "type": "boolean",
            "x-go-name": "UseTLS"
          },
          "username": {
            "description": "Username & Password are used when AuthMode == \"username\"",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Target": {
        "type": "object",
        "title": "Target includes target details.",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "access_request_status": {
            "type": "string",
            "x-go-name": "AccessRequestStatus"
          },
          "attributes": {
            "description": "this is not \"omitempty\" since an empty value causes no update\nwhile an empty map will clear the attributes",
            "type": "object",
            "additionalProperties": {},
            "x-go-name": "Attributes"
          },
          "client_permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ClientPermissions"
          },
          "comment": {
            "type": "string",
            "x-go-name": "Comment"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "is_access_request_enabled": {
            "type": "boolean",
            "x-go-name": "IsAccessRequestEnabled"
          },
          "last_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "LastVersion"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "parent_target_name": {
            "type": "string",
            "x-go-name": "ParentTargetName"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "target_details": {
            "type": "string",
            "x-go-name": "TargetDetails"
          },
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          },
          "target_items_assoc": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TargetItemAssociation"
            },
            "x-go-name": "TargetItemsAssoc"
          },
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
          },
          "target_sub_type": {
            "$ref": "#/components/schemas/TargetSubType"
          },
          "target_type": {
            "$ref": "#/components/schemas/TargetType"
          },
          "target_versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemVersion"
            },
            "x-go-name": "TargetVersions"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetItemAssociation": {
        "description": "TargetItemAssociation includes details of an association between a target\nand an item. Also, between targets in case of child target or Linked target.",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          },
          "attributes": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Attributes"
          },
          "cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "item_name": {
            "type": "string",
            "x-go-name": "ItemName"
          },
          "item_type": {
            "$ref": "#/components/schemas/ItemType"
          },
          "relationship": {
            "$ref": "#/components/schemas/AssocRelationship"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetSubType": {
        "type": "string",
        "title": "TargetSubType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetType": {
        "type": "string",
        "title": "TargetType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetTypeDetailsInput": {
        "type": "object",
        "title": "TargetTypeDetailsInput ...",
        "properties": {
          "artifactory_target_details": {
            "$ref": "#/components/schemas/ArtifactoryTargetDetails"
          },
          "aws_target_details": {
            "$ref": "#/components/schemas/AWSTargetDetails"
          },
          "azure_target_details": {
            "$ref": "#/components/schemas/AzureTargetDetails"
          },
          "chef_target_details": {
            "$ref": "#/components/schemas/ChefTargetDetails"
          },
          "custom_target_details": {
            "$ref": "#/components/schemas/CustomTargetDetails"
          },
          "db_target_details": {
            "$ref": "#/components/schemas/DbTargetDetails"
          },
          "dockerhub_target_details": {
            "$ref": "#/components/schemas/DockerhubTargetDetails"
          },
          "eks_target_details": {
            "$ref": "#/components/schemas/EKSTargetDetails"
          },
          "gcp_target_details": {
            "$ref": "#/components/schemas/GcpTargetDetails"
          },
          "gemini_target_details": {
            "$ref": "#/components/schemas/GeminiTargetDetails"
          },
          "github_target_details": {
            "$ref": "#/components/schemas/GithubTargetDetails"
          },
          "gitlab_target_details": {
            "$ref": "#/components/schemas/GitlabTargetDetails"
          },
          "gke_target_details": {
            "$ref": "#/components/schemas/GKETargetDetails"
          },
          "globalsign_atlas_target_details": {
            "$ref": "#/components/schemas/GlobalSignAtlasTargetDetails"
          },
          "globalsign_target_details": {
            "$ref": "#/components/schemas/GlobalSignGCCTargetDetails"
          },
          "godaddy_target_details": {
            "$ref": "#/components/schemas/GodaddyTargetDetails"
          },
          "hashi_vault_target_details": {
            "$ref": "#/components/schemas/HashiVaultTargetDetails"
          },
          "ldap_target_details": {
            "$ref": "#/components/schemas/LdapTargetDetails"
          },
          "letsencrypt_target_details": {
            "$ref": "#/components/schemas/LetsEncryptTargetDetails"
          },
          "linked_target_details": {
            "$ref": "#/components/schemas/LinkedTargetDetails"
          },
          "mongo_db_target_details": {
            "$ref": "#/components/schemas/MongoDBTargetDetails"
          },
          "native_k8s_target_details": {
            "$ref": "#/components/schemas/NativeK8sTargetDetails"
          },
          "openai_target_details": {
            "$ref": "#/components/schemas/OpenAITargetDetails"
          },
          "ping_target_details": {
            "$ref": "#/components/schemas/PingTargetDetails"
          },
          "rabbit_mq_target_details": {
            "$ref": "#/components/schemas/RabbitMQTargetDetails"
          },
          "salesforce_target_details": {
            "$ref": "#/components/schemas/SalesforceTargetDetails"
          },
          "sectigo_target_details": {
            "$ref": "#/components/schemas/SectigoTargetDetails"
          },
          "splunk_target_details": {
            "$ref": "#/components/schemas/SplunkTargetDetails"
          },
          "ssh_target_details": {
            "$ref": "#/components/schemas/SSHTargetDetails"
          },
          "venafi_target_details": {
            "$ref": "#/components/schemas/VenafiTargetDetails"
          },
          "web_target_details": {
            "$ref": "#/components/schemas/WebTargetDetails"
          },
          "windows_target_details": {
            "$ref": "#/components/schemas/WindowsTargetDetails"
          },
          "zerossl_target_details": {
            "$ref": "#/components/schemas/ZeroSSLTargetDetails"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "VenafiTargetDetails": {
        "type": "object",
        "title": "VenafiTargetDetails ...",
        "properties": {
          "venafi_api_key": {
            "type": "string",
            "x-go-name": "VenafiApiKey"
          },
          "venafi_base_url": {
            "type": "string",
            "x-go-name": "VenafiBaseURL"
          },
          "venafi_tpp_access_token": {
            "type": "string",
            "x-go-name": "VenafiAccessToken"
          },
          "venafi_tpp_client_id": {
            "type": "string",
            "x-go-name": "VenafiTPPClientID"
          },
          "venafi_tpp_password": {
            "description": "Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead",
            "type": "string",
            "x-go-name": "VenafiTPPPassword"
          },
          "venafi_tpp_refresh_token": {
            "type": "string",
            "x-go-name": "VenafiRefreshToken"
          },
          "venafi_tpp_username": {
            "description": "Deprecated: VenafiAccessToken and VenafiRefreshToken should be used instead",
            "type": "string",
            "x-go-name": "VenafiTPPUserName"
          },
          "venafi_use_tpp": {
            "type": "boolean",
            "x-go-name": "VenafiUseTPP"
          },
          "venafi_zone": {
            "type": "string",
            "x-go-name": "VenafiZone"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WalletDetails": {
        "type": "object",
        "properties": {
          "login_type": {
            "$ref": "#/components/schemas/LoginType"
          },
          "p12_data_base64": {
            "type": "string",
            "x-go-name": "P12DataBase64"
          },
          "sso_data_base64": {
            "type": "string",
            "x-go-name": "SSODataBase64"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types/oracle"
      },
      "WebTargetDetails": {
        "type": "object",
        "title": "WebTargetDetails ...",
        "properties": {
          "url": {
            "type": "string",
            "x-go-name": "URL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WindowsTargetDetails": {
        "description": "WindowsTargetDetails",
        "type": "object",
        "properties": {
          "certificate": {
            "type": "string",
            "x-go-name": "Certificate"
          },
          "connection_type": {
            "$ref": "#/components/schemas/TargetAuthType"
          },
          "domain_name": {
            "type": "string",
            "x-go-name": "DomainName"
          },
          "hostname": {
            "type": "string",
            "x-go-name": "Hostname"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "port": {
            "type": "string",
            "x-go-name": "Port"
          },
          "use_tls": {
            "type": "boolean",
            "x-go-name": "UseTLS"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ZeroSSLTargetDetails": {
        "description": "ZeroSSLTargetDetails",
        "type": "object",
        "properties": {
          "api_key": {
            "type": "string",
            "x-go-name": "APIKey"
          },
          "imap_fqdn": {
            "type": "string",
            "x-go-name": "FQDN"
          },
          "imap_password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "imap_port": {
            "type": "string",
            "x-go-name": "Port"
          },
          "imap_user": {
            "type": "string",
            "x-go-name": "User"
          },
          "timeout": {
            "$ref": "#/components/schemas/Duration"
          },
          "validation_email": {
            "type": "string",
            "x-go-name": "ValidationEmail"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "targetGetDetails": {
        "type": "object",
        "title": "targetGetDetails is a command that returns target details.",
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
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "show-versions": {
            "description": "Include all target versions in reply",
            "type": "boolean",
            "default": false,
            "x-go-name": "ShowVersions"
          },
          "target-version": {
            "description": "Target version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "TargetVersion"
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