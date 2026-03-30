# Source: https://docs.akeyless.io/reference/listitems.md

# /list-items

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
    "/list-items": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listItems",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listItems"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listItemsResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        },
        "x-generate-protobuf": "true"
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
      "listItemsResponse": {
        "description": "listItemsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ListItemsInPathOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AccessOrGroupPermissionAssignment": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access_type": {
            "type": "string",
            "x-go-name": "AccessType"
          },
          "assignment_name": {
            "type": "string",
            "x-go-name": "AssignmentName"
          },
          "assignment_type": {
            "$ref": "#/components/schemas/AssignmentType"
          },
          "group_id": {
            "type": "string",
            "x-go-name": "GroupId"
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
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/oidc/shared"
      },
      "AccessOrGroupPermissionAssignments": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/AccessOrGroupPermissionAssignment"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/oidc/shared"
      },
      "AllowedExtraExtensions": {
        "type": "object",
        "additionalProperties": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/pki-utils/extra_extensions"
      },
      "AssignmentType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/oidc/shared"
      },
      "AttributeTypeAndValue": {
        "description": "AttributeTypeAndValue mirrors the ASN.1 structure of the same name in\nRFC 5280, Section 4.1.2.4.",
        "type": "object",
        "properties": {
          "Type": {
            "$ref": "#/components/schemas/ObjectIdentifier"
          },
          "Value": {}
        },
        "x-go-package": "crypto/x509/pkix"
      },
      "AutoRotateType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "BastionListEntry": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "allowed_access_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedAccessIDs"
          },
          "allowed_urls": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedUrls"
          },
          "allowed_urls_per_instance": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "AllowedUrlsPerInstance"
          },
          "bastion_ssh_port": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "BastionSSHPort"
          },
          "bastion_urls_per_type": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "BastionURLsPerType"
          },
          "cluster_name": {
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "display_name": {
            "type": "string",
            "x-go-name": "DisplayName"
          },
          "has_gateway_identity": {
            "type": "boolean",
            "x-go-name": "HasGatewayIdentity"
          },
          "last_report": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastReport"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "BastionsList": {
        "type": "object",
        "properties": {
          "clusters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BastionListEntry"
            },
            "x-go-name": "Clusters"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CAMode": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertIssuerType": {
        "type": "string",
        "title": "CertIssuerType represents possible certificate issuers type.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateChainInfo": {
        "type": "object",
        "properties": {
          "auto_renew_certificate": {
            "type": "boolean",
            "x-go-name": "AutoRenewCertificate"
          },
          "certificate_chain": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateInfo"
            },
            "x-go-name": "CertificateChain"
          },
          "certificate_format": {
            "type": "string",
            "x-go-name": "CertificateFormat"
          },
          "certificate_has_private_key": {
            "type": "boolean",
            "x-go-name": "CertificateHasPrivateKey"
          },
          "certificate_issuer_gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateIssuerGwClusterId"
          },
          "certificate_issuer_gw_cluster_url": {
            "type": "string",
            "x-go-name": "CertificateIssuerGwClusterUrl"
          },
          "certificate_issuer_item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateIssuerID"
          },
          "certificate_issuer_name": {
            "type": "string",
            "x-go-name": "CertificateIssuerName"
          },
          "certificate_pem": {
            "type": "string",
            "x-go-name": "CertificatePem"
          },
          "certificate_status": {
            "$ref": "#/components/schemas/CertificateStatus"
          },
          "common_name": {
            "type": "string",
            "x-go-name": "CommonName"
          },
          "csr_pem": {
            "description": "CSRPEM contains the PEM-encoded CSR for pending certificates (HTTP-01 challenge)",
            "type": "string",
            "x-go-name": "CSRPEM"
          },
          "error_message": {
            "type": "string",
            "x-go-name": "ErrorMessage"
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
          "external_ca_id": {
            "$ref": "#/components/schemas/NullString"
          },
          "issuance_status": {
            "type": "string",
            "x-go-name": "IssuanceStatus"
          },
          "not_before": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotBefore"
          },
          "renew_before_expiration_in_days": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RenewBeforeExpirationInDays"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "CertificateFormat": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateInfo": {
        "type": "object",
        "properties": {
          "ExtKeyUsage": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ExtKeyUsage"
            }
          },
          "KeyUsage": {
            "$ref": "#/components/schemas/KeyUsage"
          },
          "crl_distribution_points": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CrlDistributionPoints"
          },
          "dns_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "DNSNames"
          },
          "email_addresses": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EmailAddresses"
          },
          "extensions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Extension"
            },
            "x-go-name": "Extensions"
          },
          "ip_addresses": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "IPAddresses"
          },
          "is_ca": {
            "type": "boolean",
            "x-go-name": "IsCA"
          },
          "issuer": {
            "$ref": "#/components/schemas/Name"
          },
          "issuing_certificate_url": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "IssuingCertificateURL"
          },
          "key_size": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "KeySize"
          },
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
          "ocsp_server": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "OCSPServer"
          },
          "public_key_algorithm_name": {
            "type": "string",
            "x-go-name": "PublicKeyAlgorithmName"
          },
          "serial_number": {
            "type": "string",
            "x-go-name": "SerialNumber"
          },
          "sha_1_fingerprint": {
            "type": "string",
            "x-go-name": "Sha1Fingerprint"
          },
          "sha_256_fingerprint": {
            "type": "string",
            "x-go-name": "Sha256Fingerprint"
          },
          "signature": {
            "type": "string",
            "x-go-name": "Signature"
          },
          "signature_algorithm_name": {
            "type": "string",
            "x-go-name": "SignatureAlgorithmName"
          },
          "subject": {
            "$ref": "#/components/schemas/Name"
          },
          "subject_public_key": {
            "type": "string",
            "x-go-name": "SubjectPublicKey"
          },
          "uris": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "URIs"
          },
          "version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateIssueInfo": {
        "type": "object",
        "title": "CertificateIssueInfo defines Certificate Issuer info.",
        "properties": {
          "cert_issuer_type": {
            "$ref": "#/components/schemas/CertIssuerType"
          },
          "max_ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxTTL"
          },
          "pki_cert_issuer_details": {
            "$ref": "#/components/schemas/PKICertificateIssueDetails"
          },
          "ssh_cert_issuer_details": {
            "$ref": "#/components/schemas/SSHCertificateIssueDetails"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateTemplateInfo": {
        "type": "object",
        "properties": {
          "common_name": {
            "type": "string",
            "x-go-name": "CommonName"
          },
          "country": {
            "type": "string",
            "x-go-name": "Country"
          },
          "csr_cnf_base_64": {
            "type": "string",
            "x-go-name": "CsrCNFBase64"
          },
          "digest_algo": {
            "type": "string",
            "x-go-name": "DigestAlgo"
          },
          "hash_algorithm": {
            "type": "string",
            "x-go-name": "HashAlgorithm"
          },
          "locality": {
            "type": "string",
            "x-go-name": "Locality"
          },
          "organization": {
            "type": "string",
            "x-go-name": "Organization"
          },
          "province": {
            "type": "string",
            "x-go-name": "Province"
          },
          "self_signed_enabled": {
            "type": "boolean",
            "x-go-name": "SelfSignedEnabled"
          },
          "ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          }
        },
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
      "ClassicKeyDetailsInfo": {
        "type": "object",
        "properties": {
          "classic_key_attributes": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "ClassicKeyAttributes"
          },
          "classic_key_id": {
            "type": "string",
            "x-go-name": "ClassicKeyId"
          },
          "credential_id": {
            "type": "string",
            "x-go-name": "CredentialId"
          },
          "gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "has_certificate": {
            "type": "boolean",
            "x-go-name": "HasCertificate"
          },
          "is_provided_by_user": {
            "type": "boolean",
            "x-go-name": "IsProvidedByUser"
          },
          "is_unexportable": {
            "type": "boolean",
            "x-go-name": "IsUnexportable"
          },
          "key_state": {
            "$ref": "#/components/schemas/ItemState"
          },
          "key_type": {
            "$ref": "#/components/schemas/ClassicKeyType"
          },
          "last_error": {
            "type": "string",
            "x-go-name": "LastError"
          },
          "public_key": {
            "type": "string",
            "x-go-name": "PublicKey"
          },
          "target_alias_helper": {
            "type": "string",
            "x-go-name": "TargetAliasHelper"
          },
          "target_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TargetTypes"
          },
          "targets": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ClassicKeyTargetInfo"
            },
            "x-go-name": "Targets"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          },
          "websites": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Websites"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyPurpose": {
        "description": "ClassicKeyPurpose defines purpose for classic keys",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyStatusInfo": {
        "type": "object",
        "properties": {
          "error_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ErrorDate"
          },
          "last_error": {
            "type": "string",
            "x-go-name": "LastError"
          },
          "last_status": {
            "$ref": "#/components/schemas/ClassicKeyTargetStatus"
          },
          "version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyTargetInfo": {
        "type": "object",
        "properties": {
          "external_kms_id": {
            "$ref": "#/components/schemas/ExternalKMSKeyId"
          },
          "key_purpose": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ClassicKeyPurpose"
            },
            "x-go-name": "Purpose"
          },
          "key_status": {
            "$ref": "#/components/schemas/ClassicKeyStatusInfo"
          },
          "target_assoc_id": {
            "type": "string",
            "x-go-name": "TargetAssociationID"
          },
          "target_type": {
            "$ref": "#/components/schemas/TargetType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyTargetStatus": {
        "description": "ClassicKeyTargetStatus defines status of classic key target",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyType": {
        "type": "string",
        "title": "ClassicKeyType defines types of keys that can be managed by ClassicKey supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClientPermissions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DesktopAppConf": {
        "type": "object",
        "properties": {
          "default_cert_issuer_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DefaultCertIssuerId"
          },
          "default_cert_issuer_name": {
            "type": "string",
            "x-go-name": "DefaultCertIssuerName"
          },
          "secure_web_access_url": {
            "type": "string",
            "x-go-name": "SecureWebAccessUrl"
          },
          "secure_web_proxy_url": {
            "type": "string",
            "x-go-name": "SecureWebProxyUrl"
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
      "DynamicSecretProducerInfo": {
        "description": "DynamicSecretProducerInfo The dynamic secret producer info\nThis parameter relevant and required only in case of create update dynamic secret.",
        "type": "object",
        "properties": {
          "failure_message": {
            "type": "string",
            "x-go-name": "FailureMessage"
          },
          "gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "k8s_allowed_namespaces": {
            "description": "Relevant only for generic k8s producer",
            "type": "string",
            "x-go-name": "AllowedNamespaces"
          },
          "k8s_dynamic_mode": {
            "description": "Relevant only for generic k8s producer",
            "type": "boolean",
            "x-go-name": "DynamicMode"
          },
          "producer_last_keep_alive": {
            "type": "string",
            "x-go-name": "ProducerLastKeepAlive"
          },
          "producer_metadata": {
            "type": "string",
            "x-go-name": "ProducerMetadata"
          },
          "producer_status": {
            "$ref": "#/components/schemas/ProducerStatus"
          },
          "producer_type": {
            "type": "string",
            "x-go-name": "ProducerType"
          },
          "user_ttl": {
            "type": "string",
            "x-go-name": "UserTtl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EmailTokenizerInfo": {
        "description": "EmailTokenizerInfo represents a tokenizer that specifically tokenizes emails",
        "type": "object",
        "properties": {
          "domain_suffix_length": {
            "description": "What length of a random domain suffix to generate\nused only if FixedDomainSuffix is empty",
            "type": "integer",
            "format": "int64",
            "x-go-name": "DomainSuffixLength"
          },
          "fixed_domain_suffix": {
            "description": "if FixedDomainSuffix isn't empty, it will be appended to the output",
            "type": "string",
            "x-go-name": "FixedDomainSuffix"
          },
          "keep_prefix_length": {
            "description": "How many letters of the plaintext to keep in the output",
            "type": "integer",
            "format": "int64",
            "x-go-name": "KeepPrefixLength"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ExtKeyUsage": {
        "description": "Each of the ExtKeyUsage* constants define a unique action.",
        "type": "integer",
        "format": "int64",
        "title": "ExtKeyUsage represents an extended set of actions that are valid for a given key.",
        "x-go-package": "crypto/x509"
      },
      "Extension": {
        "type": "object",
        "properties": {
          "Critical": {
            "type": "boolean"
          },
          "Name": {
            "type": "string"
          },
          "Value": {
            "type": "string"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ExternalKMSKeyId": {
        "type": "object",
        "properties": {
          "key_id": {
            "type": "string",
            "x-go-name": "KeyId"
          },
          "key_reference": {
            "type": "string",
            "x-go-name": "KeyReference"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GatewayDetailsForItemReplyObj": {
        "type": "object",
        "properties": {
          "cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ClusterId"
          },
          "cluster_name": {
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "cluster_url": {
            "type": "string",
            "x-go-name": "ClusterUrl"
          },
          "desktop_app": {
            "$ref": "#/components/schemas/DesktopAppConf"
          },
          "is_cluster_available": {
            "type": "boolean",
            "x-go-name": "IsAvailable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GraceRotationTiming": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "HostProviderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ImporterInfo": {
        "type": "object",
        "properties": {
          "external_item_id": {
            "type": "string",
            "x-go-name": "ExternalItemId"
          },
          "version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "IssuerOverviewInfo": {
        "type": "object",
        "title": "IssuerOverviewInfo holds PKI cert issuer fields needed for UI table rendering.",
        "properties": {
          "certificate_authority_mode": {
            "$ref": "#/components/schemas/CAMode"
          },
          "expiration_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ExpirationDate"
          },
          "key_type": {
            "type": "string",
            "x-go-name": "KeyType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Item": {
        "type": "object",
        "title": "Item describes any item in AKEYLESS.",
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
          "auto_rotate": {
            "type": "boolean",
            "x-go-name": "AutoRotate"
          },
          "bastion_details": {
            "$ref": "#/components/schemas/BastionsList"
          },
          "cert_issuer_signer_key_name": {
            "type": "string",
            "x-go-name": "CertIssuerSignerKeyName"
          },
          "certificate_issue_details": {
            "$ref": "#/components/schemas/CertificateIssueInfo"
          },
          "certificates": {
            "type": "string",
            "x-go-name": "Certificates"
          },
          "client_permissions": {
            "$ref": "#/components/schemas/ClientPermissions"
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
          "delete_protection": {
            "type": "boolean",
            "x-go-name": "ItemProtected"
          },
          "deletion_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "DeletionDate"
          },
          "display_id": {
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "gateway_details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GatewayDetailsForItemReplyObj"
            },
            "x-go-name": "GatewayDetails"
          },
          "is_access_request_enabled": {
            "type": "boolean",
            "x-go-name": "IsAccessRequestEnabled"
          },
          "is_enabled": {
            "type": "boolean",
            "x-go-name": "IsEnabled"
          },
          "item_accessibility": {
            "$ref": "#/components/schemas/ItemAccessibility"
          },
          "item_custom_fields_details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemCustomFieldsDetails"
            },
            "x-go-name": "ItemCustomFieldsDetails"
          },
          "item_general_info": {
            "$ref": "#/components/schemas/ItemGeneralInfo"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "item_metadata": {
            "type": "string",
            "x-go-name": "ItemMetadata"
          },
          "item_name": {
            "type": "string",
            "x-go-name": "ItemName"
          },
          "item_size": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Size"
          },
          "item_state": {
            "$ref": "#/components/schemas/ItemState"
          },
          "item_sub_type": {
            "$ref": "#/components/schemas/ItemSubType"
          },
          "item_tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "item_targets_assoc": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemTargetAssociation"
            },
            "x-go-name": "ItemTargetsAssoc"
          },
          "item_type": {
            "$ref": "#/components/schemas/ItemType"
          },
          "item_versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemVersion"
            },
            "x-go-name": "ItemVersions"
          },
          "last_rotation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastRotationDate"
          },
          "last_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "LastVersion"
          },
          "linked_details": {
            "$ref": "#/components/schemas/LinkedDetails"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "next_rotation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NextRotationDate"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "protection_key_type": {
            "$ref": "#/components/schemas/ItemType"
          },
          "public_value": {
            "type": "string",
            "x-go-name": "PublicValue"
          },
          "rotation_interval": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RotationInterval"
          },
          "shared_by": {
            "$ref": "#/components/schemas/RuleAssigner"
          },
          "target_versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TargetItemVersion"
            },
            "x-go-name": "TargetVersions"
          },
          "usc_sync_associated_items": {
            "description": "for USC item, hold rotated-secrets that are associated to him\nfor rotated-secret, holds the associated USCs",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemUSCSyncAssociation"
            },
            "x-go-name": "USCSyncAssociatedItems"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemAccessibility": {
        "type": "integer",
        "format": "int64",
        "title": "ItemAccessibility defines types supported by AKEYLESS.",
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
      "ItemGeneralInfo": {
        "type": "object",
        "title": "ItemGeneralInfo defines item general info.",
        "properties": {
          "cert_issue_details": {
            "$ref": "#/components/schemas/CertificateIssueInfo"
          },
          "certificate_chain_info": {
            "$ref": "#/components/schemas/CertificateChainInfo"
          },
          "certificate_format": {
            "$ref": "#/components/schemas/CertificateFormat"
          },
          "certificates_template_info": {
            "$ref": "#/components/schemas/CertificateTemplateInfo"
          },
          "classic_key_details": {
            "$ref": "#/components/schemas/ClassicKeyDetailsInfo"
          },
          "cluster_gw_url": {
            "type": "string",
            "x-go-name": "ClusterGWUrl"
          },
          "display_metadata": {
            "type": "string",
            "x-go-name": "DisplayMetadata"
          },
          "dynamic_secret_producer_details": {
            "$ref": "#/components/schemas/DynamicSecretProducerInfo"
          },
          "expiration_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "KeyExpirationEvents"
          },
          "importer_info": {
            "$ref": "#/components/schemas/ImporterInfo"
          },
          "issuer_overview_info": {
            "$ref": "#/components/schemas/IssuerOverviewInfo"
          },
          "next_rotation_events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/NextAutoRotationEvent"
            },
            "x-go-name": "NextRotationEvents"
          },
          "oidc_client_info": {
            "$ref": "#/components/schemas/OidcClientInfo"
          },
          "password_policy": {
            "$ref": "#/components/schemas/PasswordPolicyInfo"
          },
          "rotated_secret_details": {
            "$ref": "#/components/schemas/RotatedSecretDetailsInfo"
          },
          "secure_remote_access_details": {
            "$ref": "#/components/schemas/SecureRemoteAccess"
          },
          "static_secret_info": {
            "$ref": "#/components/schemas/StaticSecretDetailsInfo"
          },
          "tokenizer_info": {
            "$ref": "#/components/schemas/TokenizerInfo"
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
      "ItemState": {
        "description": "ItemState defines the different states an Item can be in",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemSubType": {
        "type": "string",
        "title": "ItemSubType defines types supported by AKEYLESS.",
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
      "ItemType": {
        "type": "string",
        "title": "ItemType defines types supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemUSCSyncAssociation": {
        "description": "ItemUSCSyncAssociation includes details of usc sync associations",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          },
          "attributes": {
            "$ref": "#/components/schemas/UscSyncInfo"
          },
          "delete_remote": {
            "type": "boolean",
            "x-go-name": "DeleteRemote"
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
            "type": "string",
            "x-go-name": "ItemType"
          }
        },
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
      "KeyUsage": {
        "description": "KeyUsage represents the set of actions that are valid for a given key. It's\na bitmap of the KeyUsage* constants.",
        "type": "integer",
        "format": "int64",
        "x-go-package": "crypto/x509"
      },
      "LinkedDetails": {
        "type": "object",
        "properties": {
          "hosts": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Hosts"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ListItemsInPathOutput": {
        "type": "object",
        "title": "ListItemsInPathOutput is a list of items and/or folders in a specific path.",
        "properties": {
          "folders": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Folders"
          },
          "has_next": {
            "type": "boolean",
            "x-go-name": "HasNext"
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Item"
            },
            "x-go-name": "Items"
          },
          "next_page": {
            "type": "string",
            "x-go-name": "NextPage"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Name": {
        "description": "Name represents an X.509 distinguished name. This only includes the common\nelements of a DN. Note that Name is only an approximation of the X.509\nstructure. If an accurate representation is needed, asn1.Unmarshal the raw\nsubject or issuer as an [RDNSequence].",
        "type": "object",
        "properties": {
          "Country": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "OrganizationalUnit"
          },
          "ExtraNames": {
            "description": "ExtraNames contains attributes to be copied, raw, into any marshaled\ndistinguished names. Values override any attributes with the same OID.\nThe ExtraNames field is not populated when parsing, see Names.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AttributeTypeAndValue"
            }
          },
          "Locality": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Province"
          },
          "Names": {
            "description": "Names contains all parsed attributes. When parsing distinguished names,\nthis can be used to extract non-standard attributes that are not parsed\nby this package. When marshaling to RDNSequences, the Names field is\nignored, see ExtraNames.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AttributeTypeAndValue"
            }
          },
          "SerialNumber": {
            "type": "string",
            "x-go-name": "CommonName"
          },
          "StreetAddress": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "PostalCode"
          }
        },
        "x-go-package": "crypto/x509/pkix"
      },
      "NextAutoRotationEvent": {
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
      "NullString": {
        "description": "var s NullString\nerr := db.QueryRow(\"SELECT name FROM foo WHERE id=?\", id).Scan(&s)\n...\nif s.Valid {\nuse s.String\n} else {\nNULL value\n}",
        "type": "object",
        "title": "NullString represents a string that may be null.\nNullString implements the [Scanner] interface so\nit can be used as a scan destination:",
        "properties": {
          "String": {
            "type": "string"
          },
          "Valid": {
            "type": "boolean"
          }
        },
        "x-go-package": "database/sql"
      },
      "ObjectIdentifier": {
        "type": "array",
        "title": "An ObjectIdentifier represents an ASN.1 OBJECT IDENTIFIER.",
        "items": {
          "type": "integer",
          "format": "int64"
        },
        "x-go-package": "encoding/asn1"
      },
      "OidcClientInfo": {
        "type": "object",
        "properties": {
          "access_permission_assignment": {
            "$ref": "#/components/schemas/AccessOrGroupPermissionAssignments"
          },
          "audience": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Audience"
          },
          "client_id": {
            "type": "string",
            "x-go-name": "ClientId"
          },
          "grant_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GrantTypes"
          },
          "issuer_url": {
            "type": "string",
            "x-go-name": "IssuerUrl"
          },
          "logout_uris": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "LogoutURIs"
          },
          "public": {
            "type": "boolean",
            "x-go-name": "Public"
          },
          "redirect_uris": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RedirectURIs"
          },
          "response_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ResponseTypes"
          },
          "scopes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Scopes"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PKICertificateIssueDetails": {
        "type": "object",
        "title": "PKICertificateIssueDetails defines PKI certificate details.",
        "properties": {
          "acme_enabled": {
            "type": "boolean",
            "x-go-name": "AcmeEnabled"
          },
          "allow_any_name": {
            "type": "boolean",
            "x-go-name": "AllowAnyName"
          },
          "allow_copy_ext_from_csr": {
            "type": "boolean",
            "x-go-name": "AllowCopyExtFromCsr"
          },
          "allow_subdomains": {
            "type": "boolean",
            "x-go-name": "AllowSubdomains"
          },
          "allowed_domains_list": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedDomains"
          },
          "allowed_extra_extensions": {
            "$ref": "#/components/schemas/AllowedExtraExtensions"
          },
          "allowed_ip_sans": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedIPSANs"
          },
          "allowed_uri_sans": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedURISANs"
          },
          "auto_renew_certificate": {
            "type": "boolean",
            "x-go-name": "AutoRenewCertificate"
          },
          "basic_constraints_valid_for_non_ca": {
            "type": "boolean",
            "x-go-name": "BasicConstraintsValidForNonCA"
          },
          "certificate_authority_mode": {
            "$ref": "#/components/schemas/CAMode"
          },
          "client_flag": {
            "type": "boolean",
            "x-go-name": "ClientFlag"
          },
          "code_signing_flag": {
            "type": "boolean",
            "x-go-name": "CodeSigningFlag"
          },
          "country": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Country"
          },
          "create_private_crl": {
            "type": "boolean",
            "x-go-name": "CreatePrivateCrl"
          },
          "create_private_ocsp": {
            "description": "CreatePrivateOcsp enables exposing an OCSP endpoint on the Gateway and\nembedding its URL in the AIA extension of issued certificates.",
            "type": "boolean",
            "x-go-name": "CreatePrivateOcsp"
          },
          "create_public_crl": {
            "type": "boolean",
            "x-go-name": "CreatePublicCrl"
          },
          "create_public_ocsp": {
            "description": "CreatePublicOcsp enables exposing a public OCSP endpoint on the Gateway and\nembedding its URL in the AIA extension of issued certificates.",
            "type": "boolean",
            "x-go-name": "CreatePublicOcsp"
          },
          "destination_path": {
            "description": "DestinationPath is the destination to save generated certificates",
            "type": "string",
            "x-go-name": "DestinationPath"
          },
          "disable_wildcards": {
            "type": "boolean",
            "x-go-name": "DisableWildcards"
          },
          "enforce_hostnames": {
            "type": "boolean",
            "x-go-name": "EnforceHostnames"
          },
          "expiration_events": {
            "description": "ExpirationNotification holds a list of expiration notices that should be sent in case a certificate is about to\nexpire, this value is being propagated to the Certificate resources that are created",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "ExpirationNotification"
          },
          "gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GwClusterID"
          },
          "gw_cluster_url": {
            "description": "GWClusterURL is required when CAMode is \"public\" and it defines the cluster URL the PKI should be issued from.\nThe GW cluster must have permissions to read associated target's details",
            "type": "string",
            "x-go-name": "GWClusterURL"
          },
          "is_ca": {
            "type": "boolean",
            "x-go-name": "IsCA"
          },
          "key_bits": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "KeyBits"
          },
          "key_type": {
            "type": "string",
            "x-go-name": "KeyType"
          },
          "key_usage_list": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "KeyUsage"
          },
          "locality": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Locality"
          },
          "max_path_len": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxPathLen"
          },
          "non_critical_key_usage": {
            "type": "boolean",
            "x-go-name": "NonCriticalKeyUsage"
          },
          "not_before_duration": {
            "$ref": "#/components/schemas/Duration"
          },
          "ocsp_next_update": {
            "description": "OcspNextUpdate defines the desired NextUpdate window for OCSP responses.\nValue is in seconds; 0 means not set. Minimum enforced is 10 minutes.",
            "type": "integer",
            "format": "int64",
            "x-go-name": "OcspNextUpdate"
          },
          "organization_list": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Organization"
          },
          "organization_unit_list": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "OrganizationalUnit"
          },
          "pki_issuer_type": {
            "$ref": "#/components/schemas/PkiIssuerType"
          },
          "postal_code": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "PostalCode"
          },
          "protect_generated_certificates": {
            "description": "ProtectGeneratedCertificates dictates whether the created certificates should be protected from deletion",
            "type": "boolean",
            "x-go-name": "ProtectGeneratedCertificates"
          },
          "province": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Province"
          },
          "renew_before_expiration_in_days": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RenewBeforeExpirationInDays"
          },
          "require_cn": {
            "type": "boolean",
            "x-go-name": "RequireCN"
          },
          "server_flag": {
            "type": "boolean",
            "x-go-name": "ServerFlag"
          },
          "street_address": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "StreetAddress"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordBreachInfo": {
        "type": "object",
        "properties": {
          "breach_check_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "BreachCheckDate"
          },
          "breach_count": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "BreachCount"
          },
          "breach_suggestions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PasswordBreachSuggestion"
            },
            "x-go-name": "BreachSuggestions"
          },
          "status": {
            "$ref": "#/components/schemas/PasswordBreachStatus"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordBreachStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordBreachSuggestion": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordPolicyInfo": {
        "type": "object",
        "properties": {
          "password_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "PasswordLength"
          },
          "use_capital_letters": {
            "type": "boolean",
            "x-go-name": "UseCapitalLetters"
          },
          "use_lower_letters": {
            "type": "boolean",
            "x-go-name": "UseLowerLetters"
          },
          "use_numbers": {
            "type": "boolean",
            "x-go-name": "UseNumbers"
          },
          "use_special_characters": {
            "type": "boolean",
            "x-go-name": "UseSpecialCharacters"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreInfo": {
        "type": "object",
        "properties": {
          "score": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Score"
          },
          "status": {
            "$ref": "#/components/schemas/PasswordScoreStatus"
          },
          "suggestions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PasswordScoreSuggestion"
            },
            "x-go-name": "Suggestions"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreSuggestion": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordSecurityInfo": {
        "type": "object",
        "properties": {
          "breach_info": {
            "$ref": "#/components/schemas/PasswordBreachInfo"
          },
          "score_info": {
            "$ref": "#/components/schemas/PasswordScoreInfo"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PkiIssuerType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ProducerStatus": {
        "description": "RotationStatus defines types of rotation Status",
        "type": "string",
        "x-go-name": "RotationStatus",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RegexpTokenizerInfo": {
        "description": "RegexpTokenizerInfo represents a general Regexp tokenization template",
        "type": "object",
        "properties": {
          "alphabet": {
            "description": "The Alphabet used for the tokenization",
            "type": "string",
            "x-go-name": "Alphabet"
          },
          "decoding_template": {
            "description": "Transformation to perform on the decrypted data",
            "type": "string",
            "x-go-name": "DecodingTemplate"
          },
          "encoding_template": {
            "description": "Transformation to perform on the encrypted data,\nif the required output template doesn't match the input string\nThe output Should still be valid for the Pattern, otherwise the secret would be able to be decrypted.",
            "type": "string",
            "x-go-name": "EncodingTemplate"
          },
          "pattern": {
            "description": "Regexp pattern to extract and deposit the text/encdata",
            "type": "string",
            "x-go-name": "Pattern"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RotatedSecretDetailsInfo": {
        "description": "RotatedSecretDetailsInfo The rotated secret rotator info",
        "type": "object",
        "properties": {
          "delete_previous_version_in_days": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "DeletePreviousVersionInDays"
          },
          "enable_custom_password_policy": {
            "type": "boolean",
            "x-go-name": "EnableCustomPasswordPolicy"
          },
          "grace_rotation": {
            "type": "boolean",
            "x-go-name": "GraceRotation"
          },
          "grace_rotation_hour": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "GraceRotationHour"
          },
          "grace_rotation_interval": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "GraceRotationInterval"
          },
          "grace_rotation_timing": {
            "$ref": "#/components/schemas/GraceRotationTiming"
          },
          "gw_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "iis_apps_details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/WindowsService"
            },
            "x-go-name": "IisAppsDetails"
          },
          "last_rotation_error": {
            "type": "string",
            "x-go-name": "LastRotatorError"
          },
          "managed_by_akeyless": {
            "type": "boolean",
            "x-go-name": "ManagedByAkeyless"
          },
          "max_versions": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxVersions"
          },
          "next_auto_rotate_type": {
            "$ref": "#/components/schemas/AutoRotateType"
          },
          "number_of_versions_to_save": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "NumberOfVersionsToSave"
          },
          "public_key_remote_path": {
            "type": "string",
            "x-go-name": "PublicKeyRemotePath"
          },
          "rotation_hour": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "RotationHour"
          },
          "rotation_interval_min": {
            "type": "boolean",
            "x-go-name": "RotationIntervalMin"
          },
          "rotation_statement": {
            "type": "string",
            "x-go-name": "RotationStatement"
          },
          "rotator_creds_type": {
            "$ref": "#/components/schemas/RotatorCredsType"
          },
          "rotator_status": {
            "$ref": "#/components/schemas/ProducerStatus"
          },
          "rotator_type": {
            "$ref": "#/components/schemas/RotatorType"
          },
          "same_password": {
            "type": "boolean",
            "x-go-name": "SamePassword"
          },
          "services_details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/WindowsService"
            },
            "x-go-name": "ServicesDetails"
          },
          "timeout_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TimeoutSeconds"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RotatorCredsType": {
        "type": "string",
        "title": "RotatorCredsType defines types supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RotatorType": {
        "type": "string",
        "title": "RotatorType defines types supported by AKEYLESS.",
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
      "SRAConcurrentConnsLevel": {
        "type": "string",
        "title": "SRAConcurrentConnsLevel indicate what the block level user can apply on sra connections.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SSHCertificateIssueDetails": {
        "type": "object",
        "title": "SSHCertificateIssueDetails defines SSH certificate details.",
        "properties": {
          "allowed_domains": {
            "description": "Relevant for host certificate",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedDomains"
          },
          "allowed_user_key_lengths": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "AllowedUserKeyLengths"
          },
          "allowed_users": {
            "description": "Relevant for user certificate",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedUsers"
          },
          "cert_type": {
            "$ref": "#/components/schemas/SSHCertificateType"
          },
          "critical_options": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "CriticalOptions"
          },
          "extensions": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Extensions"
          },
          "externally_provided_user_sub_claim_key": {
            "description": "ExternallyProvidedUserSubClaimKey is the claim key name where the user name should be taken from",
            "type": "string",
            "x-go-name": "ExternallyProvidedUserSubClaimKey"
          },
          "is_externally_provided_user": {
            "description": "IsExternallyProvidedUser is true if allow users should be taken from claims and not from AllowedUsers",
            "type": "boolean",
            "x-go-name": "IsExternallyProvidedUser"
          },
          "principals": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Principals"
          },
          "static_key_id": {
            "description": "In case it is empty, the key ID will be combination of user identifiers and a random string",
            "type": "string",
            "x-go-name": "StaticKeyID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SSHCertificateType": {
        "type": "integer",
        "format": "uint32",
        "title": "SSHCertificateType defines the types of SSH certificates.",
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
      "StaticSecretDetailsInfo": {
        "type": "object",
        "properties": {
          "format": {
            "$ref": "#/components/schemas/StaticSecretFormat"
          },
          "max_versions": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxVersions"
          },
          "notify_on_change_event": {
            "type": "boolean",
            "x-go-name": "NotifyOnChangeEvent"
          },
          "password_security_info": {
            "$ref": "#/components/schemas/PasswordSecurityInfo"
          },
          "username": {
            "type": "string",
            "x-go-name": "Username"
          },
          "website": {
            "description": "deprecated",
            "type": "string",
            "x-go-name": "Website"
          },
          "websites": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Websites"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "StaticSecretFormat": {
        "description": "StaticSecretFormat defines the format of static secret (e.g. Text)",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetItemVersion": {
        "type": "object",
        "title": "TargetItemVersion describes an item version in AKEYLESS.",
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
          "latest_version": {
            "type": "boolean",
            "x-go-name": "IsLatestVersion"
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
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
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
      "TargetType": {
        "type": "string",
        "title": "TargetType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TokenizerInfo": {
        "type": "object",
        "properties": {
          "vaultless_tokenizer_info": {
            "$ref": "#/components/schemas/VaultlessTokenizerInfo"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TokenizerTemplateType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TweakType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "UscSyncInfo": {
        "type": "object",
        "properties": {
          "delete_remote": {
            "type": "boolean",
            "x-go-name": "DeleteRemote"
          },
          "jq_secret_filter": {
            "type": "string",
            "x-go-name": "JqSecretFilter"
          },
          "last_error": {
            "type": "string",
            "x-go-name": "LastError"
          },
          "namespace": {
            "type": "string",
            "x-go-name": "Namespace"
          },
          "secret_id": {
            "type": "string",
            "x-go-name": "SecretId"
          },
          "secret_name": {
            "type": "string",
            "x-go-name": "SecretName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "VaultlessTokenizerInfo": {
        "type": "object",
        "properties": {
          "email_tokenizer_info": {
            "$ref": "#/components/schemas/EmailTokenizerInfo"
          },
          "key_name": {
            "type": "string",
            "x-go-name": "EncryptionKeyName"
          },
          "regexp_tokenizer_info": {
            "$ref": "#/components/schemas/RegexpTokenizerInfo"
          },
          "template_type": {
            "$ref": "#/components/schemas/TokenizerTemplateType"
          },
          "tweak": {
            "description": "Tweak used in the case of internal tweak type",
            "type": "string",
            "x-go-name": "Tweak"
          },
          "tweak_type": {
            "$ref": "#/components/schemas/TweakType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WindowsService": {
        "type": "object",
        "title": "WindowsService defines types supported by AKEYLESS.",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/WindowsServiceAttributes"
          },
          "host": {
            "type": "string",
            "x-go-name": "Host"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WindowsServiceAttributes": {
        "type": "object",
        "properties": {
          "connection_type": {
            "type": "string",
            "x-go-name": "ConnectionType"
          },
          "iis_app_pool": {
            "description": "IISAppPool marks this entry as an IIS Application Pool rather than a Windows Service",
            "type": "boolean",
            "x-go-name": "IISAppPool"
          },
          "port": {
            "type": "string",
            "x-go-name": "Port"
          },
          "skip_restart": {
            "description": "SkipRestart allows skipping recycle/start of the IIS App Pool after credential update",
            "type": "boolean",
            "x-go-name": "SkipRestart"
          },
          "use_tls": {
            "type": "boolean",
            "x-go-name": "UseTLS"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "listItems": {
        "type": "object",
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "advanced-filter": {
            "description": "Filter by item name/username/website or part of it",
            "type": "string",
            "x-go-name": "MultiFieldFilter"
          },
          "auto-pagination": {
            "description": "Retrieve all items using pagination, when disabled retrieving only first 1000 items",
            "type": "string",
            "default": "enabled",
            "x-go-name": "AutoPagination"
          },
          "current-folder": {
            "description": "List only items in the current folder (excludes subfolders)",
            "type": "boolean",
            "default": false,
            "x-go-name": "CurrentFolder"
          },
          "filter": {
            "description": "Filter by item name or part of it",
            "type": "string",
            "x-go-name": "Filter"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "minimal-view": {
            "description": "Show only basic information of the items",
            "type": "boolean",
            "x-go-name": "BasicData"
          },
          "modified-after": {
            "description": "List only secrets modified after specified date (in unix time)",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ModifiedAfterDate"
          },
          "pagination-token": {
            "description": "Next page reference",
            "type": "string",
            "x-go-name": "PaginationToken"
          },
          "path": {
            "description": "Path to folder",
            "type": "string",
            "x-go-name": "Path"
          },
          "sra-only": {
            "description": "Filter by items with SRA functionality enabled",
            "type": "boolean",
            "default": false,
            "x-go-name": "SraOnly"
          },
          "sub-types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SubTypesV2"
          },
          "tag": {
            "description": "Filter by item tag",
            "type": "string",
            "x-go-name": "Tag"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "The item types list of the requested items. In case it is empty, all\ntypes of items will be returned. options: [key, static-secret,\ndynamic-secret, classic-key]",
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