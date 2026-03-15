# Source: https://docs.akeyless.io/reference/kmipdescribeclient.md

# /kmip-get-client

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
    "/kmip-get-client": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "kmipDescribeClient",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/kmipDescribeClient"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/kmipDescribeClientResponse"
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
      "kmipDescribeClientResponse": {
        "description": "kmipDescribeClientResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/KMIPClientGetResponse"
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
      "KMIPClient": {
        "type": "object",
        "properties": {
          "activate_keys_on_creation": {
            "type": "boolean",
            "x-go-name": "ActivateKeysOnCreation"
          },
          "certificate_issue_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CertificateIssueDate"
          },
          "certificate_ttl_in_seconds": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateTTLInSeconds"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "rules": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PathRule"
            },
            "x-go-name": "Rules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "KMIPClientGetResponse": {
        "type": "object",
        "properties": {
          "client": {
            "$ref": "#/components/schemas/KMIPClient"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/gateway/config"
      },
      "PathRule": {
        "type": "object",
        "title": "PathRule is a single rule used in AKEYLESS RBAC.",
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
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PathRuleType": {
        "type": "string",
        "title": "PathRuleType defines a kind of every PathRule assigned to a Role.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "kmipDescribeClient": {
        "type": "object",
        "title": "kmipDescribeClient is a command that shows KMIP client details.",
        "properties": {
          "client-id": {
            "type": "string",
            "x-go-name": "ClientID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "type": "string",
            "x-go-name": "ClientName"
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