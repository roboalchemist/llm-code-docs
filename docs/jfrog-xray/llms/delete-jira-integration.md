# Source: https://docs.jfrog.com/security/reference/delete-jira-integration.md

# Delete Jira Integration

Deletes a Jira integration.

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
    "/api/v1/ticketing/jira-integrations/{integrationName}": {
      "delete": {
        "operationId": "delete-jira-integration",
        "summary": "Delete Jira Integration",
        "description": "Deletes a Jira integration.",
        "tags": [
          "Jira Integration V1"
        ],
        "parameters": [
          {
            "name": "integrationName",
            "in": "path",
            "description": "The Jira integration connection name to delete.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Integration deleted successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "404": {
            "description": "Integration does not exist",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "500": {
            "description": "Failed to delete integration",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
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
      "name": "Jira Integration V1",
      "description": "APIs from Jira Integration V1"
    }
  ]
}
```