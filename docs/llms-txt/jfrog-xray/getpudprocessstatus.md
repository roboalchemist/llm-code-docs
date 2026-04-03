# Source: https://docs.jfrog.com/artifactory/reference/getpudprocessstatus.md

# Get Status of the PUD Process

Get the current status of the PUD process (i.e., running, stopped, finished, or error) along with relevant data on the process such as total binaries deleted, total size of disk space cleaned, information on the last handled directory, and other information.

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
    "/system/storage/prune/status": {
      "get": {
        "tags": [
          "Pruning Unreferenced Data"
        ],
        "summary": "Get Status of the PUD Process",
        "description": "Get the current status of the PUD process (i.e., running, stopped, finished, or error) along with relevant data on the process such as total binaries deleted, total size of disk space cleaned, information on the last handled directory, and other information.",
        "operationId": "getPudProcessStatus",
        "responses": {
          "200": {
            "description": "Successfully retrieved PUD process status",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PudProcessStatus"
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
            "description": "Precondition Failed - No Prune task found",
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
      "PudProcessResponse": {
        "type": "object",
        "properties": {
          "info": {
            "type": "string",
            "description": "Information message about the PUD process"
          }
        }
      },
      "PudProcessStatus": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string",
            "enum": [
              "running",
              "stopped",
              "finished",
              "error"
            ],
            "description": "The status of the PUD process"
          },
          "dryRun": {
            "type": "boolean",
            "description": "Whether the PUD process is actually deleting binaries"
          },
          "timing": {
            "$ref": "#/components/schemas/PudTiming"
          },
          "progress": {
            "type": "string",
            "description": "The number of directories that have been processed thus far"
          },
          "report": {
            "$ref": "#/components/schemas/PudReport"
          },
          "lastHandledDirectory": {
            "$ref": "#/components/schemas/PudDirectoryInfo"
          },
          "error": {
            "type": "string",
            "description": "Error details (only appears when an error occurs)"
          }
        }
      },
      "PudTiming": {
        "type": "object",
        "properties": {
          "startedAtMillis": {
            "type": "integer",
            "format": "int64",
            "description": "The time in milliseconds when the PUD process started"
          },
          "startedAt": {
            "type": "string",
            "description": "The time when the PUD process started. Artifactory returns this without a\ntimezone offset (e.g., \"2024-06-09T15:07:01\"), so the format is a\nlocal ISO 8601 datetime string rather than strict RFC 3339.\n"
          },
          "durationMillis": {
            "type": "integer",
            "format": "int64",
            "description": "The duration of the PUD process in milliseconds up until the point when this report was issued"
          },
          "duration": {
            "type": "string",
            "description": "The duration of the PUD process up until the point when this report was issued"
          },
          "lastUpdatedMillis": {
            "type": "integer",
            "format": "int64",
            "description": "The time in milliseconds at which this report was issued"
          },
          "lastUpdated": {
            "type": "string",
            "description": "The time at which this report was issued. Artifactory returns this without a\ntimezone offset (e.g., \"2024-06-09T15:07:15\"), so the format is a\nlocal ISO 8601 datetime string rather than strict RFC 3339.\n"
          }
        }
      },
      "PudReport": {
        "type": "object",
        "properties": {
          "totalBinariesProcessed": {
            "type": "integer",
            "format": "int64",
            "description": "The total number of binaries processed thus far"
          },
          "totalBinariesCleaned": {
            "type": "integer",
            "format": "int64",
            "description": "The total number of binaries removed thus far"
          },
          "totalBytesCleaned": {
            "type": "integer",
            "format": "int64",
            "description": "The total number of bytes reclaimed by the PUD process"
          }
        }
      },
      "PudDirectoryInfo": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the directory that was being processed when this report was issued"
          },
          "status": {
            "type": "string",
            "enum": [
              "running",
              "stopped",
              "finished",
              "error"
            ],
            "description": "Status relating to this directory only"
          },
          "binariesProcessed": {
            "type": "integer",
            "format": "int64",
            "description": "The number of binaries processed in this directory"
          },
          "binariesCleaned": {
            "type": "integer",
            "format": "int64",
            "description": "The number of binaries removed in this directory"
          },
          "bytesCleaned": {
            "type": "integer",
            "format": "int64",
            "description": "The number of bytes reclaimed in this directory"
          },
          "timing": {
            "$ref": "#/components/schemas/PudTiming"
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