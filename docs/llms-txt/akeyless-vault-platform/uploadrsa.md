# Source: https://docs.akeyless.io/reference/uploadrsa.md

# /upload-rsa

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
    "/upload-rsa": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uploadRSA",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uploadRSA"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uploadRSAResponse"
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
      "uploadRSAResponse": {
        "description": "uploadRSAResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/uploadRSAOutput"
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
      "uploadRSA": {
        "type": "object",
        "title": "uploadRSA is a command that uploads RSA key.",
        "required": [
          "name",
          "alg"
        ],
        "properties": {
          "alg": {
            "description": "Key type. options: [RSA1024, RSA2048, RSA3072, RSA4096]",
            "type": "string",
            "x-go-name": "Alg"
          },
          "cert-file-data": {
            "description": "Certificate in a PEM format.",
            "type": "string",
            "x-go-name": "CertFileData"
          },
          "certificate-format": {
            "$ref": "#/components/schemas/CertificateFormat"
          },
          "customer-frg-id": {
            "description": "The customer fragment ID that will be used to split the key (if empty,\nthe key will be created independently of a customer fragment)",
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
            "description": "Name of key to be created",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "overwrite": {
            "description": "When the overwrite flag is set, this command will only update an existing key [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "Overwrite"
          },
          "rsa-file-data": {
            "description": "RSA private key data, base64 encoded",
            "type": "string",
            "x-go-name": "RSAFileData"
          },
          "split-level": {
            "description": "The number of fragments that the item will be split into",
            "type": "integer",
            "format": "int64",
            "default": 3,
            "x-go-name": "SplitLevel"
          },
          "tag": {
            "description": "List of the tags attached to this key",
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
      "uploadRSAOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```