# Source: https://docs.jfrog.com/security/reference/delete-ignore-rule.md

# Delete Ignore Rule

Deletes an Ignore Rule by its ID. The rule is soft-deleted and a background job is triggered to reactivate any violations that were previously suppressed by this rule.

Requires the "Manage Watches" permission. Since Xray 3.11.


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
    "/api/v1/ignore_rules/{id}": {
      "delete": {
        "operationId": "delete-ignore-rule",
        "summary": "Delete Ignore Rule",
        "description": "Deletes an Ignore Rule by its ID. The rule is soft-deleted and a background job is triggered to reactivate any violations that were previously suppressed by this rule.\n\nRequires the \"Manage Watches\" permission. Since Xray 3.11.\n",
        "tags": [
          "Ignore Rules V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The external ID of the ignore rule to delete.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "269c3072-4735-4244-4886-17ae1dc5fcd6"
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "Scope to the specified project.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Ignore rule deleted successfully. No content returned."
          },
          "400": {
            "description": "Empty ignore rule ID.",
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
                  "error": "Got an empty ignore rule id"
                }
              }
            }
          },
          "404": {
            "description": "Ignore rule not found.",
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
                  "error": "Ignore rule '269c3072-4735-4244-4886-17ae1dc5fcd6' doesn't exist"
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
                  "error": "Failed to delete ignore rule"
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
      "name": "Ignore Rules V1",
      "description": "APIs from Ignore Rules V1"
    }
  ]
}
```