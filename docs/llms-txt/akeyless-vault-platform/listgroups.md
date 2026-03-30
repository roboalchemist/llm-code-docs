# Source: https://docs.akeyless.io/reference/listgroups.md

# /list-group

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
    "/list-group": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listGroups",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listGroups"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listGroupsResponse"
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
      "listGroupsResponse": {
        "description": "listGroupsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ListGroupsOutput"
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
      "Group": {
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
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "ListGroupsOutput": {
        "type": "object",
        "properties": {
          "groups": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Group"
            },
            "x-go-name": "Groups"
          },
          "next_page": {
            "type": "string",
            "x-go-name": "NextPage"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "listGroups": {
        "type": "object",
        "title": "listGroups is a command that lists groups.",
        "properties": {
          "filter": {
            "description": "Filter by auth method name or part of it",
            "type": "string",
            "x-go-name": "Filter"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "pagination-token": {
            "description": "Next page reference",
            "type": "string",
            "x-go-name": "PaginationToken"
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