# Source: https://docs.akeyless.io/reference/gatewayupdateremoteaccessrdprecordings.md

# /gateway-update-remote-access-rdp-recording

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
    "/gateway-update-remote-access-rdp-recording": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateRemoteAccessRdpRecordings",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateRemoteAccessRdpRecordings"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayUpdateRemoteAccessRdpRecordingsResponse"
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
      "gatewayUpdateRemoteAccessRdpRecordingsResponse": {
        "description": "gatewayUpdateRemoteAccessRdpRecordingsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateRemoteAccessRdpRecordingsOutput"
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
      "gatewayUpdateRemoteAccessRdpRecordings": {
        "description": "gatewayUpdateRemoteAccessRdpRecordings is a command that update remote access rdp recording config",
        "type": "object",
        "properties": {
          "aws-storage-access-key-id": {
            "description": "AWS access key id. For more information refer to https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html",
            "type": "string",
            "x-go-name": "AccessKeyId"
          },
          "aws-storage-bucket-name": {
            "description": "The AWS bucket name. For more information refer to https://docs.aws.amazon.com/s3/",
            "type": "string",
            "x-go-name": "BucketName"
          },
          "aws-storage-bucket-prefix": {
            "description": "The folder name in S3 bucket. For more information refer to https://docs.aws.amazon.com/s3/",
            "type": "string",
            "x-go-name": "BucketPrefix"
          },
          "aws-storage-region": {
            "description": "The region where the storage is located",
            "type": "string",
            "x-go-name": "Region"
          },
          "aws-storage-secret-access-key": {
            "description": "AWS secret access key. For more information refer to https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html",
            "type": "string",
            "x-go-name": "SecretAccessKey"
          },
          "azure-storage-account-name": {
            "description": "Azure account name. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview",
            "type": "string",
            "x-go-name": "AccountName"
          },
          "azure-storage-client-id": {
            "description": "Azure client id. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs=portal",
            "type": "string",
            "x-go-name": "ClientId"
          },
          "azure-storage-client-secret": {
            "description": "Azure client secret. For more information refer to https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs=portal",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "azure-storage-container-name": {
            "description": "Azure container name. For more information refer to https://learn.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata",
            "type": "string",
            "x-go-name": "ContainerName"
          },
          "azure-storage-tenant-id": {
            "description": "Azure tenant id. For more information refer to https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant",
            "type": "string",
            "x-go-name": "TenantId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "rdp-session-recording": {
            "description": "Enable recording of rdp session [true/false]",
            "type": "string",
            "x-go-name": "IsEnabled"
          },
          "rdp-session-recording-compress": {
            "description": "Whether to compress recording files before upload",
            "type": "boolean",
            "x-go-name": "RdpSessionRecordingCompress"
          },
          "rdp-session-recording-encryption-key": {
            "description": "If provided, this key will be used to encrypt uploaded recordings.",
            "type": "string",
            "x-go-name": "RdpSessionRecordingEncKey"
          },
          "rdp-session-recording-quality": {
            "description": "RDP session recording quality [low/medium/high]",
            "type": "string",
            "x-go-name": "RdpSessionRecordingQuality"
          },
          "rdp-session-storage": {
            "description": "Rdp session recording storage destination [local/aws/azure]",
            "type": "string",
            "x-go-name": "RdpSessionStorage"
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
      },
      "gatewayUpdateRemoteAccessRdpRecordingsOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```