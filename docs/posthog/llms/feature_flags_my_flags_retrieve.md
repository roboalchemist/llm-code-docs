# Source: https://posthog.com/docs/open-api-spec/feature_flags_my_flags_retrieve.md

# feature_flags_my_flags_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/my_flags/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/my_flags/": {
      "get": {
        "operationId": "feature_flags_my_flags_retrieve",
        "description": "Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/feature-flags) for more information on feature flags.\n\nIf you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.",
        "parameters": [
          {
            "in": "query",
            "name": "groups",
            "schema": {
              "type": "string",
              "default": "{}"
            },
            "description": "Groups for feature flag evaluation (JSON object string)"
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
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MyFlagsResponse"
                  }
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
      "MyFlagsResponse": {
        "type": "object",
        "properties": {
          "feature_flag": {
            "$ref": "#/components/schemas/MinimalFeatureFlag"
          },
          "value": {}
        },
        "required": [
          "feature_flag",
          "value"
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
