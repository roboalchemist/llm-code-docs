# Source: https://posthog.com/docs/open-api-spec/environments_persons_properties_at_time_retrieve.md

# environments_persons_properties_at_time_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/persons/properties_at_time/
{
  "paths": {
    "/api/environments/{environment_id}/persons/properties_at_time/": {
      "get": {
        "operationId": "environments_persons_properties_at_time_retrieve",
        "description": "Get person properties as they existed at a specific point in time.\n\nThis endpoint reconstructs person properties by querying ClickHouse events\nfor $set and $set_once operations up to the specified timestamp.\n\nQuery parameters:\n- distinct_id: The distinct_id of the person\n- timestamp: ISO datetime string for the point in time (e.g., \"2023-06-15T14:30:00Z\")\n- include_set_once: Whether to handle $set_once operations (default: false)\n- debug: Whether to include debug information with raw events (default: false)",
        "parameters": [
          {
            "in": "query",
            "name": "debug",
            "schema": {
              "type": "boolean"
            },
            "description": "Whether to include debug information with raw events (only works when DEBUG=True, default: false)"
          },
          {
            "in": "query",
            "name": "distinct_id",
            "schema": {
              "type": "string"
            },
            "description": "The distinct_id of the person (mutually exclusive with person_id)"
          },
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
            "in": "query",
            "name": "include_set_once",
            "schema": {
              "type": "boolean"
            },
            "description": "Whether to handle $set_once operations (default: false)"
          },
          {
            "in": "query",
            "name": "person_id",
            "schema": {
              "type": "string"
            },
            "description": "The person_id (UUID) to build properties for (mutually exclusive with distinct_id)"
          },
          {
            "in": "query",
            "name": "timestamp",
            "schema": {
              "type": "string"
            },
            "description": "ISO datetime string for the point in time (e.g., '2023-06-15T14:30:00Z')",
            "required": true
          }
        ],
        "tags": [
          "persons",
          "persons"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "person:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersonPropertiesAtTimeResponse"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/PersonPropertiesAtTimeResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "description": "Bad request - invalid parameters"
                }
              },
              "text/csv": {
                "schema": {
                  "description": "Bad request - invalid parameters"
                }
              }
            },
            "description": ""
          },
          "404": {
            "content": {
              "application/json": {
                "schema": {
                  "description": "Person not found"
                }
              },
              "text/csv": {
                "schema": {
                  "description": "Person not found"
                }
              }
            },
            "description": ""
          },
          "500": {
            "content": {
              "application/json": {
                "schema": {
                  "description": "Internal server error"
                }
              },
              "text/csv": {
                "schema": {
                  "description": "Internal server error"
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
      "PersonPropertiesAtTimeResponse": {
        "type": "object",
        "description": "Serializer for the point-in-time person properties response.",
        "properties": {
          "id": {
            "type": "integer",
            "description": "The person ID"
          },
          "name": {
            "type": "string",
            "description": "The person's display name"
          },
          "distinct_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All distinct IDs associated with this person"
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true
            },
            "description": "Person properties as they existed at the specified time"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the person was first created"
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "description": "The person's UUID"
          },
          "last_seen_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When the person was last seen"
          },
          "point_in_time_metadata": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PersonPropertiesAtTimeMetadata"
              }
            ],
            "description": "Metadata about the point-in-time query"
          },
          "debug": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PersonPropertiesAtTimeDebug"
              }
            ],
            "description": "Debug information (only available when debug=true and DEBUG=True)"
          }
        },
        "required": [
          "created_at",
          "distinct_ids",
          "id",
          "last_seen_at",
          "name",
          "point_in_time_metadata",
          "properties",
          "uuid"
        ]
      },
      "PersonPropertiesAtTimeMetadata": {
        "type": "object",
        "description": "Serializer for the point-in-time query metadata.",
        "properties": {
          "queried_timestamp": {
            "type": "string",
            "description": "The timestamp that was queried in ISO format"
          },
          "include_set_once": {
            "type": "boolean",
            "description": "Whether $set_once operations were included"
          },
          "distinct_id_used": {
            "type": "string",
            "nullable": true,
            "description": "The distinct_id parameter used in the request"
          },
          "person_id_used": {
            "type": "string",
            "nullable": true,
            "description": "The person_id parameter used in the request"
          },
          "query_mode": {
            "type": "string",
            "description": "Whether the query used 'distinct_id' or 'person_id' mode"
          },
          "distinct_ids_queried": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All distinct_ids that were queried for this person"
          },
          "distinct_ids_count": {
            "type": "integer",
            "description": "Number of distinct_ids associated with this person"
          }
        },
        "required": [
          "distinct_id_used",
          "distinct_ids_count",
          "distinct_ids_queried",
          "include_set_once",
          "person_id_used",
          "queried_timestamp",
          "query_mode"
        ]
      },
      "PersonPropertiesAtTimeDebug": {
        "type": "object",
        "description": "Serializer for the debug information (only available to staff users).",
        "properties": {
          "query": {
            "type": "string",
            "description": "The ClickHouse query that was executed"
          },
          "params": {
            "type": "object",
            "additionalProperties": {},
            "description": "The parameters passed to the query"
          },
          "events_found": {
            "type": "integer",
            "description": "Number of events found"
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Raw events that were used to build the properties"
          },
          "error": {
            "type": "string",
            "description": "Error message if debug query failed"
          }
        },
        "required": [
          "events",
          "events_found",
          "params",
          "query"
        ]
      }
    }
  }
}
```
