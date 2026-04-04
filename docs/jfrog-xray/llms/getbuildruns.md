# Source: https://docs.jfrog.com/artifactory/reference/getbuildruns.md

# Build Runs

Provides information about the build runs for the given build name.

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
    "/build/{buildName}": {
      "get": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Runs",
        "description": "Provides information about the build runs for the given build name.\n\n**Since**: 2.2.0\n\n**Security**: Requires a privileged user (can be anonymous). From version 6.6, requires read permission for the build or basic read.\n",
        "operationId": "getBuildRuns",
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
            "name": "buildName",
            "in": "path",
            "description": "Build name",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "projectKey",
            "in": "query",
            "description": "Limits the response to builds contained in the specified project.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved build runs",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BuildRunsResponse"
                },
                "example": {
                  "uri": "http://localhost:8081/artifactory/api/build/my-build",
                  "buildsNumbers": [
                    {
                      "uri": "/51",
                      "started": "2024-01-15T10:30:00.000Z"
                    },
                    {
                      "uri": "/52",
                      "started": "2024-01-16T11:20:00.000Z"
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
          },
          "404": {
            "description": "Not Found - The specified build does not exist."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BuildRunsResponse": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string",
            "description": "URI of the build"
          },
          "buildsNumbers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BuildNumber"
            }
          }
        }
      },
      "BuildNumber": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string",
            "description": "URI of the build number"
          },
          "started": {
            "type": "string",
            "format": "date-time",
            "description": "Started timestamp in ISO8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ)"
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