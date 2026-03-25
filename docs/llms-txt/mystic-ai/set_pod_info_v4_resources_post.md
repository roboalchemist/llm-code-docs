# Source: https://docs.mystic.ai/reference/set_pod_info_v4_resources_post.md

# Set Pod Info

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
    "/v4/resources": {
      "post": {
        "tags": [
          "resources"
        ],
        "summary": "Set Pod Info",
        "operationId": "set_pod_info_v4_resources_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ResourcePodInfo"
              }
            }
          },
          "required": true
        },
        "responses": {
          "204": {
            "description": "Successful Response"
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
            "HTTPBearer": []
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
      "PipelineState": {
        "type": "string",
        "enum": [
          "not_loaded",
          "loading",
          "loaded",
          "load_failed",
          "startup_failed",
          "failed"
        ],
        "title": "PipelineState",
        "description": "An enumeration."
      },
      "ResourcePodInfo": {
        "properties": {
          "pod_name": {
            "type": "string",
            "title": "Pod Name"
          },
          "pod_ip": {
            "type": "string",
            "title": "Pod Ip"
          },
          "node_name": {
            "type": "string",
            "title": "Node Name"
          },
          "state": {
            "$ref": "#/components/schemas/PipelineState"
          }
        },
        "type": "object",
        "required": [
          "pod_name",
          "pod_ip",
          "node_name",
          "state"
        ],
        "title": "ResourcePodInfo",
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