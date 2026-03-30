# Source: https://posthog.com/docs/open-api-spec/signal_source_configs_list.md

# signal_source_configs_list

## OpenAPI

```json GET /api/projects/{project_id}/signal_source_configs/
{
  "paths": {
    "/api/projects/{project_id}/signal_source_configs/": {
      "get": {
        "operationId": "signal_source_configs_list",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
          },
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedSignalSourceConfigList"
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
      "PaginatedSignalSourceConfigList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SignalSourceConfig"
            }
          }
        }
      },
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
