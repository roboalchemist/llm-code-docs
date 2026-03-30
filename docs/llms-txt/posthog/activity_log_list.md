# Source: https://posthog.com/docs/open-api-spec/activity_log_list.md

# activity_log_list

## OpenAPI

```json GET /api/projects/{project_id}/activity_log/
{
  "paths": {
    "/api/projects/{project_id}/activity_log/": {
      "get": {
        "operationId": "activity_log_list",
        "parameters": [
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
          "activity_log"
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
                  "$ref": "#/components/schemas/PaginatedActivityLogList"
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
      "PaginatedActivityLogList": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/ActivityLog"
        }
      },
      "ActivityLog": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "user": {
            "$ref": "#/components/schemas/UserBasic"
          },
          "unread": {
            "type": "boolean",
            "description": "is the date of this log item newer than the user's bookmark",
            "readOnly": true
          },
          "organization_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "was_impersonated": {
            "type": "boolean",
            "nullable": true
          },
          "is_system": {
            "type": "boolean",
            "nullable": true
          },
          "activity": {
            "type": "string",
            "maxLength": 79
          },
          "item_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 72
          },
          "scope": {
            "type": "string",
            "maxLength": 79
          },
          "detail": {
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "activity",
          "id",
          "scope",
          "unread",
          "user"
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
