# Source: https://docs.mystic.ai/reference/stream_run_v4_runs_stream_post.md

# Stream Run

Submit a new streaming run request, where the run output is streamed as
it becomes available, rather than waiting for all the data to be
generated.

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
    "/v4/runs/stream": {
      "post": {
        "tags": [
          "Runs"
        ],
        "summary": "Stream Run",
        "description": "Submit a new streaming run request, where the run output is streamed as\nit becomes available, rather than waiting for all the data to be\ngenerated.",
        "operationId": "stream_run_v4_runs_stream_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunCreate"
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
      },
      "pipeline__cloud__schemas__runs__RunCreate": {
        "properties": {
          "run_id": {
            "type": "string",
            "title": "Run Id"
          },
          "inputs": {
            "items": {
              "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunInput"
            },
            "type": "array",
            "title": "Inputs"
          },
          "pipeline": {
            "type": "string",
            "title": "Pipeline"
          },
          "async_run": {
            "type": "boolean",
            "title": "Async Run",
            "default": false
          },
          "wait_for_resources": {
            "type": "boolean",
            "title": "Wait For Resources"
          }
        },
        "type": "object",
        "required": [
          "inputs",
          "pipeline"
        ],
        "title": "RunCreate",
        "description": "Base model for schemas."
      },
      "pipeline__cloud__schemas__runs__RunIOType": {
        "type": "string",
        "enum": [
          "integer",
          "string",
          "fp",
          "dictionary",
          "boolean",
          "none",
          "array",
          "pkl",
          "file",
          "stream"
        ],
        "title": "RunIOType",
        "description": "An enumeration."
      },
      "pipeline__cloud__schemas__runs__RunInput": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunIOType"
          },
          "value": {
            "title": "Value"
          },
          "file_name": {
            "type": "string",
            "title": "File Name"
          },
          "file_path": {
            "type": "string",
            "title": "File Path"
          },
          "file_url": {
            "type": "string",
            "title": "File Url"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "RunInput",
        "description": "Base model for schemas."
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