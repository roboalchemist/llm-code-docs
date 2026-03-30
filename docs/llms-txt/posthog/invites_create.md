# Source: https://posthog.com/docs/open-api-spec/invites_create.md

# invites_create

## OpenAPI

```json POST /api/organizations/{organization_id}/invites/
{
  "paths": {
    "/api/organizations/{organization_id}/invites/": {
      "post": {
        "operationId": "invites_create",
        "parameters": [
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "invites"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationInvite"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationInvite"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationInvite"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization_member:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationInvite"
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
      "OrganizationInvite": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "target_email": {
            "type": "string",
            "format": "email",
            "maxLength": 254
          },
          "first_name": {
            "type": "string",
            "maxLength": 30
          },
          "emailing_attempt_made": {
            "type": "boolean",
            "readOnly": true
          },
          "level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/OrganizationMembershipLevel"
              }
            ],
            "minimum": 0,
            "maximum": 32767
          },
          "is_expired": {
            "type": "boolean",
            "description": "Check if invite is older than INVITE_DAYS_VALIDITY days.",
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
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "private_project_access": {
            "nullable": true,
            "description": "List of team IDs and corresponding access levels to private projects."
          },
          "send_email": {
            "type": "boolean",
            "writeOnly": true,
            "default": true
          },
          "combine_pending_invites": {
            "type": "boolean",
            "writeOnly": true,
            "default": false
          }
        },
        "required": [
          "created_at",
          "created_by",
          "emailing_attempt_made",
          "id",
          "is_expired",
          "target_email",
          "updated_at"
        ]
      },
      "OrganizationMembershipLevel": {
        "enum": [
          1,
          8,
          15
        ],
        "type": "integer",
        "description": "* `1` - member\n* `8` - administrator\n* `15` - owner"
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
