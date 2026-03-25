# Source: https://posthog.com/docs/open-api-spec/signal_source_configs_create.md

# signal_source_configs_create

## OpenAPI

```json POST /api/projects/{project_id}/signal_source_configs/
{
  "paths": {
    "/api/projects/{project_id}/signal_source_configs/": {
      "post": {
        "operationId": "signal_source_configs_create",
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
          "signal_source_configs"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SignalSourceConfig"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SignalSourceConfig"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SignalSourceConfig"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SignalSourceConfig"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "signals"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "SignalSourceConfig": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "source_product": {
            "$ref": "#/components/schemas/SourceProductEnum"
          },
          "source_type": {
            "$ref": "#/components/schemas/SignalSourceConfigSourceTypeEnum"
          },
          "enabled": {
            "type": "boolean"
          },
          "config": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "status": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "id",
          "source_product",
          "source_type",
          "status",
          "updated_at"
        ]
      },
      "SourceProductEnum": {
        "enum": [
          "session_replay",
          "llm_analytics",
          "github",
          "linear",
          "zendesk"
        ],
        "type": "string",
        "description": "* `session_replay` - Session replay\n* `llm_analytics` - LLM analytics\n* `github` - GitHub\n* `linear` - Linear\n* `zendesk` - Zendesk"
      },
      "SignalSourceConfigSourceTypeEnum": {
        "enum": [
          "session_analysis_cluster",
          "evaluation",
          "issue",
          "ticket"
        ],
        "type": "string",
        "description": "* `session_analysis_cluster` - Session analysis cluster\n* `evaluation` - Evaluation\n* `issue` - Issue\n* `ticket` - Ticket"
      }
    }
  }
}
```
