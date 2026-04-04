# Source: https://docs.jfrog.com/artifactory/reference/getallbuilds.md

# All Builds

Provides information on all builds.

**Since**: 2.2.0

**Security**: Requires a privileged user (can be anonymous). From version 6.6, requires read permission for the build or basic read.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Build API",
    "description": "REST API for managing builds in JFrog Artifactory",
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
      "name": "Builds",
      "description": "Build management operations"
    }
  ],
  "paths": {
    "/build": {
      "get": {
        "tags": [
          "Builds"
        ],
        "summary": "All Builds",
        "description": "Provides information on all builds.\n\n**Since**: 2.2.0\n\n**Security**: Requires a privileged user (can be anonymous). From version 6.6, requires read permission for the build or basic read.\n",
        "operationId": "getAllBuilds",
        "security": [
          {
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "parameters": [
          {
            "name": "projectKey",
            "in": "query",
            "description": "Limits the response to the builds contained in the specified project.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved builds",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AllBuildsResponse"
                },
                "example": {
                  "uri": "http://localhost:8081/artifactory/api/build",
                  "builds": [
                    {
                      "uri": "/my-build",
                      "lastStarted": "2024-01-15T10:30:00.000Z"
                    },
                    {
                      "uri": "/jackrabbit",
                      "lastStarted": "2024-01-14T09:20:00.000Z"
                    }
                  ]
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have the necessary permissions to perform this action."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "AllBuildsResponse": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string",
            "description": "URI of the builds endpoint"
          },
          "builds": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BuildSummary"
            }
          }
        }
      },
      "BuildSummary": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string",
            "description": "URI of the build"
          },
          "lastStarted": {
            "type": "string",
            "format": "date-time",
            "description": "Last started timestamp in ISO8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ)"
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