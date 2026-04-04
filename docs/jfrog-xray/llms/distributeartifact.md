# Source: https://docs.jfrog.com/artifactory/reference/distributeartifact.md

# Distribute Artifact

Deploys artifacts from Artifactory to Bintray, and creates an entry in the corresponding Artifactory distribution repository specified. Requires Artifactory Pro.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Artifacts & Storage API",
    "description": "REST API for managing artifacts, storage, and related operations in JFrog Artifactory",
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
      "name": "Distribution",
      "description": "Artifact distribution operations"
    }
  ],
  "paths": {
    "/distribute": {
      "post": {
        "tags": [
          "Distribution"
        ],
        "summary": "Distribute Artifact",
        "description": "Deploys artifacts from Artifactory to Bintray, and creates an entry in the corresponding Artifactory distribution repository specified. Requires Artifactory Pro.",
        "operationId": "distributeArtifact",
        "requestBody": {
          "required": true,
          "description": "Distribution request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DistributeArtifactRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Artifact distributed successfully"
          },
          "400": {
            "description": "Bad Request - The request body is malformed or invalid.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have the necessary permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - The specified artifact or distribution repository does not exist.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "status": {
                  "type": "integer",
                  "description": "HTTP status code"
                },
                "message": {
                  "type": "string",
                  "description": "Error message"
                }
              }
            }
          }
        }
      },
      "DistributeArtifactRequest": {
        "type": "object",
        "required": [
          "targetRepo",
          "packagesRepoPaths"
        ],
        "properties": {
          "publish": {
            "type": "boolean",
            "default": true,
            "description": "If true, artifacts are published when deployed to Bintray. Default true."
          },
          "overrideExistingFiles": {
            "type": "boolean",
            "default": false,
            "description": "If true, Artifactory overwrites files already existing in the target path in Bintray. Existing version attributes are also overridden if defined in the distribution repository Advanced Configuration. Default false."
          },
          "gpgPassphrase": {
            "type": "string",
            "description": "If specified, Artifactory will GPG sign the version deployed to Bintray and apply the specified passphrase"
          },
          "async": {
            "type": "boolean",
            "default": false,
            "description": "If true, the artifact will be distributed asynchronously. Errors and warnings may be viewed in the log file. Default false."
          },
          "targetRepo": {
            "type": "string",
            "description": "The Distribution Repository into which artifacts should be deployed"
          },
          "packagesRepoPaths": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "An array of local or distribution repositories and corresponding paths to artifacts that should be deployed to the specified target repository in Bintray"
          },
          "dryRun": {
            "type": "boolean",
            "default": false,
            "description": "If true, distribution is only simulated. No files are actually moved. Default false."
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