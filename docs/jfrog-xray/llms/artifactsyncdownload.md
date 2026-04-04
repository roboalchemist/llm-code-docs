# Source: https://docs.jfrog.com/artifactory/reference/artifactsyncdownload.md

# Artifact Sync Download

Downloads an artifact with or without returning the actual content to the client. When tracking the progress marks are printed (by default every 1024 bytes). This is extremely useful if you want to trigger downloads on a remote Artifactory server, for example to force eager cache population of large artifacts, but want to avoid the bandwidth consumption involved in transferring the artifacts to the triggering client. 

Notes: Requires Artifactory Pro.

Since: 2.2.2

Security: Requires a privileged user (can be anonymous)


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
    "/download/{repoKey}/{filePath}": {
      "get": {
        "tags": [
          "Artifact Retrieval"
        ],
        "summary": "Artifact Sync Download",
        "description": "Downloads an artifact with or without returning the actual content to the client. When tracking the progress marks are printed (by default every 1024 bytes). This is extremely useful if you want to trigger downloads on a remote Artifactory server, for example to force eager cache population of large artifacts, but want to avoid the bandwidth consumption involved in transferring the artifacts to the triggering client. \n\nNotes: Requires Artifactory Pro.\n\nSince: 2.2.2\n\nSecurity: Requires a privileged user (can be anonymous)\n",
        "operationId": "artifactSyncDownload",
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
            "description": "File path within the repository",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "content",
            "in": "query",
            "description": "Content mode (none, progress, or omit for full content)",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "none",
                "progress"
              ]
            }
          },
          {
            "name": "mark",
            "in": "query",
            "description": "Number of bytes to print a new progress mark",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 1024
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Download completed successfully",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "text/plain": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Invalid path or non-printable characters in the repo/file path.",
            "content": {
              "text/html": {
                "schema": {
                  "type": "string"
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
            "description": "Not Found - The specified file does not exist.",
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