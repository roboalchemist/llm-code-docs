# Source: https://posthog.com/docs/open-api-spec/event_definitions_by_name_retrieve.md

# event_definitions_by_name_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/event_definitions/by_name/
{
  "paths": {
    "/api/projects/{project_id}/event_definitions/by_name/": {
      "get": {
        "operationId": "event_definitions_by_name_retrieve",
        "description": "Get event definition by exact name",
        "parameters": [
          {
            "in": "query",
            "name": "name",
            "schema": {
              "type": "string"
            },
            "description": "The exact event name to look up",
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
          "core",
          "event_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EventDefinition"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "EventDefinition": {
        "additionalProperties": false,
        "properties": {
          "elements": {
            "items": {},
            "title": "Elements",
            "type": "array"
          },
          "event": {
            "title": "Event",
            "type": "string"
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "title": "Properties"
          }
        },
        "required": [
          "elements",
          "event",
          "properties"
        ],
        "title": "EventDefinition",
        "type": "object"
      }
    }
  }
}
```
