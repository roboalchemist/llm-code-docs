# Source: https://docs.akeyless.io/reference/gatewaygetk8sauthconfig.md

# /gateway-get-k8s-auth-config

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
    "/gateway-get-k8s-auth-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetK8SAuthConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetK8SAuthConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayGetK8SAuthConfigResponse"
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
      "gatewayGetK8SAuthConfigResponse": {
        "description": "gatewayGetK8SAuthConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewayGetK8SAuthConfigOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ClusterApiType": {
        "description": "ClusterApiType defines types of API access to cluster",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "GatewayGetK8SAuthConfigOutput": {
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
          "protection_key": {
            "type": "string",
            "x-go-name": "ProtectionKey"
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
      "NativeK8sAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "gatewayGetK8SAuthConfig": {
        "description": "gatewayGetK8SAuth is a command that gets k8s auth config",
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
      }
    }
  }
}
```