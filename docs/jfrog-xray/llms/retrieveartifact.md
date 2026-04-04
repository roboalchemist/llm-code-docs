# Source: https://docs.jfrog.com/artifactory/reference/retrieveartifact.md

# Retrieve Artifact

Returns an artifact from the specified destination.

You can also use properties in deployment and resolution as part of retrieving artifacts.

Special tokens for retrieving latest versions:
- **Latest Maven Release/Integration**: Specify SNAPSHOT or [RELEASE] for the version in the requested path to get the latest Maven integration or release artifact.
- **Latest Non-Maven Release/Integration**: Specify [INTEGRATION] and [RELEASE] for the version in the requested path (replacing [folderItegRev] and [fileItegRev], as defined by the repository's Repository Layouts) to get the latest integration version or latest release version artifact accordingly based on alphabetical sorting.

Notes:
- Integration and release tokens cannot be mixed together.
- Only local, cache and virtual repositories will be used for latest version resolution.
- To change the retrieve latest behavior to retrieve the latest version based on the created date, add `artifactory.request.searchLatestReleaseByDateCreated=true` to `artifactory.system.properties` and restart Artifactory.
- Both [folderItegRev] and [fileItegRev] have to be defined in the repository layout.
- Latest version resolution requires Artifactory Pro.

Since: Latest Maven: 2.6.0; Latest non-Maven: 2.6.2
Security: Requires a user with 'read' permission (can be anonymous)


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
    "/{repoKey}/{filePath}": {
      "get": {
        "tags": [
          "Artifact Retrieval"
        ],
        "summary": "Retrieve Artifact",
        "operationId": "retrieveArtifact",
        "description": "Returns an artifact from the specified destination.\n\nYou can also use properties in deployment and resolution as part of retrieving artifacts.\n\nSpecial tokens for retrieving latest versions:\n- **Latest Maven Release/Integration**: Specify SNAPSHOT or [RELEASE] for the version in the requested path to get the latest Maven integration or release artifact.\n- **Latest Non-Maven Release/Integration**: Specify [INTEGRATION] and [RELEASE] for the version in the requested path (replacing [folderItegRev] and [fileItegRev], as defined by the repository's Repository Layouts) to get the latest integration version or latest release version artifact accordingly based on alphabetical sorting.\n\nNotes:\n- Integration and release tokens cannot be mixed together.\n- Only local, cache and virtual repositories will be used for latest version resolution.\n- To change the retrieve latest behavior to retrieve the latest version based on the created date, add `artifactory.request.searchLatestReleaseByDateCreated=true` to `artifactory.system.properties` and restart Artifactory.\n- Both [folderItegRev] and [fileItegRev] have to be defined in the repository layout.\n- Latest version resolution requires Artifactory Pro.\n\nSince: Latest Maven: 2.6.0; Latest non-Maven: 2.6.2\nSecurity: Requires a user with 'read' permission (can be anonymous)\n",
        "parameters": [
          {
            "name": "repoKey",
            "in": "path",
            "description": "Repository key",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "filePath",
            "in": "path",
            "description": "Path to the artifact within the repository. Can include special tokens: SNAPSHOT, [RELEASE], [INTEGRATION] for latest version resolution.",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "skipUpdateStats",
            "in": "query",
            "description": "Skip updating download statistics for this artifact",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "trace",
            "in": "query",
            "description": "Simulates an artifact retrieval request and returns verbose output about the resolution process. Useful for debugging artifact retrieval issues.",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved artifact or trace output",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "text/plain": {
                "schema": {
                  "type": "string",
                  "description": "Trace output when trace parameter is used"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - User does not have read permissions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - Artifact does not exist",
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