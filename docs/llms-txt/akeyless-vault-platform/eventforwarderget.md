# Source: https://docs.akeyless.io/reference/eventforwarderget.md

# /event-forwarder-get

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
    "/event-forwarder-get": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "eventForwarderGet",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eventForwarderGet"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/eventForwarderGetResponse"
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
      "eventForwarderGetResponse": {
        "description": "eventForwarderGetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/eventForwarderGetOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "CertificateStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateVersionInfo": {
        "type": "object",
        "properties": {
          "not_after": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotAfter"
          },
          "not_before": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotBefore"
          },
          "status": {
            "$ref": "#/components/schemas/CertificateStatus"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EmailEntry": {
        "type": "object",
        "properties": {
          "to_email": {
            "type": "string",
            "x-go-name": "ToEmail"
          },
          "to_name": {
            "type": "string",
            "x-go-name": "ToName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EventType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemState": {
        "description": "ItemState defines the different states an Item can be in",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemVersion": {
        "type": "object",
        "title": "ItemVersion describes an item version in AKEYLESS.",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "certificate_version_info": {
            "$ref": "#/components/schemas/CertificateVersionInfo"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "customer_fragment_id": {
            "type": "string",
            "x-go-name": "CustomerFragmentId"
          },
          "deletion_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "DeletionDate"
          },
          "item_version_state": {
            "$ref": "#/components/schemas/ItemState"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "unique_identifier": {
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          },
          "version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
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
      "NotiForwarder": {
        "type": "object",
        "properties": {
          "auth_type": {
            "$ref": "#/components/schemas/ServiceNowAuthType"
          },
          "client_id": {
            "description": "Auth - JWT",
            "type": "string",
            "x-go-name": "ClientID"
          },
          "client_permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ClientPermissions"
          },
          "comment": {
            "type": "string",
            "x-go-name": "Comment"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "endpoint": {
            "type": "string",
            "x-go-name": "Endpoint"
          },
          "event_types": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EventType"
            },
            "x-go-name": "NotificationTypes"
          },
          "gateway_cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GatewayClusterId"
          },
          "include_error": {
            "type": "boolean",
            "x-go-name": "IncludeError"
          },
          "is_enabled": {
            "type": "boolean",
            "x-go-name": "IsEnabled"
          },
          "last_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "LastVersion"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "noti_forwarder_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NotiForwarderID"
          },
          "noti_forwarder_name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "noti_forwarder_type": {
            "$ref": "#/components/schemas/NotiForwarderType"
          },
          "noti_forwarder_versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemVersion"
            },
            "x-go-name": "NotiForwarderVersions"
          },
          "override_url": {
            "type": "string",
            "x-go-name": "OverrideURL"
          },
          "paths": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Paths"
          },
          "protection_key": {
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "runner_type": {
            "$ref": "#/components/schemas/NotiForwarderRunnerType"
          },
          "slack_noti_forwarder_public_details": {
            "$ref": "#/components/schemas/SlackNotiForwarderPublicDetails"
          },
          "teams_noti_forwarder_public_details": {
            "$ref": "#/components/schemas/TeamsNotiForwarderPublicDetails"
          },
          "timespan_in_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TimespanInSeconds"
          },
          "to_emails": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EmailEntry"
            },
            "x-go-name": "ToEmails"
          },
          "user_email": {
            "type": "string",
            "x-go-name": "UserEmail"
          },
          "username": {
            "description": "Auth - User Password",
            "type": "string",
            "x-go-name": "Username"
          },
          "webhook_noti_forwarder_public_details": {
            "$ref": "#/components/schemas/WebHookNotiForwarderPublicDetails"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NotiForwarderDetailsInput": {
        "type": "object",
        "properties": {
          "app_private_key_pem_base64": {
            "type": "string",
            "x-go-name": "AppPrivateKeyPEMBase64"
          },
          "client_secret": {
            "description": "Auth - JWT",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "password": {
            "description": "Auth - User Password",
            "type": "string",
            "x-go-name": "AdminPwd"
          },
          "slack_noti_forwarder_details": {
            "$ref": "#/components/schemas/SlackNotiForwarderDetails"
          },
          "teams_noti_forwarder_details": {
            "$ref": "#/components/schemas/TeamsNotiForwarderDetails"
          },
          "webhook_noti_forwarder_details": {
            "$ref": "#/components/schemas/WebhookNotiForwarderDetails"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NotiForwarderRunnerType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "NotiForwarderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ServiceNowAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SlackNotiForwarderDetails": {
        "type": "object",
        "properties": {
          "endpoint_url": {
            "type": "string",
            "x-go-name": "EndpointURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SlackNotiForwarderPublicDetails": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TeamsNotiForwarderDetails": {
        "type": "object",
        "properties": {
          "webhook_url": {
            "type": "string",
            "x-go-name": "WebhookURL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TeamsNotiForwarderPublicDetails": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WebHookNotiForwarderAuthType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WebHookNotiForwarderPublicDetails": {
        "type": "object",
        "properties": {
          "auth_type": {
            "$ref": "#/components/schemas/WebHookNotiForwarderAuthType"
          },
          "endpoint_url": {
            "type": "string",
            "x-go-name": "EndpointURL"
          },
          "username": {
            "description": "Auth type - User Password",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "WebhookNotiForwarderDetails": {
        "type": "object",
        "properties": {
          "certificate": {
            "description": "Auth type - Certificate",
            "type": "string",
            "x-go-name": "Certificate"
          },
          "password": {
            "description": "Auth type - User Password",
            "type": "string",
            "x-go-name": "Password"
          },
          "private_key": {
            "type": "string",
            "x-go-name": "PrivateKey"
          },
          "server_certificate": {
            "type": "string",
            "x-go-name": "ServerCertificate"
          },
          "token": {
            "description": "Auth type - Token",
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "eventForwarderGet": {
        "description": "eventForwarderGet is a command that get event forwarder",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
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
      "eventForwarderGetOutput": {
        "type": "object",
        "properties": {
          "event_forwarder": {
            "$ref": "#/components/schemas/NotiForwarder"
          },
          "event_forwarder_details": {
            "$ref": "#/components/schemas/NotiForwarderDetailsInput"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```