# Source: https://docs.mystic.ai/reference/pointers_patch_v4_pointers__pointer__patch.md

# Pointers Patch

Update a pipeline pointer instance.

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
    "/v4/pointers/{pointer}": {
      "patch": {
        "tags": [
          "Pointers"
        ],
        "summary": "Pointers Patch",
        "description": "Update a pipeline pointer instance.",
        "operationId": "pointers_patch_v4_pointers__pointer__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Pointer"
            },
            "name": "pointer",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PointerPatch"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
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
      "PointerPatch": {
        "properties": {
          "pointer_or_pipeline_id": {
            "type": "string",
            "title": "Pointer Or Pipeline Id"
          },
          "locked": {
            "type": "boolean",
            "title": "Locked"
          }
        },
        "type": "object",
        "title": "PointerPatch",
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