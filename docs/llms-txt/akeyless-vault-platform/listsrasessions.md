# Source: https://docs.akeyless.io/reference/listsrasessions.md

# /list-sra-sessions

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
    "/list-sra-sessions": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listSRASessions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listSRASessions"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listSRASessionsResponse"
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
      "listSRASessionsResponse": {
        "description": "listSRASessionsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ListSraSessionsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GatewayNameInfo": {
        "type": "object",
        "properties": {
          "cluster_display_name": {
            "type": "string",
            "x-go-name": "ClusterDisplayName"
          },
          "cluster_name": {
            "type": "string",
            "x-go-name": "ClusterName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
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
      "ListSraSessionsOutput": {
        "type": "object",
        "properties": {
          "allowed_gateways": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GatewayNameInfo"
            },
            "x-go-name": "AllowedGateways"
          },
          "next_page": {
            "type": "string",
            "x-go-name": "NextPage"
          },
          "sessions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SraSessionEntryOut"
            },
            "x-go-name": "Sessions"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SraClientType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SraSessionEntryOut": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "client_type": {
            "$ref": "#/components/schemas/SraClientType"
          },
          "cluster_unique_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ClusterUniqueId"
          },
          "connection_type": {
            "type": "string",
            "x-go-name": "ConnectionType"
          },
          "end_time": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "EndTime"
          },
          "error_msg": {
            "type": "string",
            "x-go-name": "ErrorMsg"
          },
          "gateway_info": {
            "$ref": "#/components/schemas/GatewayNameInfo"
          },
          "instance_id": {
            "type": "string",
            "x-go-name": "InstanceId"
          },
          "secret_name": {
            "type": "string",
            "x-go-name": "SecretName"
          },
          "session_id": {
            "type": "string",
            "x-go-name": "SessionId"
          },
          "start_time": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "StartTime"
          },
          "status": {
            "$ref": "#/components/schemas/SraSessionStatus"
          },
          "target_host": {
            "type": "string",
            "x-go-name": "TargetHost"
          },
          "ttl": {
            "type": "string",
            "x-go-name": "Ttl"
          },
          "user_identifier": {
            "type": "string",
            "x-go-name": "UserIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SraSessionStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "listSRASessions": {
        "description": "listSRASessions is a command that returns sra sessions of the given user",
        "type": "object",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "resource-type": {
            "description": "session resource type. In case it is empty, all resources type will be returned. options: [mysql, k8s, ssh, mongodb, mssql, postgres, aws, eks, gke, rdp]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ResourceType"
          },
          "status-type": {
            "description": "session status type. In case it is empty, only active sessions will be returned. options: [connecting, connected, failed, completed, terminated]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "StatusType"
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