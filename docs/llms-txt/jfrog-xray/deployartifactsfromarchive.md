# Source: https://docs.jfrog.com/artifactory/reference/deployartifactsfromarchive.md

# Deploy Artifacts from Archive

Deploys an archive containing multiple artifacts and extracts it at the specified destination while maintaining the archive's file structure.

Deployment is performed in a single HTTP request. Only the extracted content is deployed, not the archive file itself.

By default, the deployment of artifacts is performed sequentially. However, starting from Artifactory 7.96.3, artifact deployment can be performed in multiple parallel threads using the system parameter artifactory.explode.archive.threads. For example, if you set artifactory.explode.archive.threads = 10, the deployment of the artifacts contained in the archive will be performed in 10 parallel threads per archive file, which can save considerable time for large archive files.

Supported archive types: zip, tar, tar.gz, tgz

Note: Requires Artifactory Pro. Deployment of compressed archives (unlike tar) may incur considerable CPU overhead.

Since: 2.6.3  
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
    "/{repoKey}/{archivePath}": {
      "put": {
        "tags": [
          "Deploy Artifact APIs"
        ],
        "summary": "Deploy Artifacts from Archive",
        "operationId": "deployArtifactsFromArchive",
        "description": "Deploys an archive containing multiple artifacts and extracts it at the specified destination while maintaining the archive's file structure.\n\nDeployment is performed in a single HTTP request. Only the extracted content is deployed, not the archive file itself.\n\nBy default, the deployment of artifacts is performed sequentially. However, starting from Artifactory 7.96.3, artifact deployment can be performed in multiple parallel threads using the system parameter artifactory.explode.archive.threads. For example, if you set artifactory.explode.archive.threads = 10, the deployment of the artifacts contained in the archive will be performed in 10 parallel threads per archive file, which can save considerable time for large archive files.\n\nSupported archive types: zip, tar, tar.gz, tgz\n\nNote: Requires Artifactory Pro. Deployment of compressed archives (unlike tar) may incur considerable CPU overhead.\n\nSince: 2.6.3  \nSecurity: Requires a user with 'deploy' permissions (can be anonymous)\n",
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
            "name": "archivePath",
            "in": "path",
            "description": "Path where the archive should be extracted (must end with archive filename)",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "X-Explode-Archive",
            "in": "header",
            "description": "Must be set to true to explode the archive upon deployment",
            "required": true,
            "schema": {
              "type": "boolean",
              "enum": [
                true
              ]
            }
          },
          {
            "name": "X-Explode-Archive-Atomic",
            "in": "header",
            "description": "If true, archive will be exploded in an atomic operation upon deployment",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "description": "Binary content of the archive file (zip, tar, tar.gz, or tgz)",
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
            "application/gzip": {
              "schema": {
                "type": "string",
                "format": "binary"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created - Archive deployed and extracted successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Invalid archive or missing required headers",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
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
            "description": "Permission Denied - User does not have deploy permissions or Artifactory Pro required",
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