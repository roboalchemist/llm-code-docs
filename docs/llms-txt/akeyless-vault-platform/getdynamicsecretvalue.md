# Source: https://docs.akeyless.io/reference/getdynamicsecretvalue.md

# /get-dynamic-secret-value

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
    "/get-dynamic-secret-value": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getDynamicSecretValue",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getDynamicSecretValue"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getDynamicSecretValueResponse"
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
      "getDynamicSecretValueResponse": {
        "description": "getDynamicSecretValueResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": {}
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
      "getDynamicSecretValue": {
        "type": "object",
        "title": "getDynamicSecretValue is a command that gets dynamic secret value.",
        "required": [
          "name"
        ],
        "properties": {
          "args": {
            "description": "Optional arguments as key=value pairs or JSON strings, e.g -\n\\\"--args=csr=base64_encoded_csr --args=common_name=bar\\\" or\nargs='{\\\"csr\\\":\\\"base64_encoded_csr\\\"}. It is possible to combine both\nformats.'",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Arguments"
          },
          "dbname": {
            "description": "DBName: Optional override DB name (works only if DS allows it. only relevant for MSSQL)",
            "type": "string",
            "x-go-name": "DBName"
          },
          "host": {
            "description": "Host",
            "type": "string",
            "x-go-name": "Host"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Dynamic secret name",
            "type": "string",
            "x-go-name": "DynamicSecretName"
          },
          "target": {
            "description": "Target Name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "timeout": {
            "description": "Timeout in seconds",
            "type": "integer",
            "format": "int64",
            "default": 15,
            "x-go-name": "TimeoutSec"
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