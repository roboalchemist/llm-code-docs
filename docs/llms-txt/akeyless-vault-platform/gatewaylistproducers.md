# Source: https://docs.akeyless.io/reference/gatewaylistproducers.md

# /gateway-list-producers

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
    "/gateway-list-producers": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayListProducers",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayListProducers"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayListProducersResponse"
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
      "gatewayListProducersResponse": {
        "description": "gatewayListProducersResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetProducersListReplyObj"
            }
          }
        }
      }
    },
    "schemas": {
      "GetProducersListReplyObj": {
        "type": "object",
        "properties": {
          "producers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Producer"
            },
            "x-go-name": "Producers"
          },
          "producers_errors": {
            "x-go-name": "ProducersErrors"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "Producer": {
        "type": "object",
        "properties": {
          "active": {
            "type": "boolean",
            "x-go-name": "Active"
          },
          "failure_message": {
            "type": "string",
            "x-go-name": "FailureMessage"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Id"
          },
          "init": {
            "type": "boolean",
            "x-go-name": "Init"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "gatewayListProducers": {
        "description": "gatewayListProducers is a command that returns a list of producers [Deprecated: Use dynamic-secret-list command]",
        "type": "object",
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
      }
    }
  }
}
```