# Source: https://docs.akeyless.io/reference/generateca.md

# /generate-ca

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
    "/generate-ca": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "GenerateCA",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GenerateCA"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/generateCAResponse"
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
      "generateCAResponse": {
        "description": "generateCAResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GenerateCAOutput"
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
      "GenerateCA": {
        "description": "GenerateCA is a command that creates a new PKI CA and Intermediate issuers",
        "type": "object",
        "required": [
          "pki-chain-name",
          "allowed-domains",
          "ttl"
        ],
        "properties": {
          "alg": {
            "$ref": "#/components/schemas/ClassicKeyType"
          },
          "allowed-domains": {
            "description": "A list of the allowed domains that clients can request to be included in\nthe certificate (in a comma-delimited list)",
            "type": "string",
            "x-go-name": "AllowedDomains"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "extended-key-usage": {
            "description": "A comma sepereted list of extended key usage for the intermediate (serverauth / clientauth / codesigning)",
            "type": "string",
            "default": "serverauth,clientauth",
            "x-go-name": "ExtendedKeyUsage"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-type": {
            "$ref": "#/components/schemas/KeyType"
          },
          "max-path-len": {
            "description": "The maximum number of intermediate certificates that can appear in a certification path",
            "type": "integer",
            "format": "int64",
            "default": 1,
            "x-go-name": "MaxPathLen"
          },
          "pki-chain-name": {
            "description": "PKI chain name",
            "type": "string",
            "x-go-name": "PkiChainName"
          },
          "protection-key-name": {
            "description": "The name of a key that used to encrypt the secrets values (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "split-level": {
            "description": "The number of fragments that the item will be split into",
            "type": "integer",
            "format": "int64",
            "default": 3,
            "x-go-name": "SplitLevel"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "The maximum requested Time To Live for issued certificate by default in seconds, supported formats are s,m,h,d",
            "type": "string",
            "x-go-name": "MaxTTL"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GenerateCAOutput": {
        "type": "object",
        "properties": {
          "intermediate_certificate_name": {
            "type": "string",
            "x-go-name": "IntermediateCertificateName"
          },
          "intermediate_issuer_name": {
            "type": "string",
            "x-go-name": "IntermediateIssuerName"
          },
          "intermediate_key_name": {
            "type": "string",
            "x-go-name": "IntermediateKeyName"
          },
          "root_certificate_name": {
            "type": "string",
            "x-go-name": "RootCertificateName"
          },
          "root_issuer_name": {
            "type": "string",
            "x-go-name": "RootIssuerName"
          },
          "root_key_name": {
            "type": "string",
            "x-go-name": "RootKeyName"
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
      "KeyType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      }
    }
  }
}
```