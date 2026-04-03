# Source: https://docs.jfrog.com/artifactory/reference/optimizesystemstorage.md

# Optimize System Storage

From Artifactory Self-Hosted 4.6.0 to 7.98.x - Raises a flag to invoke balancing between redundant storage units of a shared filestore following the next full garbage collection. From Artifactory Self-Hosted 7.104.5 and later - Immediately triggers balancing between redundant storage units of a sharded filestore. If balancing is already running, the process is skipped. This is an advanced feature intended for administrators.

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
      "name": "System Operations",
      "description": "System-level operations"
    }
  ],
  "paths": {
    "/system/storage/optimize": {
      "post": {
        "tags": [
          "System Operations"
        ],
        "summary": "Optimize System Storage",
        "description": "From Artifactory Self-Hosted 4.6.0 to 7.98.x - Raises a flag to invoke balancing between redundant storage units of a shared filestore following the next full garbage collection. From Artifactory Self-Hosted 7.104.5 and later - Immediately triggers balancing between redundant storage units of a sharded filestore. If balancing is already running, the process is skipped. This is an advanced feature intended for administrators.",
        "operationId": "optimizeSystemStorage",
        "responses": {
          "202": {
            "description": "Successfully started system storage optimization"
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
          "409": {
            "description": "Sharing balancer is already running",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "412": {
            "description": "Sharing balancer failed to run",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
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