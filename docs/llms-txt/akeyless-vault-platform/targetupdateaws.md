# Source: https://docs.akeyless.io/reference/targetupdateaws.md

# /target-update-aws

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
    "/target-update-aws": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetUpdateAws",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetUpdateAws"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetUpdateAwsResponse"
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
      "targetUpdateAwsResponse": {
        "description": "targetUpdateAwsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/targetUpdateOutput"
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
      "targetUpdateAws": {
        "type": "object",
        "title": "targetUpdateAws is a command that updates an existing aws target.",
        "required": [
          "access-key-id",
          "access-key",
          "name"
        ],
        "properties": {
          "access-key": {
            "description": "AWS secret access key",
            "type": "string",
            "x-go-name": "AWSSecretAccessKey"
          },
          "access-key-id": {
            "description": "AWS access key ID",
            "type": "string",
            "x-go-name": "AWSAccessKeyID"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "generate-external-id": {
            "description": "A unique auto-generated value used in your AWS account when configuring your AWS IAM role to securely delegate access to Akeyless. Relevant only when using GW cloud ID",
            "type": "boolean",
            "x-go-name": "AWSEnableExternalId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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
          "region": {
            "description": "AWS region",
            "type": "string",
            "default": "us-east-2",
            "x-go-name": "AWSRegion"
          },
          "role-arn": {
            "description": "AWS IAM role identifier that Gateway will assume in your AWS account, relevant only when using external ID",
            "type": "string",
            "x-go-name": "AWSRoleARN"
          },
          "session-token": {
            "description": "Required only for temporary security credentials retrieved using STS",
            "type": "string",
            "x-go-name": "AWSSessionToken"
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
            "description": "Use the GW's Cloud IAM",
            "type": "boolean",
            "x-go-name": "AWSUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "targetUpdateOutput": {
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