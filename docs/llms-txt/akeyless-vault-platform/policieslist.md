# Source: https://docs.akeyless.io/reference/policieslist.md

# /policy-list

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
    "/policy-list": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "policiesList",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/policiesList"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/policiesListResponse"
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
      "policiesListResponse": {
        "description": "",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/policiesListOutput"
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
      "KeyType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "policiesList": {
        "type": "object",
        "properties": {
          "aggregate": {
            "description": "Aggregate missing configurations from parent policies (requires --paths)",
            "type": "boolean",
            "x-go-name": "Aggregate"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "object-type": {
            "description": "Optional object types filter (items or targets)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ObjectTypes"
          },
          "paths": {
            "description": "Filter by exact policy paths",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Paths"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "types": {
            "description": "Filter by policy types",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Types"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "policiesListOutput": {
        "type": "object",
        "properties": {
          "policies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/policyOutput"
            },
            "x-go-name": "Policies"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "policyOutput": {
        "description": "it exposes object_types and intentionally hides enforce_on_items/enforce_on_targets.",
        "type": "object",
        "title": "policyOutput is a CLI output view that matches create/update input fields:",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountID"
          },
          "allowed_algorithms": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedAlgorithms"
          },
          "allowed_key_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedKeyNames"
          },
          "allowed_key_types": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/KeyType"
            },
            "x-go-name": "AllowedKeyTypes"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "max_rotation_interval_days": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "MaxRotationIntervalDays"
          },
          "object_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ObjectTypes"
          },
          "path": {
            "type": "string",
            "x-go-name": "Path"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```