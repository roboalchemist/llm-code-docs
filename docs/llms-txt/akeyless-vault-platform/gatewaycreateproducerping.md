# Source: https://docs.akeyless.io/reference/gatewaycreateproducerping.md

# /gateway-create-producer-ping

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
    "/gateway-create-producer-ping": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayCreateProducerPing",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayCreateProducerPing"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayCreateProducerPingResponse"
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
      "gatewayCreateProducerPingResponse": {
        "description": "gatewayCreateProducerPingResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayCreateProducerPingOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AWSAccessMode": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
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
      "Algorithm": {
        "type": "string",
        "title": "Algorithm is a type that represents a single crypto algorithm.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ChefAccessMode": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "DSProducerDetails": {
        "type": "object",
        "properties": {
          "access_token_manager_id": {
            "type": "string",
            "x-go-name": "AccessTokenManagerId"
          },
          "acl_rules": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AclRules"
          },
          "active": {
            "type": "boolean",
            "x-go-name": "Active"
          },
          "admin_name": {
            "type": "string",
            "x-go-name": "AdminName"
          },
          "admin_pwd": {
            "type": "string",
            "x-go-name": "AdminPwd"
          },
          "admin_rotation_interval_days": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RotationIntervalDays"
          },
          "administrative_port": {
            "type": "string",
            "x-go-name": "AdministrativePort"
          },
          "api_key": {
            "type": "string",
            "x-go-name": "ApiKey"
          },
          "api_key_id": {
            "type": "string",
            "x-go-name": "ApiKeyID"
          },
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
          },
          "artifactory_token_audience": {
            "type": "string",
            "x-go-name": "ArtifactoryTokenAudience"
          },
          "artifactory_token_scope": {
            "type": "string",
            "x-go-name": "ArtifactoryTokenScope"
          },
          "authorization_port": {
            "type": "string",
            "x-go-name": "AuthorizationPort"
          },
          "aws_access_key_id": {
            "type": "string",
            "x-go-name": "AWSAccessKeyID"
          },
          "aws_access_mode": {
            "$ref": "#/components/schemas/AWSAccessMode"
          },
          "aws_external_id": {
            "type": "string",
            "x-go-name": "AWSExternalID"
          },
          "aws_region": {
            "type": "string",
            "x-go-name": "AWSRegion"
          },
          "aws_role_arns": {
            "type": "string",
            "x-go-name": "AWSRoleARNs"
          },
          "aws_secret_access_key": {
            "type": "string",
            "x-go-name": "AWSSecretAccessKey"
          },
          "aws_session_tags": {
            "type": "string",
            "x-go-name": "AWSSessionTags"
          },
          "aws_session_token": {
            "type": "string",
            "x-go-name": "AWSSessionToken"
          },
          "aws_transitive_tag_keys": {
            "type": "string",
            "x-go-name": "AWSTransitiveTagKeys"
          },
          "aws_user_console_access": {
            "type": "boolean",
            "x-go-name": "AWSUserConsoleAccess"
          },
          "aws_user_groups": {
            "type": "string",
            "x-go-name": "AWSUserGroups"
          },
          "aws_user_policies": {
            "type": "string",
            "x-go-name": "AWSUserPolicies"
          },
          "aws_user_programmatic_access": {
            "type": "boolean",
            "x-go-name": "AWSUserProgAccess"
          },
          "azure_administrative_unit": {
            "type": "string",
            "x-go-name": "AzureAdministrativeUnit"
          },
          "azure_app_object_id": {
            "type": "string",
            "x-go-name": "AzureAppObjectID"
          },
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
          "azure_fixed_user_name_sub_claim_key": {
            "type": "string",
            "x-go-name": "AzureFixedUserNameSubClaimKey"
          },
          "azure_fixed_user_only": {
            "type": "boolean",
            "x-go-name": "AzureFixedUserOnly"
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
          "azure_user_groups_obj_id": {
            "type": "string",
            "x-go-name": "AzureUserGroupsObjID"
          },
          "azure_user_portal_access": {
            "type": "boolean",
            "x-go-name": "AzureUserConsoleAccess"
          },
          "azure_user_programmatic_access": {
            "type": "boolean",
            "x-go-name": "AzureUserProgAccess"
          },
          "azure_user_roles_template_id": {
            "type": "string",
            "x-go-name": "AzureUserRolesTemplateID"
          },
          "azure_username": {
            "type": "string",
            "x-go-name": "AzureUsername"
          },
          "cassandra_creation_statements": {
            "type": "string",
            "x-go-name": "CassandraCreationStatements"
          },
          "chef_organizations": {
            "type": "string",
            "x-go-name": "ChefOrganizations"
          },
          "chef_server_access_mode": {
            "$ref": "#/components/schemas/ChefAccessMode"
          },
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
          },
          "client_authentication_type": {
            "type": "string",
            "x-go-name": "ClientAuthenticationType"
          },
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
          "create_sync_url": {
            "type": "string",
            "x-go-name": "CreateSyncURL"
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
          "db_isolation_level": {
            "type": "string",
            "x-go-name": "DbIsolationLevel"
          },
          "db_max_idle_conns": {
            "type": "string",
            "x-go-name": "DbMaxIdleConns"
          },
          "db_max_open_conns": {
            "type": "string",
            "x-go-name": "DbMaxOpenConns"
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
          "delete_protection": {
            "type": "boolean",
            "x-go-name": "ItemProtected"
          },
          "dynamic_secret_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DynamicSecretId"
          },
          "dynamic_secret_key": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "dynamic_secret_name": {
            "type": "string",
            "x-go-name": "DynamicSecretName"
          },
          "dynamic_secret_type": {
            "$ref": "#/components/schemas/DynamicSecretType"
          },
          "eks_access_key_id": {
            "type": "string",
            "x-go-name": "EKSAccessID"
          },
          "eks_assume_role": {
            "type": "string",
            "x-go-name": "EKSAssumeRole"
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
          "enable_admin_rotation": {
            "type": "boolean",
            "x-go-name": "EnableAdminRotation"
          },
          "enforce_replay_prevention": {
            "description": "relevant for PRIVATE_KEY_JWT client authentication type",
            "type": "boolean",
            "x-go-name": "EnforceReplayPrevention"
          },
          "expiration_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ExpirationDate"
          },
          "externally_provided_user": {
            "type": "string",
            "x-go-name": "ExternallyProvidedUser"
          },
          "failure_message": {
            "type": "string",
            "x-go-name": "FailureMessage"
          },
          "fixed_user_only": {
            "type": "string",
            "x-go-name": "FixedUserOnly"
          },
          "gcp_access_type": {
            "$ref": "#/components/schemas/GCPAccessType"
          },
          "gcp_fixed_user_claim_keyname": {
            "type": "string",
            "x-go-name": "GCPFixedUserClaimKeyName"
          },
          "gcp_key_algo": {
            "type": "string",
            "x-go-name": "GCPKeyAlgorithm"
          },
          "gcp_project_id": {
            "type": "string",
            "x-go-name": "GCPProjectId"
          },
          "gcp_role_bindings": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "GCPRoleBindings"
          },
          "gcp_role_names": {
            "type": "string",
            "x-go-name": "GCPRoleNames"
          },
          "gcp_service_account_email": {
            "description": "GCPServiceAccountEmail overrides the deprecated field from the target",
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
          "gcp_service_account_type": {
            "$ref": "#/components/schemas/GCPServiceAccountType"
          },
          "gcp_tmp_service_account_name": {
            "type": "string",
            "x-go-name": "GCPTmpServiceAccountName"
          },
          "gcp_token_lifetime": {
            "type": "string",
            "x-go-name": "GCPTokenLifetime"
          },
          "gcp_token_scope": {
            "type": "string",
            "x-go-name": "GCPTokenScopes"
          },
          "gcp_token_type": {
            "$ref": "#/components/schemas/GCPCredentialsType"
          },
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
          },
          "github_installation_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GithubInstallationId"
          },
          "github_installation_token_permissions": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "GithubTokenPermissions"
          },
          "github_installation_token_repositories": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GithubTokenRepositories"
          },
          "github_installation_token_repositories_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "GithubTokenRepositoriesById"
          },
          "github_organization_name": {
            "type": "string",
            "x-go-name": "GithubOrganizationName"
          },
          "github_repository_path": {
            "type": "string",
            "x-go-name": "GithubRepositoryPath"
          },
          "gitlab_access_token": {
            "type": "string",
            "x-go-name": "GitlabAccessToken"
          },
          "gitlab_access_type": {
            "$ref": "#/components/schemas/TokenType"
          },
          "gitlab_certificate": {
            "type": "string",
            "x-go-name": "GitlabCertificate"
          },
          "gitlab_group_name": {
            "type": "string",
            "x-go-name": "GitlabGroupName"
          },
          "gitlab_project_name": {
            "type": "string",
            "x-go-name": "GitlabProjectName"
          },
          "gitlab_role": {
            "$ref": "#/components/schemas/GitlabRole"
          },
          "gitlab_token_scope": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GitlabTokenScope"
          },
          "gitlab_url": {
            "type": "string",
            "x-go-name": "GitlabURL"
          },
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
          "google_workspace_access_mode": {
            "$ref": "#/components/schemas/GWSAccessMode"
          },
          "google_workspace_admin_name": {
            "type": "string",
            "x-go-name": "GWSAdminName"
          },
          "google_workspace_fixed_user_name_sub_claim_key": {
            "type": "string",
            "x-go-name": "GWSFixedUserNameSubClaimKey"
          },
          "google_workspace_group_name": {
            "type": "string",
            "x-go-name": "GWSGroupName"
          },
          "google_workspace_group_role": {
            "$ref": "#/components/schemas/GWSGroupRoleType"
          },
          "google_workspace_role_name": {
            "type": "string",
            "x-go-name": "RoleName"
          },
          "google_workspace_role_scope": {
            "$ref": "#/components/schemas/GWSRoleScope"
          },
          "grace_rotated_secret_key": {
            "type": "string",
            "x-go-name": "GraceRotatedSecretKey"
          },
          "grant_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GrantTypes"
          },
          "groups": {
            "type": "string",
            "x-go-name": "Groups"
          },
          "gw_cloud_identity_external_id_opt": {
            "$ref": "#/components/schemas/AWSGatewayCloudIdentityExternalIdOpt"
          },
          "hanadb_creation_statements": {
            "type": "string",
            "x-go-name": "HanaDbCreationStatements"
          },
          "hanadb_revocation_statements": {
            "type": "string",
            "x-go-name": "HanaDbRevocationStatements"
          },
          "host_name": {
            "type": "string",
            "x-go-name": "HostName"
          },
          "host_port": {
            "type": "string",
            "x-go-name": "HostPort"
          },
          "implementation_type": {
            "type": "string",
            "x-go-name": "ImplementationType"
          },
          "is_fixed_user": {
            "type": "string",
            "x-go-name": "IsFixedUser"
          },
          "issuer": {
            "description": "relevant for CLIENT_TLS_CERTIFICATE client authentication type",
            "type": "string",
            "x-go-name": "Issuer"
          },
          "item_custom_fields_details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemCustomFieldsDetails"
            },
            "x-go-name": "ItemCustomFieldsDetails"
          },
          "item_targets_assoc": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemTargetAssociation"
            },
            "x-go-name": "ItemTargetsAssoc"
          },
          "jwks": {
            "type": "string",
            "x-go-name": "JWKs"
          },
          "jwks_url": {
            "type": "string",
            "x-go-name": "JWKsURL"
          },
          "k8s_allowed_namespaces": {
            "description": "comma-separated list of allowed namespaces. Can hold just * which signifies that any namespace is allowed",
            "type": "string",
            "x-go-name": "AllowedNamespaces"
          },
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
          "k8s_dynamic_mode": {
            "description": "when native k8s is in dynamic mode, user can define allowed namespaces,\nK8sServiceAccount doesn't exist from the start and will only be created at time of getting dynamic secret value\nBy default dynamic mode is false and producer behaves like it did before",
            "type": "boolean",
            "x-go-name": "DynamicMode"
          },
          "k8s_multiple_doc_yaml_temp_definition": {
            "description": "Yaml definition for creation of temporary objects. Field that can hold multiple docs from which following will be extracted:\nServiceAccount, Role/ClusterRole and RoleBinding/ClusterRoleBinding. If ServiceAccount not specified - it will be generated automatically",
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "K8sMultiDocYamlTempDefinition"
          },
          "k8s_namespace": {
            "type": "string",
            "x-go-name": "K8sNamespace"
          },
          "k8s_role_name": {
            "description": "Name of the pre-existing Role or ClusterRole to bind a generated service account to.",
            "type": "string",
            "x-go-name": "K8sRoleName"
          },
          "k8s_role_type": {
            "$ref": "#/components/schemas/K8SRoleType"
          },
          "k8s_service_account": {
            "type": "string",
            "x-go-name": "K8sServiceAccount"
          },
          "last_admin_rotation": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "LastAdminRotation"
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
          "ldap_fixed_user_name_sub_claim_key": {
            "type": "string",
            "x-go-name": "LdapFixedUserNameSubClaimKey"
          },
          "ldap_fixed_user_type": {
            "type": "string",
            "x-go-name": "LdapFixedUserType"
          },
          "ldap_group_dn": {
            "type": "string",
            "x-go-name": "GroupDn"
          },
          "ldap_token_expiration": {
            "type": "string",
            "x-go-name": "TokenExpirationInSec"
          },
          "ldap_url": {
            "type": "string",
            "x-go-name": "Url"
          },
          "ldap_user_attr": {
            "type": "string",
            "x-go-name": "UserAttr"
          },
          "ldap_user_dn": {
            "type": "string",
            "x-go-name": "UserDn"
          },
          "metadata": {
            "type": "string",
            "x-go-name": "Metadata"
          },
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
          "mongodb_custom_data": {
            "type": "string",
            "x-go-name": "MongoDBCustomData"
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
          "mongodb_roles": {
            "description": "common fields",
            "type": "string",
            "x-go-name": "MongoDBRoles"
          },
          "mongodb_scopes": {
            "type": "string",
            "x-go-name": "MongoDBScopes"
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
          },
          "mssql_allowed_db_names": {
            "description": "Comma-separated list of allowed DB names for runtime selection when fetching the secret value.\nEmpty string => use target DB name only (no override allowed)\n\"*\" => any DB name is allowed\nOne or more names => user must select one of the provided names",
            "type": "string",
            "x-go-name": "MSSQLAllowedDbNames"
          },
          "mssql_creation_statements": {
            "type": "string",
            "x-go-name": "MSSQLCreationStatements"
          },
          "mssql_revocation_statements": {
            "type": "string",
            "x-go-name": "MSSQLRevocationStatements"
          },
          "mysql_creation_statements": {
            "type": "string",
            "x-go-name": "MysqlCreationStatements"
          },
          "mysql_revocation_statements": {
            "type": "string",
            "x-go-name": "MysqlRevocationStatements"
          },
          "openai_url": {
            "type": "string",
            "x-go-name": "BaseURL"
          },
          "oracle_creation_statements": {
            "type": "string",
            "x-go-name": "OracleDBCreationStatements"
          },
          "oracle_revocation_statements": {
            "type": "string",
            "x-go-name": "OracleDBRevocationStatements"
          },
          "oracle_wallet_details": {
            "$ref": "#/components/schemas/WalletDetails"
          },
          "organization_id": {
            "type": "string",
            "x-go-name": "OrganizationID"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "password_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "PasswordLength"
          },
          "password_policy": {
            "type": "string",
            "x-go-name": "PasswordPolicy"
          },
          "payload": {
            "type": "string",
            "x-go-name": "Payload"
          },
          "ping_url": {
            "type": "string",
            "x-go-name": "PingURL"
          },
          "postgres_creation_statements": {
            "type": "string",
            "x-go-name": "PostgresCreationStatements"
          },
          "postgres_revocation_statements": {
            "type": "string",
            "x-go-name": "PostgresRevocationStatements"
          },
          "privileged_user": {
            "type": "string",
            "x-go-name": "PrivilegedUser"
          },
          "project_id": {
            "type": "string",
            "x-go-name": "ProjectId"
          },
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
          },
          "rabbitmq_user_conf_permission": {
            "type": "string",
            "x-go-name": "RabbitmqUserConfigPermission"
          },
          "rabbitmq_user_read_permission": {
            "type": "string",
            "x-go-name": "RabbitmqUserReadPermission"
          },
          "rabbitmq_user_tags": {
            "type": "string",
            "x-go-name": "RabbitmqUserTags"
          },
          "rabbitmq_user_vhost": {
            "type": "string",
            "x-go-name": "RabbitmqUserVHost"
          },
          "rabbitmq_user_write_permission": {
            "type": "string",
            "x-go-name": "RabbitmqUserWritePermission"
          },
          "rdp_fixed_user_name_sub_claim_key": {
            "type": "string",
            "x-go-name": "RDPFixedUserNameSubClaimKey"
          },
          "redirect_uris": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RedirectUris"
          },
          "redshift_creation_statements": {
            "type": "string",
            "x-go-name": "RedshiftCreationStatements"
          },
          "restricted_scopes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RestrictedScopes"
          },
          "revoke_sync_url": {
            "type": "string",
            "x-go-name": "RevokeSyncURL"
          },
          "rotate_sync_url": {
            "type": "string",
            "x-go-name": "RotateSyncURL"
          },
          "scopes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DockerhubScopes"
          },
          "secure_remote_access_details": {
            "$ref": "#/components/schemas/SecureRemoteAccess"
          },
          "session_extension_warn_interval_min": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "SessionExtensionWarnIntervalInMin"
          },
          "sf_account": {
            "type": "string",
            "x-go-name": "SnowflakeAccountName"
          },
          "sf_auth_mode": {
            "$ref": "#/components/schemas/SnowflakeAuthMode"
          },
          "sf_key_algo": {
            "$ref": "#/components/schemas/Algorithm"
          },
          "sf_user_role": {
            "description": "generated  users info",
            "type": "string",
            "x-go-name": "SnowflakeUserRole"
          },
          "sf_warehouse_name": {
            "type": "string",
            "x-go-name": "SnowflakeWarehouseName"
          },
          "should_stop": {
            "description": "TODO delete this after migration",
            "type": "string",
            "x-go-name": "ShouldStop"
          },
          "signing_algorithm": {
            "type": "string",
            "x-go-name": "SigningAlgorithm"
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
          },
          "subject_dn": {
            "type": "string",
            "x-go-name": "SubjectDN"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "timeout_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TimeoutSeconds"
          },
          "use_gw_cloud_identity": {
            "type": "boolean",
            "x-go-name": "EKSUseDefaultIdentity"
          },
          "use_gw_service_account": {
            "type": "boolean",
            "x-go-name": "K8sUseDefaultIdentity"
          },
          "user_name": {
            "type": "string",
            "x-go-name": "UserName"
          },
          "user_password": {
            "type": "string",
            "x-go-name": "UserPassword"
          },
          "user_principal_name": {
            "type": "string",
            "x-go-name": "AzurePrincipalName"
          },
          "user_ttl": {
            "type": "string",
            "x-go-name": "UserTtl"
          },
          "username_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "UsernameLen"
          },
          "username_policy": {
            "type": "string",
            "x-go-name": "UsernamePolicy"
          },
          "username_template": {
            "type": "string",
            "x-go-name": "UsernameTemplate"
          },
          "venafi_allow_subdomains": {
            "type": "boolean",
            "x-go-name": "VenafiAllowSubdomains"
          },
          "venafi_allowed_domains": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "VenafiAllowedDomains"
          },
          "venafi_api_key": {
            "type": "string",
            "x-go-name": "VenafiApiKey"
          },
          "venafi_auto_generated_folder": {
            "type": "string",
            "x-go-name": "VenafiAutoGeneratedFolder"
          },
          "venafi_base_url": {
            "type": "string",
            "x-go-name": "VenafiBaseURL"
          },
          "venafi_root_first_in_chain": {
            "type": "boolean",
            "x-go-name": "VenafiRootFirstInChain"
          },
          "venafi_sign_using_akeyless_pki": {
            "type": "boolean",
            "x-go-name": "VenafiSignUsingAkeylessPKI"
          },
          "venafi_signer_key_name": {
            "type": "string",
            "x-go-name": "VenafiSignerKeyName"
          },
          "venafi_store_private_key": {
            "type": "boolean",
            "x-go-name": "VenafiStorePrivateKey"
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
          },
          "warn_before_user_expiration_min": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "WarnBeforeUserExpirationInMin"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "DynamicSecretType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer"
      },
      "GCPAccessType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GCPCredentialsType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GCPServiceAccountType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GWSAccessMode": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GWSGroupRoleType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GWSRoleScope": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "GitlabRole": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "HostProviderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemCustomFieldsDetails": {
        "description": "ItemCustomFieldsDetails includes details of item custom field configuration and value",
        "type": "object",
        "properties": {
          "field_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "FieldID"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ID"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "required": {
            "type": "boolean",
            "x-go-name": "Required"
          },
          "value": {
            "type": "string",
            "x-go-name": "Value"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemSraStatus": {
        "type": "object",
        "properties": {
          "count_by_host_info": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "CountByHostInfo"
          },
          "count_info": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "additionalProperties": {
                "type": "integer",
                "format": "int64"
              }
            },
            "x-go-name": "CountInfo"
          },
          "hosts_in_use": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "HostsInUse"
          },
          "is_in_use": {
            "type": "boolean",
            "x-go-name": "IsInUse"
          },
          "last_used_item": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastUsedTime"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemTargetAssociation": {
        "description": "and a target.",
        "type": "object",
        "title": "ItemTargetAssociation includes details of an association between an item",
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
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          },
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
          },
          "target_type": {
            "type": "string",
            "x-go-name": "TargetType"
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
      "K8SRoleType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "LoginType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types/oracle"
      },
      "NativeK8sAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SRAConcurrentConnsLevel": {
        "type": "string",
        "title": "SRAConcurrentConnsLevel indicate what the block level user can apply on sra connections.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SecureRemoteAccess": {
        "type": "object",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AwsAccountId"
          },
          "allow_port_forwarding": {
            "type": "boolean",
            "x-go-name": "K8SAllowPortForwading"
          },
          "allow_providing_external_username": {
            "type": "boolean",
            "x-go-name": "AllowProvidingExternalUser"
          },
          "bastion_api": {
            "type": "string",
            "x-go-name": "BastionAPI"
          },
          "bastion_issuer": {
            "type": "string",
            "x-go-name": "BastionIssuer"
          },
          "bastion_issuer_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "BastionIssuerID"
          },
          "bastion_ssh": {
            "type": "string",
            "x-go-name": "BastionSSH"
          },
          "block_concurrent_connections": {
            "type": "boolean",
            "x-go-name": "BlockConcurrentConns"
          },
          "block_concurrent_connections_level": {
            "$ref": "#/components/schemas/SRAConcurrentConnsLevel"
          },
          "category": {
            "$ref": "#/components/schemas/SecureRemoteAccessCategory"
          },
          "connection_delay_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ConnectionDelaySeconds"
          },
          "dashboard_url": {
            "type": "string",
            "x-go-name": "K8SDashboardURL"
          },
          "db_name": {
            "type": "string",
            "x-go-name": "DbName"
          },
          "domain": {
            "type": "string",
            "x-go-name": "RDPDomain"
          },
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "endpoint": {
            "type": "string",
            "x-go-name": "K8SEndpoint"
          },
          "enforce_hosts_restriction": {
            "type": "boolean",
            "x-go-name": "EnforceHostsRestriction"
          },
          "gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "host": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Host"
          },
          "host_provider_type": {
            "$ref": "#/components/schemas/HostProviderType"
          },
          "is_cli": {
            "type": "boolean",
            "x-go-name": "AccessCliCategory"
          },
          "is_desktop_app": {
            "type": "boolean",
            "x-go-name": "AccessDesktopAppCategory"
          },
          "is_web": {
            "type": "boolean",
            "x-go-name": "AccessWebCategory"
          },
          "isolated": {
            "type": "boolean",
            "x-go-name": "Isolated"
          },
          "native": {
            "type": "boolean",
            "x-go-name": "AwsNativeCli"
          },
          "rd_gateway_server": {
            "type": "string",
            "x-go-name": "RDGatewayServer"
          },
          "rdp_user": {
            "type": "string",
            "x-go-name": "RDPUser"
          },
          "region": {
            "type": "string",
            "x-go-name": "AwsRegion"
          },
          "rotate_after_disconnect": {
            "type": "boolean",
            "x-go-name": "RotateAfterDisconnect"
          },
          "schema": {
            "type": "string",
            "x-go-name": "Schema"
          },
          "ssh_password": {
            "type": "boolean",
            "x-go-name": "SSHPassword"
          },
          "ssh_private_key": {
            "type": "boolean",
            "x-go-name": "SSHPrivateKey"
          },
          "ssh_user": {
            "type": "string",
            "x-go-name": "SSHUser"
          },
          "status_info": {
            "$ref": "#/components/schemas/ItemSraStatus"
          },
          "target_hosts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TargetNameWithHosts"
            },
            "x-go-name": "TargetNameWithHosts"
          },
          "targets": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Targets"
          },
          "url": {
            "type": "string",
            "x-go-name": "URL"
          },
          "use_internal_bastion": {
            "type": "boolean",
            "x-go-name": "UseInternalBastion"
          },
          "web_proxy": {
            "type": "boolean",
            "x-go-name": "WebProxy"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SecureRemoteAccessCategory": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SnowflakeAuthMode": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
      },
      "TargetAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetNameWithHosts": {
        "type": "object",
        "properties": {
          "hosts": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TargetHosts"
          },
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TokenType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/config"
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
      "gatewayCreateProducerPing": {
        "description": "gatewayCreateProducerPing is a command that creates ping producer [Deprecated: Use dynamic-secret-create-ping command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Dynamic secret name",
            "type": "string",
            "x-go-name": "DSName"
          },
          "ping-administrative-port": {
            "description": "Ping Federate administrative port",
            "type": "string",
            "default": "9999",
            "x-go-name": "AdministrativePort"
          },
          "ping-atm-id": {
            "description": "Set a specific Access Token Management (ATM) instance for the created OAuth Client by providing the ATM Id. If no explicit value is given, the default pingfederate server ATM will be set.",
            "type": "string",
            "x-go-name": "AccessTokenManagerId"
          },
          "ping-authorization-port": {
            "description": "Ping Federate authorization port",
            "type": "string",
            "default": "9031",
            "x-go-name": "AuthorizationPort"
          },
          "ping-cert-subject-dn": {
            "description": "The subject DN of the client certificate. If no explicit value is given, the producer will create CA certificate and matched client certificate and return it as value. Used in conjunction with ping-issuer-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)",
            "type": "string",
            "x-go-name": "CertSubjectDN"
          },
          "ping-client-authentication-type": {
            "description": "OAuth Client Authentication Type [CLIENT_SECRET, PRIVATE_KEY_JWT, CLIENT_TLS_CERTIFICATE]",
            "type": "string",
            "default": "CLIENT_SECRET",
            "x-go-name": "ClientAuthenticationType"
          },
          "ping-enforce-replay-prevention": {
            "description": "Determines whether PingFederate requires a unique signed JWT from the client for each action (relevant for PRIVATE_KEY_JWT authentication method) [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "EnforceReplayPrevention"
          },
          "ping-grant-types": {
            "description": "List of OAuth client grant types [IMPLICIT, AUTHORIZATION_CODE, CLIENT_CREDENTIALS, TOKEN_EXCHANGE, REFRESH_TOKEN, ASSERTION_GRANTS, PASSWORD, RESOURCE_OWNER_CREDENTIALS]. If no explicit value is given, AUTHORIZATION_CODE will be selected as default.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GrantTypes"
          },
          "ping-issuer-dn": {
            "description": "Issuer DN of trusted CA certificate that imported into Ping Federate server. You may select \\\"Trust Any\\\" to trust all the existing issuers in Ping Federate server. Used in conjunction with ping-cert-subject-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)",
            "type": "string",
            "x-go-name": "IssuerDN"
          },
          "ping-jwks": {
            "description": "Base64-encoded JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT (Sign Algo: RS256) and return it as value (relevant for PRIVATE_KEY_JWT authentication method)",
            "type": "string",
            "x-go-name": "JWKs"
          },
          "ping-jwks-url": {
            "description": "The URL of the JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT and return it as value (relevant for PRIVATE_KEY_JWT authentication method)",
            "type": "string",
            "x-go-name": "JWKsURL"
          },
          "ping-password": {
            "description": "Ping Federate privileged user password",
            "type": "string",
            "x-go-name": "UserPassword"
          },
          "ping-privileged-user": {
            "description": "Ping Federate privileged user",
            "type": "string",
            "x-go-name": "PrivilegedUser"
          },
          "ping-redirect-uris": {
            "description": "List of URIs to which the OAuth authorization server may redirect the resource owner's user agent after authorization is obtained. At least one redirection URI is required for the AUTHORIZATION_CODE and IMPLICIT grant types.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RedirectUris"
          },
          "ping-restricted-scopes": {
            "description": "Limit the OAuth client to specific scopes list",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RestrictedScopes"
          },
          "ping-signing-algo": {
            "description": "The signing algorithm that the client must use to sign its request objects [RS256,RS384,RS512,ES256,ES384,ES512,PS256,PS384,PS512] If no explicit value is given, the client can use any of the supported signing algorithms (relevant for PRIVATE_KEY_JWT authentication method)",
            "type": "string",
            "x-go-name": "SigningAlgorithm"
          },
          "ping-url": {
            "description": "Ping URL",
            "type": "string",
            "x-go-name": "PingURL"
          },
          "producer-encryption-key-name": {
            "description": "Dynamic producer encryption key",
            "type": "string",
            "x-go-name": "ProducerEncryptionKey"
          },
          "tags": {
            "description": "Add tags attached to this object",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "target-name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
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
          "user-ttl": {
            "description": "The time from dynamic secret creation to expiration.",
            "type": "string",
            "default": "60m",
            "x-go-name": "UserTtl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "gatewayCreateProducerPingOutput": {
        "type": "object",
        "properties": {
          "producer_details": {
            "$ref": "#/components/schemas/DSProducerDetails"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```