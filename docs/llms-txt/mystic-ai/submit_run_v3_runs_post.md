# Source: https://docs.mystic.ai/reference/submit_run_v3_runs_post.md

# Submit Run

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
    "/v3/runs": {
      "post": {
        "tags": [
          "V3 compatibility"
        ],
        "summary": "Submit Run",
        "operationId": "submit_run_v3_runs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/app__routes__v3_compatability__RunCreate"
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
                  "$ref": "#/components/schemas/Run"
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
      "Run": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "environment_id": {
            "type": "string",
            "title": "Environment Id"
          },
          "environment_hash": {
            "type": "string",
            "title": "Environment Hash"
          },
          "state": {
            "$ref": "#/components/schemas/app__routes__v3_compatability__RunState"
          },
          "error": {
            "$ref": "#/components/schemas/RunError"
          },
          "result": {
            "$ref": "#/components/schemas/RunResult"
          },
          "input_data": {
            "items": {
              "$ref": "#/components/schemas/app__routes__v3_compatability__RunInput"
            },
            "type": "array",
            "title": "Input Data"
          }
        },
        "type": "object",
        "required": [
          "id",
          "created_at",
          "pipeline_id",
          "environment_id",
          "environment_hash",
          "state"
        ],
        "title": "Run",
        "description": "Base model for schemas."
      },
      "RunError": {
        "properties": {
          "exception": {
            "type": "string",
            "title": "Exception"
          },
          "traceback": {
            "type": "string",
            "title": "Traceback"
          }
        },
        "type": "object",
        "required": [
          "exception"
        ],
        "title": "RunError",
        "description": "Base model for schemas."
      },
      "RunResult": {
        "properties": {
          "run_id": {
            "type": "string",
            "title": "Run Id"
          },
          "outputs": {
            "items": {
              "$ref": "#/components/schemas/app__routes__v3_compatability__RunOutput"
            },
            "type": "array",
            "title": "Outputs"
          }
        },
        "type": "object",
        "required": [
          "run_id",
          "outputs"
        ],
        "title": "RunResult",
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
      },
      "app__routes__v3_compatability__RunCreate": {
        "properties": {
          "pipeline_id_or_pointer": {
            "type": "string",
            "title": "Pipeline Id Or Pointer"
          },
          "input_data": {
            "items": {
              "$ref": "#/components/schemas/app__routes__v3_compatability__RunInput"
            },
            "type": "array",
            "title": "Input Data"
          },
          "async_run": {
            "type": "boolean",
            "title": "Async Run",
            "default": false
          }
        },
        "type": "object",
        "required": [
          "pipeline_id_or_pointer",
          "input_data"
        ],
        "title": "RunCreate",
        "description": "Base model for schemas."
      },
      "app__routes__v3_compatability__RunIOType": {
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
          "file"
        ],
        "title": "RunIOType",
        "description": "An enumeration."
      },
      "app__routes__v3_compatability__RunInput": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/app__routes__v3_compatability__RunIOType"
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
      "app__routes__v3_compatability__RunOutput": {
        "properties": {
          "type": {
            "$ref": "#/components/schemas/app__routes__v3_compatability__RunIOType"
          },
          "value": {
            "title": "Value"
          },
          "file": {
            "$ref": "#/components/schemas/app__routes__v3_compatability__RunOutputFile"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "RunOutput",
        "description": "Base model for schemas."
      },
      "app__routes__v3_compatability__RunOutputFile": {
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
          "url",
          "size"
        ],
        "title": "RunOutputFile",
        "description": "Base model for schemas."
      },
      "app__routes__v3_compatability__RunState": {
        "type": "integer",
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          22,
          16,
          11,
          14,
          15,
          13,
          21,
          10,
          12,
          17,
          18,
          19,
          23,
          20
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