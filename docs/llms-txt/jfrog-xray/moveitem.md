# Source: https://docs.jfrog.com/artifactory/reference/moveitem.md

# Move Item

Moves an artifact or a folder to the specified destination. Supported by local repositories only. Optionally suppress cross-layout module path translation during move. You can test the move using dry run. 

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
      "name": "Artifact Management",
      "description": "Artifact management operations (copy, move, delete)"
    }
  ],
  "paths": {
    "/move/{srcRepoKey}/{srcFilePath}": {
      "post": {
        "tags": [
          "Artifact Management"
        ],
        "summary": "Move Item",
        "description": "Moves an artifact or a folder to the specified destination. Supported by local repositories only. Optionally suppress cross-layout module path translation during move. You can test the move using dry run. \n\nNotes: Requires Artifactory Pro.\n\nSince: 2.2.2\n\nSecurity: Requires a privileged user (can be anonymous)\n",
        "operationId": "moveItem",
        "parameters": [
          {
            "name": "srcRepoKey",
            "in": "path",
            "description": "Source repository key",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "srcFilePath",
            "in": "path",
            "description": "Source file path",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "to",
            "in": "query",
            "description": "Target path (format - /{targetRepoKey}/{targetFilePath})",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "dry",
            "in": "query",
            "description": "Dry run mode (1 for dry run, 0 for actual move)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 0
            }
          },
          {
            "name": "suppressLayouts",
            "in": "query",
            "description": "Suppress cross-layout module path translation (0 or 1, default 1)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 1
            }
          },
          {
            "name": "failFast",
            "in": "query",
            "description": "Fail fast on errors (0 or 1)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Item moved successfully",
            "content": {
              "application/vnd.org.jfrog.artifactory.storage.CopyOrMoveResult+json": {
                "schema": {
                  "$ref": "#/components/schemas/CopyOrMoveResult"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - The request parameters are invalid or the source path does not exist.",
            "content": {
              "application/vnd.org.jfrog.artifactory.storage.CopyOrMoveResult+json": {
                "schema": {
                  "$ref": "#/components/schemas/CopyOrMoveResult"
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
      "CopyOrMoveResult": {
        "type": "object",
        "properties": {
          "messages": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CopyOrMoveMessage"
            }
          }
        }
      },
      "CopyOrMoveMessage": {
        "type": "object",
        "properties": {
          "level": {
            "type": "string",
            "enum": [
              "INFO",
              "WARNING",
              "ERROR"
            ]
          },
          "message": {
            "type": "string"
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