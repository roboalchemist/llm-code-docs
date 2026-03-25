# Source: https://docs.akeyless.io/reference/updateoidcapp.md

# /update-oidc-app

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
    "/update-oidc-app": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateOidcApp",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateOidcApp"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateOidcAppResponse"
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
      "updateOidcAppResponse": {
        "description": "updateOidcAppResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UpdateOidcAppOutput"
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
      "UpdateOidcAppOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateOidcApp": {
        "type": "object",
        "title": "updateOidcApp is a command that updates an oidc application.",
        "required": [
          "name"
        ],
        "properties": {
          "audience": {
            "description": "A comma separated list of allowed audiences",
            "type": "string",
            "x-go-name": "Audience"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of a key that used to encrypt the OIDC application (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "name": {
            "description": "OIDC application name",
            "type": "string",
            "x-go-name": "OidcClientName"
          },
          "permission-assignment": {
            "description": "A json string defining the access permission assignment for this app",
            "type": "string",
            "x-go-name": "AccessPermissionAssignment"
          },
          "public": {
            "description": "Set to true if the app is public (cannot keep secrets)",
            "type": "boolean",
            "x-go-name": "Public"
          },
          "redirect-uris": {
            "description": "A comma separated list of allowed redirect uris",
            "type": "string",
            "x-go-name": "RedirectURIs"
          },
          "scopes": {
            "description": "A comma separated list of allowed scopes",
            "type": "string",
            "default": "openid",
            "x-go-name": "Scopes"
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