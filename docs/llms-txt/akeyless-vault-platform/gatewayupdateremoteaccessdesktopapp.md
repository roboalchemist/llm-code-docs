# Source: https://docs.akeyless.io/reference/gatewayupdateremoteaccessdesktopapp.md

# /gateway-update-remote-access-desktop-app

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
    "/gateway-update-remote-access-desktop-app": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateRemoteAccessDesktopApp",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateRemoteAccessDesktopApp"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayUpdateRemoteAccessDesktopAppResponse"
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
      "gatewayUpdateRemoteAccessDesktopAppResponse": {
        "description": "gatewayUpdateRemoteAccessDesktopAppResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateRemoteAccessDesktopAppOutput"
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
      "gatewayUpdateRemoteAccessDesktopApp": {
        "description": "gatewayUpdateRemoteAccessDesktopApp is a command that update remote access desktop app config",
        "type": "object",
        "properties": {
          "desktop-app-secure-web-access-url": {
            "type": "string",
            "x-go-name": "SecureWebAccessUrl"
          },
          "desktop-app-secure-web-proxy": {
            "type": "string",
            "x-go-name": "SecureWebProxyUrl"
          },
          "desktop-app-ssh-cert-issuer": {
            "type": "string",
            "x-go-name": "DefaultCertIssuer"
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
      },
      "gatewayUpdateRemoteAccessDesktopAppOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```