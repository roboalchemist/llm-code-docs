# Source: https://docs.akeyless.io/reference/detokenizebatch.md

# /detokenize-batch

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
    "/detokenize-batch": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "detokenizeBatch",
        "requestBody": {
          "$ref": "#/components/requestBodies/BatchTokenizationRequest"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/detokenizeResponse"
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
      "detokenizeResponse": {
        "description": "detokenizeResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/detokenizeOutput"
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
      "BatchTokenizationRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/BatchTokenizationRequest"
            }
          }
        },
        "required": true,
        "x-go-name": "Body"
      }
    },
    "schemas": {
      "BatchTokenizationRequest": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/BatchTokenizationRequestLine"
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "BatchTokenizationRequestLine": {
        "type": "object",
        "properties": {
          "data": {
            "type": "string",
            "x-go-name": "Data"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemId"
          },
          "tweak": {
            "type": "string",
            "x-go-name": "TweakBase64"
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
      "detokenizeOutput": {
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