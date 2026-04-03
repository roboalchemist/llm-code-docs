# Source: https://docs.jfrog.com/artifactory/reference/startpudprocess.md

# Start PUD Process

This REST API is called to start a new PUD process, or resume a PUD process that was stopped before completion. The Pruning Unreferenced Data (PUD) APIs are used to delete randomly existing binaries in the filestore that are not referenced in Artifactory.

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
      "name": "Pruning Unreferenced Data",
      "description": "Pruning Unreferenced Data (PUD) operations"
    }
  ],
  "paths": {
    "/system/storage/prune/start": {
      "post": {
        "tags": [
          "Pruning Unreferenced Data"
        ],
        "summary": "Start PUD Process",
        "description": "This REST API is called to start a new PUD process, or resume a PUD process that was stopped before completion. The Pruning Unreferenced Data (PUD) APIs are used to delete randomly existing binaries in the filestore that are not referenced in Artifactory.",
        "operationId": "startPudProcess",
        "requestBody": {
          "required": false,
          "description": "PUD process parameters",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/StartPudProcessRequest"
              }
            }
          }
        },
        "responses": {
          "202": {
            "description": "Accepted - PUD process has been submitted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PudProcessResponse"
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
          },
          "412": {
            "description": "Precondition Failed - PUD process is already running or cannot be started",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PudProcessResponse"
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
      "StartPudProcessRequest": {
        "type": "object",
        "properties": {
          "dryRun": {
            "type": "boolean",
            "default": false,
            "description": "If false then unreferenced binaries will be actually removed from the filestore. If true then unreferenced binaries will not be removed from the filestore. This mode may be useful to estimate the number of unreferenced binaries in each directory without actually removing them."
          },
          "startFromDirectory": {
            "type": "string",
            "description": "If present, the PUD process will continue from the directory identified here. If this parameter is omitted, the PUD process starts to prune from the beginning of the directories list."
          },
          "startFromBinary": {
            "type": "integer",
            "format": "int32",
            "default": 0,
            "description": "If present, the PUD process continues from this position in the last directory that the previous PUD process stopped at. This parameter can be found in the response of the Get Status API at lastHandledDirectory>binariesProcessed. If omitted, the PUD process starts to prune from the first binary in the directory."
          },
          "binaryOlderThanDays": {
            "type": "integer",
            "format": "int32",
            "default": 1,
            "description": "If present, unreferenced binaries that are newer than binaryOlderThanDays are ignored by the PUD process. If binaryOlderThanDays = 0, the PUD process does not relate to the binary creation date."
          }
        }
      },
      "PudProcessResponse": {
        "type": "object",
        "properties": {
          "info": {
            "type": "string",
            "description": "Information message about the PUD process"
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