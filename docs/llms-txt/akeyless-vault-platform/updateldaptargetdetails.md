# Source: https://docs.akeyless.io/reference/updateldaptargetdetails.md

# /update-ldap-target-details

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
    "/update-ldap-target-details": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateLdapTargetDetails",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateLdapTargetDetails"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateTargetResponse"
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
      "updateTargetResponse": {
        "description": "updateTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateTargetOutput"
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
      "updateLdapTargetDetails": {
        "type": "object",
        "title": "updateLdapTargetDetails is a command that updates an existing target.",
        "required": [
          "name"
        ],
        "properties": {
          "bind-dn": {
            "type": "string",
            "x-go-name": "BindDn"
          },
          "bind-dn-password": {
            "type": "string",
            "x-go-name": "BindDnPassword"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "key": {
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "ldap-ca-cert": {
            "type": "string",
            "x-go-name": "LdapCACert"
          },
          "ldap-url": {
            "type": "string",
            "x-go-name": "LdapUrl"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "new-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "NewVersion"
          },
          "protection_key": {
            "description": "The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "token-expiration": {
            "type": "string",
            "x-go-name": "TokenExpiration"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateTargetOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```