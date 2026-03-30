# Source: https://docs.akeyless.io/reference/gatewayupdatelogforwardingawss3.md

# /gateway-update-log-forwarding-aws-s3

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
    "/gateway-update-log-forwarding-aws-s3": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateLogForwardingAwsS3",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateLogForwardingAwsS3"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayUpdateLogForwardingResponse"
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
      "gatewayUpdateLogForwardingResponse": {
        "description": "gatewayUpdateLogForwardingResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateLogForwardingOutput"
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
      "gatewayUpdateLogForwardingAwsS3": {
        "description": "gatewayUpdateLogForwardingAwsS3 is a command that updates log forwarding config (aws-s3 target)",
        "type": "object",
        "properties": {
          "access-id": {
            "description": "AWS access id relevant for access_key auth-type",
            "type": "string",
            "x-go-name": "AwsAccessId"
          },
          "access-key": {
            "description": "AWS access key relevant for access_key auth-type",
            "type": "string",
            "x-go-name": "AwsAccessKey"
          },
          "auth-type": {
            "description": "AWS auth type [access_key/cloud_id/assume_role]",
            "type": "string",
            "x-go-name": "AwsAuthType"
          },
          "bucket-name": {
            "description": "AWS S3 bucket name",
            "type": "string",
            "x-go-name": "AwsBucketName"
          },
          "enable": {
            "description": "Enable Log Forwarding [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "Enable"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "log-folder": {
            "description": "AWS S3 destination folder for logs",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "AwsLogFolder"
          },
          "output-format": {
            "description": "Logs format [text/json]",
            "type": "string",
            "default": "text",
            "x-go-name": "OutputFormat"
          },
          "pull-interval": {
            "description": "Pull interval in seconds",
            "type": "string",
            "default": "10",
            "x-go-name": "PullIntervalSec"
          },
          "region": {
            "description": "AWS region",
            "type": "string",
            "x-go-name": "AwsRegion"
          },
          "role-arn": {
            "description": "AWS role arn relevant for assume_role auth-type",
            "type": "string",
            "x-go-name": "AwsRoleARN"
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
      "gatewayUpdateLogForwardingOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```