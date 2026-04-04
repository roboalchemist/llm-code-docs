# Source: https://posthog.com/docs/open-api-spec/persons_bulk_delete_create.md

# persons_bulk_delete_create

## OpenAPI

```json POST /api/projects/{project_id}/persons/bulk_delete/
{
  "paths": {
    "/api/projects/{project_id}/persons/bulk_delete/": {
      "post": {
        "operationId": "persons_bulk_delete_create",
        "description": "This endpoint allows you to bulk delete persons, either by the PostHog person IDs or by distinct IDs. You can pass in a maximum of 1000 IDs per call. Only events captured before the request will be deleted.",
        "parameters": [
          {
            "in": "query",
            "name": "delete_events",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "If true, a task to delete all events associated with this person will be created and queued. The task does not run immediately and instead is batched together and at 5AM UTC every Sunday"
          },
          {
            "in": "query",
            "name": "delete_recordings",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "If true, a task to delete all recordings associated with this person will be created and queued. The task does not run immediately and instead is batched together and at 5AM UTC every Sunday"
          },
          {
            "in": "query",
            "name": "distinct_ids",
            "schema": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "A list of distinct IDs, up to 1000 of them. We'll delete all persons associated with those distinct IDs."
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
            "in": "query",
            "name": "ids",
            "schema": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "A list of PostHog person IDs, up to 1000 of them. We'll delete all the persons listed."
          },
          {
            "in": "query",
            "name": "keep_person",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "If true, the person record itself will not be deleted. This is useful if you want to keep the person record for auditing purposes but remove events and recordings associated with them"
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
            "description": "No response body"
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
