# Source: https://docs.akeyless.io/reference/generatecsr.md

# /generate-csr

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
    "/generate-csr": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "generateCsr",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/generateCsr"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/generateCsrResponse"
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
      "generateCsrResponse": {
        "description": "generateCsrResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/generateCsrOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ClassicKeyType": {
        "type": "string",
        "title": "ClassicKeyType defines types of keys that can be managed by ClassicKey supported by AKEYLESS.",
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
      "generateCsr": {
        "type": "object",
        "title": "GenerateCsr is a command that generates CSR.",
        "required": [
          "name",
          "key-type",
          "common-name"
        ],
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/ClassicKeyType"
          },
          "alt-names": {
            "description": "A comma-separated list of dns alternative names",
            "type": "string",
            "x-go-name": "DNSNames"
          },
          "certificate-type": {
            "description": "The certificate type to be included in the CSR certificate (ssl-client/ssl-server/certificate-signing)",
            "type": "string",
            "x-go-name": "CertificateType"
          },
          "city": {
            "description": "The city to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "City"
          },
          "common-name": {
            "description": "The common name to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "CommonName"
          },
          "country": {
            "description": "The country to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "Country"
          },
          "critical": {
            "description": "Add critical to the key usage extension (will be false if not added)",
            "type": "boolean",
            "x-go-name": "Critical"
          },
          "dep": {
            "description": "The department to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "Department"
          },
          "email-addresses": {
            "description": "A comma-separated list of email addresses alternative names",
            "type": "string",
            "x-go-name": "EmailAddresses"
          },
          "export-private-key": {
            "description": "The flag to indicate if the private key should be exported",
            "type": "boolean",
            "default": false,
            "x-go-name": "ExportPrivateKey"
          },
          "generate-key": {
            "description": "Generate a new classic key for the csr",
            "type": "boolean",
            "x-go-name": "GenerateKey"
          },
          "hash-algorithm": {
            "description": "Specifies the hash algorithm used for the encryption key's operations, available options: SHA256, SHA384, SHA512",
            "type": "string",
            "default": "SHA256",
            "x-go-name": "HashAlgorithm"
          },
          "ip-addresses": {
            "description": "A comma-separated list of ip addresses alternative names",
            "type": "string",
            "x-go-name": "IpAddresses"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-type": {
            "description": "The type of the key to generate (classic-key/dfc)",
            "type": "string",
            "default": "classic-key",
            "x-go-name": "KeyType"
          },
          "name": {
            "description": "The key name",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "org": {
            "description": "The organization to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "Organization"
          },
          "split-level": {
            "description": "The number of fragments that the item will be split into (not includes\ncustomer fragment)",
            "type": "integer",
            "format": "int64",
            "default": 3,
            "x-go-name": "SplitLevel"
          },
          "state": {
            "description": "The state to be included in the CSR certificate",
            "type": "string",
            "x-go-name": "State"
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
          "uri-sans": {
            "description": "A comma-separated list of uri alternative names",
            "type": "string",
            "x-go-name": "URISANs"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "generateCsrOutput": {
        "type": "object",
        "properties": {
          "data": {
            "type": "string",
            "x-go-name": "Data"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```