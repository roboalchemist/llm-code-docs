# Source: https://docs.jfrog.com/artifactory/reference/promotebuild.md

# Build Promotion

Change the status of a build, optionally moving or copying the build's artifacts and its dependencies to a target repository and setting properties on promoted artifacts. All artifacts from all scopes are included by default while dependencies are not. Scopes are additive (or). From version 5.7, the target repository can be a virtual repository.

**Security**: Requires Deploy permission for the build.


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
    "/build/promote/{buildName}/{buildNumber}": {
      "post": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Promotion",
        "description": "Change the status of a build, optionally moving or copying the build's artifacts and its dependencies to a target repository and setting properties on promoted artifacts. All artifacts from all scopes are included by default while dependencies are not. Scopes are additive (or). From version 5.7, the target repository can be a virtual repository.\n\n**Security**: Requires Deploy permission for the build.\n",
        "operationId": "promoteBuild",
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
            "name": "buildNumber",
            "in": "path",
            "description": "Build number",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "project",
            "in": "query",
            "description": "The name of the project that contains the build to be promoted. If not defined, Artifactory uses the default build-info repo.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Build promotion request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BuildPromotionRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BuildPromotionResponse"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have Deploy permission for the build."
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
      "BuildPromotionRequest": {
        "type": "object",
        "required": [
          "ciUser",
          "timestamp",
          "copy",
          "artifacts",
          "dependencies",
          "failFast"
        ],
        "properties": {
          "status": {
            "type": "string",
            "description": "The new status of the build. This is especially important when performing a promotion that only changes the status of the build without copying or moving artifacts and dependencies."
          },
          "comment": {
            "type": "string",
            "description": "An optional comment describing the reason for the promotion."
          },
          "ciUser": {
            "type": "string",
            "description": "The user that invoked promotion from the CI server."
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the promotion command was received by Artifactory (ISO8601 format). The format is yyyy-MM-dd'T'HH:mm:ss.SSSZ."
          },
          "dryRun": {
            "type": "boolean",
            "default": false,
            "description": "When set to true, performs a dry run of the promotion without executing any operation in Artifactory."
          },
          "sourceRepo": {
            "type": "string",
            "description": "The repository from which the build contents will be copied or moved. If this property is not defined, the source repository is resolved automatically."
          },
          "targetRepo": {
            "type": "string",
            "description": "The target repository to which the build contents will be copied or moved. This property does not need to defined if the promotion involves a change of status only."
          },
          "copy": {
            "type": "boolean",
            "default": false,
            "description": "Determines how to perform the build promotion. true Copies the artifacts (and optionally, the dependencies) to the targetRepo. false"
          },
          "artifacts": {
            "type": "boolean",
            "default": true,
            "description": "Determines whether to move/copy the build's artifacts."
          },
          "dependencies": {
            "type": "boolean",
            "default": false,
            "description": "Determines whether to move/copy the build's dependencies."
          },
          "scopes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "An array of dependency scopes that indicate the circumstances under which a dependency is available. Relevant when dependencies is set to true. Common examples include compile and runtime."
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "description": "A list of properties to attach to the build's artifacts (regardless of whether a targetRepo is defined)."
          },
          "failFast": {
            "type": "boolean",
            "default": true,
            "description": "When set to true, fails and aborts the promotion operation upon receiving an error."
          }
        }
      },
      "BuildPromotionResponse": {
        "type": "object",
        "properties": {
          "messages": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PromotionMessage"
            }
          }
        }
      },
      "PromotionMessage": {
        "type": "object",
        "properties": {
          "level": {
            "type": "string",
            "enum": [
              "error",
              "warning",
              "info"
            ]
          },
          "message": {
            "type": "string"
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