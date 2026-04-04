# Source: https://docs.jfrog.com/artifactory/reference/getbuildinfo.md

# Build Info

Returns information about the specified build. Requires JFrog Container Registry or Artifactory Pro.

**Since**: 2.2.0

**Security**: Requires a privileged user with deploy permissions. From version 6.6, requires read permission for the build.


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
    "/build/{buildName}/{buildNumber}": {
      "get": {
        "tags": [
          "Builds"
        ],
        "summary": "Build Info",
        "description": "Returns information about the specified build. Requires JFrog Container Registry or Artifactory Pro.\n\n**Since**: 2.2.0\n\n**Security**: Requires a privileged user with deploy permissions. From version 6.6, requires read permission for the build.\n",
        "operationId": "getBuildInfo",
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
            "name": "started",
            "in": "query",
            "description": "The timestamp of when the build started. Should be in the format: 'yyyy-MM-dd'T'HH:mm:ss.SSSZ'",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "diff",
            "in": "query",
            "description": "The number of an older build to which you want to compare contents. For more information, see Builds Diff.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "project",
            "in": "query",
            "description": "The project associated with the build. If a project is not specified, or if you are not working with projects, the default build-info repository associated with your Artifactory instance is used.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved build info",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BuildInfoResponse"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have read permission for the build."
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
      },
      "BuildInfoResponse": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "buildInfo": {
            "$ref": "#/components/schemas/BuildInfo"
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