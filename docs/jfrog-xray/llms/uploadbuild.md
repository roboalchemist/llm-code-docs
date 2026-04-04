# Source: https://docs.jfrog.com/artifactory/reference/uploadbuild.md

# Build Upload

Uploads a build by providing a buildinfo JSON file. All build modules must have the build.name and build.number properties set as well as the correct SHA1 and MD5 to be properly linked in the build info.

**Security**: Requires a privileged user. From version 6.6, requires deploy permission for the build, and delete permission for overriding existing build info artifact.


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
      "put": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Upload",
        "description": "Uploads a build by providing a buildinfo JSON file. All build modules must have the build.name and build.number properties set as well as the correct SHA1 and MD5 to be properly linked in the build info.\n\n**Security**: Requires a privileged user. From version 6.6, requires deploy permission for the build, and delete permission for overriding existing build info artifact.\n",
        "operationId": "uploadBuild",
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
            "name": "project",
            "in": "query",
            "description": "Limits the response to builds contained in the specified project.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Build info JSON file",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BuildInfo"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Build uploaded successfully"
          },
          "400": {
            "description": "Bad Request - The request body is malformed or a required parameter is missing."
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have deploy permission for the build, and delete permission for overriding existing build info artifact."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BuildInfo": {
        "type": "object",
        "description": "Build info JSON structure",
        "properties": {
          "version": {
            "type": "string",
            "description": "Build Info schema version"
          },
          "name": {
            "type": "string",
            "description": "Build name"
          },
          "number": {
            "type": "string",
            "description": "Build number"
          },
          "type": {
            "type": "string",
            "enum": [
              "MAVEN",
              "GRADLE",
              "ANT",
              "IVY",
              "GENERIC"
            ],
            "description": "Build type"
          },
          "buildAgent": {
            "$ref": "#/components/schemas/BuildAgent"
          },
          "agent": {
            "$ref": "#/components/schemas/Agent"
          },
          "started": {
            "type": "string",
            "format": "date-time",
            "description": "Build start time in the format of yyyy-MM-dd'T'HH:mm:ss.SSSZ"
          },
          "artifactoryPluginVersion": {
            "type": "string"
          },
          "durationMillis": {
            "type": "integer",
            "format": "int64",
            "description": "Build duration in milliseconds"
          },
          "artifactoryPrincipal": {
            "type": "string",
            "description": "Artifactory principal (the Artifactory user used for deployment)"
          },
          "url": {
            "type": "string",
            "description": "CI server URL"
          },
          "vcs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VcsInfo"
            }
          },
          "licenseControl": {
            "$ref": "#/components/schemas/LicenseControl"
          },
          "buildRetention": {
            "$ref": "#/components/schemas/BuildRetention"
          },
          "modules": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BuildModule"
            }
          },
          "issues": {
            "$ref": "#/components/schemas/Issues"
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "description": "Environment variables and properties collected from the CI server"
          }
        }
      },
      "BuildAgent": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Build tool type"
          },
          "version": {
            "type": "string",
            "description": "Build tool version"
          }
        }
      },
      "Agent": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "CI server type"
          },
          "version": {
            "type": "string",
            "description": "CI server version"
          }
        }
      },
      "VcsInfo": {
        "type": "object",
        "properties": {
          "revision": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "branch": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        }
      },
      "LicenseControl": {
        "type": "object",
        "properties": {
          "runChecks": {
            "type": "boolean",
            "description": "Artifactory will run automatic license scanning after the build is complete"
          },
          "includePublishedArtifacts": {
            "type": "boolean",
            "description": "Should Artifactory run license checks on the build artifacts, in addition to the build dependencies"
          },
          "autoDiscover": {
            "type": "boolean",
            "description": "Should Artifactory auto discover licenses"
          },
          "scopesList": {
            "type": "string",
            "description": "A space-separated list of dependency scopes/configurations to run license violation checks on"
          },
          "licenseViolationsRecipientsList": {
            "type": "string",
            "description": "Emails of recipients that should be notified of license violations in the build info (space-separated list)"
          }
        }
      },
      "BuildRetention": {
        "type": "object",
        "properties": {
          "deleteBuildArtifacts": {
            "type": "boolean",
            "description": "Automatically remove build artifacts stored in Artifactory"
          },
          "count": {
            "type": "integer",
            "description": "The maximum number of builds to store in Artifactory"
          },
          "minimumBuildDate": {
            "type": "integer",
            "format": "int64",
            "description": "Earliest build date to store in Artifactory"
          },
          "buildNumbersNotToBeDiscarded": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of build numbers that should not be removed from Artifactory"
          }
        }
      },
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
      },
      "Issues": {
        "type": "object",
        "properties": {
          "tracker": {
            "$ref": "#/components/schemas/Tracker"
          },
          "aggregateBuildIssues": {
            "type": "boolean",
            "description": "Whether or not there are issues that already appeared in previous builds"
          },
          "aggregationBuildStatus": {
            "type": "string"
          },
          "affectedIssues": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AffectedIssue"
            }
          }
        }
      },
      "Tracker": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "version": {
            "type": "string"
          }
        }
      },
      "AffectedIssue": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string"
          },
          "url": {
            "type": "string"
          },
          "summary": {
            "type": "string"
          },
          "aggregated": {
            "type": "boolean",
            "description": "Whether or not this specific issue already appeared in previous builds"
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