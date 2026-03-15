# Source: https://docs.akeyless.io/reference/deletegatewayallowedaccessid.md

# /gateway-delete-allowed-management-access

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
    "/gateway-delete-allowed-management-access": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "deleteGatewayAllowedAccessId",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/deleteGatewayAllowedAccessId"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/deleteGatewayAllowedAccessIdResponse"
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
      "deleteGatewayAllowedAccessIdResponse": {
        "description": "deleteGatewayAllowedAccessIdResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/deleteGatewayAllowedAccessIdOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
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
      "deleteGatewayAllowedAccessId": {
        "description": "deleteGatewayAllowedAccessId is a command that deletes access-id",
        "type": "object",
        "required": [
          "cluster-name",
          "access-id"
        ],
        "properties": {
          "access-id": {
            "description": "The access id to be stripped of access to gateway",
            "type": "string",
            "x-go-name": "AccessId"
          },
          "cluster-name": {
            "description": "The name of the updated cluster, e.g. acc-abcd12345678/p-123456789012/defaultCluster",
            "type": "string",
            "x-go-name": "ClusterName"
          },
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
      "deleteGatewayAllowedAccessIdOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```