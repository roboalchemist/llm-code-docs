# Source: https://posthog.com/docs/open-api-spec/llm_analytics_evaluation_summary_create.md

# llm_analytics_evaluation_summary_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/evaluation_summary/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/evaluation_summary/": {
      "post": {
        "operationId": "llm_analytics_evaluation_summary_create",
        "description": "\nGenerate an AI-powered summary of evaluation results.\n\nThis endpoint analyzes evaluation runs and identifies patterns in passing\nand failing evaluations, providing actionable recommendations.\n\nData is fetched server-side by evaluation ID to ensure data integrity.\n\n**Use Cases:**\n- Understand why evaluations are passing or failing\n- Identify systematic issues in LLM responses\n- Get recommendations for improving response quality\n- Review patterns across many evaluation runs at once\n        ",
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
                "$ref": "#/components/schemas/EvaluationSummaryRequest"
              },
              "examples": {
                "EvaluationSummaryRequest": {
                  "value": {
                    "evaluation_id": "550e8400-e29b-41d4-a716-446655440000",
                    "filter": "all",
                    "force_refresh": false
                  },
                  "summary": "Evaluation Summary Request",
                  "description": "Summarize evaluation results by ID"
                }
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/EvaluationSummaryRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/EvaluationSummaryRequest"
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
                  "$ref": "#/components/schemas/EvaluationSummaryResponse"
                },
                "examples": {
                  "SuccessResponse": {
                    "value": {
                      "overall_assessment": "Evaluations show generally good quality with some factual accuracy issues.",
                      "pass_patterns": [
                        {
                          "title": "Clear Communication",
                          "description": "Responses consistently provided well-structured information",
                          "frequency": "common",
                          "example_generation_ids": [
                            "gen_abc123",
                            "gen_ghi789"
                          ]
                        }
                      ],
                      "fail_patterns": [
                        {
                          "title": "Factual Errors",
                          "description": "Some responses contained inaccurate information",
                          "frequency": "occasional",
                          "example_generation_ids": [
                            "gen_def456"
                          ]
                        }
                      ],
                      "na_patterns": [],
                      "recommendations": [
                        "Implement fact-checking for critical claims",
                        "Add source citations where applicable"
                      ],
                      "statistics": {
                        "total_analyzed": 3,
                        "pass_count": 2,
                        "fail_count": 1,
                        "na_count": 0
                      }
                    },
                    "summary": "Success Response"
                  }
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
          },
          "404": {
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
      "EvaluationSummaryRequest": {
        "type": "object",
        "description": "Request serializer for evaluation summary - accepts IDs only, fetches data server-side.",
        "properties": {
          "evaluation_id": {
            "type": "string",
            "format": "uuid",
            "description": "UUID of the evaluation config to summarize"
          },
          "filter": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FilterEnum"
              }
            ],
            "default": "all",
            "description": "Filter type to apply ('all', 'pass', 'fail', or 'na')\n\n* `all` - all\n* `pass` - pass\n* `fail` - fail\n* `na` - na"
          },
          "generation_ids": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uuid"
            },
            "description": "Optional: specific generation IDs to include in summary (max 250)",
            "maxItems": 250
          },
          "force_refresh": {
            "type": "boolean",
            "default": false,
            "description": "If true, bypass cache and generate a fresh summary"
          }
        },
        "required": [
          "evaluation_id"
        ]
      },
      "EvaluationSummaryResponse": {
        "type": "object",
        "properties": {
          "overall_assessment": {
            "type": "string"
          },
          "pass_patterns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EvaluationPattern"
            }
          },
          "fail_patterns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EvaluationPattern"
            }
          },
          "na_patterns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EvaluationPattern"
            }
          },
          "recommendations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "statistics": {
            "$ref": "#/components/schemas/EvaluationSummaryStatistics"
          }
        },
        "required": [
          "fail_patterns",
          "na_patterns",
          "overall_assessment",
          "pass_patterns",
          "recommendations",
          "statistics"
        ]
      },
      "FilterEnum": {
        "enum": [
          "all",
          "pass",
          "fail",
          "na"
        ],
        "type": "string",
        "description": "* `all` - all\n* `pass` - pass\n* `fail` - fail\n* `na` - na"
      },
      "EvaluationPattern": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "frequency": {
            "type": "string"
          },
          "example_generation_ids": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "description",
          "example_generation_ids",
          "frequency",
          "title"
        ]
      },
      "EvaluationSummaryStatistics": {
        "type": "object",
        "properties": {
          "total_analyzed": {
            "type": "integer"
          },
          "pass_count": {
            "type": "integer"
          },
          "fail_count": {
            "type": "integer"
          },
          "na_count": {
            "type": "integer"
          }
        },
        "required": [
          "fail_count",
          "na_count",
          "pass_count",
          "total_analyzed"
        ]
      }
    }
  }
}
```
