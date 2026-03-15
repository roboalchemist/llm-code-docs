# Source: https://posthog.com/docs/open-api-spec/llm_analytics_sentiment_create.md

# llm_analytics_sentiment_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/sentiment/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/sentiment/": {
      "post": {
        "operationId": "llm_analytics_sentiment_create",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "LLM Analytics",
          "llm_analytics"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SentimentRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SentimentRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SentimentRequest"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "llm_analytics:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SentimentBatchResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {}
                }
              }
            },
            "description": ""
          },
          "500": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {}
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "LLM Analytics",
          "llm_analytics"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "SentimentRequest": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "maxItems": 5,
            "minItems": 1
          },
          "analysis_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AnalysisLevelEnum"
              }
            ],
            "default": "trace"
          },
          "force_refresh": {
            "type": "boolean",
            "default": false
          },
          "date_from": {
            "type": "string",
            "nullable": true
          },
          "date_to": {
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "ids"
        ]
      },
      "SentimentBatchResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/SentimentResult"
            }
          }
        },
        "required": [
          "results"
        ]
      },
      "AnalysisLevelEnum": {
        "enum": [
          "trace",
          "generation"
        ],
        "type": "string",
        "description": "* `trace` - trace\n* `generation` - generation"
      },
      "SentimentResult": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string"
          },
          "score": {
            "type": "number",
            "format": "double"
          },
          "scores": {
            "type": "object",
            "additionalProperties": {
              "type": "number",
              "format": "double"
            }
          },
          "messages": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/MessageSentiment"
            }
          },
          "message_count": {
            "type": "integer"
          }
        },
        "required": [
          "label",
          "message_count",
          "messages",
          "score",
          "scores"
        ]
      },
      "MessageSentiment": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string"
          },
          "score": {
            "type": "number",
            "format": "double"
          },
          "scores": {
            "type": "object",
            "additionalProperties": {
              "type": "number",
              "format": "double"
            }
          }
        },
        "required": [
          "label",
          "score",
          "scores"
        ]
      }
    }
  }
}
```
