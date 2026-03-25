# Source: https://posthog.com/docs/open-api-spec/llm_analytics_text_repr_create.md

# llm_analytics_text_repr_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/text_repr/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/text_repr/": {
      "post": {
        "operationId": "llm_analytics_text_repr_create",
        "description": "\nGenerate a human-readable text representation of an LLM trace event.\n\nThis endpoint converts LLM analytics events ($ai_generation, $ai_span, $ai_embedding, or $ai_trace)\ninto formatted text representations suitable for display, logging, or analysis.\n\n**Supported Event Types:**\n- `$ai_generation`: Individual LLM API calls with input/output messages\n- `$ai_span`: Logical spans with state transitions\n- `$ai_embedding`: Embedding generation events (text input → vector)\n- `$ai_trace`: Full traces with hierarchical structure\n\n**Options:**\n- `max_length`: Maximum character count (default: 2000000)\n- `truncated`: Enable middle-content truncation within events (default: true)\n- `truncate_buffer`: Characters at start/end when truncating (default: 1000)\n- `include_markers`: Use interactive markers vs plain text indicators (default: true)\n  - Frontend: set true for `<<<TRUNCATED|base64|...>>>` markers\n  - Backend/LLM: set false for `... (X chars truncated) ...` text\n- `collapsed`: Show summary vs full trace tree (default: false)\n- `include_hierarchy`: Include tree structure for traces (default: true)\n- `max_depth`: Maximum depth for hierarchical rendering (default: unlimited)\n- `tools_collapse_threshold`: Number of tools before auto-collapsing list (default: 5)\n  - Tool lists >5 items show `<<<TOOLS_EXPANDABLE|...>>>` marker for frontend\n  - Or `[+] AVAILABLE TOOLS: N` for backend when `include_markers: false`\n- `include_line_numbers`: Prefix each line with line number like L001:, L010: (default: false)\n\n**Use Cases:**\n- Frontend display: `truncated: true, include_markers: true, include_line_numbers: true`\n- Backend LLM context (summary): `truncated: true, include_markers: false, collapsed: true`\n- Backend LLM context (full): `truncated: false`\n\nThe response includes the formatted text and metadata about the rendering.\n        ",
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
                "$ref": "#/components/schemas/TextReprRequest"
              },
              "examples": {
                "GenerationExample": {
                  "value": {
                    "event_type": "$ai_generation",
                    "data": {
                      "id": "gen_123",
                      "properties": {
                        "$ai_input": [
                          {
                            "role": "user",
                            "content": "What is the capital of France?"
                          }
                        ],
                        "$ai_output_choices": [
                          {
                            "message": {
                              "role": "assistant",
                              "content": "The capital of France is Paris."
                            }
                          }
                        ]
                      }
                    },
                    "options": {
                      "max_length": 10000
                    }
                  },
                  "summary": "Generation Example",
                  "description": "Stringify an $ai_generation event"
                },
                "TraceExample": {
                  "value": {
                    "event_type": "$ai_trace",
                    "data": {
                      "trace": {
                        "trace_id": "trace_123",
                        "name": "ChatBot Interaction"
                      },
                      "hierarchy": [
                        {
                          "id": "gen_1",
                          "event": "$ai_generation",
                          "children": []
                        }
                      ]
                    }
                  },
                  "summary": "Trace Example",
                  "description": "Stringify a full trace with hierarchy"
                }
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TextReprRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TextReprRequest"
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
                  "$ref": "#/components/schemas/TextReprResponse"
                },
                "examples": {
                  "SuccessResponse": {
                    "value": {
                      "text": "INPUT:\n\n[1] USER\n\nWhat is the capital of France?\n\n...",
                      "metadata": {
                        "event_type": "$ai_generation",
                        "event_id": "gen_123",
                        "rendering": "detailed",
                        "char_count": 150,
                        "truncated": false
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
          },
          "503": {
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
      "TextReprRequest": {
        "type": "object",
        "properties": {
          "event_type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EventTypeEnum"
              }
            ],
            "description": "Type of LLM event to stringify\n\n* `$ai_generation` - $ai_generation\n* `$ai_span` - $ai_span\n* `$ai_embedding` - $ai_embedding\n* `$ai_trace` - $ai_trace"
          },
          "data": {
            "description": "Event data to stringify. For traces, should include 'trace' and 'hierarchy' fields."
          },
          "options": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TextReprOptions"
              }
            ],
            "description": "Optional configuration for text generation"
          }
        },
        "required": [
          "data",
          "event_type"
        ]
      },
      "TextReprResponse": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string",
            "description": "Generated text representation of the event"
          },
          "metadata": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TextReprMetadata"
              }
            ],
            "description": "Metadata about the text representation"
          }
        },
        "required": [
          "metadata",
          "text"
        ]
      },
      "EventTypeEnum": {
        "enum": [
          "$ai_generation",
          "$ai_span",
          "$ai_embedding",
          "$ai_trace"
        ],
        "type": "string",
        "description": "* `$ai_generation` - $ai_generation\n* `$ai_span` - $ai_span\n* `$ai_embedding` - $ai_embedding\n* `$ai_trace` - $ai_trace"
      },
      "TextReprOptions": {
        "type": "object",
        "properties": {
          "max_length": {
            "type": "integer",
            "description": "Maximum length of generated text (default: 2000000)"
          },
          "truncated": {
            "type": "boolean",
            "description": "Use truncation for long content within events (default: true)"
          },
          "truncate_buffer": {
            "type": "integer",
            "description": "Characters to show at start/end when truncating (default: 1000)"
          },
          "include_markers": {
            "type": "boolean",
            "description": "Use interactive markers for frontend vs plain text for backend/LLM (default: true)"
          },
          "collapsed": {
            "type": "boolean",
            "description": "Show summary vs full tree hierarchy for traces (default: false)"
          },
          "include_metadata": {
            "type": "boolean",
            "description": "Include metadata in response"
          },
          "include_hierarchy": {
            "type": "boolean",
            "description": "Include hierarchy information (for traces)"
          },
          "max_depth": {
            "type": "integer",
            "description": "Maximum depth for hierarchical rendering"
          },
          "tools_collapse_threshold": {
            "type": "integer",
            "description": "Number of tools before collapsing the list (default: 5)"
          },
          "include_line_numbers": {
            "type": "boolean",
            "description": "Prefix each line with line number (default: false)"
          }
        }
      },
      "TextReprMetadata": {
        "type": "object",
        "properties": {
          "event_type": {
            "type": "string"
          },
          "event_id": {
            "type": "string"
          },
          "trace_id": {
            "type": "string"
          },
          "rendering": {
            "type": "string"
          },
          "char_count": {
            "type": "integer"
          },
          "truncated": {
            "type": "boolean"
          },
          "error": {
            "type": "string"
          }
        },
        "required": [
          "char_count",
          "rendering",
          "truncated"
        ]
      }
    }
  }
}
```
