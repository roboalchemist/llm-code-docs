# Source: https://docs.mystic.ai/reference/create_v4_pointers_post.md

# Create

Create a pipeline pointer instance.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/pointers": {
      "post": {
        "tags": [
          "Pointers"
        ],
        "summary": "Create",
        "description": "Create a pipeline pointer instance.",
        "operationId": "create_v4_pointers_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PointerCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PointerGet"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          },
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "PointerCreate": {
        "properties": {
          "pointer_or_pipeline_id": {
            "type": "string",
            "title": "Pointer Or Pipeline Id"
          },
          "pointer": {
            "type": "string",
            "title": "Pointer"
          },
          "locked": {
            "type": "boolean",
            "title": "Locked"
          }
        },
        "type": "object",
        "required": [
          "pointer_or_pipeline_id",
          "pointer"
        ],
        "title": "PointerCreate",
        "description": "Base model for schemas."
      },
      "PointerGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "pointer": {
            "type": "string",
            "title": "Pointer"
          },
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "locked": {
            "type": "boolean",
            "title": "Locked"
          }
        },
        "type": "object",
        "required": [
          "id",
          "pointer",
          "pipeline_id",
          "locked"
        ],
        "title": "PointerGet",
        "description": "Base model for schemas."
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      },
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```