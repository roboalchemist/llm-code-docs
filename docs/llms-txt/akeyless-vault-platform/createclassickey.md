# Source: https://docs.akeyless.io/reference/createclassickey.md

# /create-classic-key

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
    "/create-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "CreateClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/CreateClassicKeyResponse"
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
      "CreateClassicKeyResponse": {
        "description": "CreateClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateClassicKeyOutput"
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
      "CertificateFormat": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ClassicKeyType": {
        "type": "string",
        "title": "ClassicKeyType defines types of keys that can be managed by ClassicKey supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CreateClassicKey": {
        "description": "CreateClassicKey is a command that creates classic key",
        "type": "object",
        "required": [
          "name",
          "alg"
        ],
        "properties": {
          "alg": {
            "description": "Classic Key type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, RSA1024, RSA2048, RSA3072, RSA4096, EC256, EC384, GPG]",
            "type": "string",
            "x-go-name": "Alg"
          },
          "auto-rotate": {
            "description": "Whether to automatically rotate every rotation_interval days, or disable existing automatic rotation [true/false]",
            "type": "string",
            "x-go-name": "AutoRotate"
          },
          "cert-file-data": {
            "description": "Certificate in a PEM format.",
            "type": "string",
            "x-go-name": "CertFileData"
          },
          "certificate-common-name": {
            "description": "Common name for the generated certificate. Relevant only for generate-self-signed-certificate.",
            "type": "string",
            "x-go-name": "CertificateCommonName"
          },
          "certificate-country": {
            "description": "Country name for the generated certificate. Relevant only for generate-self-signed-certificate.",
            "type": "string",
            "x-go-name": "CertificateCountry"
          },
          "certificate-digest-algo": {
            "description": "Digest algorithm to be used for the certificate key signing.",
            "type": "string",
            "x-go-name": "CertificateDigestAlgo"
          },
          "certificate-format": {
            "$ref": "#/components/schemas/CertificateFormat"
          },
          "certificate-locality": {
            "description": "Locality for the generated certificate. Relevant only for generate-self-signed-certificate.",
            "type": "string",
            "x-go-name": "CertificateLocality"
          },
          "certificate-organization": {
            "description": "Organization name for the generated certificate. Relevant only for generate-self-signed-certificate.",
            "type": "string",
            "x-go-name": "CertificateOrganization"
          },
          "certificate-province": {
            "description": "Province name for the generated certificate. Relevant only for generate-self-signed-certificate.",
            "type": "string",
            "x-go-name": "CertificateProvince"
          },
          "certificate-ttl": {
            "description": "TTL in days for the generated certificate. Required only for generate-self-signed-certificate.",
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateTTL"
          },
          "conf-file-data": {
            "description": "The csr config data in base64 encoding",
            "type": "string",
            "x-go-name": "ConfFileData"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "generate-self-signed-certificate": {
            "description": "Whether to generate a self signed certificate with the key. If set, --certificate-ttl must be provided.",
            "type": "boolean",
            "x-go-name": "GenerateSelfSignedCertificate"
          },
          "gpg-alg": {
            "description": "gpg alg: Relevant only if GPG key type selected; options: [RSA1024, RSA2048, RSA3072, RSA4096, Ed25519]",
            "type": "string",
            "x-go-name": "GPGAlg"
          },
          "hash-algorithm": {
            "description": "Specifies the hash algorithm used for the encryption key's operations, available options: [SHA256, SHA384, SHA512]",
            "type": "string",
            "default": "SHA256",
            "x-go-name": "CertificateHashAlgorithm"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-data": {
            "description": "Base64-encoded classic key value",
            "type": "string",
            "x-go-name": "ClassicKeyValue"
          },
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "ClassicKey name",
            "type": "string",
            "x-go-name": "ClassicKeyName"
          },
          "protection-key-name": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "rotation-event-in": {
            "description": "How many days before the rotation of the item would you like to be notified",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RotationEventsInDays"
          },
          "rotation-interval": {
            "description": "The number of days to wait between every automatic rotation (1-365)",
            "type": "string",
            "x-go-name": "RotationInterval"
          },
          "tags": {
            "description": "Add tags attached to this object",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
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
      "CreateClassicKeyOutput": {
        "type": "object",
        "properties": {
          "classic_key_id": {
            "type": "string",
            "x-go-name": "ClassicKeyId"
          },
          "classic_key_name": {
            "type": "string",
            "x-go-name": "ClassicKeyName"
          },
          "classic_key_type": {
            "$ref": "#/components/schemas/ClassicKeyType"
          },
          "public_key": {
            "type": "string",
            "x-go-name": "PublicKey"
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
      }
    }
  }
}
```