# Source: https://docs.akeyless.io/reference/getpkicertificate.md

# /get-pki-certificate

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
    "/get-pki-certificate": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "GetPKICertificate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GetPKICertificate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getPKICertificateResponse"
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
      "getPKICertificateResponse": {
        "description": "getPKICertificateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/getPKICertificateOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GetPKICertificate": {
        "type": "object",
        "title": "GetPKICertificate is a command that generates PKI certificate.",
        "required": [
          "cert-issuer-name"
        ],
        "properties": {
          "alt-names": {
            "description": "The Subject Alternative Names to be included in the PKI certificate (in\na comma-separated list) (if CSR is supplied this flag is ignored and any DNS.* names are taken from it)",
            "type": "string",
            "x-go-name": "AltNames"
          },
          "cert-issuer-name": {
            "description": "The name of the PKI certificate issuer",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "common-name": {
            "description": "The common name to be included in the PKI certificate (if CSR is supplied this flag is ignored and the CSR subject CN is taken)",
            "type": "string",
            "x-go-name": "CommonName"
          },
          "csr-data-base64": {
            "description": "Certificate Signing Request contents encoded in base64 to generate the certificate with",
            "type": "string",
            "x-go-name": "CSRData"
          },
          "extended-key-usage": {
            "description": "A comma-separated list of extended key usage requests which will be used for certificate issuance. Supported values: 'clientauth', 'serverauth', 'codesigning'. If critical is present the extension will be marked as critical",
            "type": "string",
            "x-go-name": "ExtKeyUsage"
          },
          "extra-extensions": {
            "description": "A json string that defines the requested extra extensions for the certificate",
            "type": "string",
            "x-go-name": "ExtraExtensions"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-data-base64": {
            "description": "PKI key file contents. If this option is used, the certificate\nwill be printed to stdout",
            "type": "string",
            "x-go-name": "KeyData"
          },
          "max-path-len": {
            "description": "The maximum path length for the generated certificate. -1, means unlimited unless the signing certificate has a maximum path length set",
            "type": "integer",
            "format": "int64",
            "default": -1,
            "x-go-name": "MaxPathLen"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "Updated certificate lifetime in seconds (must be less than the Certificate Issuer default TTL)",
            "type": "string",
            "x-go-name": "Ttl"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "uri-sans": {
            "description": "The URI Subject Alternative Names to be included in the PKI certificate\n(in a comma-separated list) (if CSR is supplied this flag is ignored and any URI.* names are taken from it)",
            "type": "string",
            "x-go-name": "URISANs"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "HTTPChallengeInfo": {
        "description": "HTTPChallengeInfo contains HTTP-01 challenge details for user display",
        "type": "object",
        "properties": {
          "file_content": {
            "type": "string",
            "x-go-name": "FileContent"
          },
          "file_path": {
            "type": "string",
            "x-go-name": "FilePath"
          },
          "instructions": {
            "type": "string",
            "x-go-name": "Instructions"
          },
          "key_auth": {
            "type": "string",
            "x-go-name": "KeyAuth"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "getPKICertificateOutput": {
        "type": "object",
        "properties": {
          "cert_display_id": {
            "type": "string",
            "x-go-name": "CertDisplayID"
          },
          "cert_item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertItemID"
          },
          "data": {
            "type": "string",
            "x-go-name": "Data"
          },
          "http_challenge_info": {
            "$ref": "#/components/schemas/HTTPChallengeInfo"
          },
          "parent_cert": {
            "type": "string",
            "x-go-name": "ParentCert"
          },
          "path": {
            "type": "string",
            "x-go-name": "Path"
          },
          "reading_token": {
            "type": "string",
            "x-go-name": "IssuanceToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```