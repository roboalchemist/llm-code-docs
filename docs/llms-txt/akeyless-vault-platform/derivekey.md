# Source: https://docs.akeyless.io/reference/derivekey.md

# /derive-key

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
    "/derive-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "DeriveKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DeriveKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/DeriveKeyResponse"
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
      "DeriveKeyResponse": {
        "description": "DeriveKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/DeriveKeyOutput"
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
      "DeriveKey": {
        "type": "object",
        "title": "DeriveKey is a command that gets a static secret value.",
        "required": [
          "alg",
          "key-len",
          "iter",
          "name"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "alg": {
            "description": "Kdf algorithm",
            "type": "string",
            "default": "pbkdf2",
            "x-go-name": "KDFAlgorithm"
          },
          "hash-function": {
            "description": "HashFunction the hash function to use (relevant for pbkdf2)",
            "type": "string",
            "default": "sha256",
            "x-go-name": "HashFunction"
          },
          "iter": {
            "description": "IterationCount the number of iterations",
            "type": "integer",
            "format": "int64",
            "x-go-name": "IterationCount"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-len": {
            "description": "KeyLength the byte length of the generated key",
            "type": "integer",
            "format": "int64",
            "x-go-name": "KeyLength"
          },
          "mem": {
            "description": "MemorySizeInKb the memory paramter in kb (relevant for argon2id)",
            "type": "integer",
            "format": "int64",
            "default": 16384,
            "x-go-name": "MemorySizeInKb"
          },
          "name": {
            "description": "Static Secret full name",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "parallelism": {
            "description": "Parallelism the number of threads to use (relevant for argon2id)",
            "type": "integer",
            "format": "int64",
            "default": 1,
            "x-go-name": "Parallelism"
          },
          "salt": {
            "description": "Salt Base64 encoded salt value. If not provided, the salt will be generated as part of the operation. The salt should be securely-generated random bytes, minimum 64 bits, 128 bits is recommended",
            "type": "string",
            "x-go-name": "Salt"
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
      "DeriveKeyOutput": {
        "type": "object",
        "properties": {
          "Key": {
            "type": "string"
          },
          "Salt": {
            "type": "string"
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
      }
    }
  }
}
```