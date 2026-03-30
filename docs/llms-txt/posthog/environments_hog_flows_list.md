# Source: https://posthog.com/docs/open-api-spec/environments_hog_flows_list.md

# environments_hog_flows_list

## OpenAPI

```json GET /api/environments/{environment_id}/hog_flows/
{
  "paths": {
    "/api/environments/{environment_id}/hog_flows/": {
      "get": {
        "operationId": "environments_hog_flows_list",
        "parameters": [
          {
            "in": "query",
            "name": "created_at",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "in": "query",
            "name": "created_by",
            "schema": {
              "type": "integer"
            }
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
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            }
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
          },
          {
            "in": "query",
            "name": "updated_at",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
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
                  "$ref": "#/components/schemas/PaginatedHogFlowMinimalList"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "workflows"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedHogFlowMinimalList": {
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
              "$ref": "#/components/schemas/HogFlowMinimal"
            }
          }
        }
      },
      "HogFlowMinimal": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "description": {
            "type": "string",
            "readOnly": true
          },
          "version": {
            "type": "integer",
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/StatusA5eEnum"
              }
            ],
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
            "readOnly": true
          },
          "trigger": {
            "readOnly": true
          },
          "trigger_masking": {
            "readOnly": true,
            "nullable": true
          },
          "conversion": {
            "readOnly": true,
            "nullable": true
          },
          "exit_condition": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ExitConditionEnum"
              }
            ],
            "readOnly": true
          },
          "edges": {
            "readOnly": true
          },
          "actions": {
            "readOnly": true
          },
          "abort_action": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "variables": {
            "readOnly": true,
            "nullable": true
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
          "conversion",
          "created_at",
          "created_by",
          "description",
          "edges",
          "exit_condition",
          "id",
          "name",
          "status",
          "trigger",
          "trigger_masking",
          "updated_at",
          "variables",
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
