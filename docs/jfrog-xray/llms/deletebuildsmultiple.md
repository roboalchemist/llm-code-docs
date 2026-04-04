# Source: https://docs.jfrog.com/artifactory/reference/deletebuildsmultiple.md

# Delete Builds (Multiple)

Removes builds stored in Artifactory. Useful for cleaning up old build info data. Requires Artifactory Pro. This endpoint allows deleting multiple build numbers of a certain build, including build numbers containing special characters.

**Since**: 6.13

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
    "/build/delete": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Delete Builds (Multiple)",
        "description": "Removes builds stored in Artifactory. Useful for cleaning up old build info data. Requires Artifactory Pro. This endpoint allows deleting multiple build numbers of a certain build, including build numbers containing special characters.\n\n**Since**: 6.13\n\n**Security**: Requires a privileged user. From version 6.6, requires delete permission for the Build.\n",
        "operationId": "deleteBuildsMultiple",
        "security": [
          {
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Delete builds request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DeleteBuildsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Builds deleted successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                }
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
            "description": "Permission Denied - The user does not have delete permission for the build."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "DeleteBuildsRequest": {
        "type": "object",
        "required": [
          "buildName"
        ],
        "properties": {
          "project": {
            "type": "string",
            "description": "The project to which the build belongs. If a project is not specified, the default project is used."
          },
          "buildName": {
            "type": "string",
            "description": "The build name."
          },
          "buildNumbers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The build numbers to delete. This property can be left undefined if deleteAll is set to true."
          },
          "deleteArtifacts": {
            "type": "boolean",
            "default": false,
            "description": "When set to true, deletes the artifacts associated with the builds in addition to the metadata."
          },
          "deleteAll": {
            "type": "boolean",
            "default": false,
            "description": "When set to true, deletes all build numbers of the defined build."
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