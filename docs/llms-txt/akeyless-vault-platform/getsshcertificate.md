# Source: https://docs.akeyless.io/reference/getsshcertificate.md

# /get-ssh-certificate

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
    "/get-ssh-certificate": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getSSHCertificate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getSSHCertificate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getSSHCertificateResponse"
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
      "getSSHCertificateResponse": {
        "description": "getSSHCertificateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/getSSHCertificateOutput"
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
      "getSSHCertificate": {
        "type": "object",
        "title": "getSSHCertificate is a command that generates SSH certificate.",
        "required": [
          "cert-username",
          "cert-issuer-name"
        ],
        "properties": {
          "cert-issuer-name": {
            "description": "The name of the SSH certificate issuer",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "cert-username": {
            "description": "The username to sign in the SSH certificate",
            "type": "string",
            "default": "-",
            "x-go-name": "Username"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "legacy-signing-alg-name": {
            "description": "Set this option to output legacy ('ssh-rsa-cert-v01@openssh.com') signing algorithm name in the certificate.",
            "type": "boolean",
            "default": false,
            "x-go-name": "LegacySigningAlgName"
          },
          "public-key-data": {
            "description": "SSH public key file contents. If this option is used, the certificate\nwill be printed to stdout",
            "type": "string",
            "x-go-name": "PublicKeyData"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "Updated certificate lifetime in seconds (must be less than the Certificate Issuer default TTL)",
            "type": "integer",
            "format": "int64",
            "x-go-name": "Ttl"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "getSSHCertificateOutput": {
        "type": "object",
        "properties": {
          "data": {
            "type": "string",
            "x-go-name": "Data"
          },
          "path": {
            "type": "string",
            "x-go-name": "Path"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```