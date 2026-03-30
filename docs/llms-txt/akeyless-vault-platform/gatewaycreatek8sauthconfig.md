# Source: https://docs.akeyless.io/reference/gatewaycreatek8sauthconfig.md

# /gateway-create-k8s-auth-config

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
    "/gateway-create-k8s-auth-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayCreateK8SAuthConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayCreateK8SAuthConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayCreateK8SAuthConfigResponse"
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
      "gatewayCreateK8SAuthConfigResponse": {
        "description": "gatewayCreateK8SAuthConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayCreateK8SAuthConfigOutput"
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
      "gatewayCreateK8SAuthConfig": {
        "description": "gatewayCreateK8SAuth is a command that creates k8s auth config",
        "type": "object",
        "required": [
          "name",
          "access-id",
          "signing-key",
          "k8s-host"
        ],
        "properties": {
          "access-id": {
            "description": "The access ID of the Kubernetes auth method",
            "type": "string",
            "x-go-name": "AuthMethodAccessId"
          },
          "cluster-api-type": {
            "description": "Cluster access type. options: [native_k8s, rancher]",
            "type": "string",
            "default": "native_k8s",
            "x-go-name": "ClusterApiType"
          },
          "disable-issuer-validation": {
            "description": "Disable issuer validation [true/false]",
            "type": "string",
            "x-go-name": "DisableISSValidation"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "k8s-auth-type": {
            "description": "K8S auth type [token/certificate]. (relevant for \"native_k8s\" only)",
            "type": "string",
            "default": "token",
            "x-go-name": "K8sAuthType"
          },
          "k8s-ca-cert": {
            "description": "The CA Certificate (base64 encoded) to use to call into the kubernetes API server",
            "type": "string",
            "x-go-name": "K8SCACert"
          },
          "k8s-client-certificate": {
            "description": "Content of the k8 client certificate (PEM format) in a Base64 format (relevant for \"native_k8s\" only)",
            "type": "string",
            "x-go-name": "K8sClientCertificate"
          },
          "k8s-client-key": {
            "description": "Content of the k8 client private key (PEM format) in a Base64 format (relevant for \"native_k8s\" only)",
            "type": "string",
            "x-go-name": "K8sClientKey"
          },
          "k8s-host": {
            "description": "The URL of the kubernetes API server",
            "type": "string",
            "x-go-name": "K8SHost"
          },
          "k8s-issuer": {
            "description": "The Kubernetes JWT issuer name. K8SIssuer is the claim that specifies who issued the Kubernetes token",
            "type": "string",
            "default": "kubernetes/serviceaccount",
            "x-go-name": "K8SIssuer"
          },
          "name": {
            "description": "K8S Auth config name",
            "type": "string",
            "x-go-name": "K8SAuthConfigName"
          },
          "rancher-api-key": {
            "description": "The api key used to access the TokenReview API to validate other JWTs (relevant for \"rancher\" only)",
            "type": "string",
            "x-go-name": "RancherApiKey"
          },
          "rancher-cluster-id": {
            "description": "The cluster id as define in rancher (relevant for \"rancher\" only)",
            "type": "string",
            "x-go-name": "RancherClusterId"
          },
          "signing-key": {
            "description": "The private key (base64 encoded) associated with the public key defined in the Kubernetes auth",
            "type": "string",
            "x-go-name": "AuthMethodSigningKey"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "token-exp": {
            "description": "Time in seconds of expiration of the Akeyless Kube Auth Method token",
            "type": "integer",
            "format": "int64",
            "default": 300,
            "x-go-name": "AuthMethodTokenExpiration"
          },
          "token-reviewer-jwt": {
            "description": "A Kubernetes service account JWT used to access the TokenReview API to validate other JWTs (relevant for \"native_k8s\" only).\nIf not set, the JWT submitted in the authentication process will be used to access the Kubernetes TokenReview API.",
            "type": "string",
            "x-go-name": "K8STokenReviewerJWT"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "use-gw-service-account": {
            "description": "Use the GW's service account",
            "type": "boolean",
            "x-go-name": "UseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "gatewayCreateK8SAuthConfigOutput": {
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