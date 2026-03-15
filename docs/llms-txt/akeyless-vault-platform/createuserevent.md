# Source: https://docs.akeyless.io/reference/createuserevent.md

# /create-user-event

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
    "/create-user-event": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createUserEvent",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createUserEvent"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createUserEventResponse"
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
      "createUserEventResponse": {
        "description": "createUserEventResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createUserEventOutput"
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
      "EventSource": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EventType": {
        "type": "string",
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
      "createUserEvent": {
        "type": "object",
        "title": "createUserEvent is a command that creates user event.",
        "required": [
          "item-name",
          "item-type",
          "event-type"
        ],
        "properties": {
          "capabilities": {
            "description": "List of the required capabilities options: [read, update, delete,sra_transparently_connect].\nRelevant only for request-access event types",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Capabilities"
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
          "event-source": {
            "$ref": "#/components/schemas/EventSource"
          },
          "event-type": {
            "$ref": "#/components/schemas/EventType"
          },
          "item-name": {
            "description": "EventItemName Event item name",
            "type": "string",
            "x-go-name": "EventItemName"
          },
          "item-type": {
            "description": "EventItemType Event item type",
            "type": "string",
            "x-go-name": "EventItemType"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "request-access-ttl": {
            "description": "For how long to grant the requested access, in minutes",
            "type": "integer",
            "format": "int64",
            "x-go-name": "RequestAccessTtlMin"
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
      "createUserEventOutput": {
        "type": "object",
        "properties": {
          "response": {
            "type": "string",
            "x-go-name": "Response"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```