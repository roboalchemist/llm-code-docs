# Source: https://posthog.com/docs/open-api-spec/hog_flows_retrieve.md

# hog_flows_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/hog_flows/{id}/
{
  "paths": {
    "/api/projects/{project_id}/hog_flows/{id}/": {
      "get": {
        "operationId": "hog_flows_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this hog flow.",
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
          "workflows",
          "hog_flows"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "hog_flow:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HogFlow"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "workflows"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "HogFlow": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "description": {
            "type": "string"
          },
          "version": {
            "type": "integer",
            "readOnly": true
          },
          "status": {
            "$ref": "#/components/schemas/StatusA5eEnum"
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
            "readOnly": true
          },
          "trigger": {},
          "trigger_masking": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFlowMasking"
              }
            ],
            "nullable": true
          },
          "conversion": {
            "nullable": true
          },
          "exit_condition": {
            "$ref": "#/components/schemas/ExitConditionEnum"
          },
          "edges": {},
          "actions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HogFlowAction"
            }
          },
          "abort_action": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "variables": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            }
          },
          "billable_action_types": {
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "abort_action",
          "actions",
          "billable_action_types",
          "created_at",
          "created_by",
          "id",
          "updated_at",
          "version"
        ]
      },
      "StatusA5eEnum": {
        "enum": [
          "draft",
          "active",
          "archived"
        ],
        "type": "string",
        "description": "* `draft` - Draft\n* `active` - Active\n* `archived` - Archived"
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
      "HogFlowMasking": {
        "type": "object",
        "properties": {
          "ttl": {
            "type": "integer",
            "maximum": 94608000,
            "minimum": 60,
            "nullable": true
          },
          "threshold": {
            "type": "integer",
            "nullable": true
          },
          "hash": {
            "type": "string"
          },
          "bytecode": {
            "nullable": true
          }
        },
        "required": [
          "hash"
        ]
      },
      "ExitConditionEnum": {
        "enum": [
          "exit_on_conversion",
          "exit_on_trigger_not_matched",
          "exit_on_trigger_not_matched_or_conversion",
          "exit_only_at_end"
        ],
        "type": "string",
        "description": "* `exit_on_conversion` - Conversion\n* `exit_on_trigger_not_matched` - Trigger Not Matched\n* `exit_on_trigger_not_matched_or_conversion` - Trigger Not Matched Or Conversion\n* `exit_only_at_end` - Only At End"
      },
      "HogFlowAction": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "default": ""
          },
          "on_error": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/OnErrorEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "created_at": {
            "type": "integer"
          },
          "updated_at": {
            "type": "integer"
          },
          "filters": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionFilters"
              }
            ],
            "nullable": true
          },
          "type": {
            "type": "string",
            "maxLength": 100
          },
          "config": {},
          "output_variable": {
            "nullable": true
          }
        },
        "required": [
          "config",
          "id",
          "name",
          "type"
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
      },
      "OnErrorEnum": {
        "enum": [
          "continue",
          "abort",
          "complete",
          "branch"
        ],
        "type": "string",
        "description": "* `continue` - continue\n* `abort` - abort\n* `complete` - complete\n* `branch` - branch"
      },
      "HogFunctionFilters": {
        "type": "object",
        "properties": {
          "source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionFiltersSourceEnum"
              }
            ],
            "default": "events"
          },
          "actions": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "data_warehouse": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "properties": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "bytecode": {
            "nullable": true
          },
          "transpiled": {},
          "filter_test_accounts": {
            "type": "boolean"
          },
          "bytecode_error": {
            "type": "string"
          }
        }
      },
      "HogFunctionFiltersSourceEnum": {
        "enum": [
          "events",
          "person-updates",
          "data-warehouse-table"
        ],
        "type": "string",
        "description": "* `events` - events\n* `person-updates` - person-updates\n* `data-warehouse-table` - data-warehouse-table"
      }
    }
  }
}
```
