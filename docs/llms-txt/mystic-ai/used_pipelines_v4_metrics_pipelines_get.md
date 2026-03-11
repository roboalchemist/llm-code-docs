# Source: https://docs.mystic.ai/reference/used_pipelines_v4_metrics_pipelines_get.md

# Used Pipelines

Retrieve paginated metrics for all pipelines used by a user, optionally
filtered by 'search'.

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
    "/v4/metrics/pipelines": {
      "get": {
        "tags": [
          "Metrics"
        ],
        "summary": "Used Pipelines",
        "description": "Retrieve paginated metrics for all pipelines used by a user, optionally\nfiltered by 'search'.",
        "operationId": "used_pipelines_v4_metrics_pipelines_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "string",
              "title": "Search"
            },
            "name": "search",
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
                  "$ref": "#/components/schemas/Paginated_PipelineMetrics_"
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
      "Paginated_PipelineMetrics_": {
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
              "$ref": "#/components/schemas/PipelineMetrics"
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
        "title": "Paginated[PipelineMetrics]",
        "description": "Response for paginated resource lists."
      },
      "PipelineMetrics": {
        "properties": {
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "pipeline_name": {
            "type": "string",
            "title": "Pipeline Name"
          },
          "pointers": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Pointers"
          },
          "run_count": {
            "type": "integer",
            "title": "Run Count"
          },
          "failed_run_count": {
            "type": "integer",
            "title": "Failed Run Count"
          },
          "last_run_at": {
            "type": "string",
            "format": "date-time",
            "title": "Last Run At"
          },
          "last_failed_at": {
            "type": "string",
            "format": "date-time",
            "title": "Last Failed At"
          },
          "avg_compute_time_ms": {
            "type": "integer",
            "title": "Avg Compute Time Ms"
          },
          "total_compute_time_ms": {
            "type": "integer",
            "title": "Total Compute Time Ms"
          }
        },
        "type": "object",
        "required": [
          "pipeline_id",
          "pipeline_name",
          "pointers",
          "run_count",
          "failed_run_count",
          "avg_compute_time_ms",
          "total_compute_time_ms"
        ],
        "title": "PipelineMetrics",
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