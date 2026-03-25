# Source: https://docs.akeyless.io/reference/assoc-role-am.md

# /assoc-role-am

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
    "/assoc-role-am": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "assocRoleAuthMethod",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/assocRoleAuthMethod"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/assocRoleAuthMethodResponse"
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
      "assocRoleAuthMethodResponse": {
        "description": "assocRoleAuthMethodResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateRoleAuthMethodAssocOutput"
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
      "CreateRoleAuthMethodAssocOutput": {
        "description": "CreateRoleAuthMethodAssocOutput defines output of CreateRoleAuthMethodAssoc\noperation.",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
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
      "assocRoleAuthMethod": {
        "description": "assocRoleAuthMethod is a command that creates an association between role\nand auth method.",
        "type": "object",
        "required": [
          "role-name",
          "am-name"
        ],
        "properties": {
          "am-name": {
            "description": "The auth method to associate",
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "case-sensitive": {
            "description": "Treat sub claims as case-sensitive [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "IsSubClaimsCaseSensitive"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "role-name": {
            "description": "The role to associate",
            "type": "string",
            "x-go-name": "RoleName"
          },
          "sub-claims": {
            "description": "key/val of sub claims, e.g group=admins,developers",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "SubClaims"
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