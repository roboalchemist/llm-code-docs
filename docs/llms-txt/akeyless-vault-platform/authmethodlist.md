# Source: https://docs.akeyless.io/reference/authmethodlist.md

# /auth-method-list

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
    "/auth-method-list": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodList",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodList"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/authMethodListResponse"
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
      "authMethodListResponse": {
        "description": "authMethodListResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ListAuthMethodsOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      }
    },
    "schemas": {
      "APIKeyAccessRules": {
        "type": "object",
        "title": "APIKeyAccessRules is a set of rules for API Key access type.",
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/Algorithm"
          },
          "key": {
            "description": "The public key value of the API-key.",
            "type": "string",
            "x-go-name": "PubKeyValue"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AWSIAMAccessRules": {
        "type": "object",
        "title": "AWSIAMAccessRules contains access rules specific to AWS IAM.",
        "properties": {
          "account_id": {
            "description": "The list of account ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AccountID"
          },
          "arn": {
            "description": "The list of ARNs that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Arn"
          },
          "resource_id": {
            "description": "The list of resource ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ResourceID"
          },
          "role_id": {
            "description": "The list of role ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RoleID"
          },
          "role_name": {
            "description": "The list of role names that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RoleName"
          },
          "sts_endpoint": {
            "description": "The sts URL.",
            "type": "string",
            "x-go-name": "StsEndpoint"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          },
          "user_id": {
            "description": "The list of user ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserID"
          },
          "user_name": {
            "description": "The list of user names that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Algorithm": {
        "type": "string",
        "title": "Algorithm is a type that represents a single crypto algorithm.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AuthExpirationEvent": {
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
      "AuthMethod": {
        "type": "object",
        "title": "AuthMethod represents a single Auth method.",
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
          "access_info": {
            "$ref": "#/components/schemas/AuthMethodAccessInfo"
          },
          "account_id": {
            "type": "string",
            "x-go-name": "AccountID"
          },
          "associated_gw_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "AssociatedGwIds"
          },
          "auth_method_access_id": {
            "type": "string",
            "x-go-name": "AuthMethodAccessID"
          },
          "auth_method_additional_data": {
            "$ref": "#/components/schemas/AuthMethodAdditionalData"
          },
          "auth_method_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "AuthMethodId"
          },
          "auth_method_name": {
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "auth_method_roles_assoc": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AuthMethodRoleAssociation"
            },
            "x-go-name": "AuthMethodRolesAssoc"
          },
          "client_permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ClientPermissions"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "delete_protection": {
            "type": "boolean",
            "x-go-name": "DeleteProtection"
          },
          "description": {
            "type": "string",
            "x-go-name": "Description"
          },
          "expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AuthExpirationEvent"
            },
            "x-go-name": "ExpirationEvents"
          },
          "is_approved": {
            "type": "boolean",
            "x-go-name": "IsApproved"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AuthMethodAccessInfo": {
        "type": "object",
        "title": "AuthMethodAccessInfo includes auth method access information.",
        "properties": {
          "access_expires": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "AccessExpires"
          },
          "access_id_alias": {
            "description": "for accounts where AccessId holds encrypted email this field will hold generated AccessId,\nfor accounts based on regular AccessId it will be equal to accessId itself",
            "type": "string",
            "x-go-name": "AccessIdAlias"
          },
          "allowed_client_type": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedClientTypes"
          },
          "api_key_access_rules": {
            "$ref": "#/components/schemas/APIKeyAccessRules"
          },
          "audit_logs_claims": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuditLogsClaims"
          },
          "aws_iam_access_rules": {
            "$ref": "#/components/schemas/AWSIAMAccessRules"
          },
          "azure_ad_access_rules": {
            "$ref": "#/components/schemas/AzureADAccessRules"
          },
          "cert_access_rules": {
            "$ref": "#/components/schemas/CertAccessRules"
          },
          "cidr_whitelist": {
            "type": "string",
            "x-go-name": "CIDRWhitelist"
          },
          "email_pass_access_rules": {
            "$ref": "#/components/schemas/EmailPassAccessRules"
          },
          "force_sub_claims": {
            "description": "if true the role associated with this auth method must include sub claims",
            "type": "boolean",
            "x-go-name": "ForceSubClaims"
          },
          "gcp_access_rules": {
            "$ref": "#/components/schemas/GCPAccessRules"
          },
          "gw_cidr_whitelist": {
            "type": "string",
            "x-go-name": "GWCIDRWhitelist"
          },
          "huawei_access_rules": {
            "$ref": "#/components/schemas/HuaweiAccessRules"
          },
          "jwt_ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtl"
          },
          "k8s_access_rules": {
            "$ref": "#/components/schemas/KubernetesAccessRules"
          },
          "kerberos_access_rules": {
            "$ref": "#/components/schemas/KerberosAccessRules"
          },
          "ldap_access_rules": {
            "$ref": "#/components/schemas/LDAPAccessRules"
          },
          "oauth2_access_rules": {
            "$ref": "#/components/schemas/OAuth2AccessRules"
          },
          "oci_access_rules": {
            "$ref": "#/components/schemas/OCIAccessRules"
          },
          "oidc_access_rules": {
            "$ref": "#/components/schemas/OIDCAccessRules"
          },
          "product_types": {
            "description": "List of product types this auth method will be in use of",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Product"
            },
            "x-go-name": "ProductTypes"
          },
          "rules_type": {
            "type": "string",
            "x-go-name": "AccessRulesType"
          },
          "saml_access_rules": {
            "$ref": "#/components/schemas/SAMLAccessRules"
          },
          "sub_claims_delimiters": {
            "$ref": "#/components/schemas/SubClaimsDelimiters"
          },
          "universal_identity_access_rules": {
            "$ref": "#/components/schemas/UniversalIdentityAccessRules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AuthMethodAdditionalData": {
        "type": "object",
        "title": "AuthMethodAdditionalData  Store specific authentication provider data, such as Kerberos.",
        "properties": {
          "kerberos_data": {
            "$ref": "#/components/schemas/KerberosAuthMethodInfo"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AuthMethodRoleAssociation": {
        "description": "AuthMethodRoleAssociation includes details of an association between an auth\nmethod and a role.",
        "type": "object",
        "properties": {
          "allowed_ops": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedOperations"
          },
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          },
          "auth_method_sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "AuthMethodSubClaims"
          },
          "is_sub_claims_case_sensitive": {
            "type": "boolean",
            "x-go-name": "IsSubClaimsCaseSensitive"
          },
          "is_subclaims_with_operator": {
            "type": "boolean",
            "x-go-name": "IsSubclaimsWithOperator"
          },
          "role_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RoleId"
          },
          "role_name": {
            "type": "string",
            "x-go-name": "RoleName"
          },
          "rules": {
            "$ref": "#/components/schemas/Rules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AzureADAccessRules": {
        "description": "AzureADAccessRules contains access rules specific to Azure Active Directory\nauthentication.",
        "type": "object",
        "properties": {
          "ad_endpoint": {
            "description": "The audience in the JWT.",
            "type": "string",
            "x-go-name": "Audience"
          },
          "azure_cloud": {
            "description": "Azure cloud environment [AzureCloud/AzureUSGovernment/AzureChinaCloud]. For create/update, cloud is inferred from jwks_uri.",
            "type": "string",
            "x-go-name": "AzureCloud"
          },
          "bound_group_ids": {
            "description": "The list of group ids that login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundGroupIDs"
          },
          "bound_resource_groups": {
            "description": "The list of resource groups that login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceGroups"
          },
          "bound_resource_ids": {
            "description": "The list of full resource ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceIds"
          },
          "bound_resource_names": {
            "description": "The list of resource names that the login is restricted to (e.g, a\nvirtual machine name, scale set name, etc).",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceNames"
          },
          "bound_resource_providers": {
            "description": "The list of resource providers that login is restricted to (e.g,\nMicrosoft.Compute, Microsoft.ManagedIdentity, etc).",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceProviders"
          },
          "bound_resource_types": {
            "description": "The list of resource types that login is restricted to  (e.g,\nvirtualMachines, userAssignedIdentities, etc).",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceTypes"
          },
          "bound_service_principal_ids": {
            "description": "The list of service principal IDs that login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundServicePrincipalIDs"
          },
          "bound_subscription_ids": {
            "description": "The list of subscription IDs that login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundSubscriptionsIDs"
          },
          "bound_tenant_id": {
            "description": "The tenants id for the Azure Active Directory organization.",
            "type": "string",
            "x-go-name": "BoundTenantID"
          },
          "issuer": {
            "description": "Issuer URL",
            "type": "string",
            "x-go-name": "Issuer"
          },
          "jwks_uri": {
            "description": "The URL to the JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.",
            "type": "string",
            "x-go-name": "JWKeySetURL"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertAccessRules": {
        "type": "object",
        "title": "CertAccessRules contains access rules specific to certificate authentication.",
        "properties": {
          "allowed_cors": {
            "description": "a list of allowed cors domains if used for browser authentication",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedCors"
          },
          "bound_common_names": {
            "description": "A list of names. At least one must exist in the Common Name. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundCommonNames"
          },
          "bound_dns_sans": {
            "description": "A list of DNS names. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundDnsSans"
          },
          "bound_email_sans": {
            "description": "A list of Email Addresses. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundEmailSans"
          },
          "bound_extensions": {
            "description": "A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values must match. Supports globbing on \"value\".",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundExtensions"
          },
          "bound_organizational_units": {
            "description": "A list of Organizational Units names. At least one must exist in the OU field.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundOrganizationalUnits"
          },
          "bound_uri_sans": {
            "description": "A list of URIs. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundUriSans"
          },
          "certificate": {
            "description": "Base64 encdoed PEM certificate",
            "type": "string",
            "x-go-name": "Certificate"
          },
          "require_crl_dp": {
            "description": "RequireCrlDp indicates whether CRL distribution points are required on the leaf client certificate,\nand whether CRL validation must be enforced during authentication.",
            "type": "boolean",
            "x-go-name": "RequireCrlDp"
          },
          "revoked_cert_ids": {
            "description": "A list of revoked cert ids",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RevokedCertIds"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EmailPassAccessRules": {
        "type": "object",
        "title": "EmailPassAccessRules is a set of rules for email password access type.",
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/HashAlgorithm"
          },
          "email": {
            "description": "The Email value",
            "type": "string",
            "x-go-name": "Email"
          },
          "enc_email_with_shared_key": {
            "description": "EncEmailWithSharedKey is the email of this auth method,\nencrypted with the shared auth/uam key (for use in uam)",
            "type": "string",
            "x-go-name": "EncEmailWithSharedKey"
          },
          "hash_pass": {
            "description": "The password value",
            "type": "string",
            "x-go-name": "HashPass"
          },
          "last_reset_password": {
            "description": "The last password change date",
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastResetPassword"
          },
          "mfa_type": {
            "$ref": "#/components/schemas/MFAType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GCPAccessRules": {
        "type": "object",
        "title": "GCPAccessRules contains access rules specific to GCP IAM or GCE authentication.",
        "properties": {
          "audience": {
            "description": "The audience in the JWT",
            "type": "string",
            "default": "akeyless.io",
            "x-go-name": "Audience"
          },
          "bound_labels": {
            "description": "A map of GCP labels formatted as \"key:value\" strings that must be set on authorized GCE instances.\nTODO: Because GCP labels are not currently ACL'd ....",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "BoundLabels"
          },
          "bound_projects": {
            "description": "Human and Machine authentication section\nArray of GCP project IDs. Only entities belonging to any of the provided\nprojects can authenticate.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundProjects"
          },
          "bound_regions": {
            "description": "List of regions that a GCE instance must belong to in order to be authenticated.\nTODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundRegions"
          },
          "bound_service_accounts": {
            "description": "List of service accounts the service account must be part of in order to be authenticated",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundServiceAccounts"
          },
          "bound_zones": {
            "description": "=== Machine authentication section ===\nList of zones that a GCE instance must belong to in order to be authenticated.\nTODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundZones"
          },
          "service_account": {
            "description": "ServiceAccount holds the credentials file contents to be used by Akeyless\nto validate IAM (Human) and GCE (Machine) logins against GCP\nbase64 encoded string",
            "type": "string",
            "x-go-name": "ServiceAccount"
          },
          "type": {
            "$ref": "#/components/schemas/GCPAccessRulesType"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GCPAccessRulesType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "HashAlgorithm": {
        "type": "string",
        "title": "HashAlgorithm is a type that represents a single hash algorithm.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "HuaweiAccessRules": {
        "type": "object",
        "title": "HuaweiAccessRules defines access rules specific to Huawei authentication.",
        "properties": {
          "auth_endpoint": {
            "description": "The auth URL.",
            "type": "string",
            "x-go-name": "AuthEndpoint"
          },
          "domain_id": {
            "description": "The list of domain ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DomainID"
          },
          "domain_name": {
            "description": "The list of domainNames that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DomainName"
          },
          "tenant_id": {
            "description": "The list of tenantIDs  that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TenantID"
          },
          "tenant_name": {
            "description": "The list of tenantNames  that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TenantName"
          },
          "user_id": {
            "description": "The list of user ids that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserID"
          },
          "user_name": {
            "description": "The list of user names that the login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "UserName"
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
      "KerberosAccessRules": {
        "type": "object",
        "title": "KerberosAccessRules contains access rules specific to Kerberos.",
        "properties": {
          "sign_public_key": {
            "type": "string",
            "x-go-name": "SignPublicKey"
          },
          "unique_identifier": {
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "KerberosAuthMethodInfo": {
        "type": "object",
        "properties": {
          "kerberos_keytab": {
            "type": "string",
            "x-go-name": "KerberosKeytab"
          },
          "kerberos_krb5_conf": {
            "type": "string",
            "x-go-name": "KerberosKrb5Conf"
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
          "ldap_certificate": {
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
          "ldap_url_address": {
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
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "KubernetesAccessRules": {
        "type": "object",
        "title": "KubernetesAccessRules includes access rules specific to the Kubernetes auth method.",
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/Algorithm"
          },
          "audience": {
            "description": "Audience is an optional Kubernetes jwt claim to verify",
            "type": "string",
            "x-go-name": "Audience"
          },
          "bound_namespaces": {
            "description": "A list of namespaces that the authentication is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Namespaces"
          },
          "bound_pod_names": {
            "description": "A list of pods names that the authentication is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "PodNames"
          },
          "bound_service_account_names": {
            "description": "A list of service account names that the authentication is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ServiceAccountNames"
          },
          "gen_key_pair": {
            "description": "Generate public/private key (the private key is required for the K8S Auth Config in the Akeyless Gateway)",
            "type": "string",
            "x-go-name": "GenKeyPair"
          },
          "pub_key": {
            "description": "The public key value of the Kubernetes auth method configuration in the Akeyless Gateway.",
            "type": "string",
            "x-go-name": "PubKeyValue"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "LDAPAccessRules": {
        "type": "object",
        "title": "LDAPAccessRules includes access rules specific to LDAP authentication.",
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/Algorithm"
          },
          "gen_key_pair": {
            "description": "Generate public/private key (the private key is required for the LDAP Auth Config in the Akeyless Gateway)",
            "type": "string",
            "x-go-name": "GenKeyPair"
          },
          "key": {
            "description": "The public key value of LDAP.",
            "type": "string",
            "x-go-name": "PubKeyValue"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ListAuthMethodsOutput": {
        "type": "object",
        "title": "ListAuthMethodsOutput is a list of auth methods.",
        "properties": {
          "auth_methods": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AuthMethod"
            },
            "x-go-name": "AuthMethods"
          },
          "next_page": {
            "type": "string",
            "x-go-name": "NextPage"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "MFAType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OAuth2AccessRules": {
        "description": "OAuth2AccessRules contains access rules specific to OAuth2 authentication\nmethod.",
        "type": "object",
        "properties": {
          "audience": {
            "description": "The audience in the JWT.",
            "type": "string",
            "x-go-name": "Audience"
          },
          "authorized_gw_cluster_name": {
            "description": "The gateway cluster name that is authorized to access JWKeySetURL",
            "type": "string",
            "x-go-name": "AuthorizedGwClusterName"
          },
          "bound_claims": {
            "description": "The claims that login is restricted to.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OAuth2CustomClaim"
            },
            "x-go-name": "BoundCustomClaims"
          },
          "bound_clients_id": {
            "description": "The clients ids that login is restricted to.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundClientsIDs"
          },
          "certificate": {
            "description": "Certificate to use when calling jwks_uri from the gateway. in PEM format",
            "type": "string",
            "x-go-name": "Certificate"
          },
          "issuer": {
            "description": "Issuer URL",
            "type": "string",
            "x-go-name": "Issuer"
          },
          "jwks_json_data": {
            "description": "The JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.\nbase64 encoded string",
            "type": "string",
            "x-go-name": "JWKeySetJsonData"
          },
          "jwks_uri": {
            "description": "The URL to the JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.",
            "type": "string",
            "x-go-name": "JWKeySetURL"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OAuth2CustomClaim": {
        "description": "OAuth2CustomClaim is a custom claim specific to OAuth2 authentication\nmethod.",
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "values": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Values"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OCIAccessRules": {
        "description": "OCIAccessRules contains access rules specific to Oracle cloud instance / user authentication",
        "type": "object",
        "properties": {
          "group_ocids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GroupOCIDs"
          },
          "tenant_ocid": {
            "type": "string",
            "x-go-name": "TenantOCID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OIDCAccessRules": {
        "description": "OIDCAccessRules contains access rules specific to Open Id Connect authentication\nmethod.",
        "type": "object",
        "properties": {
          "allowed_redirect_URIs": {
            "description": "Allowed redirect URIs after the authentication",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedRedirectURIs"
          },
          "audience": {
            "description": "Audience claim to be used as part of the authentication flow. In case set, it must match the one configured on the Identity Provider's Application",
            "type": "string",
            "x-go-name": "Audience"
          },
          "bound_claims": {
            "description": "The claims that login is restricted to.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OIDCCustomClaim"
            },
            "x-go-name": "BoundCustomClaims"
          },
          "client_id": {
            "description": "Client ID",
            "type": "string",
            "x-go-name": "ClientID"
          },
          "client_secret": {
            "description": "Client Secret",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "is_internal": {
            "description": "IsInternal indicates whether this is an internal Auth Method where the client has no control\nover it, or it was created by the client\ne.g - Sign In with Google will create an OIDC Auth Method with IsInternal=true",
            "type": "boolean",
            "x-go-name": "IsInternal"
          },
          "issuer": {
            "description": "Issuer URL",
            "type": "string",
            "x-go-name": "Issuer"
          },
          "required_scopes": {
            "description": "A list of required scopes to request from the oidc provider, and to check on the token",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RequiredScopes"
          },
          "required_scopes_prefix": {
            "description": "A prefix to add to the required scopes (for example, azures' Application ID URI)",
            "type": "string",
            "x-go-name": "RequiredScopesPrefix"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "OIDCCustomClaim": {
        "description": "OIDCCustomClaim is a custom claim specific to OIDC authentication\nmethod.",
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "values": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Values"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "Product": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "Rules": {
        "type": "object",
        "title": "Rules are a part of AKEYLESS RBAC.",
        "properties": {
          "admin": {
            "description": "Is admin",
            "type": "boolean",
            "x-go-name": "Admin"
          },
          "path_rules": {
            "description": "The path the rules refers to",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PathRule"
            },
            "x-go-name": "PathRules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SAMLAccessRules": {
        "type": "object",
        "title": "SAMLAccessRules defines access rules specific to SAML authentication method.",
        "properties": {
          "allowed_redirect_URIs": {
            "description": "Allowed redirect URIs after the authentication",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedRedirectURIs"
          },
          "bound_attributes": {
            "description": "The attributes that login is restricted to.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SAMLAttribute"
            },
            "x-go-name": "BoundAttributes"
          },
          "idp_metadata_url": {
            "description": "IDP metadata url",
            "type": "string",
            "x-go-name": "IDPMetadataURL"
          },
          "idp_metadata_xml": {
            "description": "IDP metadata XML",
            "type": "string",
            "x-go-name": "IDPMetadataXML"
          },
          "unique_identifier": {
            "description": "A unique identifier to distinguish different users",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SAMLAttribute": {
        "type": "object",
        "title": "SAMLAttribute defines an attribute of SAML authentication.",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "values": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Values"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SubClaimsDelimiters": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "UniversalIdentityAccessRules": {
        "type": "object",
        "title": "UniversalIdentityAccessRules contains access rules specific to Universal Identity.",
        "properties": {
          "deny_inheritance": {
            "type": "boolean",
            "x-go-name": "DenyInheritance"
          },
          "deny_rotate": {
            "type": "boolean",
            "x-go-name": "DenyRotate"
          },
          "ttl": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "TTL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "authMethodList": {
        "description": "authMethodList is a command that returns a list of auth methods",
        "type": "object",
        "properties": {
          "filter": {
            "description": "Filter by auth method name or part of it",
            "type": "string",
            "x-go-name": "Filter"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "pagination-token": {
            "description": "Next page reference",
            "type": "string",
            "x-go-name": "PaginationToken"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "The Auth method types list of the requested method. In case it is empty, all\ntypes of auth methods will be returned. options: [api_key, azure_ad, oauth2/jwt, saml2,\nldap, aws_iam, oidc, universal_identity, gcp, k8s, cert]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Types"
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