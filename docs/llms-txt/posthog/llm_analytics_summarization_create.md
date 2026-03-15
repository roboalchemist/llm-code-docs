# Source: https://posthog.com/docs/open-api-spec/llm_analytics_summarization_create.md

# llm_analytics_summarization_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/summarization/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/summarization/": {
      "post": {
        "operationId": "llm_analytics_summarization_create",
        "description": "\nGenerate an AI-powered summary of an LLM trace or event.\n\nThis endpoint analyzes the provided trace/event, generates a line-numbered text\nrepresentation, and uses an LLM to create a concise summary with line references.\n\n**Summary Format:**\n- 5-10 bullet points covering main flow and key decisions\n- \"Interesting Notes\" section for failures, successes, or unusual patterns\n- Line references in [L45] or [L45-52] format pointing to relevant sections\n\n**Use Cases:**\n- Quick understanding of complex traces\n- Identifying key events and patterns\n- Debugging with AI-assisted analysis\n- Documentation and reporting\n\nThe response includes the summary text and optional metadata.\n        ",
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
                "$ref": "#/components/schemas/SummarizeRequest"
              },
              "examples": {
                "TraceSummarization": {
                  "value": {
                    "summarize_type": "trace",
                    "data": {
                      "trace": {
                        "id": "trace_123",
                        "properties": {
                          "$ai_span_name": "ChatBot Interaction"
                        }
                      },
                      "hierarchy": [
                        {
                          "event": {
                            "id": "gen_1",
                            "event": "$ai_generation",
                            "properties": {
                              "$ai_input": [
                                {
                                  "role": "user",
                                  "content": "Hello"
                                }
                              ],
                              "$ai_output_choices": [
                                {
                                  "message": {
                                    "role": "assistant",
                                    "content": "Hi there!"
                                  }
                                }
                              ]
                            }
                          },
                          "children": []
                        }
                      ]
                    }
                  },
                  "summary": "Trace Summarization",
                  "description": "Summarize a full trace with hierarchy"
                },
                "EventSummarization": {
                  "value": {
                    "summarize_type": "event",
                    "data": {
                      "event": {
                        "id": "gen_456",
                        "event": "$ai_generation",
                        "properties": {
                          "$ai_input": [
                            {
                              "role": "user",
                              "content": "Explain Python"
                            }
                          ],
                          "$ai_output_choices": [
                            {
                              "message": {
                                "role": "assistant",
                                "content": "Python is..."
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  "summary": "Event Summarization",
                  "description": "Summarize a single generation event"
                }
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SummarizeRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SummarizeRequest"
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
                  "$ref": "#/components/schemas/SummarizeResponse"
                },
                "examples": {
                  "SuccessResponse": {
                    "value": {
                      "summary": "## Summary\n- User initiated conversation with greeting [L5-8]\n- Assistant responded with friendly message [L12-15]\n\n## Interesting Notes\n- Standard greeting pattern with no errors",
                      "metadata": {
                        "text_repr_length": 450,
                        "model": "gpt-4.1"
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
      "SummarizeRequest": {
        "type": "object",
        "properties": {
          "summarize_type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SummarizeTypeEnum"
              }
            ],
            "description": "Type of entity to summarize\n\n* `trace` - trace\n* `event` - event"
          },
          "mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Mode02aEnum"
              }
            ],
            "default": "minimal",
            "description": "Summary detail level: 'minimal' for 3-5 points, 'detailed' for 5-10 points\n\n* `minimal` - minimal\n* `detailed` - detailed"
          },
          "data": {
            "description": "Data to summarize. For traces: {trace, hierarchy}. For events: {event}."
          },
          "force_refresh": {
            "type": "boolean",
            "default": false,
            "description": "Force regenerate summary, bypassing cache"
          },
          "model": {
            "type": "string",
            "nullable": true,
            "description": "LLM model to use (defaults based on provider)"
          }
        },
        "required": [
          "data",
          "summarize_type"
        ]
      },
      "SummarizeResponse": {
        "type": "object",
        "properties": {
          "summary": {
            "allOf": [
              {
                "$ref": "#/components/schemas/StructuredSummary"
              }
            ],
            "description": "Structured AI-generated summary with flow, bullets, and optional notes"
          },
          "text_repr": {
            "type": "string",
            "description": "Line-numbered text representation that the summary references"
          },
          "metadata": {
            "description": "Metadata about the summarization"
          }
        },
        "required": [
          "summary",
          "text_repr"
        ]
      },
      "SummarizeTypeEnum": {
        "enum": [
          "trace",
          "event"
        ],
        "type": "string",
        "description": "* `trace` - trace\n* `event` - event"
      },
      "Mode02aEnum": {
        "enum": [
          "minimal",
          "detailed"
        ],
        "type": "string",
        "description": "* `minimal` - minimal\n* `detailed` - detailed"
      },
      "StructuredSummary": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "Concise title (no longer than 10 words) summarizing the trace/event"
          },
          "flow_diagram": {
            "type": "string",
            "description": "Mermaid flowchart code showing the main flow"
          },
          "summary_bullets": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SummaryBullet"
            },
            "description": "Main summary bullets"
          },
          "interesting_notes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/InterestingNote"
            },
            "description": "Interesting notes (0-2 for minimal, more for detailed)"
          }
        },
        "required": [
          "flow_diagram",
          "interesting_notes",
          "summary_bullets",
          "title"
        ]
      },
      "SummaryBullet": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string"
          },
          "line_refs": {
            "type": "string"
          }
        },
        "required": [
          "line_refs",
          "text"
        ]
      },
      "InterestingNote": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string"
          },
          "line_refs": {
            "type": "string"
          }
        },
        "required": [
          "line_refs",
          "text"
        ]
      }
    }
  }
}
```
