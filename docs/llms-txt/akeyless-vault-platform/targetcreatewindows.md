# Source: https://docs.akeyless.io/reference/targetcreatewindows.md

# /target-create-windows

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
    "/target-create-windows": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateWindows",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateWindows"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateWindowsResponse"
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
      "targetCreateWindowsResponse": {
        "description": "targetCreateWindowsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/targetCreateOutput"
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
      "targetCreateOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "targetCreateWindows": {
        "description": "GatewayCreateProducerWindowsCmd is a command that creates a new windows target",
        "type": "object",
        "required": [
          "hostname",
          "username",
          "password",
          "name"
        ],
        "properties": {
          "certificate": {
            "description": "SSL CA certificate in base64 encoding generated from a trusted Certificate Authority (CA)",
            "type": "string",
            "x-go-name": "Certificate"
          },
          "connection-type": {
            "description": "Type of connection to Windows Server [credentials/parent-target]",
            "type": "string",
            "default": "credentials",
            "x-go-name": "ConnectionType"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "domain": {
            "description": "User domain name",
            "type": "string",
            "x-go-name": "DomainName"
          },
          "hostname": {
            "description": "Server hostname",
            "type": "string",
            "x-go-name": "Hostname"
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
          "parent-target-name": {
            "description": "Name of the parent target, relevant only when connection-type is parent-target",
            "type": "string",
            "x-go-name": "ParentTargetName"
          },
          "password": {
            "description": "Privileged user password",
            "type": "string",
            "default": "dummy_value",
            "x-go-name": "Password"
          },
          "port": {
            "description": "Server WinRM port",
            "type": "string",
            "default": "5986",
            "x-go-name": "Port"
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
          "use-tls": {
            "description": "Enable/Disable TLS for WinRM over HTTPS [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "UseTLS"
          },
          "username": {
            "description": "Privileged username",
            "type": "string",
            "default": "dummy_value",
            "x-go-name": "Username"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```