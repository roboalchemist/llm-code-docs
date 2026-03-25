# Source: https://posthog.com/docs/open-api-spec/feature_flags_activity_retrieve.md

# feature_flags_activity_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/activity/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/activity/": {
      "get": {
        "operationId": "feature_flags_activity_retrieve",
        "description": "Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/feature-flags) for more information on feature flags.\n\nIf you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.",
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 10
            },
            "description": "Number of items per page"
          },
          {
            "in": "query",
            "name": "page",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            },
            "description": "Page number"
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
          "feature_flags",
          "feature_flags"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "activity_log:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ActivityLogPaginatedResponse"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "feature_flags"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "ActivityLogPaginatedResponse": {
        "type": "object",
        "description": "Response shape for paginated activity log endpoints.",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ActivityLogEntry"
            }
          },
          "next": {
            "type": "string",
            "format": "uri",
            "nullable": true
          },
          "previous": {
            "type": "string",
            "format": "uri",
            "nullable": true
          },
          "total_count": {
            "type": "integer"
          }
        },
        "required": [
          "next",
          "previous",
          "results",
          "total_count"
        ]
      },
      "ActivityLogEntry": {
        "type": "object",
        "properties": {
          "user": {
            "type": "string",
            "readOnly": true
          },
          "activity": {
            "type": "string",
            "readOnly": true
          },
          "scope": {
            "type": "string",
            "readOnly": true
          },
          "item_id": {
            "type": "string",
            "readOnly": true
          },
          "detail": {
            "$ref": "#/components/schemas/Detail"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "activity",
          "created_at",
          "item_id",
          "scope",
          "user"
        ]
      },
      "Detail": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "changes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Change"
            }
          },
          "merge": {
            "$ref": "#/components/schemas/Merge"
          },
          "trigger": {
            "$ref": "#/components/schemas/Trigger"
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "short_id": {
            "type": "string",
            "readOnly": true
          },
          "type": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "id",
          "name",
          "short_id",
          "type"
        ]
      },
      "Change": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "readOnly": true
          },
          "action": {
            "type": "string",
            "readOnly": true
          },
          "field": {
            "type": "string",
            "readOnly": true
          },
          "before": {
            "readOnly": true
          },
          "after": {
            "readOnly": true
          }
        },
        "required": [
          "action",
          "after",
          "before",
          "field",
          "type"
        ]
      },
      "Merge": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "readOnly": true
          },
          "source": {
            "readOnly": true
          },
          "target": {
            "readOnly": true
          }
        },
        "required": [
          "source",
          "target",
          "type"
        ]
      },
      "Trigger": {
        "type": "object",
        "properties": {
          "job_type": {
            "type": "string",
            "readOnly": true
          },
          "job_id": {
            "type": "string",
            "readOnly": true
          },
          "payload": {
            "readOnly": true
          }
        },
        "required": [
          "job_id",
          "job_type",
          "payload"
        ]
      }
    }
  }
}
```
