# Source: https://docs.jfrog.com/artifactory/reference/retrievefolderorrepositoryarchive.md

# Retrieve Folder or Repository Archive

Returns an archive file (supports zip/tar/tar.gz/tgz) containing all the artifacts that reside under the specified path (folder or repository root). Requires Enable Folder Download to be set. 

Requires Artifactory Pro. 

Since: 4.1.0

Security: Requires a privileged user with read permissions on the path.

Downloading a folder or a repository's root is only supported for local (or cache) repositories.


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
    "/archive/download/{repoKey}/{path}": {
      "get": {
        "tags": [
          "Artifact Retrieval"
        ],
        "summary": "Retrieve Folder or Repository Archive",
        "description": "Returns an archive file (supports zip/tar/tar.gz/tgz) containing all the artifacts that reside under the specified path (folder or repository root). Requires Enable Folder Download to be set. \n\nRequires Artifactory Pro. \n\nSince: 4.1.0\n\nSecurity: Requires a privileged user with read permissions on the path.\n\nDownloading a folder or a repository's root is only supported for local (or cache) repositories.\n",
        "operationId": "retrieveFolderOrRepositoryArchive",
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
            "name": "path",
            "in": "path",
            "description": "Path within the repository (use empty string for repository root)",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "archiveType",
            "in": "query",
            "description": "Archive type",
            "required": true,
            "schema": {
              "type": "string",
              "enum": [
                "zip",
                "tar",
                "tar.gz",
                "tgz"
              ]
            }
          },
          {
            "name": "includeChecksumFiles",
            "in": "query",
            "description": "Include checksum files in the archive",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved folder or repository archive",
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
            "description": "Bad Request - Invalid path characters or malformed archive type.",
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
            "description": "Permission Denied - The user does not have read permissions on the path, or folder download is blocked by Xray.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - The specified repository or path does not exist.",
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