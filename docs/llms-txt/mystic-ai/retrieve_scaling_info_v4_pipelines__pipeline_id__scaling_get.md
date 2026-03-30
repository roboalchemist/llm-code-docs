# Source: https://docs.mystic.ai/reference/retrieve_scaling_info_v4_pipelines__pipeline_id__scaling_get.md

# Retrieve Scaling Info

Get real-time scaling information for the given pipeline.

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
    "/v4/pipelines/{pipeline_id}/scaling": {
      "get": {
        "tags": [
          "Pipelines"
        ],
        "summary": "Retrieve Scaling Info",
        "description": "Get real-time scaling information for the given pipeline.",
        "operationId": "retrieve_scaling_info_v4_pipelines__pipeline_id__scaling_get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Pipeline Id"
            },
            "name": "pipeline_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PipelineScalingInfo"
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
      "PipelineScalingInfo": {
        "properties": {
          "current_replicas": {
            "type": "integer",
            "title": "Current Replicas"
          },
          "desired_replicas": {
            "type": "integer",
            "title": "Desired Replicas"
          },
          "current_pipeline_states": {
            "additionalProperties": {
              "type": "integer"
            },
            "type": "object",
            "title": "Current Pipeline States"
          }
        },
        "type": "object",
        "required": [
          "current_replicas",
          "desired_replicas",
          "current_pipeline_states"
        ],
        "title": "PipelineScalingInfo",
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