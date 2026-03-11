# Source: https://docs.mystic.ai/reference/patch_v4_scaling_configs__name__patch.md

# Patch

Patch a scaling configuration

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
    "/v4/scaling-configs/{name}": {
      "patch": {
        "tags": [
          "Scaling configurations"
        ],
        "summary": "Patch",
        "description": "Patch a scaling configuration",
        "operationId": "patch_v4_scaling_configs__name__patch",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Name"
            },
            "name": "name",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ScalingConfigPatch"
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
                  "$ref": "#/components/schemas/ScalingConfigGet"
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
      "ScalingConfigGet": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "minimum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Minimum Nodes",
            "default": 0
          },
          "maximum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Maximum Nodes",
            "default": 100
          },
          "type": {
            "$ref": "#/components/schemas/ScalingConfigType"
          },
          "args": {
            "type": "object",
            "title": "Args"
          },
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "title": "Updated At"
          }
        },
        "type": "object",
        "required": [
          "name",
          "type",
          "args",
          "id",
          "created_at",
          "updated_at"
        ],
        "title": "ScalingConfigGet",
        "description": "Base model for schemas."
      },
      "ScalingConfigPatch": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/ScalingConfigType"
          },
          "args": {
            "type": "object",
            "title": "Args"
          },
          "minimum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Minimum Nodes"
          },
          "maximum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Maximum Nodes"
          }
        },
        "additionalProperties": false,
        "type": "object",
        "title": "ScalingConfigPatch",
        "description": "Tag type for marking schemas for patching.\n\nA Patchable schema is one used for updating other schemas."
      },
      "ScalingConfigType": {
        "type": "string",
        "enum": [
          "windows"
        ],
        "title": "ScalingConfigType",
        "description": "An enumeration."
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