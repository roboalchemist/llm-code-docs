# Source: https://docs.akeyless.io/reference/createdfckey.md

# /create-dfc-key

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
    "/create-dfc-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createDFCKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createDFCKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createDFCKeyResponse"
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
      "createDFCKeyResponse": {
        "description": "createDFCKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createDFCKeyOutput"
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
      "Duration": {
        "description": "A Duration represents the elapsed time between two instants\nas an int64 nanosecond count. The representation limits the\nlargest representable duration to approximately 290 years.",
        "type": "integer",
        "format": "int64",
        "x-go-package": "time"
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
      "createDFCKey": {
        "type": "object",
        "title": "createDFCKey is a command that creates a new DFC key.",
        "required": [
          "name",
          "alg"
        ],
        "properties": {
          "alg": {
            "description": "DFCKey type; options: [AES128GCM, AES256GCM, AES128SIV, AES256SIV, AES128CBC, AES256CBC, RSA1024,\nRSA2048, RSA3072, RSA4096]",
            "type": "string",
            "x-go-name": "Alg"
          },
          "auto-rotate": {
            "description": "Whether to automatically rotate every rotation_interval days, or disable existing automatic rotation [true/false]",
            "type": "string",
            "x-go-name": "AutoRotate"
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
          "customer-frg-id": {
            "description": "The customer fragment ID that will be used to create the DFC key (if empty, the key will be created independently of a customer fragment)",
            "type": "string",
            "x-go-name": "CustomerFragmentID"
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
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "DFCKey name",
            "type": "string",
            "x-go-name": "DFCKeyName"
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
            "description": "The number of days to wait between every automatic rotation (7-365)",
            "type": "string",
            "x-go-name": "RotationInterval"
          },
          "split-level": {
            "description": "The number of fragments that the item will be split into (not includes\ncustomer fragment)",
            "type": "integer",
            "format": "int64",
            "default": 3,
            "x-go-name": "SplitLevel"
          },
          "tag": {
            "description": "List of the tags attached to this DFC key",
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
      "createDFCKeyOutput": {
        "type": "object",
        "properties": {
          "fragment_results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Duration"
            },
            "x-go-name": "FragmentResults"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```