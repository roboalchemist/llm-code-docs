# Source: https://docs.jfrog.com/artifactory/reference/getrubygemversionlist.md

# Get RubyGem Version List

Returns the list of versions and other metadata associated with a specific Ruby gem.

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
    "/gems/{repoName}/api/v1/versions/{gemName}": {
      "get": {
        "tags": [
          "Artifact Retrieval"
        ],
        "summary": "Get RubyGem Version List",
        "description": "Returns the list of versions and other metadata associated with a specific Ruby gem.",
        "operationId": "getRubyGemVersionList",
        "parameters": [
          {
            "name": "repoName",
            "in": "path",
            "description": "Repository name",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "gemName",
            "in": "path",
            "description": "Gem name",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved RubyGem version list",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/RubyGemVersion"
                  }
                }
              },
              "application/yaml": {
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
          "404": {
            "description": "Not Found - The specified gem does not exist.",
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
      "RubyGemVersion": {
        "type": "object",
        "properties": {
          "authors": {
            "type": "string"
          },
          "built_at": {
            "type": "string",
            "format": "date-time"
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "description": {
            "type": "string"
          },
          "downloads_count": {
            "type": "integer"
          },
          "metadata": {
            "type": "object",
            "additionalProperties": true
          },
          "number": {
            "type": "string"
          },
          "summary": {
            "type": "string"
          },
          "platform": {
            "type": "string"
          },
          "ruby_version": {
            "type": "string"
          },
          "prerelease": {
            "type": "boolean"
          },
          "licenses": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "requirements": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "sha": {
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