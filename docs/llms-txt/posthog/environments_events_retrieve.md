# Source: https://posthog.com/docs/open-api-spec/environments_events_retrieve.md

# environments_events_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/events/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/events/{id}/": {
      "get": {
        "operationId": "environments_events_retrieve",
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
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
            }
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "events"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ClickhouseEvent"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/ClickhouseEvent"
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
      "ClickhouseEvent": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true
          },
          "properties": {
            "type": "string",
            "readOnly": true
          },
          "event": {
            "type": "string",
            "readOnly": true
          },
          "timestamp": {
            "type": "string",
            "readOnly": true
          },
          "person": {
            "type": "string",
            "readOnly": true
          },
          "elements": {
            "type": "string",
            "readOnly": true
          },
          "elements_chain": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "distinct_id",
          "elements",
          "elements_chain",
          "event",
          "id",
          "person",
          "properties",
          "timestamp"
        ]
      }
    }
  }
}
```
