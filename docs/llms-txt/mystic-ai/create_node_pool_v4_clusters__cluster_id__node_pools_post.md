# Source: https://docs.mystic.ai/reference/create_node_pool_v4_clusters__cluster_id__node_pools_post.md

# Create Node Pool

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
    "/v4/clusters/{cluster_id}/node-pools": {
      "post": {
        "tags": [
          "Cluster"
        ],
        "summary": "Create Node Pool",
        "operationId": "create_node_pool_v4_clusters__cluster_id__node_pools_post",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Cluster Id"
            },
            "name": "cluster_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/NodePoolCreate"
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
                "schema": {}
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
      "Accelerator": {
        "type": "string",
        "enum": [
          "nvidia_t4",
          "nvidia_a100",
          "nvidia_a100_80gb",
          "nvidia_h100",
          "nvidia_l4",
          "cpu",
          "nvidia_a100_5gb",
          "nvidia_a100_10gb",
          "nvidia_a100_20gb",
          "nvidia_a100_80gb_10gb",
          "nvidia_a100_80gb_20gb",
          "nvidia_a100_80gb_40gb",
          "nvidia_a10",
          "nvidia_a10_12gb",
          "nvidia_a10_8gb",
          "nvidia_a10_4gb"
        ],
        "title": "Accelerator",
        "description": "An enumeration."
      },
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
      "NodePoolCreate": {
        "properties": {
          "accelerators": {
            "items": {
              "$ref": "#/components/schemas/Accelerator"
            },
            "type": "array"
          },
          "spot": {
            "type": "boolean",
            "title": "Spot",
            "default": true
          }
        },
        "type": "object",
        "required": [
          "accelerators"
        ],
        "title": "NodePoolCreate",
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