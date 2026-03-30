# Source: https://docs.akeyless.io/reference/updatenativek8starget.md

# /update-k8s-target

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
    "/update-k8s-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateNativeK8STarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateNativeK8STarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateNativeK8STargetResponse"
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
      "updateNativeK8STargetResponse": {
        "description": "updateNativeK8STargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateNativeK8STargetOutput"
            }
          }
        }
      }
    },
    "schemas": {
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
      "updateNativeK8STarget": {
        "description": "updateNativeK8STarget is a command that updates an existing target. [Deprecated: Use target-update-k8s command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "k8s-auth-type": {
            "description": "K8S auth type [token/certificate]",
            "type": "string",
            "default": "token",
            "x-go-name": "K8sAuthType"
          },
          "k8s-client-certificate": {
            "description": "Content of the k8 client certificate (PEM format) in a Base64 format",
            "type": "string",
            "x-go-name": "K8sClientCertificate"
          },
          "k8s-client-key": {
            "description": "Content of the k8 client private key (PEM format) in a Base64 format",
            "type": "string",
            "x-go-name": "K8sClientKey"
          },
          "k8s-cluster-ca-cert": {
            "description": "K8S cluster CA certificate",
            "type": "string",
            "x-go-name": "ClusterCACert"
          },
          "k8s-cluster-endpoint": {
            "description": "K8S cluster URL endpoint",
            "type": "string",
            "x-go-name": "ClusterEndpoint"
          },
          "k8s-cluster-name": {
            "description": "K8S cluster name",
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "k8s-cluster-token": {
            "description": "K8S cluster Bearer token",
            "type": "string",
            "x-go-name": "ClusterBearerToken"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "key": {
            "description": "The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "new-name": {
            "description": "New target name",
            "type": "string",
            "x-go-name": "NewTargetName"
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
          "update-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "CreateNewVersion"
          },
          "use-gw-service-account": {
            "description": "Use the GW's service account",
            "type": "boolean",
            "x-go-name": "UseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateNativeK8STargetOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```