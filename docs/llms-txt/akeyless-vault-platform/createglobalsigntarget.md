# Source: https://docs.akeyless.io/reference/createglobalsigntarget.md

# /create-globalsign-target

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
    "/create-globalsign-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createGlobalSignTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createGlobalSignTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createGlobalSignTargetResponse"
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
      "createGlobalSignTargetResponse": {
        "description": "createGlobalSignTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createGlobalSignTargetOutput"
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
      "createGlobalSignTarget": {
        "description": "createGlobalSignTarget is a command that creates a new target. [Deprecated: Use target-create-globalsign command]",
        "type": "object",
        "required": [
          "name",
          "username",
          "password",
          "profile-id",
          "contact-first-name",
          "contact-last-name",
          "contact-phone",
          "contact-email"
        ],
        "properties": {
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "contact-email": {
            "description": "Email of the GlobalSign GCC account contact",
            "type": "string",
            "x-go-name": "ContactEmail"
          },
          "contact-first-name": {
            "description": "First name of the GlobalSign GCC account contact",
            "type": "string",
            "x-go-name": "ContactFirstName"
          },
          "contact-last-name": {
            "description": "Last name of the GlobalSign GCC account contact",
            "type": "string",
            "x-go-name": "ContactLastName"
          },
          "contact-phone": {
            "description": "Telephone of the GlobalSign GCC account contact",
            "type": "string",
            "x-go-name": "ContactPhone"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "password": {
            "description": "Password of the GlobalSign GCC account",
            "type": "string",
            "x-go-name": "Password"
          },
          "profile-id": {
            "description": "Profile ID of the GlobalSign GCC account",
            "type": "string",
            "x-go-name": "ProfileID"
          },
          "timeout": {
            "description": "Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.",
            "type": "string",
            "default": "5m",
            "x-go-name": "Timeout"
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
          "username": {
            "description": "Username of the GlobalSign GCC account",
            "type": "string",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createGlobalSignTargetOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```