# Source: https://docs.jfrog.com/security/reference/get-contextual-analysis-scan-status.md

# Get Artifact Contextual Analysis Scan Status

Returns the status of a contextual analysis scan for a specific artifact. Requires Read permission.

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
    "/api/v1/artifact/contextualAnalysis/scanStatus": {
      "post": {
        "operationId": "get-contextual-analysis-scan-status",
        "summary": "Get Artifact Contextual Analysis Scan Status",
        "description": "Returns the status of a contextual analysis scan for a specific artifact. Requires Read permission.",
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
            "description": "Scan status returned successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "description": "Current scan status (e.g. not_scanned, in_progress, completed)."
                    }
                  }
                },
                "example": {
                  "status": "scanning"
                }
              }
            }
          },
          "400": {
            "description": "Bad request - invalid or missing parameters."
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