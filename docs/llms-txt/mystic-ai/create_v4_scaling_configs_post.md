# Source: https://docs.mystic.ai/reference/create_v4_scaling_configs_post.md

# Create

Create a scaling configuration for pipelines

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
    "/v4/scaling-configs": {
      "post": {
        "tags": [
          "Scaling configurations"
        ],
        "summary": "Create",
        "description": "Create a scaling configuration for pipelines",
        "operationId": "create_v4_scaling_configs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ScalingConfigCreate"
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
      "ScalingConfigCreate": {
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
          }
        },
        "type": "object",
        "required": [
          "name",
          "type",
          "args"
        ],
        "title": "ScalingConfigCreate",
        "description": "Base model for schemas."
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