# Source: https://posthog.com/docs/open-api-spec/event_definitions_retrieve.md

# event_definitions_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/event_definitions/{id}/
{
  "paths": {
    "/api/projects/{project_id}/event_definitions/{id}/": {
      "get": {
        "operationId": "event_definitions_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this event definition.",
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
          "core",
          "event_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EnterpriseEventDefinition"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "EnterpriseEventDefinition": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "owner": {
            "type": "integer",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "last_seen_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "verified": {
            "type": "boolean"
          },
          "verified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "verified_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "hidden": {
            "type": "boolean",
            "nullable": true
          },
          "enforcement_mode": {
            "$ref": "#/components/schemas/EnforcementModeEnum"
          },
          "is_action": {
            "type": "boolean",
            "readOnly": true
          },
          "action_id": {
            "type": "integer",
            "readOnly": true
          },
          "is_calculating": {
            "type": "boolean",
            "readOnly": true
          },
          "last_calculated_at": {
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
          "post_to_slack": {
            "type": "boolean",
            "default": false
          },
          "default_columns": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "media_preview_urls": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          }
        },
        "required": [
          "action_id",
          "created_at",
          "created_by",
          "id",
          "is_action",
          "is_calculating",
          "last_calculated_at",
          "last_seen_at",
          "last_updated_at",
          "media_preview_urls",
          "name",
          "updated_at",
          "updated_by",
          "verified_at",
          "verified_by"
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
      "EnforcementModeEnum": {
        "enum": [
          "allow",
          "reject"
        ],
        "type": "string",
        "description": "* `allow` - Allow\n* `reject` - Reject"
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
