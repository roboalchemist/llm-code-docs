# Source: https://posthog.com/docs/open-api-spec/environments_persons_partial_update.md

# environments_persons_partial_update

## OpenAPI

```json PATCH /api/environments/{environment_id}/persons/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/persons/{id}/": {
      "patch": {
        "operationId": "environments_persons_partial_update",
        "description": "This endpoint is meant for reading and deleting persons. To create or update persons, we recommend using the [capture API](https://posthog.com/docs/api/capture), the `$set` and `$unset` [properties](https://posthog.com/docs/product-analytics/user-properties), or one of our SDKs.",
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
              "type": "integer"
            },
            "description": "A unique integer value identifying this person.",
            "required": true
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
                "$ref": "#/components/schemas/PatchedPerson"
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
        "deprecated": true,
        "x-explicit-tags": [
          "persons"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedPerson": {
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
        }
      },
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
