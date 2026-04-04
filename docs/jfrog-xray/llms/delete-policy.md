# Source: https://docs.jfrog.com/security/reference/delete-policy.md

# Delete Policy

Deletes an existing policy by name. A policy cannot be deleted if it is currently assigned to one or more watches — you must unassign it first. Upon successful deletion, any associated violations are updated asynchronously and related ignore rules are cleaned up.

Requires the "Manage Policies" role to be set on the User or Group level.

Note: This endpoint does not support the `projectKey` query parameter.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/policies/{name}": {
      "delete": {
        "operationId": "delete-policy",
        "summary": "Delete Policy",
        "description": "Deletes an existing policy by name. A policy cannot be deleted if it is currently assigned to one or more watches — you must unassign it first. Upon successful deletion, any associated violations are updated asynchronously and related ignore rules are cleaned up.\n\nRequires the \"Manage Policies\" role to be set on the User or Group level.\n\nNote: This endpoint does not support the `projectKey` query parameter.\n",
        "tags": [
          "Policies V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The name of the policy to delete.",
            "example": "sec-policy"
          }
        ],
        "responses": {
          "200": {
            "description": "Policy deleted successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Success message."
                    }
                  }
                },
                "example": {
                  "info": "Policy sec-policy was deleted successfully"
                }
              }
            }
          },
          "400": {
            "description": "Policy name is empty, or the policy is still assigned to watches and cannot be deleted.\n",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to delete Policy sec-policy : Policy is assigned to 2 watches"
                }
              }
            }
          },
          "404": {
            "description": "Policy not found.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Policy sec-policy was not found"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to delete Policy sec-policy"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Policies V1",
      "description": "APIs from Policies V1"
    }
  ]
}
```