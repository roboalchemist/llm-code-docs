# Source: https://posthog.com/docs/open-api-spec/feature_flags_enrich_usage_dashboard_create.md

# feature_flags_enrich_usage_dashboard_create

## OpenAPI

```json POST /api/projects/{project_id}/feature_flags/{id}/enrich_usage_dashboard/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/{id}/enrich_usage_dashboard/": {
      "post": {
        "operationId": "feature_flags_enrich_usage_dashboard_create",
        "description": "Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/feature-flags) for more information on feature flags.\n\nIf you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this feature flag.",
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
          "feature_flags",
          "feature_flags"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlag"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlag"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlag"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "feature_flags"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "FeatureFlag": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "description": "contains the description for the flag (field name `name` is kept for backwards-compatibility)"
          },
          "key": {
            "type": "string",
            "maxLength": 400
          },
          "filters": {
            "type": "object",
            "additionalProperties": {}
          },
          "deleted": {
            "type": "boolean"
          },
          "active": {
            "type": "boolean"
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
            "format": "date-time"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "version": {
            "type": "integer",
            "default": 0
          },
          "last_modified_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "ensure_experience_continuity": {
            "type": "boolean",
            "nullable": true
          },
          "experiment_set": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "readOnly": true
          },
          "surveys": {
            "type": "object",
            "additionalProperties": {},
            "readOnly": true
          },
          "features": {
            "type": "object",
            "additionalProperties": {},
            "readOnly": true
          },
          "rollback_conditions": {
            "nullable": true
          },
          "performed_rollback": {
            "type": "boolean",
            "nullable": true
          },
          "can_edit": {
            "type": "boolean",
            "readOnly": true
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "evaluation_tags": {
            "type": "array",
            "items": {},
            "writeOnly": true
          },
          "usage_dashboard": {
            "type": "integer",
            "readOnly": true
          },
          "analytics_dashboards": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "has_enriched_analytics": {
            "type": "boolean",
            "nullable": true
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          },
          "creation_context": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagCreationContextEnum"
              }
            ],
            "writeOnly": true,
            "description": "Indicates the origin product of the feature flag. Choices: 'feature_flags', 'experiments', 'surveys', 'early_access_features', 'web_experiments', 'product_tours'.\n\n* `feature_flags` - feature_flags\n* `experiments` - experiments\n* `surveys` - surveys\n* `early_access_features` - early_access_features\n* `web_experiments` - web_experiments\n* `product_tours` - product_tours"
          },
          "is_remote_configuration": {
            "type": "boolean",
            "nullable": true
          },
          "has_encrypted_payloads": {
            "type": "boolean",
            "nullable": true
          },
          "status": {
            "type": "string",
            "readOnly": true
          },
          "evaluation_runtime": {
            "nullable": true,
            "description": "Specifies where this feature flag should be evaluated\n\n* `server` - Server\n* `client` - Client\n* `all` - All",
            "oneOf": [
              {
                "$ref": "#/components/schemas/EvaluationRuntimeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "bucketing_identifier": {
            "nullable": true,
            "description": "Identifier used for bucketing users into rollout and variants\n\n* `distinct_id` - User ID (default)\n* `device_id` - Device ID",
            "oneOf": [
              {
                "$ref": "#/components/schemas/BucketingIdentifierEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "last_called_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "Last time this feature flag was called (from $feature_flag_called events)"
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "_should_create_usage_dashboard": {
            "type": "boolean",
            "writeOnly": true,
            "default": true,
            "title": " should create usage dashboard"
          },
          "is_used_in_replay_settings": {
            "type": "boolean",
            "description": "Check if this feature flag is used in any team's session recording linked flag setting.",
            "readOnly": true
          }
        },
        "required": [
          "can_edit",
          "created_by",
          "experiment_set",
          "features",
          "id",
          "is_used_in_replay_settings",
          "key",
          "last_modified_by",
          "status",
          "surveys",
          "updated_at",
          "usage_dashboard",
          "user_access_level"
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
      "FeatureFlagCreationContextEnum": {
        "enum": [
          "feature_flags",
          "experiments",
          "surveys",
          "early_access_features",
          "web_experiments",
          "product_tours"
        ],
        "type": "string",
        "description": "* `feature_flags` - feature_flags\n* `experiments` - experiments\n* `surveys` - surveys\n* `early_access_features` - early_access_features\n* `web_experiments` - web_experiments\n* `product_tours` - product_tours"
      },
      "EvaluationRuntimeEnum": {
        "enum": [
          "server",
          "client",
          "all"
        ],
        "type": "string",
        "description": "* `server` - Server\n* `client` - Client\n* `all` - All"
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
      "BucketingIdentifierEnum": {
        "enum": [
          "distinct_id",
          "device_id"
        ],
        "type": "string",
        "description": "* `distinct_id` - User ID (default)\n* `device_id` - Device ID"
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
      }
    }
  }
}
```
