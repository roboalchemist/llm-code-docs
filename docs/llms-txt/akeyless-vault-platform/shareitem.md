# Source: https://docs.akeyless.io/reference/shareitem.md

# /share-item

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
    "/share-item": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "shareItem",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/shareItem"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/shareItemResponse"
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
      "shareItemResponse": {
        "description": "shareItemResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/shareItemOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "EmailError": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "x-go-name": "Email"
          },
          "error": {
            "type": "string",
            "x-go-name": "Error"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/uam"
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
      "PathRuleType": {
        "type": "string",
        "title": "PathRuleType defines a kind of every PathRule assigned to a Role.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ResponseStopShareItem": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EmailError"
            },
            "x-go-name": "Errors"
          },
          "item_name": {
            "type": "string",
            "x-go-name": "ItemName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/uam"
      },
      "RuleAssigner": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "unique_id": {
            "type": "string",
            "x-go-name": "UniqueId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SharingItemFullInfo": {
        "type": "object",
        "properties": {
          "assigners": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RuleAssigner"
            },
            "x-go-name": "Assigners"
          },
          "capabilities": {
            "description": "The approved/denied capabilities in the path",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Capabilities"
          },
          "cb": {
            "type": "integer",
            "format": "uint64",
            "x-go-name": "CapabilitiesBitmap"
          },
          "is_limit_access": {
            "description": "flag that indicate that this rule is allowed to be access RemainingAccess of times.",
            "type": "boolean",
            "x-go-name": "IsLimitAccess"
          },
          "item_id": {
            "description": "The item id this rule directly refers to (when applicable)",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "number_of_access_used": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAccessUsed"
          },
          "number_of_allowed_access": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAllowedAccess"
          },
          "path": {
            "description": "The path the rule refers to",
            "type": "string",
            "x-go-name": "Path"
          },
          "start_time": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "StartTime"
          },
          "ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          },
          "type": {
            "$ref": "#/components/schemas/PathRuleType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/uam"
      },
      "shareItem": {
        "type": "object",
        "title": "shareItem is a command to start/stop/describe sharing a given item with user that don't use akeyless.",
        "required": [
          "item-name",
          "action"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "action": {
            "description": "Action to be performed on the item [start/stop/describe]",
            "type": "string",
            "x-go-name": "Action"
          },
          "emails": {
            "description": "List of emails to start/stop sharing the secret with",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Emails"
          },
          "item-name": {
            "description": "Item name",
            "type": "string",
            "x-go-name": "ItemName"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "share-type": {
            "description": "Share type [email/token]",
            "type": "string",
            "default": "email",
            "x-go-name": "ShareType"
          },
          "shared-token-id": {
            "description": "Shared token ids in order to stop sharing a secret",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SharedTokenIds"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "TTL of the Availability of the shared secret in seconds",
            "type": "integer",
            "format": "int32",
            "x-go-name": "TTL"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "view-once": {
            "description": "ViewOnlyOnce Shared secrets can only be viewed once [true/false]",
            "type": "boolean",
            "default": false,
            "x-go-name": "ViewOnlyOnce"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "shareItemOutput": {
        "type": "object",
        "properties": {
          "email_error": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "EmailError"
          },
          "items_error": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ResponseStopShareItem"
            },
            "x-go-name": "ItemsError"
          },
          "s_token": {
            "type": "string",
            "x-go-name": "SToken"
          },
          "shared_users": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SharedUsersBCOnly"
          },
          "shared_users_full_info": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SharingItemFullInfo"
            },
            "x-go-name": "SharedUsersFullInfo"
          },
          "sharing_url": {
            "type": "string",
            "x-go-name": "SharingUrl"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```