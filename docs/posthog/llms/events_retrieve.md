# Source: https://posthog.com/docs/open-api-spec/events_retrieve.md

# events_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/events/{id}/
{
  "paths": {
    "/api/projects/{project_id}/events/{id}/": {
      "get": {
        "operationId": "events_retrieve",
        "parameters": [
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
