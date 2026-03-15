# Source: https://docs.akeyless.io/reference/accountcustomfieldcreate.md

# Create a new custom field.

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
    "/account-custom-field-create": {
      "post": {
        "tags": [
          "v2"
        ],
        "summary": "Create a new custom field.",
        "operationId": "accountCustomFieldCreate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/accountCustomFieldCreate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/accountCustomFieldCreateResponse"
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
      "accountCustomFieldCreateResponse": {
        "description": "accountCustomFieldCreateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AccountCustomFieldCreateOutput"
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
      "AccountCustomFieldCreateOutput": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Id"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
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
      "accountCustomFieldCreate": {
        "description": "accountCustomFieldCreate is a command that creates a new custom field in the account settings",
        "type": "object",
        "required": [
          "object",
          "object-type",
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
            "description": "The name of the custom field",
            "type": "string",
            "x-go-name": "FieldName"
          },
          "object": {
            "description": "The object to create the custom field",
            "type": "string",
            "default": "ITEM",
            "x-go-name": "Object"
          },
          "object-type": {
            "description": "The object type to create the custom field [e.g. STATIC_SECRET,DYNAMIC_SECRET,ROTATED_SECRET]",
            "type": "string",
            "x-go-name": "ObjectType"
          },
          "required": {
            "description": "Specify whether the custom field is mandatory",
            "type": "boolean",
            "default": false,
            "x-go-name": "Required"
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