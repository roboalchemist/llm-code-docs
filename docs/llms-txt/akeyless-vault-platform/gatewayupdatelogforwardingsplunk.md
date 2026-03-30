# Source: https://docs.akeyless.io/reference/gatewayupdatelogforwardingsplunk.md

# /gateway-update-log-forwarding-splunk

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
    "/gateway-update-log-forwarding-splunk": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateLogForwardingSplunk",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateLogForwardingSplunk"
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
      "gatewayUpdateLogForwardingOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "gatewayUpdateLogForwardingSplunk": {
        "description": "gatewayUpdateLogForwardingSplunk is a command that updates log forwarding config (splunk target)",
        "type": "object",
        "properties": {
          "enable": {
            "description": "Enable Log Forwarding [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "Enable"
          },
          "enable-batch": {
            "description": "Enable batch forwarding [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "EnableBatch"
          },
          "enable-tls": {
            "description": "Enable tls",
            "type": "boolean",
            "x-go-name": "SplunkEnableTLS"
          },
          "index": {
            "description": "Splunk index",
            "type": "string",
            "x-go-name": "SplunkIndex"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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
          "source": {
            "description": "Splunk source",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "SplunkSource"
          },
          "source-type": {
            "description": "Splunk source type",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "SplunkSourceType"
          },
          "splunk-token": {
            "description": "Splunk token",
            "type": "string",
            "x-go-name": "SplunkToken"
          },
          "splunk-url": {
            "description": "Splunk server URL",
            "type": "string",
            "x-go-name": "SplunkUrl"
          },
          "tls-certificate": {
            "description": "Splunk tls certificate",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "SplunkTlsCertificate"
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