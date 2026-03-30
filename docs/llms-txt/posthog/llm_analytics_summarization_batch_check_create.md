# Source: https://posthog.com/docs/open-api-spec/llm_analytics_summarization_batch_check_create.md

# llm_analytics_summarization_batch_check_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/summarization/batch_check/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/summarization/batch_check/": {
      "post": {
        "operationId": "llm_analytics_summarization_batch_check_create",
        "description": "\nCheck which traces have cached summaries available.\n\nThis endpoint allows batch checking of multiple trace IDs to see which ones\nhave cached summaries. Returns only the traces that have cached summaries\nwith their titles.\n\n**Use Cases:**\n- Load cached summaries on session view load\n- Avoid unnecessary LLM calls for already-summarized traces\n- Display summary previews without generating new summaries\n        ",
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
                "$ref": "#/components/schemas/BatchCheckRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/BatchCheckRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/BatchCheckRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BatchCheckResponse"
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
          "403": {
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
      "BatchCheckRequest": {
        "type": "object",
        "properties": {
          "trace_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of trace IDs to check for cached summaries",
            "maxItems": 100
          },
          "mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Mode02aEnum"
              }
            ],
            "default": "minimal",
            "description": "Summary detail level to check for\n\n* `minimal` - minimal\n* `detailed` - detailed"
          },
          "model": {
            "type": "string",
            "nullable": true,
            "description": "LLM model used for cached summaries"
          }
        },
        "required": [
          "trace_ids"
        ]
      },
      "BatchCheckResponse": {
        "type": "object",
        "properties": {
          "summaries": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CachedSummary"
            }
          }
        },
        "required": [
          "summaries"
        ]
      },
      "Mode02aEnum": {
        "enum": [
          "minimal",
          "detailed"
        ],
        "type": "string",
        "description": "* `minimal` - minimal\n* `detailed` - detailed"
      },
      "CachedSummary": {
        "type": "object",
        "properties": {
          "trace_id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "cached": {
            "type": "boolean",
            "default": true
          }
        },
        "required": [
          "title",
          "trace_id"
        ]
      }
    }
  }
}
```
