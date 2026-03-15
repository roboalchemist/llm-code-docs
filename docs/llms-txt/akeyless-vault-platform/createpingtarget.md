# Source: https://docs.akeyless.io/reference/createpingtarget.md

# /create-ping-target

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
    "/create-ping-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createPingTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createPingTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createPingTargetResponse"
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
      "createPingTargetResponse": {
        "description": "createPingTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createPingTargetOutput"
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
      "createPingTarget": {
        "description": "createPingTarget is a command that creates a new target. [Deprecated: Use target-create-ping command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "administrative-port": {
            "description": "Ping Federate administrative port",
            "type": "string",
            "default": "9999",
            "x-go-name": "AdministrativePort"
          },
          "authorization-port": {
            "description": "Ping Federate authorization port",
            "type": "string",
            "default": "9031",
            "x-go-name": "AuthorizationPort"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
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
            "description": "Ping Federate privileged user password",
            "type": "string",
            "x-go-name": "UserPassword"
          },
          "ping-url": {
            "description": "Ping URL",
            "type": "string",
            "x-go-name": "PingURL"
          },
          "privileged-user": {
            "description": "Ping Federate privileged user",
            "type": "string",
            "x-go-name": "PrivilegedUser"
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
      "createPingTargetOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```