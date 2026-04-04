# Source: https://posthog.com/docs/open-api-spec/feature_flags_create.md

# feature_flags_create

## OpenAPI

```json POST /api/projects/{project_id}/feature_flags/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/": {
      "post": {
        "operationId": "feature_flags_create",
        "description": "Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/feature-flags) for more information on feature flags.\n\nIf you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.",
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
          "feature_flags",
          "feature_flags"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlagCreateRequestSchema"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlagCreateRequestSchema"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/FeatureFlagCreateRequestSchema"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "feature_flag:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FeatureFlag"
                }
              }
            },
            "description": ""
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
      "FeatureFlagCreateRequestSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Feature flag key."
          },
          "name": {
            "type": "string",
            "description": "Feature flag description (stored in the `name` field for backwards compatibility)."
          },
          "filters": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFiltersSchema"
              }
            ],
            "description": "Feature flag targeting configuration."
          },
          "active": {
            "type": "boolean",
            "description": "Whether the feature flag is active."
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Organizational tags for this feature flag."
          },
          "evaluation_tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Evaluation context tags. Must be a subset of `tags`."
          }
        }
      },
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
      "FeatureFlagFiltersSchema": {
        "type": "object",
        "properties": {
          "groups": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagConditionGroupSchema"
            },
            "description": "Release condition groups for the feature flag."
          },
          "multivariate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagMultivariateSchema"
              }
            ],
            "nullable": true,
            "description": "Multivariate configuration for variant-based rollouts."
          },
          "aggregation_group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index for group-based feature flags."
          },
          "payloads": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "description": "Optional payload values keyed by variant key."
          },
          "super_groups": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Additional super condition groups used by experiments."
          }
        }
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
      "FeatureFlagConditionGroupSchema": {
        "type": "object",
        "properties": {
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagFilterPropertySchema"
            },
            "description": "Property conditions for this release condition group."
          },
          "rollout_percentage": {
            "type": "number",
            "format": "double",
            "description": "Rollout percentage for this release condition group."
          },
          "variant": {
            "type": "string",
            "nullable": true,
            "description": "Variant key override for multivariate flags."
          }
        }
      },
      "FeatureFlagMultivariateSchema": {
        "type": "object",
        "properties": {
          "variants": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagMultivariateVariantSchema"
            },
            "description": "Variant definitions for multivariate feature flags."
          }
        },
        "required": [
          "variants"
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
      "FeatureFlagFilterPropertySchema": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyGenericSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyExistsSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyDateSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertySemverSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyMultiContainsSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchema"
          }
        ]
      },
      "FeatureFlagMultivariateVariantSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Unique key for this variant."
          },
          "name": {
            "type": "string",
            "description": "Human-readable name for this variant."
          },
          "rollout_percentage": {
            "type": "number",
            "format": "double",
            "description": "Variant rollout percentage."
          }
        },
        "required": [
          "key",
          "rollout_percentage"
        ]
      },
      "FeatureFlagFilterPropertyGenericSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "value": {
            "description": "Comparison value for the property filter. Supports strings, numbers, booleans, and arrays."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyGenericSchemaOperatorEnum"
              }
            ],
            "description": "Operator used to compare the property value.\n\n* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex\n* `gt` - gt\n* `gte` - gte\n* `lt` - lt\n* `lte` - lte"
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyExistsSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Operator3e6Enum"
              }
            ],
            "description": "Existence operator.\n\n* `is_set` - is_set\n* `is_not_set` - is_not_set"
          },
          "value": {
            "description": "Optional value. Runtime behavior determines whether this is ignored."
          }
        },
        "required": [
          "key",
          "operator"
        ]
      },
      "FeatureFlagFilterPropertyDateSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyDateSchemaOperatorEnum"
              }
            ],
            "description": "Date comparison operator.\n\n* `is_date_exact` - is_date_exact\n* `is_date_after` - is_date_after\n* `is_date_before` - is_date_before"
          },
          "value": {
            "type": "string",
            "description": "Date value in ISO format or relative date expression."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertySemverSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertySemverSchemaOperatorEnum"
              }
            ],
            "description": "Semantic version comparison operator.\n\n* `semver_gt` - semver_gt\n* `semver_gte` - semver_gte\n* `semver_lt` - semver_lt\n* `semver_lte` - semver_lte\n* `semver_eq` - semver_eq\n* `semver_neq` - semver_neq\n* `semver_tilde` - semver_tilde\n* `semver_caret` - semver_caret\n* `semver_wildcard` - semver_wildcard"
          },
          "value": {
            "type": "string",
            "description": "Semantic version string."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyMultiContainsSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyMultiContainsSchemaOperatorEnum"
              }
            ],
            "description": "Multi-contains operator.\n\n* `icontains_multi` - icontains_multi\n* `not_icontains_multi` - not_icontains_multi"
          },
          "value": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of strings to evaluate against."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyCohortInSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchemaTypeEnum"
              }
            ],
            "description": "Cohort property type required for in/not_in operators.\n\n* `cohort` - cohort"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchemaOperatorEnum"
              }
            ],
            "description": "Membership operator for cohort properties.\n\n* `in` - in\n* `not_in` - not_in"
          },
          "value": {
            "description": "Cohort comparison value (single or list, depending on usage)."
          }
        },
        "required": [
          "key",
          "operator",
          "type",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchemaTypeEnum"
              }
            ],
            "description": "Flag property type required for flag dependency checks.\n\n* `flag` - flag"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchemaOperatorEnum"
              }
            ],
            "description": "Operator for feature flag dependency evaluation.\n\n* `flag_evaluates_to` - flag_evaluates_to"
          },
          "value": {
            "description": "Value to compare flag evaluation against."
          }
        },
        "required": [
          "key",
          "operator",
          "type",
          "value"
        ]
      },
      "Type380Enum": {
        "enum": [
          "cohort",
          "person",
          "group"
        ],
        "type": "string",
        "description": "* `cohort` - cohort\n* `person` - person\n* `group` - group"
      },
      "FeatureFlagFilterPropertyGenericSchemaOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex",
          "gt",
          "gte",
          "lt",
          "lte"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex\n* `gt` - gt\n* `gte` - gte\n* `lt` - lt\n* `lte` - lte"
      },
      "Operator3e6Enum": {
        "enum": [
          "is_set",
          "is_not_set"
        ],
        "type": "string",
        "description": "* `is_set` - is_set\n* `is_not_set` - is_not_set"
      },
      "FeatureFlagFilterPropertyDateSchemaOperatorEnum": {
        "enum": [
          "is_date_exact",
          "is_date_after",
          "is_date_before"
        ],
        "type": "string",
        "description": "* `is_date_exact` - is_date_exact\n* `is_date_after` - is_date_after\n* `is_date_before` - is_date_before"
      },
      "FeatureFlagFilterPropertySemverSchemaOperatorEnum": {
        "enum": [
          "semver_gt",
          "semver_gte",
          "semver_lt",
          "semver_lte",
          "semver_eq",
          "semver_neq",
          "semver_tilde",
          "semver_caret",
          "semver_wildcard"
        ],
        "type": "string",
        "description": "* `semver_gt` - semver_gt\n* `semver_gte` - semver_gte\n* `semver_lt` - semver_lt\n* `semver_lte` - semver_lte\n* `semver_eq` - semver_eq\n* `semver_neq` - semver_neq\n* `semver_tilde` - semver_tilde\n* `semver_caret` - semver_caret\n* `semver_wildcard` - semver_wildcard"
      },
      "FeatureFlagFilterPropertyMultiContainsSchemaOperatorEnum": {
        "enum": [
          "icontains_multi",
          "not_icontains_multi"
        ],
        "type": "string",
        "description": "* `icontains_multi` - icontains_multi\n* `not_icontains_multi` - not_icontains_multi"
      },
      "FeatureFlagFilterPropertyCohortInSchemaTypeEnum": {
        "enum": [
          "cohort"
        ],
        "type": "string",
        "description": "* `cohort` - cohort"
      },
      "FeatureFlagFilterPropertyCohortInSchemaOperatorEnum": {
        "enum": [
          "in",
          "not_in"
        ],
        "type": "string",
        "description": "* `in` - in\n* `not_in` - not_in"
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchemaTypeEnum": {
        "enum": [
          "flag"
        ],
        "type": "string",
        "description": "* `flag` - flag"
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchemaOperatorEnum": {
        "enum": [
          "flag_evaluates_to"
        ],
        "type": "string",
        "description": "* `flag_evaluates_to` - flag_evaluates_to"
      }
    }
  }
}
```
