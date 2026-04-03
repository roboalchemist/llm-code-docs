# Source: https://docs.jfrog.com/security/reference/cancel-contextual-analysis-scan.md

# Cancel Artifact Contextual Analysis Scan

Cancels a running contextual analysis scan for a specific artifact. Requires Read permission.

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
    "/api/v1/artifact/contextualAnalysis/cancelScan": {
      "post": {
        "operationId": "cancel-contextual-analysis-scan",
        "summary": "Cancel Artifact Contextual Analysis Scan",
        "description": "Cancels a running contextual analysis scan for a specific artifact. Requires Read permission.",
        "tags": [
          "Contextual Analysis V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "repo": {
                    "type": "string",
                    "description": "Repository name containing the artifact."
                  },
                  "path": {
                    "type": "string",
                    "description": "Path to the artifact in the repository."
                  },
                  "componentId": {
                    "type": "string",
                    "description": "Component identifier (e.g. gav://, npm://)."
                  },
                  "project": {
                    "type": "string",
                    "description": "Project key (optional)."
                  }
                },
                "required": [
                  "repo",
                  "path"
                ]
              },
              "example": {
                "repo": "my-docker-local",
                "path": "my-image/latest/manifest.json"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Scan canceled successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Confirmation message."
                    }
                  }
                },
                "example": {
                  "info": "Scan Canceled"
                }
              }
            }
          },
          "404": {
            "description": "Artifact or scan not found."
          },
          "500": {
            "description": "Internal server error."
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
      "name": "Contextual Analysis V1",
      "description": "APIs from Contextual Analysis V1"
    }
  ]
}
```