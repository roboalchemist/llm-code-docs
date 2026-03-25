# Source: https://posthog.com/docs/open-api-spec/early_access_feature_list.md

# early_access_feature_list

## OpenAPI

```json GET /api/projects/{project_id}/early_access_feature/
{
  "paths": {
    "/api/projects/{project_id}/early_access_feature/": {
      "get": {
        "operationId": "early_access_feature_list",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
          "early_access_features",
          "early_access_feature"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "early_access_feature:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedEarlyAccessFeatureList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "early_access_features"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedEarlyAccessFeatureList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/EarlyAccessFeature"
            }
          }
        }
      },
      "EarlyAccessFeature": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "feature_flag": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MinimalFeatureFlag"
              }
            ],
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 200
          },
          "description": {
            "type": "string"
          },
          "stage": {
            "$ref": "#/components/schemas/StageEnum"
          },
          "documentation_url": {
            "type": "string",
            "format": "uri",
            "maxLength": 800
          },
          "payload": {
            "type": "string",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "feature_flag",
          "id",
          "name",
          "payload",
          "stage"
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
      "StageEnum": {
        "enum": [
          "draft",
          "concept",
          "alpha",
          "beta",
          "general-availability",
          "archived"
        ],
        "type": "string",
        "description": "* `draft` - draft\n* `concept` - concept\n* `alpha` - alpha\n* `beta` - beta\n* `general-availability` - general availability\n* `archived` - archived"
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
