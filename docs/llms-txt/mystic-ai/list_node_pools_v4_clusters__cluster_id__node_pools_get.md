# Source: https://docs.mystic.ai/reference/list_node_pools_v4_clusters__cluster_id__node_pools_get.md

# List Node Pools

List node pools for a given cluster

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
      "get": {
        "tags": [
          "Cluster"
        ],
        "summary": "List Node Pools",
        "description": "List node pools for a given cluster",
        "operationId": "list_node_pools_v4_clusters__cluster_id__node_pools_get",
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
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/NodePool"
                  },
                  "type": "array",
                  "title": "Response List Node Pools V4 Clusters  Cluster Id  Node Pools Get"
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
      "NodePool": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "accelerators": {
            "items": {
              "$ref": "#/components/schemas/Accelerator"
            },
            "type": "array"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "autoscaling": {
            "$ref": "#/components/schemas/NodePoolAutoscaling"
          },
          "console_link": {
            "type": "string",
            "maxLength": 2083,
            "minLength": 1,
            "format": "uri",
            "title": "Console Link"
          },
          "use_spot_instances": {
            "type": "boolean",
            "title": "Use Spot Instances",
            "default": false
          },
          "num_pipelines": {
            "type": "integer",
            "title": "Num Pipelines",
            "default": 0
          }
        },
        "type": "object",
        "required": [
          "name",
          "accelerators",
          "status",
          "console_link"
        ],
        "title": "NodePool",
        "description": "Base model for schemas."
      },
      "NodePoolAutoscaling": {
        "properties": {
          "min_nodes": {
            "type": "integer",
            "title": "Min Nodes"
          },
          "max_nodes": {
            "type": "integer",
            "title": "Max Nodes"
          },
          "current_nodes": {
            "type": "integer",
            "title": "Current Nodes"
          }
        },
        "type": "object",
        "required": [
          "min_nodes",
          "max_nodes",
          "current_nodes"
        ],
        "title": "NodePoolAutoscaling",
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