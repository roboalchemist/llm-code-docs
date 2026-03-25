# Source: https://posthog.com/docs/open-api-spec/environments_logs_alerts_list.md

# environments_logs_alerts_list

## OpenAPI

```json GET /api/environments/{environment_id}/logs/alerts/
{
  "paths": {
    "/api/environments/{environment_id}/logs/alerts/": {
      "get": {
        "operationId": "environments_logs_alerts_list",
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
          }
        ],
        "tags": [
          "logs",
          "logs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedLogsAlertConfigurationList"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "logs"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedLogsAlertConfigurationList": {
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
              "$ref": "#/components/schemas/LogsAlertConfiguration"
            }
          }
        }
      },
      "LogsAlertConfiguration": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "enabled": {
            "type": "boolean"
          },
          "filters": {
            "description": "Filter criteria — subset of LogsViewerFilters. Must contain at least one of: severityLevels (list of severity strings), serviceNames (list of service name strings), or filterGroup (property filter group object)."
          },
          "threshold_count": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 1
          },
          "threshold_operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ThresholdOperatorEnum"
              }
            ],
            "default": "above",
            "description": "Whether the alert fires when the count is above or below the threshold.\n\n* `above` - Above\n* `below` - Below"
          },
          "window_minutes": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "check_interval_minutes": {
            "type": "integer",
            "readOnly": true
          },
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/LogsAlertConfigurationStateEnum"
              }
            ],
            "readOnly": true
          },
          "evaluation_periods": {
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "description": "Total number of check periods in the sliding evaluation window (M in N-of-M)."
          },
          "datapoints_to_alarm": {
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "description": "How many periods within the evaluation window must breach the threshold to trigger (N in N-of-M)."
          },
          "cooldown_minutes": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "snooze_until": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "next_check_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_notified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_checked_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "consecutive_failures": {
            "type": "integer",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "check_interval_minutes",
          "consecutive_failures",
          "created_at",
          "created_by",
          "filters",
          "id",
          "last_checked_at",
          "last_notified_at",
          "name",
          "next_check_at",
          "state",
          "threshold_count",
          "updated_at"
        ]
      },
      "ThresholdOperatorEnum": {
        "enum": [
          "above",
          "below"
        ],
        "type": "string",
        "description": "* `above` - Above\n* `below` - Below"
      },
      "LogsAlertConfigurationStateEnum": {
        "enum": [
          "not_firing",
          "firing",
          "pending_resolve",
          "errored",
          "snoozed"
        ],
        "type": "string",
        "description": "* `not_firing` - Not firing\n* `firing` - Firing\n* `pending_resolve` - Pending resolve\n* `errored` - Errored\n* `snoozed` - Snoozed"
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
