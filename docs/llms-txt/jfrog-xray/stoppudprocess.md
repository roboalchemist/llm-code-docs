# Source: https://docs.jfrog.com/artifactory/reference/stoppudprocess.md

# Stop PUD Process

This REST API is called to stop the PUD process.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Artifacts & Storage API",
    "description": "REST API for managing artifacts, storage, and related operations in JFrog Artifactory",
    "version": "1.0.0",
    "contact": {
      "name": "JFrog Support"
    }
  },
  "servers": [
    {
      "url": "https://{jfrog_url}/artifactory/api",
      "description": "JFrog Platform",
      "variables": {
        "jfrog_url": {
          "default": "myserver.jfrog.io",
          "description": "Your JFrog Platform hostname (e.g., mycompany.jfrog.io)"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Pruning Unreferenced Data",
      "description": "Pruning Unreferenced Data (PUD) operations"
    }
  ],
  "paths": {
    "/system/storage/prune/stop": {
      "post": {
        "tags": [
          "Pruning Unreferenced Data"
        ],
        "summary": "Stop PUD Process",
        "description": "This REST API is called to stop the PUD process.",
        "operationId": "stopPudProcess",
        "responses": {
          "202": {
            "description": "Accepted - Prune task stop request submitted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PudProcessResponse"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have admin permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "412": {
            "description": "Precondition Failed - No running Prune task found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PudProcessResponse"
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
      "PudProcessResponse": {
        "type": "object",
        "properties": {
          "info": {
            "type": "string",
            "description": "Information message about the PUD process"
          }
        }
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "status": {
                  "type": "integer",
                  "description": "HTTP status code"
                },
                "message": {
                  "type": "string",
                  "description": "Error message"
                }
              }
            }
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "JWT token authentication"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication"
      }
    }
  },
  "security": [
    {
      "bearerAuth": []
    },
    {
      "basicAuth": []
    }
  ]
}
```