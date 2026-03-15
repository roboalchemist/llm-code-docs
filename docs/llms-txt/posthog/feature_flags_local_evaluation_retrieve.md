# Source: https://posthog.com/docs/open-api-spec/feature_flags_local_evaluation_retrieve.md

# feature_flags_local_evaluation_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/local_evaluation/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/local_evaluation/": {
      "get": {
        "operationId": "feature_flags_local_evaluation_retrieve",
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
          },
          {
            "in": "query",
            "name": "send_cohorts",
            "schema": {
              "type": "boolean",
              "nullable": true,
              "default": false
            },
            "description": "Include cohorts in response"
          }
        ],
        "tags": [
          "feature_flags",
          "feature_flags"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "feature_flag:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LocalEvaluationResponse"
                }
              }
            },
            "description": ""
          },
          "402": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Unspecified response body"
                }
              }
            },
            "description": ""
          },
          "500": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Unspecified response body"
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
      "LocalEvaluationResponse": {
        "type": "object",
        "properties": {
          "flags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MinimalFeatureFlag"
            }
          },
          "group_type_mapping": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "cohorts": {
            "type": "object",
            "additionalProperties": {},
            "description": "Cohort definitions keyed by cohort ID. Each value is a property group structure with 'type' (OR/AND) and 'values' (array of property groups or property filters)."
          }
        },
        "required": [
          "cohorts",
          "flags",
          "group_type_mapping"
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
      }
    }
  }
}
```
