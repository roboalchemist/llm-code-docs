# Source: https://docs.jfrog.com/artifactory/reference/deletebuilds.md

# Delete Builds

Removes builds stored in Artifactory. Useful for cleaning up old build info data. Requires Artifactory Pro.

**Since**: 2.2.4

**Security**: Requires a privileged user. From version 6.6, requires delete permission for the Build.


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
      "delete": {
        "tags": [
          "Builds"
        ],
        "summary": "Delete Builds",
        "description": "Removes builds stored in Artifactory. Useful for cleaning up old build info data. Requires Artifactory Pro.\n\n**Since**: 2.2.4\n\n**Security**: Requires a privileged user. From version 6.6, requires delete permission for the Build.\n",
        "operationId": "deleteBuilds",
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
            "name": "buildNumbers",
            "in": "query",
            "description": "Comma-separated list of build numbers to delete",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "artifacts",
            "in": "query",
            "description": "Whether to delete artifacts (0 or 1)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 0
            }
          },
          {
            "name": "deleteAll",
            "in": "query",
            "description": "Whether to delete all builds (0 or 1)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 0
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Builds deleted successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                },
                "example": "The following builds has been deleted successfully: 'my-build#51', 'my-build#52', 'my-build#55'."
              }
            }
          },
          "400": {
            "description": "Bad Request - No build numbers provided or the request is malformed."
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