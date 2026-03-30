# Source: https://posthog.com/docs/open-api-spec/environments_plugin_configs_logs_list.md

# environments_plugin_configs_logs_list

## OpenAPI

```json GET /api/environments/{environment_id}/plugin_configs/{plugin_config_id}/logs/
{
  "paths": {
    "/api/environments/{environment_id}/plugin_configs/{plugin_config_id}/logs/": {
      "get": {
        "operationId": "environments_plugin_configs_logs_list",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
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
            "name": "plugin_config_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "plugin_configs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "plugin:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedPluginLogEntryList"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedPluginLogEntryList": {
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
              "$ref": "#/components/schemas/PluginLogEntry"
            }
          }
        }
      },
      "PluginLogEntry": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "team_id": {
            "type": "integer"
          },
          "plugin_id": {
            "type": "integer"
          },
          "plugin_config_id": {
            "type": "integer"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time"
          },
          "source": {
            "$ref": "#/components/schemas/PluginLogEntrySourceEnum"
          },
          "type": {
            "$ref": "#/components/schemas/PluginLogEntryTypeEnum"
          },
          "message": {
            "type": "string"
          },
          "instance_id": {
            "type": "string",
            "format": "uuid"
          }
        },
        "required": [
          "id",
          "instance_id",
          "message",
          "plugin_config_id",
          "plugin_id",
          "source",
          "team_id",
          "timestamp",
          "type"
        ]
      },
      "PluginLogEntrySourceEnum": {
        "enum": [
          "SYSTEM",
          "PLUGIN",
          "CONSOLE"
        ],
        "type": "string",
        "description": "* `SYSTEM` - SYSTEM\n* `PLUGIN` - PLUGIN\n* `CONSOLE` - CONSOLE"
      },
      "PluginLogEntryTypeEnum": {
        "enum": [
          "DEBUG",
          "LOG",
          "INFO",
          "WARN",
          "ERROR"
        ],
        "type": "string",
        "description": "* `DEBUG` - DEBUG\n* `LOG` - LOG\n* `INFO` - INFO\n* `WARN` - WARN\n* `ERROR` - ERROR"
      }
    }
  }
}
```
