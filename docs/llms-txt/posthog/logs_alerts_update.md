# Source: https://posthog.com/docs/open-api-spec/logs_alerts_update.md

# logs_alerts_update

## OpenAPI

```json PUT /api/projects/{project_id}/logs/alerts/{id}/
{
  "paths": {
    "/api/projects/{project_id}/logs/alerts/{id}/": {
      "put": {
        "operationId": "logs_alerts_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this logs alert configuration.",
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
          "logs",
          "logs"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LogsAlertConfiguration"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/LogsAlertConfiguration"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/LogsAlertConfiguration"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LogsAlertConfiguration"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "logs"
        ]
      }
    }
  },
  "components": {
    "schemas": {
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
