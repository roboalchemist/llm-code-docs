# Source: https://docs.akeyless.io/reference/getgroup.md

# /get-group

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
    "/get-group": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getGroup",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getGroup"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getGroupResponse"
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
      "getGroupResponse": {
        "description": "getGroupResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetGroupOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AccessPermissionAssignment": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access_type": {
            "type": "string",
            "x-go-name": "AccessType"
          },
          "sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "SubClaims"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/oidc/shared"
      },
      "GetGroupOutput": {
        "type": "object",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountId"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "description": {
            "type": "string",
            "x-go-name": "Description"
          },
          "group_alias": {
            "type": "string",
            "x-go-name": "GroupAlias"
          },
          "group_id": {
            "type": "string",
            "x-go-name": "GroupId"
          },
          "group_name": {
            "type": "string",
            "x-go-name": "GroupName"
          },
          "is_subclaims_with_operator": {
            "type": "boolean",
            "x-go-name": "IsSubclaimsWithOperator"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "user_assignments": {
            "$ref": "#/components/schemas/GroupPermissionsAssignments"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GroupPermissionsAssignments": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/AccessPermissionAssignment"
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
      "getGroup": {
        "type": "object",
        "title": "getGroup is a command that returns a group's info.",
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
            "description": "Group name",
            "type": "string",
            "x-go-name": "NName"
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