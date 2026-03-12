# Source: https://help.cloudsmith.io/reference/repos_x509_ecdsa_list.md

# Retrieve the active X.509 ECDSA certificate for the Repository.

Retrieve the active X.509 ECDSA certificate for the Repository.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/repos/{owner}/{identifier}/x509-ecdsa/": {
      "get": {
        "operationId": "repos_x509_ecdsa_list",
        "summary": "Retrieve the active X.509 ECDSA certificate for the Repository.",
        "description": "Retrieve the active X.509 ECDSA certificate for the Repository.",
        "responses": {
          "200": {
            "description": "Retrieved the active X.509 ECDSA Certificate.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryX509EcdsaCertificate"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "repos"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "identifier",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "RepositoryX509EcdsaCertificate": {
        "type": "object",
        "properties": {
          "active": {
            "title": "Active",
            "description": "If selected this is the active key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "certificate": {
            "title": "Certificate",
            "description": "The issued certificate.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "certificate_chain": {
            "title": "Certificate chain",
            "description": "Base64 encoded CA certificate chain.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "certificate_chain_fingerprint": {
            "title": "Certificate chain fingerprint",
            "type": "string",
            "readOnly": true
          },
          "certificate_chain_fingerprint_short": {
            "title": "Certificate chain fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "certificate_fingerprint": {
            "title": "Certificate fingerprint",
            "description": "The SHA-256 long identifier used",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "certificate_fingerprint_short": {
            "title": "Certificate fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "default": {
            "title": "Default",
            "description": "If selected this is the default key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "issuing_status": {
            "title": "Issuing status",
            "type": "string",
            "enum": [
              "Certificate is pending to be issued",
              "Certificate successfully issued",
              "Error issuing certificate"
            ],
            "default": "Certificate is pending to be issued"
          }
        }
      }
    }
  }
}
```