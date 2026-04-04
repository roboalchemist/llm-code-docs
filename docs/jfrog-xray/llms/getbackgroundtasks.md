# Source: https://docs.jfrog.com/artifactory/reference/getbackgroundtasks.md

# Get Background Tasks

Returns list of background tasks currently scheduled or running in Artifactory. In HA, the nodeId is added to each task. Task can be in one of few states - scheduled, running, stopped, cancelled. Running task also shows the task start time.

Since: 4.4.0

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
      "name": "System Operations",
      "description": "System-level operations"
    }
  ],
  "paths": {
    "/tasks": {
      "get": {
        "tags": [
          "System Operations"
        ],
        "summary": "Get Background Tasks",
        "description": "Returns list of background tasks currently scheduled or running in Artifactory. In HA, the nodeId is added to each task. Task can be in one of few states - scheduled, running, stopped, cancelled. Running task also shows the task start time.\n\nSince: 4.4.0\n\nSecurity: Requires a valid admin user\n",
        "operationId": "getBackgroundTasks",
        "responses": {
          "200": {
            "description": "Successfully retrieved background tasks",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BackgroundTasks"
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
      },
      "BackgroundTasks": {
        "type": "object",
        "properties": {
          "tasks": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BackgroundTask"
            }
          }
        }
      },
      "BackgroundTask": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "state": {
            "type": "string",
            "enum": [
              "scheduled",
              "running",
              "stopped",
              "cancelled"
            ]
          },
          "description": {
            "type": "string"
          },
          "nodeId": {
            "type": "string"
          },
          "started": {
            "type": "string",
            "format": "date-time"
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