# Source: https://docs.akeyless.io/reference/eventforwarderupdateservicenow.md

# /event-forwarder-update-servicenow

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
    "/event-forwarder-update-servicenow": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "eventForwarderUpdateServiceNow",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eventForwarderUpdateServiceNow"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/eventForwarderUpdateServiceNowResponse"
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
      "eventForwarderUpdateServiceNowResponse": {
        "description": "eventForwarderUpdateServiceNowResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/eventForwarderCreateUpdateOutput"
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
      "eventForwarderCreateUpdateOutput": {
        "type": "object",
        "properties": {
          "event_forwarder_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "EventForwarderID"
          },
          "event_forwarder_name": {
            "type": "string",
            "x-go-name": "EventForwarderName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "eventForwarderUpdateServiceNow": {
        "description": "eventForwarderUpdateServiceNow is a command that updates service now event forwarder",
        "type": "object",
        "required": [
          "gateways-event-source-locations",
          "name"
        ],
        "properties": {
          "admin-name": {
            "description": "Workstation Admin Name",
            "type": "string",
            "x-go-name": "AdminName"
          },
          "admin-pwd": {
            "description": "Workstation Admin Password",
            "type": "string",
            "x-go-name": "AdminPwd"
          },
          "app-private-key-base64": {
            "description": "The RSA Private Key to use when connecting with jwt authentication",
            "type": "string",
            "x-go-name": "AppPrivateKeyBase64"
          },
          "auth-methods-event-source-locations": {
            "description": "Auth Method Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuthMethodsEventSources"
          },
          "auth-type": {
            "description": "The authentication type to use [user-pass/jwt]",
            "type": "string",
            "default": "user-pass",
            "x-go-name": "AuthType"
          },
          "client-id": {
            "description": "The client ID to use when connecting with jwt authentication",
            "type": "string",
            "x-go-name": "ClientID"
          },
          "client-secret": {
            "description": "The client secret to use when connecting with jwt authentication",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "enable": {
            "description": "Enable/Disable Event Forwarder [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "Enable"
          },
          "event-types": {
            "description": "List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, next-automatic-rotation, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated, rate-limiting, usage-report, secret-sync]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventTypes"
          },
          "gateways-event-source-locations": {
            "description": "Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GatewayEventSources"
          },
          "host": {
            "description": "Workstation Host",
            "type": "string",
            "x-go-name": "Host"
          },
          "items-event-source-locations": {
            "description": "Items Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ItemsEventSources"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
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
          "new-name": {
            "description": "New EventForwarder name",
            "type": "string",
            "x-go-name": "NewName"
          },
          "targets-event-source-locations": {
            "description": "Targets Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TargetsEventSources"
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
            "description": "The user email to identify with when connecting with jwt authentication",
            "type": "string",
            "x-go-name": "UserEmail"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```