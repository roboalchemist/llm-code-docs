# Source: https://posthog.com/docs/open-api-spec/roles_role_memberships_create.md

# roles_role_memberships_create

## OpenAPI

```json POST /api/organizations/{organization_id}/roles/{role_id}/role_memberships/
{
  "paths": {
    "/api/organizations/{organization_id}/roles/{role_id}/role_memberships/": {
      "post": {
        "operationId": "roles_role_memberships_create",
        "parameters": [
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "role_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "organizations",
          "roles"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RoleMembership"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/RoleMembership"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/RoleMembership"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RoleMembership"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "organizations"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "RoleMembership": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "role_id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "organization_member": {
            "allOf": [
              {
                "$ref": "#/components/schemas/OrganizationMember"
              }
            ],
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
          "user_uuid": {
            "type": "string",
            "format": "uuid",
            "writeOnly": true
          }
        },
        "required": [
          "id",
          "joined_at",
          "organization_member",
          "role_id",
          "updated_at",
          "user",
          "user_uuid"
        ]
      },
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
