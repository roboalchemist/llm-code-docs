# Source: https://docs.jfrog.com/artifactory/reference/appendbuild.md

# Build Append

Modifies an existing build by appending one or more new modules to it.

**Security**: Requires Deploy and Delete permissions for the specified build.


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
    "/build/append/{buildName}/{buildNumber}": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Append",
        "description": "Modifies an existing build by appending one or more new modules to it.\n\n**Security**: Requires Deploy and Delete permissions for the specified build.\n",
        "operationId": "appendBuild",
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
            "description": "The name of the parent build that will receive the module.",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "buildNumber",
            "in": "path",
            "description": "The number of the parent build that will receive the module.",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "started",
            "in": "query",
            "description": "The start date & time of the parent build that will receive the module (ISO 8601 format).",
            "required": false,
            "schema": {
              "type": "string",
              "description": "ISO 8601 format without timezone Z suffix (e.g. 2024-01-01T00:00:00.000+0000)"
            }
          },
          {
            "name": "buildRepo",
            "in": "query",
            "description": "The repository key of the parent build.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "project",
            "in": "query",
            "description": "The project key of the parent build.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Array of build modules to append",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/BuildModule"
                }
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Appended successfully"
          },
          "400": {
            "description": "Bad Request - The request body is malformed or a required parameter is missing."
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have Deploy and Delete permissions for the specified build."
          },
          "404": {
            "description": "Build-Info not found"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BuildModule": {
        "type": "object",
        "properties": {
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "description": "Module properties"
          },
          "id": {
            "type": "string",
            "description": "Module ID"
          },
          "type": {
            "type": "string",
            "description": "Module type"
          },
          "artifacts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Artifact"
            }
          },
          "dependencies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Dependency"
            }
          }
        }
      },
      "Artifact": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "sha1": {
            "type": "string"
          },
          "sha256": {
            "type": "string"
          },
          "md5": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "originalDeploymentRepo": {
            "type": "string"
          }
        }
      },
      "Dependency": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "sha1": {
            "type": "string"
          },
          "sha256": {
            "type": "string"
          },
          "md5": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "scopes": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "requestedBy": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
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