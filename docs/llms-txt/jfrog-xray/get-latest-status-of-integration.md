# Source: https://docs.jfrog.com/security/reference/get-latest-status-of-integration.md

# Get Jira Integration Status

Retrieves the latest status of an existing Jira integration by its connection name.

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
    "/api/v1/ticketing/integrations/status/check": {
      "get": {
        "operationId": "get-latest-status-of-integration",
        "summary": "Get Jira Integration Status",
        "description": "Retrieves the latest status of an existing Jira integration by its connection name.",
        "tags": [
          "Jira Integration V1"
        ],
        "parameters": [
          {
            "name": "integrationName",
            "in": "query",
            "required": true,
            "description": "The name of the integration to check (PDF §21.3).",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Integration status retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationStatusResponse"
                },
                "examples": {
                  "healthy": {
                    "value": {
                      "status": "HEALTHY_INTEGRATION",
                      "reason": "Integration is healthy and operational.",
                      "time": "2024-01-01T12:00:00Z",
                      "integration_name": "jira-connection-1"
                    }
                  },
                  "faulty": {
                    "value": {
                      "status": "FAULTY_CONFIGURATION",
                      "reason": "The system is unable to connect to Jira.",
                      "time": "2024-01-01T12:00:00Z",
                      "integration_name": "jira-connection-1"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request (e.g. missing integrationName)",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "404": {
            "description": "No integration found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationStatusResponse"
                }
              }
            }
          },
          "500": {
            "description": "Server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationStatusResponse"
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
    },
    "schemas": {
      "JiraIntegrationStatusResponse": {
        "type": "object",
        "description": "Integration health check (PDF §21.3).",
        "required": [
          "status",
          "reason",
          "time",
          "integration_name"
        ],
        "properties": {
          "status": {
            "type": "string",
            "description": "HEALTHY_INTEGRATION, INTEGRATION_NOT_FOUND, INTERNAL_SERVER_ERROR, FAULTY_CONFIGURATION."
          },
          "reason": {
            "type": "string"
          },
          "time": {
            "type": "string",
            "description": "RFC 3339 timestamp."
          },
          "integration_name": {
            "type": "string"
          }
        },
        "additionalProperties": true
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