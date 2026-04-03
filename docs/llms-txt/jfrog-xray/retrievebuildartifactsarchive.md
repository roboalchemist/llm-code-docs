# Source: https://docs.jfrog.com/artifactory/reference/retrievebuildartifactsarchive.md

# Retrieve Build Artifacts Archive

Returns an archive file (supports zip/tar/tar.gz/tgz) containing all the artifacts related to a specific build, you can optionally provide mappings to filter the results; the mappings support regexp capturing groups which enables you to dynamically construct the target path inside the result archive file. 

Requires Artifactory Pro.

Since: 2.6.5

Security: Requires a privileged user (can be anonymous)


**Consumes:** [application/json (application/vnd.org.jfrog.artifactory.build.BuildArtifactsRequest+json)](https://docs.jfrog.com/integrations/docs/configuration-json-files#build-artifacts-request-json)

**Produces:** application/zip (for zip archive type), application/x-tar (for tar archive type), application/x-gzip (for tar.gz/tgz archive type)

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
      "name": "Artifact Retrieval",
      "description": "Artifact retrieval operations"
    }
  ],
  "paths": {
    "/archive/buildArtifacts": {
      "post": {
        "tags": [
          "Artifact Retrieval"
        ],
        "summary": "Retrieve Build Artifacts Archive",
        "description": "Returns an archive file (supports zip/tar/tar.gz/tgz) containing all the artifacts related to a specific build, you can optionally provide mappings to filter the results; the mappings support regexp capturing groups which enables you to dynamically construct the target path inside the result archive file. \n\nRequires Artifactory Pro.\n\nSince: 2.6.5\n\nSecurity: Requires a privileged user (can be anonymous)\n",
        "operationId": "retrieveBuildArtifactsArchive",
        "requestBody": {
          "required": true,
          "description": "Build artifacts archive request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BuildArtifactsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully retrieved build artifacts archive",
            "content": {
              "application/zip": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "application/x-tar": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "application/x-gzip": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
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
      "BuildArtifactsRequest": {
        "type": "object",
        "required": [
          "buildName",
          "buildNumber",
          "archiveType"
        ],
        "properties": {
          "buildName": {
            "type": "string",
            "minLength": 1,
            "description": "The build name for search by"
          },
          "buildNumber": {
            "type": "string",
            "minLength": 1,
            "description": "The build number to search by, can be LATEST to search for the latest build number"
          },
          "buildStatus": {
            "type": "string",
            "description": "Optionally search by latest build status (e.g \"Released\")"
          },
          "repos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Optionally refine search for specific repos, omit to search within all repositories"
          },
          "archiveType": {
            "type": "string",
            "enum": [
              "tar",
              "zip",
              "tar.gz",
              "tgz"
            ],
            "description": "The archive file type to return"
          },
          "mappings": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ArchiveMapping"
            },
            "description": "Optionally refine the search by providing a list of regexp patterns to search by"
          }
        }
      },
      "ArchiveMapping": {
        "type": "object",
        "properties": {
          "input": {
            "type": "string",
            "description": "Regexp pattern to search by"
          },
          "output": {
            "type": "string",
            "description": "Optionally provide different path of the found artifacts inside the result archive, supports regexp groups tokens"
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