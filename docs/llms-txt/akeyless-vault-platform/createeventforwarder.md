# Source: https://docs.akeyless.io/reference/createeventforwarder.md

# /create-event-forwarder

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
    "/create-event-forwarder": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createEventForwarder",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createEventForwarder"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createEventForwarderResponse"
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
      "createEventForwarderResponse": {
        "description": "createEventForwarderResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createEventForwarderOutput"
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
      "NotiForwarderRunnerType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NotiForwarderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "createEventForwarder": {
        "description": "createEventForwarder is a command that creates a new event forwarder [Deprecated - please use event-forwarder-create-* command]",
        "type": "object",
        "required": [
          "name",
          "forwarder-type",
          "runner-type",
          "event-source-locations"
        ],
        "properties": {
          "admin-name": {
            "description": "Workstation Admin Name",
            "type": "string",
            "x-go-name": "AdminName"
          },
          "admin-pwd": {
            "description": "Workstation Admin password",
            "type": "string",
            "x-go-name": "AdminPwd"
          },
          "app-private-key-base64": {
            "description": "The RSA Private Key PEM formatted in base64 to use when connecting to ServiceNow with jwt authentication",
            "type": "string",
            "x-go-name": "AppPrivateKeyBase64"
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
          "client-secret": {
            "description": "The client secret to use when connecting to ServiceNow with jwt authentication",
            "type": "string",
            "x-go-name": "ClientSecret"
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
          "email-to": {
            "description": "A comma seperated list of email addresses to send event to (relevant only for \"email\" Event Forwarder)",
            "type": "string",
            "x-go-name": "EmailTo"
          },
          "event-source-locations": {
            "description": "Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventSources"
          },
          "event-source-type": {
            "description": "Event Source type [item, target, auth_method, gateway]",
            "type": "string",
            "default": "item",
            "x-go-name": "EventSourceType"
          },
          "event-types": {
            "description": "List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventTypes"
          },
          "every": {
            "description": "Rate of periodic runner repetition in hours",
            "type": "string",
            "x-go-name": "RunEvery"
          },
          "forwarder-type": {
            "$ref": "#/components/schemas/NotiForwarderType"
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
          "key": {
            "description": "The name of a key that used to encrypt the EventForwarder secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "name": {
            "description": "EventForwarder name",
            "type": "string",
            "x-go-name": "EventForwarderName"
          },
          "runner-type": {
            "$ref": "#/components/schemas/NotiForwarderRunnerType"
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
      "createEventForwarderOutput": {
        "type": "object",
        "properties": {
          "event_forwarder_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "EventForwarderID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```