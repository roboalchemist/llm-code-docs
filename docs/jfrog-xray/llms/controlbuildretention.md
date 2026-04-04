# Source: https://docs.jfrog.com/artifactory/reference/controlbuildretention.md

# Control Build Retention

Specifies retention parameters for build info. Note that setting build retention does not immediately delete any builds. Requires Artifactory Pro.

**Security**: Requires delete permission for the build.


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
    "/build/retention/{buildName}": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Control Build Retention",
        "description": "Specifies retention parameters for build info. Note that setting build retention does not immediately delete any builds. Requires Artifactory Pro.\n\n**Security**: Requires delete permission for the build.\n",
        "operationId": "controlBuildRetention",
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
            "name": "async",
            "in": "query",
            "description": "Controls how the endpoint responds. When true, returns immediately and operation proceeds in background. When false, waits for completion unless build.retention.always.async is set to true.",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": true
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Build retention parameters",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BuildRetentionRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Build retention configured successfully"
          },
          "400": {
            "description": "Bad Request - The request body is malformed or a required parameter is missing."
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have delete permission for the build."
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
      "BuildRetentionRequest": {
        "type": "object",
        "properties": {
          "deleteBuildArtifacts": {
            "type": "boolean",
            "description": "When true, automatically removes build artifacts stored in Artifactory"
          },
          "count": {
            "type": "integer",
            "description": "The maximum number of builds to store in Artifactory"
          },
          "minimumBuildDate": {
            "type": "string",
            "format": "date-time",
            "description": "Earliest build date to store in Artifactory - ISO8601 (yyyy-MM-dd'T'HH:mm:ss.SSSZ)"
          },
          "buildNumbersNotToBeDiscarded": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of build numbers that should not be removed from Artifactory"
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