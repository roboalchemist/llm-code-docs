# Source: https://docs.mystic.ai/reference/retrieve_detailed_v4_runs__run_id__detailed_get.md

# Retrieve Detailed

Retrieve a more detailed version of a run.

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
    "/v4/runs/{run_id}/detailed": {
      "get": {
        "tags": [
          "Runs"
        ],
        "summary": "Retrieve Detailed",
        "description": "Retrieve a more detailed version of a run.",
        "operationId": "retrieve_detailed_v4_runs__run_id__detailed_get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Run Id"
            },
            "name": "run_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/app__schemas__run__GetDetailed"
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
      "ContainerRunError": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/ContainerRunErrorType"
          },
          "message": {
            "type": "string",
            "title": "Message"
          },
          "traceback": {
            "type": "string",
            "title": "Traceback"
          }
        },
        "type": "object",
        "required": [
          "type",
          "message"
        ],
        "title": "ContainerRunError",
        "description": "Base model for schemas."
      },
      "ContainerRunErrorType": {
        "type": "string",
        "enum": [
          "input_error",
          "cuda_oom",
          "cuda_error",
          "oom",
          "pipeline_error",
          "startup_error",
          "pipeline_loading",
          "timeout",
          "unknown"
        ],
        "title": "ContainerRunErrorType",
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
      "app__schemas__run__GetDetailed": {
        "properties": {
          "inputs": {
            "items": {
              "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunInput"
            },
            "type": "array",
            "title": "Inputs"
          },
          "outputs": {
            "items": {
              "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunOutput"
            },
            "type": "array",
            "title": "Outputs"
          },
          "error": {
            "$ref": "#/components/schemas/ContainerRunError"
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
          },
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "state": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunState"
          },
          "queue_position": {
            "type": "integer",
            "title": "Queue Position"
          },
          "compute_time_ms": {
            "type": "integer",
            "title": "Compute Time Ms"
          },
          "started_at": {
            "type": "string",
            "format": "date-time",
            "title": "Started At"
          },
          "ended_at": {
            "type": "string",
            "format": "date-time",
            "title": "Ended At"
          },
          "accelerators": {
            "items": {
              "$ref": "#/components/schemas/Accelerator"
            },
            "type": "array"
          }
        },
        "type": "object",
        "required": [
          "id",
          "created_at",
          "updated_at",
          "pipeline_id",
          "state"
        ],
        "title": "GetDetailed",
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
      },
      "pipeline__cloud__schemas__runs__RunOutput": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunIOType"
          },
          "value": {
            "title": "Value"
          },
          "file": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunOutputFile"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "RunOutput",
        "description": "Base model for schemas."
      },
      "pipeline__cloud__schemas__runs__RunOutputFile": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "path": {
            "type": "string",
            "title": "Path"
          },
          "url": {
            "type": "string",
            "title": "Url"
          },
          "size": {
            "type": "integer",
            "title": "Size"
          }
        },
        "type": "object",
        "required": [
          "name",
          "path",
          "size"
        ],
        "title": "RunOutputFile",
        "description": "Base model for schemas."
      },
      "pipeline__cloud__schemas__runs__RunState": {
        "type": "string",
        "enum": [
          "created",
          "routing",
          "queued",
          "running",
          "completed",
          "failed",
          "no_resources_available",
          "node_preempted",
          "unknown"
        ],
        "title": "RunState",
        "description": "An enumeration."
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