# Source: https://posthog.com/docs/open-api-spec/members_scoped_api_keys_retrieve.md

# members_scoped_api_keys_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/members/{user__uuid}/scoped_api_keys/
{
  "paths": {
    "/api/organizations/{organization_id}/members/{user__uuid}/scoped_api_keys/": {
      "get": {
        "operationId": "members_scoped_api_keys_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "user__uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "members"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationMember"
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
      "OrganizationMember": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "user": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
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
          "joined_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "is_2fa_enabled": {
            "type": "boolean",
            "readOnly": true
          },
          "has_social_auth": {
            "type": "boolean",
            "readOnly": true
          },
          "last_login": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "has_social_auth",
          "id",
          "is_2fa_enabled",
          "joined_at",
          "last_login",
          "updated_at",
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
      "OrganizationMembershipLevel": {
        "enum": [
          1,
          8,
          15
        ],
        "type": "integer",
        "description": "* `1` - member\n* `8` - administrator\n* `15` - owner"
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
