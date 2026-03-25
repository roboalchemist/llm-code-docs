# Source: https://docs.akeyless.io/reference/user-event-last-status.md

# /user-event-last-status

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
    "/user-event-last-status": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getLastUserEventStatus",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getLastUserEventStatus"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getLastUserEventStatusResponse"
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
      "getLastUserEventStatusResponse": {
        "description": "getLastUserEventStatusResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetUserEventStatusOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AccessRequestStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EventSource": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "EventType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GetUserEventStatusOutput": {
        "type": "object",
        "properties": {
          "access_status": {
            "$ref": "#/components/schemas/AccessRequestStatus"
          },
          "event_created_at": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "EventCreatedAt"
          },
          "status": {
            "type": "string",
            "x-go-name": "Status"
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
      "getLastUserEventStatus": {
        "type": "object",
        "title": "getLastUserEventStatus is a command that get last user event status.",
        "required": [
          "item-name",
          "item-type",
          "event-type"
        ],
        "properties": {
          "event-source": {
            "$ref": "#/components/schemas/EventSource"
          },
          "event-type": {
            "$ref": "#/components/schemas/EventType"
          },
          "item-name": {
            "description": "Event item name",
            "type": "string",
            "x-go-name": "EventItemName"
          },
          "item-type": {
            "description": "Event item type can be either \"target\" or type of item eg \"static_secret\"/\"dynamic_secret\"\nTo get type of some item run `akeyless describe-item -n {ITEM_NAME} --jq-expression .item_type`",
            "type": "string",
            "x-go-name": "EventItemType"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "time-back": {
            "description": "The time back to search the event, for example if the value is \"5m\" we will return the last user event issued in the last 5 minutes.\nBy default, we will search without any time boundary.",
            "type": "string",
            "x-go-name": "TimeBack"
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