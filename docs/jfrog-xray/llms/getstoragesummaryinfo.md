# Source: https://docs.jfrog.com/artifactory/reference/getstoragesummaryinfo.md

# Get Storage Summary Info

Returns storage summary information regarding binaries, file store and repositories.
Since: 4.2.0
Security: Requires authentication using Access Tokens, either as admin or using a scoped token with the system:info/storage:r scope.


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
      "name": "Storage Info",
      "description": "Storage information operations"
    }
  ],
  "paths": {
    "/storageinfo": {
      "get": {
        "tags": [
          "Storage Info"
        ],
        "summary": "Get Storage Summary Info",
        "description": "Returns storage summary information regarding binaries, file store and repositories.\nSince: 4.2.0\nSecurity: Requires authentication using Access Tokens, either as admin or using a scoped token with the system:info/storage:r scope.\n",
        "operationId": "getStorageSummaryInfo",
        "responses": {
          "200": {
            "description": "Successfully retrieved storage summary information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StorageSummaryInfo"
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
            "description": "Permission Denied - The user does not have the necessary permissions",
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
      "StorageSummaryInfo": {
        "type": "object",
        "properties": {
          "binariesSummary": {
            "$ref": "#/components/schemas/BinariesSummary"
          },
          "fileStoreSummary": {
            "$ref": "#/components/schemas/FileStoreSummary"
          },
          "repositoriesSummaryList": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RepositorySummary"
            }
          }
        }
      },
      "BinariesSummary": {
        "type": "object",
        "properties": {
          "binariesCount": {
            "type": "string"
          },
          "binariesSize": {
            "type": "string"
          },
          "artifactsSize": {
            "type": "string"
          },
          "optimization": {
            "type": "string"
          },
          "itemsCount": {
            "type": "string"
          },
          "artifactsCount": {
            "type": "string"
          }
        }
      },
      "FileStoreSummary": {
        "type": "object",
        "properties": {
          "storageType": {
            "type": "string"
          },
          "storageDirectory": {
            "type": "string"
          },
          "totalSpace": {
            "type": "string"
          },
          "usedSpace": {
            "type": "string"
          },
          "freeSpace": {
            "type": "string"
          }
        }
      },
      "RepositorySummary": {
        "type": "object",
        "properties": {
          "repoKey": {
            "type": "string"
          },
          "repoType": {
            "type": "string"
          },
          "foldersCount": {
            "type": "integer"
          },
          "filesCount": {
            "type": "integer"
          },
          "usedSpace": {
            "type": "string"
          },
          "usedSpaceInBytes": {
            "type": "integer"
          },
          "itemsCount": {
            "type": "integer"
          },
          "packageType": {
            "type": "string"
          },
          "projectKey": {
            "type": "string"
          },
          "percentage": {
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