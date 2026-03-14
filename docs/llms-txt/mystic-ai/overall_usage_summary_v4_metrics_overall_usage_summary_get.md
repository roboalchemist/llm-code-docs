# Source: https://docs.mystic.ai/reference/overall_usage_summary_v4_metrics_overall_usage_summary_get.md

# Overall Usage Summary

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
    "/v4/metrics/overall-usage-summary": {
      "get": {
        "tags": [
          "Metrics"
        ],
        "summary": "Overall Usage Summary",
        "operationId": "overall_usage_summary_v4_metrics_overall_usage_summary_get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "format": "date-time",
              "title": "Start"
            },
            "name": "start",
            "in": "query"
          },
          {
            "required": true,
            "schema": {
              "type": "string",
              "format": "date-time",
              "title": "End"
            },
            "name": "end",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "string",
              "title": "Pipeline Id"
            },
            "name": "pipeline_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OverallUsageSummary"
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
      "OverallUsageSummary": {
        "properties": {
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "start": {
            "type": "number",
            "title": "Start"
          },
          "end": {
            "type": "number",
            "title": "End"
          },
          "run_count": {
            "type": "integer",
            "title": "Run Count"
          },
          "failed_run_count": {
            "type": "integer",
            "title": "Failed Run Count"
          },
          "total_compute_time_ms": {
            "type": "integer",
            "title": "Total Compute Time Ms"
          },
          "successful_run_count_change": {
            "type": "number",
            "title": "Successful Run Count Change"
          },
          "failed_run_count_change": {
            "type": "number",
            "title": "Failed Run Count Change"
          }
        },
        "type": "object",
        "required": [
          "start",
          "end",
          "run_count",
          "failed_run_count",
          "total_compute_time_ms"
        ],
        "title": "OverallUsageSummary",
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