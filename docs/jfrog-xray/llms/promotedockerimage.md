# Source: https://docs.jfrog.com/artifactory/reference/promotedockerimage.md

# Promote Docker Image

Promotes a Docker image from one repository to another. Supports local and federated repositories. This REST API also supports promoting Helm OCI images. Requires JFrog Container Registry or Artifactory Pro.

**Since**: 3.7

**Security**: Requires a privileged user


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
    "/docker/{repoKey}/v2/promote": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Promote Docker Image",
        "description": "Promotes a Docker image from one repository to another. Supports local and federated repositories. This REST API also supports promoting Helm OCI images. Requires JFrog Container Registry or Artifactory Pro.\n\n**Since**: 3.7\n\n**Security**: Requires a privileged user\n",
        "operationId": "promoteDockerImage",
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
            "name": "repoKey",
            "in": "path",
            "description": "Source repository key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Docker promotion request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DockerPromotionRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Docker image promoted successfully",
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
            "description": "Permission Denied - The user does not have the necessary permissions to perform this action."
          },
          "404": {
            "description": "Not Found - The specified repository or Docker image does not exist."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "DockerPromotionRequest": {
        "type": "object",
        "required": [
          "targetRepo",
          "dockerRepository"
        ],
        "properties": {
          "targetRepo": {
            "type": "string",
            "description": "The target repository for the move or copy"
          },
          "dockerRepository": {
            "type": "string",
            "description": "The image name to promote"
          },
          "targetDockerRepository": {
            "type": "string",
            "description": "An optional docker repository name, if null, will use the same name as 'dockerRepository'"
          },
          "tag": {
            "type": "string",
            "description": "An optional tag name to promote, if null - the entire docker repository will be promoted. Available from v4.10."
          },
          "targetTag": {
            "type": "string",
            "description": "An optional target tag to assign the image after promotion, if null - will use the same tag"
          },
          "copy": {
            "type": "boolean",
            "default": false,
            "description": "An optional value to set whether to copy instead of move. Default false"
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