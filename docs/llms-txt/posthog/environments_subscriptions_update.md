# Source: https://posthog.com/docs/open-api-spec/environments_subscriptions_update.md

# environments_subscriptions_update

## OpenAPI

```json PUT /api/environments/{environment_id}/subscriptions/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/subscriptions/{id}/": {
      "put": {
        "operationId": "environments_subscriptions_update",
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this subscription.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "subscriptions"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Subscription"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Subscription"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Subscription"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "subscription:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Subscription"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Subscription": {
        "type": "object",
        "description": "Standard Subscription serializer.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "dashboard": {
            "type": "integer",
            "nullable": true
          },
          "insight": {
            "type": "integer",
            "nullable": true
          },
          "dashboard_export_insights": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "target_type": {
            "$ref": "#/components/schemas/TargetTypeEnum"
          },
          "target_value": {
            "type": "string"
          },
          "frequency": {
            "$ref": "#/components/schemas/FrequencyEnum"
          },
          "interval": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648
          },
          "byweekday": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ByweekdayEnum"
            },
            "nullable": true
          },
          "bysetpos": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "count": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "start_date": {
            "type": "string",
            "format": "date-time"
          },
          "until_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
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
          "deleted": {
            "type": "boolean"
          },
          "title": {
            "type": "string",
            "nullable": true,
            "maxLength": 100
          },
          "summary": {
            "type": "string",
            "readOnly": true
          },
          "next_delivery_date": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "integration_id": {
            "type": "integer",
            "nullable": true
          },
          "invite_message": {
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "frequency",
          "id",
          "next_delivery_date",
          "start_date",
          "summary",
          "target_type",
          "target_value"
        ]
      },
      "TargetTypeEnum": {
        "enum": [
          "email",
          "slack",
          "webhook"
        ],
        "type": "string",
        "description": "* `email` - Email\n* `slack` - Slack\n* `webhook` - Webhook"
      },
      "FrequencyEnum": {
        "enum": [
          "daily",
          "weekly",
          "monthly",
          "yearly"
        ],
        "type": "string",
        "description": "* `daily` - Daily\n* `weekly` - Weekly\n* `monthly` - Monthly\n* `yearly` - Yearly"
      },
      "ByweekdayEnum": {
        "enum": [
          "monday",
          "tuesday",
          "wednesday",
          "thursday",
          "friday",
          "saturday",
          "sunday"
        ],
        "type": "string",
        "description": "* `monday` - Monday\n* `tuesday` - Tuesday\n* `wednesday` - Wednesday\n* `thursday` - Thursday\n* `friday` - Friday\n* `saturday` - Saturday\n* `sunday` - Sunday"
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
