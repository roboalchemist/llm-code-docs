# Source: https://docs.jfrog.com/artifactory/reference/deleteitemproperties.md

# Delete Item Properties

Deletes the specified properties from an item (file, folder, or repository).
 
Requires Artifactory Pro, supported by local and local-cached repositories only.

Since: 2.3.2  
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
      "name": "Item Management APIs",
      "description": "Item management operations including properties, deployment, and deletion"
    }
  ],
  "paths": {
    "/storage/{repoKey}/{itemPath}": {
      "delete": {
        "tags": [
          "Item Management APIs"
        ],
        "summary": "Delete Item Properties",
        "operationId": "deleteItemProperties",
        "description": "Deletes the specified properties from an item (file, folder, or repository).\n \nRequires Artifactory Pro, supported by local and local-cached repositories only.\n\nSince: 2.3.2  \nSecurity: Requires a privileged user (can be anonymous)\n",
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
            "name": "itemPath",
            "in": "path",
            "description": "Item path within the repository",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "properties",
            "in": "query",
            "description": "Comma-separated list of property keys to delete. Required.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "recursive",
            "in": "query",
            "description": "Delete properties recursively from all items in folder (0 or 1). Default: 1 (recursive) for folders.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 1
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Properties deleted successfully (no content)"
          },
          "400": {
            "description": "Bad Request - The properties parameter is missing or malformed.",
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
            "description": "Not Found - The specified item or repository does not exist.",
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