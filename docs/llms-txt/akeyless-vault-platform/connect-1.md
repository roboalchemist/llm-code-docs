# Source: https://docs.akeyless.io/reference/connect-1.md

# /connect

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
    "/connect": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "Connect",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Connect"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/connectResponse"
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
      "connectResponse": {
        "description": "connectResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/connectOutput"
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
      "Connect": {
        "description": "Connect is a command that performs secure remote access",
        "type": "object",
        "properties": {
          "Helper": {
            "$ref": "#/components/schemas/ConnectHepler"
          },
          "RcFileOverride": {
            "description": "used to override .akeyless-connect.rc in tests",
            "type": "string"
          },
          "bastion-ctrl-path": {
            "description": "Deprecated. use bastion-ctrl-path",
            "type": "string",
            "x-go-name": "BastionAPIPath"
          },
          "bastion-ctrl-port": {
            "description": "Deprecated. use sra-ctrl-port",
            "type": "string",
            "x-go-name": "BastionPort"
          },
          "bastion-ctrl-proto": {
            "description": "Deprecated. use sra-ctrl-proto",
            "type": "string",
            "x-go-name": "BastionProtocol"
          },
          "bastion-ctrl-subdomain": {
            "description": "Deprecated. use sra-ctrl-subdomain",
            "type": "string",
            "x-go-name": "BastionAPIPrefix"
          },
          "cert-issuer-name": {
            "description": "The Akeyless certificate issuer name",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "gateway-url": {
            "description": "The Gateway URL (configuration management) address, e.g. http://localhost:8000",
            "type": "string",
            "x-go-name": "BastionGatewayUrl"
          },
          "identity-file": {
            "description": "The file from which the identity (private key) for public key authentication is read",
            "type": "string",
            "x-go-name": "IdentityFile"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "justification": {
            "type": "string",
            "x-go-name": "Justification"
          },
          "name": {
            "description": "The Secret name (for database and AWS producers - producer name)",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "sra-ctrl-path": {
            "description": "The Bastion API path",
            "type": "string",
            "x-go-name": "SraAPIPath"
          },
          "sra-ctrl-port": {
            "description": "The Bastion API Port",
            "type": "string",
            "default": "9900",
            "x-go-name": "SraPort"
          },
          "sra-ctrl-proto": {
            "description": "The SRA API protocol",
            "type": "string",
            "default": "http",
            "x-go-name": "SraProtocol"
          },
          "sra-ctrl-subdomain": {
            "description": "The SRA API prefix",
            "type": "string",
            "x-go-name": "SraAPIPrefix"
          },
          "ssh-command": {
            "description": "Path to SSH executable. e.g. /usr/bin/ssh",
            "type": "string",
            "x-go-name": "SSHLocation"
          },
          "ssh-extra-args": {
            "description": "Additional SSH arguments (except -i)",
            "type": "string",
            "x-go-name": "SSHExtraArgs"
          },
          "ssh-legacy-signing-alg": {
            "description": "Set this option to output legacy ('ssh-rsa-cert-v01@openssh.com') signing algorithm name in the ssh certificate.",
            "type": "boolean",
            "default": false,
            "x-go-name": "SSHLegacySigningAlg"
          },
          "target": {
            "description": "The target",
            "type": "string",
            "x-go-name": "Target"
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
          "use-ssh-agent": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "UseSshAgent"
          },
          "via-bastion": {
            "description": "Deprecated. Use via-sra",
            "type": "string",
            "x-go-name": "ViaBastion"
          },
          "via-sra": {
            "description": "The jump box server",
            "type": "string",
            "x-go-name": "ViaSRA"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "ConnectHepler": {
        "type": "object",
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
      "connectOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```