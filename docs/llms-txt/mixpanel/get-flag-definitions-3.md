# Source: https://developer.mixpanel.com/reference/get-flag-definitions-3.md

# Get Feature Flag Definitions

Retrieve all enabled feature flag definitions for the authenticated project. Returns complete flag metadata including rulesets, variants, and rollout configurations.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Feature Flags API",
    "description": "Use the Feature Flags API to evaluate feature flags for users and retrieve feature flag definitions.",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com",
      "description": "Mixpanel's feature flags API server.",
      "variables": {
        "regionAndDomain": {
          "default": "api.mixpanel",
          "enum": [
            "api.mixpanel",
            "api-eu.mixpanel",
            "api-in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `api.mixpanel` - The default (US) servers used for most projects\n  * `api-eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `api-in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Get Flag Definitions",
      "description": "Retrieve feature flag definitions"
    }
  ],
  "paths": {
    "/flags/definitions": {
      "get": {
        "operationId": "get-flag-definitions",
        "security": [
          {
            "ProjectSecret": []
          }
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/ProjectToken"
          }
        ],
        "tags": [
          "Get Flag Definitions"
        ],
        "summary": "Get Feature Flag Definitions",
        "description": "Retrieve all enabled feature flag definitions for the authenticated project. Returns complete flag metadata including rulesets, variants, and rollout configurations.",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FlagDefinitionsResponse"
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      }
    },
    "parameters": {
      "ProjectToken": {
        "name": "token",
        "in": "query",
        "schema": {
          "type": "string"
        },
        "description": "Your project token",
        "required": true
      }
    },
    "schemas": {
      "FlagDefinitionsResponse": {
        "title": "FlagDefinitionsResponse",
        "description": "Response containing all enabled feature flag definitions",
        "type": "object",
        "required": [
          "flags"
        ],
        "properties": {
          "flags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ExperimentationFlagMetadata"
            },
            "description": "Array of enabled feature flag definitions"
          }
        }
      },
      "ExperimentationFlagMetadata": {
        "title": "ExperimentationFlagMetadata",
        "description": "Complete metadata for a feature flag",
        "type": "object",
        "required": [
          "id",
          "name",
          "key",
          "status",
          "project_id",
          "workspace_id",
          "ruleset",
          "context"
        ],
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the flag",
            "example": "flag_abc123"
          },
          "name": {
            "type": "string",
            "description": "Human-readable name of the flag",
            "example": "New Checkout Flow"
          },
          "key": {
            "type": "string",
            "description": "Unique key used to reference the flag",
            "example": "new_checkout_flow"
          },
          "status": {
            "type": "string",
            "enum": [
              "enabled",
              "disabled",
              "archived"
            ],
            "description": "Current status of the flag",
            "example": "enabled"
          },
          "project_id": {
            "type": "integer",
            "format": "int32",
            "description": "ID of the project this flag belongs to",
            "example": 12345
          },
          "workspace_id": {
            "type": "integer",
            "format": "int64",
            "description": "ID of the workspace (dataview) this flag belongs to",
            "example": 67890
          },
          "ruleset": {
            "$ref": "#/components/schemas/RuleSet"
          },
          "context": {
            "type": "string",
            "description": "The context variable used for flag evaluation (e.g., distinct_id, device_id)",
            "example": "device_id"
          },
          "experiment_id": {
            "type": "string",
            "description": "ID of the associated experiment, if any",
            "example": "exp_123"
          },
          "is_experiment_active": {
            "type": "boolean",
            "description": "Whether the associated experiment is currently active",
            "example": true
          }
        }
      },
      "RuleSet": {
        "title": "RuleSet",
        "description": "Complete ruleset for a feature flag including variants and rollout configuration",
        "type": "object",
        "required": [
          "variants",
          "rollout"
        ],
        "properties": {
          "variants": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Variant"
            },
            "description": "Array of variant definitions for this flag"
          },
          "rollout": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Rollout"
            },
            "description": "Array of rollout rules defining how the flag is distributed"
          },
          "test": {
            "$ref": "#/components/schemas/TestUsers"
          }
        }
      },
      "Variant": {
        "title": "Variant",
        "description": "A variant definition for a feature flag",
        "type": "object",
        "required": [
          "key",
          "value",
          "is_control",
          "split"
        ],
        "properties": {
          "key": {
            "type": "string",
            "description": "Unique key for this variant",
            "example": "treatment"
          },
          "value": {
            "description": "The value for this variant (can be any type)",
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              },
              {
                "type": "object"
              }
            ],
            "example": true
          },
          "is_control": {
            "type": "boolean",
            "description": "Whether this is the control variant",
            "example": false
          },
          "is_sticky": {
            "type": "boolean",
            "description": "Whether users should stick to this variant once assigned",
            "example": true
          },
          "split": {
            "type": "number",
            "format": "double",
            "description": "The proportion of users that should receive this variant (0.0 to 1.0)",
            "example": 0.5
          }
        }
      },
      "Rollout": {
        "title": "Rollout",
        "description": "A rollout rule defining how a flag is distributed to a cohort",
        "type": "object",
        "required": [
          "rollout_percentage"
        ],
        "properties": {
          "rollout_percentage": {
            "type": "number",
            "format": "double",
            "description": "The percentage of the cohort that should receive this flag (0.0 to 1.0)",
            "example": 0.8
          },
          "cohort_hash": {
            "type": "string",
            "description": "Hash of the cohort definition for lookup",
            "example": "cohort_abc123"
          },
          "runtime_evaluation_rule": {
            "type": "object",
            "additionalProperties": true,
            "description": "JsonLogic rule that's evaluated at request time based on runtime parameters in the request",
            "example": {
              "platform": "web"
            }
          },
          "runtime_evaluation_definition": {
            "deprecated": true,
            "type": "object",
            "additionalProperties": true,
            "description": "Key-value pairs that are evaluated at request time for cohort matching, replaced by the more powerful runtime_evaluation_rule",
            "example": {
              "platform": "web"
            }
          },
          "variant_splits": {
            "type": "object",
            "additionalProperties": {
              "type": "number",
              "format": "double"
            },
            "description": "Dictionary mapping variant keys to their allocation splits within this rollout",
            "example": {
              "control": 0.5,
              "treatment": 0.5
            }
          },
          "variant_override": {
            "deprecated": true,
            "$ref": "#/components/schemas/VariantOverride"
          }
        }
      },
      "VariantOverride": {
        "deprecated": true,
        "title": "VariantOverride",
        "description": "Override to force a specific variant for a rollout rule (replaced by variant_splits)",
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "The variant key to force",
            "example": "treatment"
          }
        }
      },
      "TestUsers": {
        "title": "TestUsers",
        "description": "Mapping of test users to their assigned variants",
        "type": "object",
        "properties": {
          "users": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "description": "Map of distinct_id to variant_key for QA testing",
            "example": {
              "qa_user_1": "treatment",
              "qa_user_2": "control"
            }
          }
        }
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Details about the error that occurred"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      }
    },
    "responses": {
      "401Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "403Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    }
  },
  "x-readme-deploy-id": "feature-flags-api"
}
```