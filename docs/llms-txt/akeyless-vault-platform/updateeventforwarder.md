# Source: https://docs.akeyless.io/reference/updateeventforwarder.md

# /update-event-forwarder

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
    "/update-event-forwarder": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateEventForwarder",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateEventForwarder"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateEventForwarderResponse"
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
      "updateEventForwarderResponse": {
        "description": "updateEventForwarderResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateEventForwarderOutput"
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
      "updateEventForwarder": {
        "description": "updateEventForwarder is a command that updates an event forwarder [Deprecated - please use event-forwarder-update-* command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "admin-name": {
            "description": "Workstation Admin Name",
            "type": "string",
            "x-go-name": "AdminName"
          },
          "auth-type": {
            "description": "The authentication type to use when connecting to ServiceNow (user-pass / jwt)",
            "type": "string",
            "default": "user-pass",
            "x-go-name": "AuthType"
          },
          "client-id": {
            "description": "The client ID to use when connecting to ServiceNow with jwt authentication",
            "type": "string",
            "x-go-name": "ClientID"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "default": "default_comment",
            "x-go-name": "Description"
          },
          "email-to": {
            "description": "A comma seperated list of email addresses to send event to (relevant only for \"email\" Event Forwarder)",
            "type": "string",
            "x-go-name": "EmailTo"
          },
          "enable": {
            "description": "Enable/Disable Event Forwarder [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "Enable"
          },
          "event-source-locations": {
            "description": "Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventSources"
          },
          "event-types": {
            "description": "Event types",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventTypes"
          },
          "host": {
            "description": "Workstation Host",
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
            "description": "EventForwarder name",
            "type": "string",
            "x-go-name": "EventForwarderName"
          },
          "new-comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "default": "default_comment",
            "x-go-name": "NewComment"
          },
          "new-name": {
            "description": "New EventForwarder name",
            "type": "string",
            "x-go-name": "NewName"
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
          "user-email": {
            "description": "The user email to use when connecting to ServiceNow with jwt authentication",
            "type": "string",
            "x-go-name": "UserEmail"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateEventForwarderOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```