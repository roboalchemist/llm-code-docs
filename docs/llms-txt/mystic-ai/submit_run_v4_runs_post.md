# Source: https://docs.mystic.ai/reference/submit_run_v4_runs_post.md

# Submit Run

Submits a new run request

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
    "/v4/runs": {
      "post": {
        "tags": [
          "Runs"
        ],
        "summary": "Submit Run",
        "description": "Submits a new run request",
        "operationId": "submit_run_v4_runs_post",
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
                "schema": {
                  "$ref": "#/components/schemas/ClusterRunResult"
                }
              }
            }
          },
          "401": {
            "description": "Not authenticated",
            "content": {
              "application/json": {
                "example": {
                  "detail": {
                    "message": "Not authenticated."
                  }
                }
              }
            }
          },
          "402": {
            "description": "Account deactivated due to billing. Please add a payment method.",
            "content": {
              "application/json": {
                "example": {
                  "detail": {
                    "message": "Account deactivated due to billing."
                  }
                }
              }
            }
          },
          "403": {
            "description": "Permission denied (for example, accessing a pipeline that is owned by another user)",
            "content": {
              "application/json": {
                "example": {
                  "detail": {
                    "message": "Permission denied accessing resource instance",
                    "parameter": "pipeline"
                  }
                }
              }
            }
          },
          "404": {
            "description": "Resource not found",
            "content": {
              "application/json": {
                "example": {
                  "detail": {
                    "message": "Pipeline not found"
                  }
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
          },
          "503": {
            "description": "This pipeline is currently starting up. This is normal behaviour for pipelines that are new or have not been run in a while. Please wait a few minutes before next run.",
            "content": {
              "application/json": {
                "example": {
                  "id": "run_9602357c47ec478fae194cbbbd701751",
                  "created_at": 1705589076.999664,
                  "updated_at": 1705589076.999664,
                  "pipeline_id": "pipeline_f04db29be7e34264ac7e544095fc4315",
                  "state": "no_resources_available"
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
      "ClusterRunResult": {
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
        "title": "ClusterRunResult",
        "description": "Base model for schemas."
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