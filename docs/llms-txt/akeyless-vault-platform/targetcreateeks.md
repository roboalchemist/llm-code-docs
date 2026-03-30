# Source: https://docs.akeyless.io/reference/targetcreateeks.md

# /target-create-eks

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
    "/target-create-eks": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateEks",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateEks"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateEksResponse"
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
      "targetCreateEksResponse": {
        "description": "targetCreateEksResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/targetCreateOutput"
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
      "targetCreateEks": {
        "type": "object",
        "title": "targetCreateEks is a command that creates a new eks target.",
        "required": [
          "eks-cluster-name",
          "eks-cluster-endpoint",
          "eks-cluster-ca-cert",
          "eks-access-key-id",
          "eks-secret-access-key",
          "name"
        ],
        "properties": {
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "eks-access-key-id": {
            "description": "Access Key ID",
            "type": "string",
            "x-go-name": "AccessId"
          },
          "eks-cluster-ca-cert": {
            "description": "EKS cluster CA certificate",
            "type": "string",
            "x-go-name": "ClusterCACert"
          },
          "eks-cluster-endpoint": {
            "description": "EKS cluster URL endpoint",
            "type": "string",
            "x-go-name": "ClusterEndpoint"
          },
          "eks-cluster-name": {
            "description": "EKS cluster name",
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "eks-region": {
            "description": "Region",
            "type": "string",
            "default": "us-east-2",
            "x-go-name": "Region"
          },
          "eks-secret-access-key": {
            "description": "Secret Access Key",
            "type": "string",
            "x-go-name": "AccessKey"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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
          "use-gw-cloud-identity": {
            "type": "boolean",
            "x-go-name": "UseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "targetCreateOutput": {
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