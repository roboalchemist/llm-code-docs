# Source: https://posthog.com/docs/open-api-spec/persons_update.md

# persons_update

## OpenAPI

```json PUT /api/projects/{project_id}/persons/{id}/
{
  "paths": {
    "/api/projects/{project_id}/persons/{id}/": {
      "put": {
        "operationId": "persons_update",
        "description": "Only for setting properties on the person. \"properties\" from the request data will be updated via a \"$set\" event.\nThis means that only the properties listed will be updated, but other properties won't be removed nor updated.\nIf you would like to remove a property use the `delete_property` endpoint.",
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
              "type": "integer"
            },
            "description": "A unique integer value identifying this person.",
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
          "persons",
          "persons"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Person"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "person:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Person"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/Person"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "persons"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Person": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "distinct_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "properties": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "last_seen_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "distinct_ids",
          "id",
          "last_seen_at",
          "name",
          "uuid"
        ]
      }
    }
  }
}
```
