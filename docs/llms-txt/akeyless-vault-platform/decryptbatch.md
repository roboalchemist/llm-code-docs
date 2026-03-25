# Source: https://docs.akeyless.io/reference/decryptbatch.md

# /decrypt-batch

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
    "/decrypt-batch": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "decryptBatch",
        "requestBody": {
          "$ref": "#/components/requestBodies/BatchEncryptionRequest"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/decryptResponse"
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
      "decryptResponse": {
        "description": "decryptResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/decryptOutput"
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
    "requestBodies": {
      "BatchEncryptionRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/BatchEncryptionRequest"
            }
          }
        },
        "required": true,
        "x-go-name": "Body"
      }
    },
    "schemas": {
      "BatchEncryptionRequest": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/BatchEncryptionRequestLine"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "BatchEncryptionRequestLine": {
        "type": "object",
        "properties": {
          "context": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "EncContext"
          },
          "data": {
            "type": "string",
            "x-go-name": "DataBase64"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemId"
          },
          "item_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "ItemVersion"
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
      "decryptOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```