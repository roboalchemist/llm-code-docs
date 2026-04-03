# Source: https://docs.jfrog.com/security/reference/update-jira-integration.md

# Update Jira Integration

Updates an existing Jira integration's configuration (PDF §21.4).

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
      "put": {
        "operationId": "update-jira-integration",
        "summary": "Update Jira Integration",
        "description": "Updates an existing Jira integration's configuration (PDF §21.4).",
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
            "description": "Connection name in the path (PDF — {connection_name})."
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/JiraIntegrationUpdateRequest"
              },
              "examples": {
                "updateCloud": {
                  "summary": "Update — Jira Cloud",
                  "value": {
                    "connection_name": "cloudProjectABC",
                    "auth_type": "basic",
                    "username": "customer@gmail.com",
                    "password": "password",
                    "installation_type": "cloud",
                    "jira_server_url": "https://customer.atlassian.net",
                    "skip_proxy": false
                  }
                }
              },
              "example": {
                "connection_name": "cloudProjectABC",
                "auth_type": "basic",
                "username": "customer@gmail.com",
                "password": "password",
                "installation_type": "cloud",
                "jira_server_url": "https://customer.atlassian.net",
                "skip_proxy": false
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success - Integration updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationCreateResponse"
                },
                "examples": {
                  "success": {
                    "value": {
                      "info": "Integration has been successfully updated"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "One or more fields are missing/invalid",
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
                      "error": "No integration found with the given connection name"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Failed to update integration",
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
    },
    "schemas": {
      "JiraIntegrationUpdateRequest": {
        "type": "object",
        "description": "Update Jira integration (PDF §21.4 — JSON body; path carries connection name; query parameters none).",
        "required": [
          "connection_name"
        ],
        "properties": {
          "connection_name": {
            "type": "string",
            "description": "Name of the connection to update."
          },
          "auth_type": {
            "type": "string",
            "enum": [
              "basic"
            ]
          },
          "username": {
            "type": "string"
          },
          "password": {
            "type": "string"
          },
          "installation_type": {
            "type": "string",
            "enum": [
              "cloud",
              "server"
            ]
          },
          "jira_server_url": {
            "type": "string",
            "format": "uri"
          },
          "skip_proxy": {
            "type": "boolean",
            "default": false
          }
        },
        "additionalProperties": true
      },
      "JiraIntegrationCreateResponse": {
        "type": "object",
        "description": "Create/update success or error wrapper (PDF).",
        "properties": {
          "info": {
            "type": "string",
            "description": "Present on success."
          },
          "error": {
            "type": "string",
            "description": "Present on failure responses."
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