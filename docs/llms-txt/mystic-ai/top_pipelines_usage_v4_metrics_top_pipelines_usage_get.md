# Source: https://docs.mystic.ai/reference/top_pipelines_usage_v4_metrics_top_pipelines_usage_get.md

# Top Pipelines Usage

Retrieve usage metrics for top 'num_pipelines' (in terms of number of
runs) for the provided time period.

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
    "/v4/metrics/top-pipelines-usage": {
      "get": {
        "tags": [
          "Metrics"
        ],
        "summary": "Top Pipelines Usage",
        "description": "Retrieve usage metrics for top 'num_pipelines' (in terms of number of\nruns) for the provided time period.",
        "operationId": "top_pipelines_usage_v4_metrics_top_pipelines_usage_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Num Pipelines",
              "default": 20
            },
            "name": "num_pipelines",
            "in": "query"
          },
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
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/DurationUnit"
            },
            "name": "interval_unit",
            "in": "query"
          },
          {
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Interval Value"
            },
            "name": "interval_value",
            "in": "query"
          }
        ],
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
      "DurationUnit": {
        "type": "string",
        "enum": [
          "seconds",
          "minutes",
          "hours",
          "days",
          "weeks"
        ],
        "title": "DurationUnit",
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