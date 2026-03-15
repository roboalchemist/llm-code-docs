# Source: https://docs.akeyless.io/reference/createrole.md

# /create-role

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
    "/create-role": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createRole",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createRole"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createRoleResponse"
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
      "createRoleResponse": {
        "description": "createRoleResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createRoleOutput"
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
      "createRole": {
        "type": "object",
        "title": "createRole is a command that creates a new role .",
        "required": [
          "name"
        ],
        "properties": {
          "analytics-access": {
            "description": "Allow this role to view analytics. Currently only 'none', 'own', 'all'\nvalues are supported, allowing associated auth methods to view reports\nproduced by the same auth methods.",
            "type": "string",
            "x-go-name": "AnalyticsAccess"
          },
          "audit-access": {
            "description": "Allow this role to view audit logs. Currently only 'none', 'own', 'scoped' and 'all'\nvalues are supported, allowing associated auth methods to view audit\nlogs produced by the same auth methods.",
            "type": "string",
            "x-go-name": "AuditAccess"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "event-center-access": {
            "description": "Allow this role to view Event Center. Currently only 'none', 'scoped' and 'all'\nvalues are supported",
            "type": "string",
            "x-go-name": "EventCenterAccess"
          },
          "event-forwarders-access": {
            "description": "Allow this role to manage Event Forwarders. Currently only 'none' and 'all' values are supported.",
            "type": "string",
            "x-go-name": "EventForwardersAccess"
          },
          "event-forwarders-name": {
            "description": "Allow this role to manage the following Event Forwarders.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "EventForwardersName"
          },
          "gw-analytics-access": {
            "description": "Allow this role to view gw analytics. Currently only 'none', 'scoped', 'all'\nvalues are supported, allowing associated auth methods to view reports\nproduced by the same auth methods.",
            "type": "string",
            "x-go-name": "GwAnalyticsAccess"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Role name",
            "type": "string",
            "x-go-name": "RoleName"
          },
          "reverse-rbac-access": {
            "description": "Allow this role to view Reverse RBAC. Supported values: 'scoped', 'all'.",
            "type": "string",
            "x-go-name": "ReverseRbacAccess"
          },
          "sra-reports-access": {
            "description": "Allow this role to view SRA Clusters. Currently only 'none', 'scoped',\n'all' values are supported.",
            "type": "string",
            "x-go-name": "SRAReportsAccess"
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
          "usage-reports-access": {
            "description": "Allow this role to view Usage Report. Currently only 'none' and\n'all' values are supported.",
            "type": "string",
            "x-go-name": "UsageReportsAccess"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createRoleOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```