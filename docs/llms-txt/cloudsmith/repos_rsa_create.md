# Source: https://help.cloudsmith.io/reference/repos_rsa_create.md

# Set the active RSA key for the Repository.

Set the active RSA key for the Repository.

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
    "/repos/{owner}/{identifier}/rsa/": {
      "post": {
        "operationId": "repos_rsa_create",
        "summary": "Set the active RSA key for the Repository.",
        "description": "Set the active RSA key for the Repository.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryRsaKeyCreate"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "The provided RSA key is the same as the current RSA key.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryRsaKey"
                }
              }
            }
          },
          "201": {
            "description": "The provided RSA key was assigned to the Repository.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryRsaKey"
                }
              }
            }
          },
          "400": {
            "description": "The provided RSA key is not valid",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "402": {
            "description": "Custom RSA keys are not active; upgrade your account!",
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
      "RepositoryRsaKey": {
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
            "description": "The long identifier used by RSA for this key.",
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
            "description": "The SSH fingerprint used by RSA for this key.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "RepositoryRsaKeyCreate": {
        "required": [
          "rsa_private_key"
        ],
        "type": "object",
        "properties": {
          "rsa_passphrase": {
            "title": "Rsa passphrase",
            "description": "The RSA passphrase used for signing.",
            "type": "string",
            "minLength": 1
          },
          "rsa_private_key": {
            "title": "Rsa private key",
            "description": "The RSA private key.",
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```