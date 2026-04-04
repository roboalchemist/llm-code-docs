# Source: https://docs.jfrog.com/artifactory/reference/renamebuild.md

# Build Rename

Renames a build stored in Artifactory. Typically used to keep the build info in sync with a renamed build on the CI server. Requires Artifactory Pro.

**Security**: Requires deploy and delete permission for the build.


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
    "/build/rename/{buildName}": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Rename",
        "description": "Renames a build stored in Artifactory. Typically used to keep the build info in sync with a renamed build on the CI server. Requires Artifactory Pro.\n\n**Security**: Requires deploy and delete permission for the build.\n",
        "operationId": "renameBuild",
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
            "description": "Current build name",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "to",
            "in": "query",
            "description": "The new name for the build. This parameter is required.",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "project",
            "in": "query",
            "description": "The name of the project associated with the build. This parameter is required if the build is part of a project.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Build renamed successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                },
                "example": "Build renaming of 'myJobName' to 'myNewJobName' was successfully started."
              }
            }
          },
          "400": {
            "description": "Bad Request - The request body is malformed or a required parameter is missing."
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have deploy and delete permission for the build."
          },
          "404": {
            "description": "Not Found - The specified build does not exist."
          }
        }
      }
    }
  },
  "components": {
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