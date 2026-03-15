# Source: https://docs.akeyless.io/reference/describepermissions.md

# /describe-permissions

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
    "/describe-permissions": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "describePermissions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/describePermissions"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/DescribePermissionsResponse"
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
      "DescribePermissionsResponse": {
        "description": "DescribePermissionsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/DescribePermissionsOutput"
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
      "ClientPermissions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DescribePermissionsOutput": {
        "type": "object",
        "title": "DescribePermissionsOutput defines output of DescribePermissionsOutput operation.",
        "properties": {
          "client_permissions": {
            "$ref": "#/components/schemas/ClientPermissions"
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
      "describePermissions": {
        "description": "describePermissions is a command that shows which permissions your have to a\nparticular path.",
        "type": "object",
        "required": [
          "path",
          "type"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "path": {
            "description": "Path to an object",
            "type": "string",
            "x-go-name": "Path"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Type of object (item, am, role, target)",
            "type": "string",
            "x-go-name": "Type"
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