# Source: https://docs.mystic.ai/reference/index_v4_runs_get.md

# Index

Retrieve a paginated set of runs that satisfy query parameters.

Supported query params:

- `pipeline_id`: filter by a given pipeline ID
    - e.g. `pipeline_id=pipeline_some-random-string`
- `order_by`: order by a given field
    - supported fields are `created_at`, `state`, `compute_time_ms`; default
        is `created_at:desc`
    - e.g. `order_by=compute_time_ms:desc`
- include_pointers: include any pointers that point to the pipelines the runs were
executed against

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
      "get": {
        "tags": [
          "Runs"
        ],
        "summary": "Index",
        "description": "Retrieve a paginated set of runs that satisfy query parameters.\n\nSupported query params:\n\n- `pipeline_id`: filter by a given pipeline ID\n    - e.g. `pipeline_id=pipeline_some-random-string`\n- `order_by`: order by a given field\n    - supported fields are `created_at`, `state`, `compute_time_ms`; default\n        is `created_at:desc`\n    - e.g. `order_by=compute_time_ms:desc`\n- include_pointers: include any pointers that point to the pipelines the runs were\nexecuted against",
        "operationId": "index_v4_runs_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "string",
              "title": "Pipeline Id"
            },
            "name": "pipeline_id",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "boolean",
              "title": "Include Pointers",
              "default": false
            },
            "name": "include_pointers",
            "in": "query"
          },
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
          },
          {
            "required": false,
            "schema": {
              "type": "string",
              "pattern": "[^:]*(:(asc|desc))?$",
              "title": "Order By"
            },
            "name": "order_by",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Paginated_RunGet_"
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
      "Paginated_RunGet_": {
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
              "$ref": "#/components/schemas/RunGet"
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
        "title": "Paginated[RunGet]",
        "description": "Response for paginated resource lists."
      },
      "RunGet": {
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
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "title": "Updated At"
          },
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "pointers": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Pointers"
          },
          "state": {
            "$ref": "#/components/schemas/pipeline__cloud__schemas__runs__RunState"
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
        "title": "RunGet",
        "description": "A brief view of a run"
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