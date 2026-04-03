# Source: https://docs.jfrog.com/security/reference/create-jira-integration.md

# Create Jira Integration

Creates a new Jira integration.

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
    "/api/v1/ticketing/jira-integrations": {
      "post": {
        "operationId": "create-jira-integration",
        "summary": "Create Jira Integration",
        "description": "Creates a new Jira integration.",
        "tags": [
          "Jira Integration V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/JiraIntegrationCreateRequest"
              },
              "examples": {
                "jiraCloud": {
                  "summary": "Jira Cloud (PDF)",
                  "value": {
                    "connection_name": "cloudProjectABC",
                    "auth_type": "basic",
                    "username": "customer@gmail.com",
                    "password": "password",
                    "installation_type": "cloud",
                    "jira_server_url": "https://customer.atlassian.net",
                    "skip_proxy": false
                  }
                },
                "jiraServer": {
                  "summary": "Self-hosted Jira Server (PDF)",
                  "value": {
                    "connection_name": "ServerProjectXYZ",
                    "auth_type": "basic",
                    "username": "customer@gmail.com",
                    "password": "password",
                    "installation_type": "server",
                    "jira_server_url": "http://10.35.12.11",
                    "skip_proxy": true
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
            "description": "Success - Integration created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationCreateResponse"
                },
                "examples": {
                  "success": {
                    "value": {
                      "info": "Integration has been successfully created"
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
                  "$ref": "#/components/schemas/JiraIntegrationCreateResponse"
                },
                "examples": {
                  "badRequest": {
                    "value": {
                      "error": "We were not able to connect to your Jira based on the credentials you provided, please check all the values and try again."
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
                  "$ref": "#/components/schemas/JiraIntegrationCreateResponse"
                }
              }
            }
          },
          "500": {
            "description": "Failed to create integration",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JiraIntegrationCreateResponse"
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
      "JiraIntegrationCreateRequest": {
        "type": "object",
        "description": "Create Jira integration (PDF §21.1 — JSON body; query parameters none).",
        "required": [
          "connection_name",
          "auth_type",
          "username",
          "password",
          "installation_type",
          "jira_server_url"
        ],
        "properties": {
          "connection_name": {
            "type": "string",
            "description": "A unique identifier for the connection."
          },
          "auth_type": {
            "type": "string",
            "description": "Authentication method. Valid values — basic.",
            "enum": [
              "basic"
            ]
          },
          "username": {
            "type": "string",
            "description": "Username for authentication."
          },
          "password": {
            "type": "string",
            "description": "Password for authentication."
          },
          "installation_type": {
            "type": "string",
            "description": "cloud or server.",
            "enum": [
              "cloud",
              "server"
            ]
          },
          "jira_server_url": {
            "type": "string",
            "description": "URL of the Jira server where tickets will be created.",
            "format": "uri"
          },
          "skip_proxy": {
            "type": "boolean",
            "description": "Whether to bypass proxy settings. Default false.",
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