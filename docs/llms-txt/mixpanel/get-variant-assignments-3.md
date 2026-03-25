# Source: https://developer.mixpanel.com/reference/get-variant-assignments-3.md

# Evaluate Feature Flags (GET)

Evaluate all enabled feature flags for a user with the provided context. Returns selected variants for flags the user is eligible for.

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
      "name": "Get Variant Assignments",
      "description": "Evaluate feature flags for a specific user"
    }
  ],
  "paths": {
    "/flags": {
      "get": {
        "operationId": "get-variant-assignments",
        "security": [
          {
            "ProjectSecret": []
          }
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/ProjectToken"
          },
          {
            "name": "context",
            "in": "query",
            "description": "URL-encoded JSON object containing evaluation context with distinct_id (required) and optional device_id and custom_properties object",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "%7B++%22distinct_id%22%3A%22user123%22%2C++%22device_id%22%3A%22device456%22%2C++%22custom_properties%22%3A+%7B++++%22some_key%22%3A+%22some_value%22%2C++++%22another_key%22%3A+32++%7D%7D%22"
          }
        ],
        "tags": [
          "Get Variant Assignments"
        ],
        "summary": "Evaluate Feature Flags (GET)",
        "description": "Evaluate all enabled feature flags for a user with the provided context. Returns selected variants for flags the user is eligible for.",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EvaluateFlagsResponse"
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/400BadRequest"
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
      "EvaluateFlagsResponse": {
        "title": "EvaluateFlagsResponse",
        "description": "Response containing evaluated feature flags for the user",
        "type": "object",
        "required": [
          "flags"
        ],
        "properties": {
          "flags": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/SelectedVariant"
            },
            "description": "Map of flag keys to their selected variants",
            "example": {
              "new_checkout_flow": {
                "variant_key": "treatment",
                "variant_value": true,
                "experiment_id": "exp_123",
                "is_experiment_active": true
              }
            }
          }
        }
      },
      "SelectedVariant": {
        "title": "SelectedVariant",
        "description": "The selected variant for a feature flag",
        "type": "object",
        "required": [
          "variant_key",
          "variant_value"
        ],
        "properties": {
          "variant_key": {
            "type": "string",
            "description": "The key of the selected variant",
            "example": "treatment"
          },
          "variant_value": {
            "description": "The value of the selected variant (can be any type)",
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
          "experiment_id": {
            "type": "string",
            "description": "The ID of the associated experiment, if any",
            "example": "exp_123"
          },
          "is_experiment_active": {
            "type": "boolean",
            "description": "Whether the associated experiment is currently active",
            "example": true
          },
          "is_qa_tester": {
            "type": "boolean",
            "description": "Whether the user was identified as a QA tester",
            "example": false
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
      "400BadRequest": {
        "description": "Bad request",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
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