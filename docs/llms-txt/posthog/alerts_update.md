# Source: https://posthog.com/docs/open-api-spec/alerts_update.md

# alerts_update

## OpenAPI

```json PUT /api/projects/{project_id}/alerts/{id}/
{
  "paths": {
    "/api/projects/{project_id}/alerts/{id}/": {
      "put": {
        "operationId": "alerts_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this alert configuration.",
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
          "alerts"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Alert"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Alert"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Alert"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "alert:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Alert"
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
      "Alert": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "insight": {
            "type": "integer",
            "description": "Insight ID monitored by this alert. Note: Response returns full InsightBasicSerializer object."
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "subscribed_users": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "User IDs to subscribe to this alert. Note: Response returns full UserBasicSerializer object."
          },
          "threshold": {
            "$ref": "#/components/schemas/Threshold"
          },
          "condition": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AlertCondition"
              }
            ],
            "nullable": true
          },
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/State66aEnum"
              }
            ],
            "readOnly": true
          },
          "enabled": {
            "type": "boolean"
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
          "next_check_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "checks": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AlertCheck"
            },
            "readOnly": true
          },
          "config": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TrendsAlertConfig"
              }
            ],
            "nullable": true
          },
          "calculation_interval": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/CalculationIntervalEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "snoozed_until": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "skip_weekend": {
            "type": "boolean",
            "nullable": true
          },
          "last_value": {
            "type": "number",
            "format": "double",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "checks",
          "created_at",
          "created_by",
          "id",
          "insight",
          "last_checked_at",
          "last_notified_at",
          "last_value",
          "next_check_at",
          "state",
          "subscribed_users",
          "threshold"
        ]
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
      "Threshold": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "configuration": {
            "$ref": "#/components/schemas/InsightThreshold"
          }
        },
        "required": [
          "configuration",
          "created_at",
          "id"
        ]
      },
      "AlertCondition": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "$ref": "#/components/schemas/AlertConditionType"
          }
        },
        "required": [
          "type"
        ],
        "title": "AlertCondition",
        "type": "object"
      },
      "State66aEnum": {
        "enum": [
          "Firing",
          "Not firing",
          "Errored",
          "Snoozed"
        ],
        "type": "string",
        "description": "* `Firing` - Firing\n* `Not firing` - Not firing\n* `Errored` - Errored\n* `Snoozed` - Snoozed"
      },
      "AlertCheck": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "calculated_value": {
            "type": "number",
            "format": "double",
            "readOnly": true,
            "nullable": true
          },
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/State66aEnum"
              }
            ],
            "readOnly": true
          },
          "targets_notified": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "required": [
          "calculated_value",
          "created_at",
          "id",
          "state",
          "targets_notified"
        ]
      },
      "TrendsAlertConfig": {
        "additionalProperties": false,
        "properties": {
          "check_ongoing_interval": {
            "default": null,
            "title": "Check Ongoing Interval",
            "type": "boolean",
            "nullable": true
          },
          "series_index": {
            "title": "Series Index",
            "type": "integer"
          },
          "type": {
            "default": "TrendsAlertConfig",
            "title": "Type",
            "type": "string",
            "enum": [
              "TrendsAlertConfig"
            ]
          }
        },
        "required": [
          "series_index"
        ],
        "title": "TrendsAlertConfig",
        "type": "object"
      },
      "CalculationIntervalEnum": {
        "enum": [
          "hourly",
          "daily",
          "weekly",
          "monthly"
        ],
        "type": "string",
        "description": "* `hourly` - hourly\n* `daily` - daily\n* `weekly` - weekly\n* `monthly` - monthly"
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
      "InsightThreshold": {
        "additionalProperties": false,
        "properties": {
          "bounds": {
            "default": null,
            "$ref": "#/components/schemas/InsightsThresholdBounds",
            "nullable": true
          },
          "type": {
            "$ref": "#/components/schemas/InsightThresholdType"
          }
        },
        "required": [
          "type"
        ],
        "title": "InsightThreshold",
        "type": "object"
      },
      "AlertConditionType": {
        "enum": [
          "absolute_value",
          "relative_increase",
          "relative_decrease"
        ],
        "title": "AlertConditionType",
        "type": "string"
      },
      "InsightsThresholdBounds": {
        "additionalProperties": false,
        "properties": {
          "lower": {
            "default": null,
            "title": "Lower",
            "type": "number",
            "nullable": true
          },
          "upper": {
            "default": null,
            "title": "Upper",
            "type": "number",
            "nullable": true
          }
        },
        "title": "InsightsThresholdBounds",
        "type": "object"
      },
      "InsightThresholdType": {
        "enum": [
          "absolute",
          "percentage"
        ],
        "title": "InsightThresholdType",
        "type": "string"
      }
    }
  }
}
```
