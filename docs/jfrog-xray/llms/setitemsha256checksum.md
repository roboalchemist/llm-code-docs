# Source: https://docs.jfrog.com/artifactory/reference/setitemsha256checksum.md

# Set Item SHA256 Checksum

Calculates an artifact's SHA256 checksum and attaches it as a property (with key "sha256"). If the artifact is a folder, then recursively calculates the SHA256 of each item in the folder and attaches the property to each item.
Since: 4.2.1
Security: Requires an admin user
Note: Artifactory natively supports SHA-256 since version 5.5. This API has been maintained to provide backward compatibility for users of older Artifactory versions.


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
      "name": "Item Management APIs",
      "description": "Item management operations including properties, deployment, and deletion"
    }
  ],
  "paths": {
    "/checksum/sha256": {
      "post": {
        "tags": [
          "Item Management APIs"
        ],
        "summary": "Set Item SHA256 Checksum",
        "operationId": "setItemSha256Checksum",
        "description": "Calculates an artifact's SHA256 checksum and attaches it as a property (with key \"sha256\"). If the artifact is a folder, then recursively calculates the SHA256 of each item in the folder and attaches the property to each item.\nSince: 4.2.1\nSecurity: Requires an admin user\nNote: Artifactory natively supports SHA-256 since version 5.5. This API has been maintained to provide backward compatibility for users of older Artifactory versions.\n",
        "requestBody": {
          "required": true,
          "description": "Repository and path information",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Sha256ChecksumRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "SHA256 checksum calculated and attached successfully"
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
            "description": "Permission Denied - The user does not have admin permissions.",
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
      "Sha256ChecksumRequest": {
        "type": "object",
        "required": [
          "repoKey",
          "path"
        ],
        "properties": {
          "repoKey": {
            "type": "string",
            "minLength": 1,
            "description": "Repository key"
          },
          "path": {
            "type": "string",
            "minLength": 1,
            "description": "Path to the artifact or folder"
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