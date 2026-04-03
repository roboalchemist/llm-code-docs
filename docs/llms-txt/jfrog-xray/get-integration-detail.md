# Source: https://docs.jfrog.com/security/reference/get-integration-detail.md

# Get Jira Integration Details

Retrieves full configuration details by connection name (PDF §21.2).

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
    "/api/v1/ticketing/jira-integrations/{integrationName}/details": {
      "get": {
        "operationId": "get-integration-detail",
        "summary": "Get Jira Integration Details",
        "description": "Retrieves full configuration details by connection name (PDF §21.2).",
        "tags": [
          "Jira Integration V1"
        ],
        "parameters": [
          {
            "name": "integrationName",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Jira integration connection name (PDF — path parameter)."
          }
        ],
        "responses": {
          "200": {
            "description": "Integration details retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "connection_name": {
                      "type": "string"
                    },
                    "auth_type": {
                      "type": "string"
                    },
                    "username": {
                      "type": "string"
                    },
                    "installation_type": {
                      "type": "string"
                    },
                    "jira_server_url": {
                      "type": "string",
                      "format": "uri"
                    },
                    "skip_proxy": {
                      "type": "boolean"
                    }
                  }
                },
                "examples": {
                  "success": {
                    "value": {
                      "auth_type": "basic",
                      "connection_name": "jira-connection-1",
                      "jira_server_url": "https://jira.example.com",
                      "username": "adminUser",
                      "installation_type": "cloud",
                      "skip_proxy": false
                    }
                  }
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
            "description": "No integration found",
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
                "examples": {
                  "notFound": {
                    "value": {
                      "error": "Integration not found"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Server error",
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