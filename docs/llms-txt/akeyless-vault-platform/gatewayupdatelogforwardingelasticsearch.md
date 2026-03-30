# Source: https://docs.akeyless.io/reference/gatewayupdatelogforwardingelasticsearch.md

# /gateway-update-log-forwarding-elasticsearch

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
    "/gateway-update-log-forwarding-elasticsearch": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateLogForwardingElasticsearch",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateLogForwardingElasticsearch"
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
      "gatewayUpdateLogForwardingElasticsearch": {
        "description": "gatewayUpdateLogForwardingElasticsearch is a command that updates log forwarding config (elasticsearch target)",
        "type": "object",
        "properties": {
          "api-key": {
            "description": "Elasticsearch api key relevant only for api_key auth-type",
            "type": "string",
            "x-go-name": "ElasticsearchApiKey"
          },
          "auth-type": {
            "description": "Elasticsearch auth type [api_key/password]",
            "type": "string",
            "x-go-name": "ElasticsearchAuthType"
          },
          "cloud-id": {
            "description": "Elasticsearch cloud id relevant only for cloud server-type",
            "type": "string",
            "x-go-name": "ElasticsearchCloudId"
          },
          "enable": {
            "description": "Enable Log Forwarding [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "Enable"
          },
          "enable-tls": {
            "description": "Enable tls",
            "type": "boolean",
            "x-go-name": "ElasticsearchEnableTLS"
          },
          "index": {
            "description": "Elasticsearch index",
            "type": "string",
            "x-go-name": "ElasticsearchIndex"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "nodes": {
            "description": "Elasticsearch nodes relevant only for nodes server-type",
            "type": "string",
            "x-go-name": "ElasticsearchNodes"
          },
          "output-format": {
            "description": "Logs format [text/json]",
            "type": "string",
            "default": "text",
            "x-go-name": "OutputFormat"
          },
          "password": {
            "description": "Elasticsearch password relevant only for password auth-type",
            "type": "string",
            "x-go-name": "ElasticsearchPassword"
          },
          "pull-interval": {
            "description": "Pull interval in seconds",
            "type": "string",
            "default": "10",
            "x-go-name": "PullIntervalSec"
          },
          "server-type": {
            "description": "Elasticsearch server type [cloud/nodes]",
            "type": "string",
            "x-go-name": "ElasticsearchServerType"
          },
          "tls-certificate": {
            "description": "Elasticsearch tls certificate",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "ElasticsearchTlsCertificate"
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
          "user-name": {
            "description": "Elasticsearch user name relevant only for password auth-type",
            "type": "string",
            "x-go-name": "ElasticsearchUserName"
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