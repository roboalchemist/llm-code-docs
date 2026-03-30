# Source: https://docs.akeyless.io/reference/targetcreatesplunk.md

# /target-create-splunk

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
    "/target-create-splunk": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateSplunk",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateSplunk"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateSplunkResponse"
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
      "targetCreateSplunkResponse": {
        "description": "targetCreateSplunkResponse wraps response body.",
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
      },
      "targetCreateSplunk": {
        "description": "targetCreateSplunk is a command that creates a new splunk target",
        "type": "object",
        "title": "Splunk",
        "required": [
          "name",
          "url"
        ],
        "properties": {
          "audience": {
            "description": "Splunk token audience (required when using token authentication for rotation)",
            "type": "string",
            "x-go-name": "Audience"
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
          "password": {
            "description": "Splunk Password (used when authenticating with username/password)",
            "type": "string",
            "x-go-name": "Password"
          },
          "token": {
            "description": "Splunk Token (used when authenticating with token)",
            "type": "string",
            "x-go-name": "Token"
          },
          "token-owner": {
            "description": "Splunk Token Owner (required when using token authentication for rotation)",
            "type": "string",
            "x-go-name": "TokenOwner"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "url": {
            "description": "Splunk server URL",
            "type": "string",
            "x-go-name": "SplunkURL"
          },
          "use-tls": {
            "description": "Use TLS certificate verification when connecting to the Splunk management API",
            "type": "boolean",
            "default": true,
            "x-go-name": "UseTLS"
          },
          "username": {
            "description": "Splunk Username (used when authenticating with username/password)",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```