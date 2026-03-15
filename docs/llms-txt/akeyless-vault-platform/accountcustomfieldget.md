# Source: https://docs.akeyless.io/reference/accountcustomfieldget.md

# Get an account custom field by ID.

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
    "/account-custom-field-get": {
      "post": {
        "tags": [
          "v2"
        ],
        "summary": "Get an account custom field by ID.",
        "operationId": "accountCustomFieldGet",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/accountCustomFieldGet"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/accountCustomFieldGetResponse"
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
      "accountCustomFieldGetResponse": {
        "description": "accountCustomFieldGetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AccountCustomFieldGetOutput"
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
      "AccountCustomFieldGetOutput": {
        "type": "object",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountID"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "deletion_date": {
            "$ref": "#/components/schemas/NullTime"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ID"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "object": {
            "type": "string",
            "x-go-name": "Object"
          },
          "object_type": {
            "type": "string",
            "x-go-name": "ObjectType"
          },
          "required": {
            "type": "boolean",
            "x-go-name": "Required"
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
      "NullTime": {
        "description": "NullTime implements the [Scanner] interface so\nit can be used as a scan destination, similar to [NullString].",
        "type": "object",
        "title": "NullTime represents a [time.Time] that may be null.",
        "properties": {
          "Time": {
            "type": "string",
            "format": "date-time"
          },
          "Valid": {
            "type": "boolean"
          }
        },
        "x-go-package": "database/sql"
      },
      "accountCustomFieldGet": {
        "description": "accountCustomFieldGet is a command that retrieves an account custom field",
        "type": "object",
        "required": [
          "id"
        ],
        "properties": {
          "id": {
            "description": "The custom field id",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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