# Source: https://docs.akeyless.io/reference/kubeconfiggenerate.md

# /kubeconfig-generate

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
    "/kubeconfig-generate": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "KubeconfigGenerate",
        "responses": {
          "200": {
            "$ref": "#/components/responses/kubeconfigGenerateResponse"
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
      "kubeconfigGenerateResponse": {
        "description": "kubeconfigGenerateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/KubeconfigGenerateOutput"
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
      "KubeConfigValue": {
        "type": "object",
        "title": "KubeConfigValue represents the entire Kubeconfig structure.",
        "properties": {
          "apiVersion": {
            "type": "string",
            "x-go-name": "APIVersion"
          },
          "clusters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/KubeconfigNamedCluster"
            },
            "x-go-name": "Clusters"
          },
          "contexts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/KubeconfigNamedContext"
            },
            "x-go-name": "Contexts"
          },
          "current-context": {
            "type": "string",
            "x-go-name": "CurrentContext"
          },
          "kind": {
            "type": "string",
            "x-go-name": "Kind"
          },
          "users": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/KubeconfigUser"
            },
            "x-go-name": "Users"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigCluster": {
        "type": "object",
        "title": "KubeconfigCluster represents the cluster details.",
        "properties": {
          "certificate-authority": {
            "description": "CertificateAuthority is optional and can be omitted if not used.",
            "type": "string",
            "x-go-name": "CertificateAuthority"
          },
          "certificate-authority-data": {
            "type": "string",
            "x-go-name": "CertificateAuthorityData"
          },
          "server": {
            "type": "string",
            "x-go-name": "Server"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigContext": {
        "type": "object",
        "title": "KubeconfigContext represents the context details.",
        "properties": {
          "cluster": {
            "type": "string",
            "x-go-name": "Cluster"
          },
          "namespace": {
            "type": "string",
            "x-go-name": "Namespace"
          },
          "user": {
            "type": "string",
            "x-go-name": "User"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigExec": {
        "type": "object",
        "title": "KubeconfigExec represents the exec command configuration.",
        "properties": {
          "apiVersion": {
            "type": "string",
            "x-go-name": "APIVersion"
          },
          "args": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Args"
          },
          "command": {
            "type": "string",
            "x-go-name": "Command"
          },
          "interactiveMode": {
            "type": "string",
            "x-go-name": "InteractiveMode"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigGenerateOutput": {
        "type": "object",
        "properties": {
          "conflicted_clusters_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ConflictedClustersNames"
          },
          "data": {
            "$ref": "#/components/schemas/KubeConfigValue"
          },
          "errors": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Errors"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "KubeconfigNamedCluster": {
        "type": "object",
        "title": "KubeconfigNamedCluster represents a named cluster in the Kubeconfig.",
        "properties": {
          "cluster": {
            "$ref": "#/components/schemas/KubeconfigCluster"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigNamedContext": {
        "type": "object",
        "title": "KubeconfigNamedContext represents a named context in the Kubeconfig.",
        "properties": {
          "context": {
            "$ref": "#/components/schemas/KubeconfigContext"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigUser": {
        "type": "object",
        "title": "KubeconfigUser represents a user entry in the Kubeconfig.",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "user": {
            "$ref": "#/components/schemas/KubeconfigUserExec"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      },
      "KubeconfigUserExec": {
        "type": "object",
        "title": "KubeconfigUserExec represents the exec configuration for a user.",
        "properties": {
          "exec": {
            "$ref": "#/components/schemas/KubeconfigExec"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/helpers/kubeconfig"
      }
    }
  }
}
```