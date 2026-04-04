# Source: https://posthog.com/docs/open-api-spec/retrieve.md

# retrieve

## OpenAPI

```json GET /api/organizations/{id}/
{
  "paths": {
    "/api/organizations/{id}/": {
      "get": {
        "operationId": "retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this organization.",
            "required": true
          }
        ],
        "tags": [
          "organizations",
          "organizations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Organization"
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
      "Organization": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 64
          },
          "slug": {
            "type": "string",
            "readOnly": true,
            "pattern": "^[-a-zA-Z0-9_]+$"
          },
          "logo_media_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
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
          "membership_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MembershipLevelEnum"
              }
            ],
            "nullable": true,
            "readOnly": true
          },
          "plugins_access_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PluginsAccessLevelEnum"
              }
            ],
            "readOnly": true
          },
          "teams": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "projects": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "available_product_features": {
            "type": "array",
            "items": {},
            "readOnly": true,
            "nullable": true
          },
          "is_member_join_email_enabled": {
            "type": "boolean"
          },
          "metadata": {
            "type": "string",
            "readOnly": true
          },
          "customer_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "enforce_2fa": {
            "type": "boolean",
            "nullable": true
          },
          "members_can_invite": {
            "type": "boolean",
            "nullable": true
          },
          "members_can_use_personal_api_keys": {
            "type": "boolean"
          },
          "allow_publicly_shared_resources": {
            "type": "boolean"
          },
          "member_count": {
            "type": "string",
            "readOnly": true
          },
          "is_ai_data_processing_approved": {
            "type": "boolean",
            "nullable": true
          },
          "default_experiment_stats_method": {
            "nullable": true,
            "description": "Default statistical method for new experiments in this organization.\n\n* `bayesian` - Bayesian\n* `frequentist` - Frequentist",
            "oneOf": [
              {
                "$ref": "#/components/schemas/DefaultExperimentStatsMethodEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "default_anonymize_ips": {
            "type": "boolean",
            "description": "Default setting for 'Discard client IP data' for new projects in this organization."
          },
          "default_role_id": {
            "type": "string",
            "nullable": true,
            "description": "ID of the role to automatically assign to new members joining the organization"
          },
          "is_active": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true,
            "title": "Active",
            "description": "Set this to 'No' to temporarily disable an organization."
          },
          "is_not_active_reason": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "title": "De-activated reason",
            "description": "(optional) reason for why the organization has been de-activated. This will be displayed to users on the web app."
          }
        },
        "required": [
          "available_product_features",
          "created_at",
          "customer_id",
          "id",
          "is_active",
          "is_not_active_reason",
          "member_count",
          "membership_level",
          "metadata",
          "name",
          "plugins_access_level",
          "projects",
          "slug",
          "teams",
          "updated_at"
        ]
      },
      "MembershipLevelEnum": {
        "enum": [
          1,
          8,
          15
        ],
        "type": "integer"
      },
      "PluginsAccessLevelEnum": {
        "enum": [
          0,
          3,
          6,
          9
        ],
        "type": "integer",
        "description": "* `0` - none\n* `3` - config\n* `6` - install\n* `9` - root"
      },
      "DefaultExperimentStatsMethodEnum": {
        "enum": [
          "bayesian",
          "frequentist"
        ],
        "type": "string",
        "description": "* `bayesian` - Bayesian\n* `frequentist` - Frequentist"
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
