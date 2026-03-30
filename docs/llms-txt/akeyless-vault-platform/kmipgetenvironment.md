# Source: https://docs.akeyless.io/reference/kmipgetenvironment.md

# /kmip-get-environment

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
    "/kmip-get-environment": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "kmipDescribeServer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/kmipDescribeServer"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/kmipDescribeServerResponse"
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
      "kmipDescribeServerResponse": {
        "description": "kmipDescribeServerResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/kmipDescribeServerOutput"
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
      "kmipDescribeServer": {
        "type": "object",
        "title": "kmipDescribeServer is a command that shows KMIP environment details.",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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
      "kmipDescribeServerOutput": {
        "type": "object",
        "properties": {
          "active": {
            "type": "boolean",
            "x-go-name": "Active"
          },
          "ca_cert": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "CACert"
          },
          "certificate_issue_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CertificateIssueDate"
          },
          "certificate_ttl_in_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateTTLInSeconds"
          },
          "hostname": {
            "type": "string",
            "x-go-name": "Hostname"
          },
          "root": {
            "type": "string",
            "x-go-name": "Root"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```