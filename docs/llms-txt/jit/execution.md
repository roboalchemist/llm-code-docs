# Source: https://docs.jit.io/reference/execution.md

# Trigger plan item execution

Trigger executions for plan items and assets to run against

**NOTE** This endpoint only supports triggering executions for plan items.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Executions",
      "description": "Executions management endpoints"
    }
  ],
  "paths": {
    "/trigger/event": {
      "post": {
        "summary": "Trigger plan item execution",
        "description": "Trigger executions for plan items and assets to run against\n\n**NOTE** This endpoint only supports triggering executions for plan items.",
        "operationId": "execution",
        "parameters": [],
        "tags": [
          "Executions"
        ],
        "requestBody": {
          "description": "The fields describing the execution request.",
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ManualExecutionRequest"
              }
            }
          }
        },
        "responses": {
          "202": {
            "description": "Trigger execution response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ManualExecutionResponse"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TriggerAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BadRequest"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TriggerAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UnauthorizedAuthorizerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TriggerAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForbiddenError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TriggerAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TriggerAccess-Control-Allow-Origin"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BadRequest": {
        "title": "ValidationErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INVALID_INPUT",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable message containing fields that failed validation.",
            "example": "sample_field1: ensure this value is greater than or equal to 5\ninner_object -> sample_field2: field required",
            "type": "string"
          },
          "invalid_parameters": {
            "title": "Input parameters to errors map",
            "description": "Dictionary mapping input parameter for their corresponding error messages for programmatic use.\n\n**Important**: This dictionary should match your input. Parameters with invalid inputs display their respective messages.",
            "nullable": true,
            "example": {
              "sample_field1": "ensure this value is greater than or equal to 5",
              "inner_object": {
                "sample_field2": "field required"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "ForbiddenError": {
        "title": "ForbiddenErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FORBIDDEN",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Request is missing the required permissions.",
            "type": "string"
          },
          "missing_permissions": {
            "title": "Missing permissions",
            "description": "List of missing permissions.",
            "nullable": true,
            "example": [
              "jit.category.write",
              "jit.category.read"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "UnauthorizedAuthorizerError": {
        "title": "UnauthorizedAuthorizerErrorResponse",
        "type": "object",
        "properties": {
          "Message": {
            "title": "Error message",
            "description": "Human readable error message.\n\n**Important**: This schema does not contain `error` field.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "Message"
        ]
      },
      "ManualExecutionRequest": {
        "title": "ManualExecutionRequest",
        "type": "object",
        "properties": {
          "plan_item_slug": {
            "title": "Plan item slug",
            "description": "The slug of the plan item to execute",
            "example": "item-branch-protection-scm",
            "type": "string"
          },
          "assets": {
            "title": "Assets to execute",
            "description": "List of assets to execute. Each asset can be specified by its ID or by its name and type",
            "example": [
              {
                "name": "users-service",
                "type": "repo"
              },
              {
                "id": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c"
              }
            ],
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "title": "AssetTriggerFilters",
                  "type": "object",
                  "properties": {
                    "name": {
                      "title": "Asset name",
                      "description": "The name of the asset to execute",
                      "example": "users-service",
                      "type": "string"
                    },
                    "type": {
                      "title": "Asset type",
                      "description": "The type of the asset to execute",
                      "example": "repo",
                      "enum": [
                        "repo",
                        "org",
                        "aws_account",
                        "gcp_account",
                        "azure_account",
                        "web",
                        "api",
                        "image",
                        "external_integ"
                      ],
                      "type": "string"
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
              },
              {
                "type": "array",
                "items": {
                  "title": "AssetTriggerId",
                  "type": "object",
                  "properties": {
                    "id": {
                      "title": "Asset ID",
                      "description": "The unique Identifier of the asset to execute",
                      "example": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c",
                      "type": "string"
                    }
                  },
                  "required": [
                    "id"
                  ]
                }
              }
            ]
          },
          "priority": {
            "title": "Execution priority",
            "description": "1 Represents the highest priority, 3 the lowest",
            "example": 3,
            "allOf": [
              {
                "title": "ExecutionPriority",
                "description": "An enumeration.",
                "enum": [
                  1,
                  3
                ],
                "type": "integer"
              }
            ]
          }
        },
        "required": [
          "plan_item_slug"
        ]
      },
      "ManualExecutionResponse": {
        "title": "ManualExecutionResponse",
        "type": "object",
        "properties": {
          "jit_event_id": {
            "title": "Jit Event ID",
            "description": "The Jit Event ID of the created execution, in uuid format",
            "example": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "jit_event_id"
        ]
      },
      "TriggerAccess-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "*"
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```