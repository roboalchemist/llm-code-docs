# Source: https://posthog.com/docs/open-api-spec/experiments_duplicate_create.md

# experiments_duplicate_create

## OpenAPI

```json POST /api/projects/{project_id}/experiments/{id}/duplicate/
{
  "paths": {
    "/api/projects/{project_id}/experiments/{id}/duplicate/": {
      "post": {
        "operationId": "experiments_duplicate_create",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this experiment.",
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
          "experiments",
          "experiments"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Experiment"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Experiment"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Experiment"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "experiments"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Experiment": {
        "type": "object",
        "description": "Mixin for serializers to add user access control fields",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "start_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "end_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "feature_flag_key": {
            "type": "string"
          },
          "feature_flag": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MinimalFeatureFlag"
              }
            ],
            "readOnly": true
          },
          "holdout": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ExperimentHoldout"
              }
            ],
            "readOnly": true
          },
          "holdout_id": {
            "type": "integer",
            "nullable": true
          },
          "exposure_cohort": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "parameters": {
            "nullable": true
          },
          "secondary_metrics": {
            "nullable": true
          },
          "saved_metrics": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ExperimentToSavedMetric"
            },
            "readOnly": true
          },
          "saved_metrics_ids": {
            "type": "array",
            "items": {},
            "nullable": true
          },
          "filters": {},
          "archived": {
            "type": "boolean"
          },
          "deleted": {
            "type": "boolean",
            "nullable": true
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
          "type": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ExperimentTypeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "exposure_criteria": {
            "nullable": true
          },
          "metrics": {
            "nullable": true
          },
          "metrics_secondary": {
            "nullable": true
          },
          "stats_config": {
            "nullable": true
          },
          "scheduling_config": {
            "nullable": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "conclusion": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ConclusionEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "conclusion_comment": {
            "type": "string",
            "nullable": true
          },
          "primary_metrics_ordered_uuids": {
            "nullable": true
          },
          "secondary_metrics_ordered_uuids": {
            "nullable": true
          },
          "exposure_preaggregation_enabled": {
            "type": "boolean"
          },
          "status": {
            "readOnly": true,
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ExperimentStatusEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          }
        },
        "required": [
          "created_at",
          "created_by",
          "exposure_cohort",
          "feature_flag",
          "feature_flag_key",
          "holdout",
          "id",
          "name",
          "saved_metrics",
          "status",
          "updated_at",
          "user_access_level"
        ]
      },
      "MinimalFeatureFlag": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string"
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
          "ensure_experience_continuity": {
            "type": "boolean",
            "nullable": true
          },
          "has_encrypted_payloads": {
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
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
          "evaluation_tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "evaluation_contexts": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          }
        },
        "required": [
          "evaluation_contexts",
          "evaluation_tags",
          "id",
          "key",
          "team_id"
        ]
      },
      "ExperimentHoldout": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "filters": {},
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
          }
        },
        "required": [
          "created_at",
          "created_by",
          "id",
          "name",
          "updated_at"
        ]
      },
      "ExperimentToSavedMetric": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "experiment": {
            "type": "integer"
          },
          "saved_metric": {
            "type": "integer"
          },
          "metadata": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "query": {
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "experiment",
          "id",
          "name",
          "query",
          "saved_metric"
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
      "ExperimentTypeEnum": {
        "enum": [
          "web",
          "product"
        ],
        "type": "string",
        "description": "* `web` - web\n* `product` - product"
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
      "ConclusionEnum": {
        "enum": [
          "won",
          "lost",
          "inconclusive",
          "stopped_early",
          "invalid"
        ],
        "type": "string",
        "description": "* `won` - Won\n* `lost` - Lost\n* `inconclusive` - Inconclusive\n* `stopped_early` - Stopped Early\n* `invalid` - Invalid"
      },
      "ExperimentStatusEnum": {
        "enum": [
          "draft",
          "running",
          "stopped"
        ],
        "type": "string",
        "description": "* `draft` - Draft\n* `running` - Running\n* `stopped` - Stopped"
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
