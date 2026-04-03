# Source: https://docs.jfrog.com/artifactory/reference/deployartifactbychecksum.md

# Deploy Artifact by Checksum

Deploy an artifact to the specified destination by checking if the artifact content already exists in Artifactory.

If Artifactory already contains a user-readable artifact with the same checksum, the artifact content is copied to the new location and returns a response without requiring content transfer.

Otherwise, a 404 error is returned to indicate that content upload is expected to deploy the artifact.

If the X-Checksum-Deploy header is set to false, the artifact will be uploaded successfully with a 201 response, even if it didn't exist before, and submitted checksums will have the status Uploaded: Identical.

You can also attach properties when deploying artifacts.

Since: 2.5.1  
Security: Requires a user with Deploy permissions (can be anonymous)


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
      "name": "Deploy Artifact APIs",
      "description": "Deploy artifact operations including standard deployment, checksum deployment, and archive deployment"
    }
  ],
  "paths": {
    "/{repoKey}/{filePath}/checksum": {
      "put": {
        "tags": [
          "Deploy Artifact APIs"
        ],
        "summary": "Deploy Artifact by Checksum",
        "operationId": "deployArtifactByChecksum",
        "description": "Deploy an artifact to the specified destination by checking if the artifact content already exists in Artifactory.\n\nIf Artifactory already contains a user-readable artifact with the same checksum, the artifact content is copied to the new location and returns a response without requiring content transfer.\n\nOtherwise, a 404 error is returned to indicate that content upload is expected to deploy the artifact.\n\nIf the X-Checksum-Deploy header is set to false, the artifact will be uploaded successfully with a 201 response, even if it didn't exist before, and submitted checksums will have the status Uploaded: Identical.\n\nYou can also attach properties when deploying artifacts.\n\nSince: 2.5.1  \nSecurity: Requires a user with Deploy permissions (can be anonymous)\n",
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
            "description": "Path to the artifact within the repository",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "X-Checksum-Deploy",
            "in": "header",
            "description": "Must be set to true for checksum-based deployment",
            "required": true,
            "schema": {
              "type": "boolean",
              "enum": [
                true
              ]
            }
          },
          {
            "name": "X-Checksum-Sha1",
            "in": "header",
            "description": "SHA1 checksum value. At least one checksum header (X-Checksum-Sha1, X-Checksum-Sha256, or X-Checksum) must be provided.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Checksum-Sha256",
            "in": "header",
            "description": "SHA256 checksum value. At least one checksum header (X-Checksum-Sha1, X-Checksum-Sha256, or X-Checksum) must be provided.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Checksum",
            "in": "header",
            "description": "Generic checksum value (type resolved by length: 32 chars=MD5, 40 chars=SHA1, 64 chars=SHA256). At least one checksum header (X-Checksum-Sha1, X-Checksum-Sha256, or X-Checksum) must be provided.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": false,
          "description": "Binary content of the artifact (not needed if artifact exists)",
          "content": {
            "application/octet-stream": {
              "schema": {
                "type": "string",
                "format": "binary"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created - Artifact deployed successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ItemCreated"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Missing required checksum header or invalid checksum value.",
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
            "description": "Permission Denied - The user does not have deploy permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - Artifact with checksum not found, content upload required",
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
      "Checksums": {
        "type": "object",
        "properties": {
          "md5": {
            "type": "string"
          },
          "sha1": {
            "type": "string"
          },
          "sha256": {
            "type": "string"
          }
        }
      },
      "ItemCreated": {
        "type": "object",
        "properties": {
          "repo": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "createdBy": {
            "type": "string"
          },
          "downloadUri": {
            "type": "string"
          },
          "mimeType": {
            "type": "string"
          },
          "size": {
            "type": "string",
            "description": "Size in bytes"
          },
          "checksums": {
            "$ref": "#/components/schemas/Checksums"
          },
          "originalChecksums": {
            "$ref": "#/components/schemas/Checksums"
          },
          "uri": {
            "type": "string"
          }
        }
      },
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