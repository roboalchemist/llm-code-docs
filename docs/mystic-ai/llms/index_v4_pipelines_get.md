# Source: https://docs.mystic.ai/reference/index_v4_pipelines_get.md

# Index

Retrieve a paginated set of pipelines.

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
    "/v4/pipelines": {
      "get": {
        "tags": [
          "Pipelines"
        ],
        "summary": "Index",
        "description": "Retrieve a paginated set of pipelines.",
        "operationId": "index_v4_pipelines_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Skip",
              "default": 0
            },
            "name": "skip",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Limit",
              "default": 20
            },
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Paginated_PipelineGet_"
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
      "IOVariable": {
        "properties": {
          "run_io_type": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunIOType"
          },
          "title": {
            "type": "string",
            "title": "Title"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "examples": {
            "items": {},
            "type": "array",
            "title": "Examples"
          },
          "gt": {
            "type": "integer",
            "title": "Gt"
          },
          "ge": {
            "type": "integer",
            "title": "Ge"
          },
          "lt": {
            "type": "integer",
            "title": "Lt"
          },
          "le": {
            "type": "integer",
            "title": "Le"
          },
          "multiple_of": {
            "type": "integer",
            "title": "Multiple Of"
          },
          "allow_inf_nan": {
            "type": "boolean",
            "title": "Allow Inf Nan"
          },
          "max_digits": {
            "type": "integer",
            "title": "Max Digits"
          },
          "decimal_places": {
            "type": "integer",
            "title": "Decimal Places"
          },
          "min_length": {
            "type": "integer",
            "title": "Min Length"
          },
          "max_length": {
            "type": "integer",
            "title": "Max Length"
          },
          "choices": {
            "items": {},
            "type": "array",
            "title": "Choices"
          },
          "dict_schema": {
            "items": {
              "type": "object"
            },
            "type": "array",
            "title": "Dict Schema"
          },
          "default": {
            "title": "Default"
          },
          "optional": {
            "type": "boolean",
            "title": "Optional"
          }
        },
        "type": "object",
        "required": [
          "run_io_type"
        ],
        "title": "IOVariable",
        "description": "Base model for schemas."
      },
      "Paginated_PipelineGet_": {
        "properties": {
          "skip": {
            "type": "integer",
            "minimum": 0,
            "title": "Skip"
          },
          "limit": {
            "type": "integer",
            "maximum": 1000,
            "minimum": 1,
            "title": "Limit"
          },
          "total": {
            "type": "integer",
            "minimum": 0,
            "title": "Total"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/PipelineGet"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "skip",
          "limit",
          "total",
          "data"
        ],
        "title": "Paginated[PipelineGet]",
        "description": "Response for paginated resource lists."
      },
      "PipelineClusterConfig": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "node_pool": {
            "type": "string",
            "title": "Node Pool"
          }
        },
        "type": "object",
        "required": [
          "id",
          "node_pool"
        ],
        "title": "PipelineClusterConfig"
      },
      "PipelineContainerState": {
        "properties": {
          "state": {
            "$ref": "#/components/schemas/PipelineState"
          },
          "message": {
            "type": "string",
            "title": "Message"
          }
        },
        "type": "object",
        "required": [
          "state"
        ],
        "title": "PipelineContainerState",
        "description": "Base model for schemas."
      },
      "PipelineGet": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "image": {
            "type": "string",
            "title": "Image"
          },
          "input_variables": {
            "items": {
              "$ref": "#/components/schemas/IOVariable"
            },
            "type": "array",
            "title": "Input Variables"
          },
          "output_variables": {
            "items": {
              "$ref": "#/components/schemas/IOVariable"
            },
            "type": "array",
            "title": "Output Variables"
          },
          "extras": {
            "type": "object",
            "title": "Extras"
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
          "accelerators": {
            "items": {
              "$ref": "#/components/schemas/Accelerator"
            },
            "type": "array"
          },
          "cluster": {
            "$ref": "#/components/schemas/PipelineClusterConfig"
          },
          "scaling_config": {
            "type": "string",
            "title": "Scaling Config"
          },
          "failed_state_info": {
            "$ref": "#/components/schemas/PipelineContainerState"
          }
        },
        "type": "object",
        "required": [
          "name",
          "image",
          "input_variables",
          "output_variables",
          "id",
          "created_at",
          "updated_at"
        ],
        "title": "PipelineGet",
        "description": "Base model for schemas."
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