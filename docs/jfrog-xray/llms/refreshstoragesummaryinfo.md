# Source: https://docs.jfrog.com/artifactory/reference/refreshstoragesummaryinfo.md

# Refresh Storage Summary Info

Refreshes storage summary information regarding binaries, file store and repositories.
Security: Requires a valid admin user


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
      "name": "Storage Info",
      "description": "Storage information operations"
    }
  ],
  "paths": {
    "/storageinfo/calculate": {
      "post": {
        "tags": [
          "Storage Info"
        ],
        "summary": "Refresh Storage Summary Info",
        "description": "Refreshes storage summary information regarding binaries, file store and repositories.\nSecurity: Requires a valid admin user\n",
        "operationId": "refreshStorageSummaryInfo",
        "responses": {
          "202": {
            "description": "Storage summary information refresh initiated successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string",
                  "description": "Informational message confirming the scheduled refresh"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have admin permissions",
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