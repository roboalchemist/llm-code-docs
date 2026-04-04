# Source: https://posthog.com/docs/open-api-spec/integrations_retrieve.md

# integrations_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/integrations/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/integrations/{id}/": {
      "get": {
        "operationId": "integrations_retrieve",
        "description": "ViewSet for organization-level integrations.\n\nProvides read-only access to integrations that are scoped to the entire organization\n(vs. project-level integrations). Examples include Vercel, AWS Marketplace, etc.\n\nThis is read-only. Creation is handled by the integration installation flows\n(e.g., Vercel marketplace installation). Deletion requires contacting support\ndue to billing implications.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this organization integration.",
            "required": true
          },
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
          "organizations",
          "integrations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization_integration:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationIntegration"
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
      "OrganizationIntegration": {
        "type": "object",
        "description": "Serializer for organization-level integrations.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "kind": {
            "allOf": [
              {
                "$ref": "#/components/schemas/OrganizationIntegrationKindEnum"
              }
            ],
            "readOnly": true
          },
          "integration_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "config": {
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
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          }
        },
        "required": [
          "config",
          "created_at",
          "created_by",
          "id",
          "integration_id",
          "kind",
          "updated_at"
        ]
      },
      "OrganizationIntegrationKindEnum": {
        "enum": [
          "vercel"
        ],
        "type": "string",
        "description": "* `vercel` - Vercel"
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
