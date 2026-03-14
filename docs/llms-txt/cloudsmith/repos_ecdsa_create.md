# Source: https://help.cloudsmith.io/reference/repos_ecdsa_create.md

# Set the active ECDSA key for the Repository.

Set the active ECDSA key for the Repository.

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
    "/repos/{owner}/{identifier}/ecdsa/": {
      "post": {
        "operationId": "repos_ecdsa_create",
        "summary": "Set the active ECDSA key for the Repository.",
        "description": "Set the active ECDSA key for the Repository.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryEcdsaKeyCreate"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "The provided ECDSA key is the same as the current ECDSA key.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryEcdsaKey"
                }
              }
            }
          },
          "201": {
            "description": "The provided ECDSA key was assigned to the Repository.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryEcdsaKey"
                }
              }
            }
          },
          "400": {
            "description": "The provided ECDSA key is not valid",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "402": {
            "description": "Custom ECDSA keys are not active; upgrade your account!",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Organization/Repository does not exist, or you do not have permissions.",
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
      "RepositoryEcdsaKey": {
        "type": "object",
        "properties": {
          "active": {
            "title": "Active",
            "description": "If selected this is the active key for this repository.",
            "type": "boolean",
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
          "fingerprint": {
            "title": "Fingerprint",
            "description": "The long identifier used by ECDSA for this key.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "fingerprint_short": {
            "title": "Fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "public_key": {
            "title": "Public key",
            "description": "The public key given to repository users.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "ssh_fingerprint": {
            "title": "Ssh fingerprint",
            "description": "The SSH fingerprint used by ECDSA for this key.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "RepositoryEcdsaKeyCreate": {
        "required": [
          "ecdsa_private_key"
        ],
        "type": "object",
        "properties": {
          "ecdsa_passphrase": {
            "title": "Ecdsa passphrase",
            "description": "The ECDSA passphrase used for signing.",
            "type": "string",
            "minLength": 1
          },
          "ecdsa_private_key": {
            "title": "Ecdsa private key",
            "description": "The ECDSA private key.",
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```