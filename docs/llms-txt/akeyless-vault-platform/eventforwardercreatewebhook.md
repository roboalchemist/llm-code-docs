# Source: https://docs.akeyless.io/reference/eventforwardercreatewebhook.md

# /event-forwarder-create-webhook

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
    "/event-forwarder-create-webhook": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "eventForwarderCreateWebhook",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eventForwarderCreateWebhook"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/eventForwarderCreateWebhookResponse"
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
      "eventForwarderCreateWebhookResponse": {
        "description": "eventForwarderCreateWebhookResponse wraps response body.",
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
      "NotiForwarderRunnerType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "eventForwarderCreateWebhook": {
        "description": "eventForwarderCreateWebhook is a command that creates webhook event forwarder",
        "type": "object",
        "required": [
          "gateways-event-source-locations",
          "runner-type",
          "name"
        ],
        "properties": {
          "auth-methods-event-source-locations": {
            "description": "Auth Method Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuthMethodsEventSources"
          },
          "auth-token": {
            "description": "Base64 encoded Token string for authentication type Token",
            "type": "string",
            "x-go-name": "AuthToken"
          },
          "auth-type": {
            "description": "The Webhook authentication type [user-pass, bearer-token, certificate]",
            "type": "string",
            "default": "user-pass",
            "x-go-name": "AuthType"
          },
          "client-cert-data": {
            "description": "Base64 encoded PEM certificate, relevant for certificate auth-type",
            "type": "string",
            "x-go-name": "ClientCertDataBase64"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "event-types": {
            "description": "List of event types to notify about [request-access, certificate-pending-expiration, certificate-expired, certificate-provisioning-success, certificate-provisioning-failure, auth-method-pending-expiration, auth-method-expired, next-automatic-rotation, rotated-secret-success, rotated-secret-failure, dynamic-secret-failure, multi-auth-failure, uid-rotation-failure, apply-justification, email-auth-method-approved, usage, rotation-usage, gateway-inactive, static-secret-updated, rate-limiting, usage-report, secret-sync]",
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
          "gateways-event-source-locations": {
            "description": "Event sources",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GatewayEventSources"
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
          "password": {
            "description": "Password for authentication relevant for user-pass auth-type",
            "type": "string",
            "x-go-name": "Password"
          },
          "private-key-data": {
            "description": "Base64 encoded PEM RSA Private Key, relevant for certificate auth-type",
            "type": "string",
            "x-go-name": "PrivateKeyBase64"
          },
          "runner-type": {
            "$ref": "#/components/schemas/NotiForwarderRunnerType"
          },
          "server-certificates": {
            "description": "Base64 encoded PEM certificate of the Webhook",
            "type": "string",
            "x-go-name": "ServerCertificateBase64"
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
          "url": {
            "description": "Webhook URL",
            "type": "string",
            "x-go-name": "EndpointURL"
          },
          "username": {
            "description": "Username for authentication relevant for user-pass auth-type",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```