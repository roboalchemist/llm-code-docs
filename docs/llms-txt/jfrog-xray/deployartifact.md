# Source: https://docs.jfrog.com/artifactory/reference/deployartifact.md

# Deploy Artifact or Create Directory

**Deploy Artifact**: Deploy an artifact to the specified destination.

**Create Directory**: Create a new directory by specifying a path that ends with `/` and omitting the request body.

You can also attach properties as part of deploying artifacts or creating directories.

Important: In certain cases (particularly when working with large artifacts), the Created timestamp might be later than the Last Modified timestamp. This can occur because the Last Modified timestamp records when the upload began, whereas the Created timestamp is set only when the upload is complete and committed to the database.

Security: Requires a user with 'deploy' permissions (can be anonymous)


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
    "/{repoKey}/{filePath}": {
      "put": {
        "tags": [
          "Deploy Artifact APIs"
        ],
        "summary": "Deploy Artifact or Create Directory",
        "operationId": "deployArtifact",
        "description": "**Deploy Artifact**: Deploy an artifact to the specified destination.\n\n**Create Directory**: Create a new directory by specifying a path that ends with `/` and omitting the request body.\n\nYou can also attach properties as part of deploying artifacts or creating directories.\n\nImportant: In certain cases (particularly when working with large artifacts), the Created timestamp might be later than the Last Modified timestamp. This can occur because the Last Modified timestamp records when the upload began, whereas the Created timestamp is set only when the upload is complete and committed to the database.\n\nSecurity: Requires a user with 'deploy' permissions (can be anonymous)\n",
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
            "description": "Path to the artifact or directory within the repository. For directories, the path must end with `/`.",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "X-Checksum-Sha1",
            "in": "header",
            "description": "SHA1 checksum to verify the integrity of the deployment. Artifactory rejects the deployment if the checksum does not match. Only applicable for artifact deployment.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Checksum-Sha256",
            "in": "header",
            "description": "SHA256 checksum to verify the integrity of the deployment. Artifactory rejects the deployment if the checksum does not match. Only applicable for artifact deployment.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": false,
          "description": "Binary content of the artifact to deploy. Omit for directory creation.",
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
            "description": "Created - Artifact deployed or directory created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ItemCreated"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Invalid path, invalid checksum header, or malformed request.",
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
            "description": "Permission Denied - The user does not have deploy permissions on this repository.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - Repository not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "405": {
            "description": "Method Not Allowed - The target path resolves to a repository that does not accept PUT (e.g., a virtual repository).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "409": {
            "description": "Conflict - Duplicate artifact or checksum mismatch",
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