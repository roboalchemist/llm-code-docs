# Source: https://docs.jit.io/reference/plan.md

# Update a plan

Update a plan by specifying its slug.

**Note**: In the absence of an existing plan, a new one is created.

Use the **/plans** endpoint to retrieve all plans along with Plan Item slugs that the authenticated user has access to.

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
      "name": "Plans",
      "description": "Returns, adds, edits, or removes plans and their items",
      "externalDocs": {
        "url": "https://docs.jit.io/docs/my-plan-tab",
        "description": "Learn about managing plans in JIT"
      }
    }
  ],
  "paths": {
    "/plan/{slug}": {
      "patch": {
        "summary": "Update a plan",
        "description": "Update a plan by specifying its slug.\n\n**Note**: In the absence of an existing plan, a new one is created.\n\nUse the **/plans** endpoint to retrieve all plans along with Plan Item slugs that the authenticated user has access to.",
        "operationId": "plan",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "description": "Unique slug that represents a human-readable text string used to uniquely identify a plan.\n\nUse the **/plans** endpoint to retrieve all plans along with Plan Item slugs that the authenticated user has access to.",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/slug"
            }
          }
        ],
        "tags": [
          "Plans"
        ],
        "requestBody": {
          "required": false,
          "description": "Request fields to update a plan.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PartialUpdatePlanRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "The plan was updated successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PartialUpdatePlanResponse"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
      "PartialUpdatePlanRequest": {
        "title": "PartialUpdatePlanRequest",
        "type": "object",
        "properties": {
          "is_goal": {
            "title": "Is Goal",
            "description": "Indicates whether the plan is a goal.",
            "default": false,
            "example": true,
            "type": "boolean"
          }
        }
      },
      "PartialUpdatePlanResponse": {
        "title": "PartialUpdatePlanResponse",
        "type": "object",
        "properties": {
          "slug": {
            "title": "Plan Slug",
            "description": "Unique slug that represents a human-readable text string used to uniquely identify a plan.\n\nUse the **/plans** endpoint to retrieve all plans along with Plan Item slugs that the authenticated user has access to.",
            "minLength": 1,
            "example": "plan-aws-ftr",
            "readOnly": true,
            "type": "string"
          },
          "is_goal": {
            "title": "Is Goal",
            "description": "Indicates whether the plan is a goal.",
            "default": false,
            "example": true,
            "type": "boolean"
          }
        },
        "required": [
          "slug"
        ]
      },
      "PlanAccess-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "*"
      },
      "slug": {
        "description": "Unique slug that represents a human-readable text string used to uniquely identify a plan.\n\nUse the **/plans** endpoint to retrieve all plans along with Plan Item slugs that the authenticated user has access to.",
        "example": "plan-aws-ftr",
        "title": "Plan Slug",
        "type": "string"
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