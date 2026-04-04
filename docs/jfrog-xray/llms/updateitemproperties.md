# Source: https://docs.jfrog.com/artifactory/reference/updateitemproperties.md

# Update Item Properties

Attach and modify properties to an item - file, folder, or repository.
Requires Artifactory Pro, supported by local and local-cached repositories only.
Since: 6.1.0
Security: Requires a privileged user (Annotate authorization required)


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
    "/metadata/{repoKey}/{itemPath}": {
      "patch": {
        "tags": [
          "Item Management APIs"
        ],
        "summary": "Update Item Properties",
        "operationId": "updateItemProperties",
        "description": "Attach and modify properties to an item - file, folder, or repository.\nRequires Artifactory Pro, supported by local and local-cached repositories only.\nSince: 6.1.0\nSecurity: Requires a privileged user (Annotate authorization required)\n",
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
            "name": "recursiveProperties",
            "in": "query",
            "description": "Apply properties recursively (0 or 1)",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          },
          {
            "name": "atomicProperties",
            "in": "query",
            "description": "Atomic properties update (0 or 1)",
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
        "requestBody": {
          "required": true,
          "description": "Properties to update",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdatePropertiesRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Properties updated successfully (no content)"
          },
          "400": {
            "description": "Bad Request - The request body is malformed or invalid, or props/stats fields are missing.",
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
            "description": "Permission Denied - The user does not have Annotate authorization.",
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
      "UpdatePropertiesRequest": {
        "type": "object",
        "properties": {
          "props": {
            "type": "object",
            "additionalProperties": {
              "oneOf": [
                {
                  "type": "string",
                  "description": "Single property value"
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string"
                  },
                  "description": "Multiple property values"
                },
                {
                  "type": "null",
                  "description": "Set to null to remove the property"
                }
              ]
            },
            "description": "Properties to update. Each property can be:\n- A single string value: \"value1\"\n- An array of strings: [\"value1\", \"value2\"]\n- null to remove the property\n"
          }
        },
        "example": {
          "props": {
            "singleValue": "myValue",
            "multiValue": [
              "value1",
              "value2"
            ],
            "toBeRemoved": null
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