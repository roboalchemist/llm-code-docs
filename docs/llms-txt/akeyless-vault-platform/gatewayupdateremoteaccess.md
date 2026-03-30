# Source: https://docs.akeyless.io/reference/gatewayupdateremoteaccess.md

# /gateway-update-remote-access

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
    "/gateway-update-remote-access": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateRemoteAccess",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateRemoteAccess"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayUpdateRemoteAccessResponse"
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
      "gatewayUpdateRemoteAccessResponse": {
        "description": "gatewayUpdateRemoteAccessResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateRemoteAccessOutput"
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
      "gatewayUpdateRemoteAccess": {
        "description": "gatewayUpdateRemoteAccess is a command that update remote access config",
        "type": "object",
        "properties": {
          "allowed-ssh-url": {
            "description": "Specify a valid SSH-URL to tunnel to SSH session",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "AllowedSSHURL"
          },
          "allowed-urls": {
            "description": "List of valid URLs to redirect from the Portal back to the remote access server (in a comma-delimited list)",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "AllowedBastionUrls"
          },
          "default-session-ttl-minutes": {
            "description": "Default session TTL in minutes",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "DefaultSessionTTLMinutes"
          },
          "hide-session-recording": {
            "description": "Specifies whether to show/hide if the session is currently recorded [true/false]",
            "type": "string",
            "x-go-name": "HideSessionRecording"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "kexalgs": {
            "description": "Decide which algorithm will be used as part of the SSH initial hand-shake process",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "Kexalgs"
          },
          "keyboard-layout": {
            "description": "Enable support for additional keyboard layouts",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "KeyboardLayout"
          },
          "legacy-ssh-algorithm": {
            "description": "Signs SSH certificates using legacy ssh-rsa-cert-01@openssh.com signing algorithm [true/false]",
            "type": "string",
            "x-go-name": "LegacySshAlgorithm"
          },
          "rdp-target-configuration": {
            "description": "Specify the usernameSubClaim that exists inside the IDP JWT, e.g. email",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "RdpTargetConfig"
          },
          "ssh-target-configuration": {
            "description": "Specify the usernameSubClaim that exists inside the IDP JWT, e.g. email",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "SshTargetConfig"
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
      "gatewayUpdateRemoteAccessOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```