# Source: https://docs.akeyless.io/reference/getcertificatevalue.md

# /get-certificate-value

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
    "/get-certificate-value": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getCertificateValue",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getCertificateValue"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getCertificateValueResponse"
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
      "getCertificateValueResponse": {
        "description": "getCertificateValueResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetCertificateValueOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GetCertificateValueOutput": {
        "type": "object",
        "properties": {
          "certificate_pem": {
            "type": "string",
            "x-go-name": "CertificatePem"
          },
          "private_key_pem": {
            "type": "string",
            "x-go-name": "PrivateKeyPem"
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
      "getCertificateValue": {
        "type": "object",
        "title": "getCertificateValue is a command that gets a certificate value.",
        "properties": {
          "cert-issuer-name": {
            "description": "The parent PKI Certificate Issuer's name of the certificate, required when used with display-id and token",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "display-id": {
            "description": "Certificate display ID",
            "type": "string",
            "x-go-name": "CertificateDisplayID"
          },
          "ignore-cache": {
            "description": "Retrieve the Secret value without checking the Gateway's cache [true/false]. This flag is only relevant when using the RestAPI",
            "type": "string",
            "default": "false",
            "x-go-name": "IgnoreCache"
          },
          "issuance-token": {
            "description": "Token for getting the issued certificate",
            "type": "string",
            "x-go-name": "IssuanceToken"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Certificate name",
            "type": "string",
            "x-go-name": "CertificateName"
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
          "version": {
            "description": "Certificate version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```