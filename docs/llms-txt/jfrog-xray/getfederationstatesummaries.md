# Source: https://docs.jfrog.com/artifactory/reference/getfederationstatesummaries.md

# Get Federation State Summaries

Returns the number of Federation members that are currently in each of the following states - HEALTHY, NOT_AVAILABLE, DELAYED, PENDING_FS, FULL_SYNC_RUNNING, ERROR, DISABLED

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Federated Repositories API",
    "description": "REST API for managing federated repositories in JFrog Artifactory, including conversion, synchronization, monitoring, and binary task management.",
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
      "name": "Federation Monitoring",
      "description": "Federation monitoring operations"
    }
  ],
  "paths": {
    "/federation/status/stateSummary": {
      "get": {
        "tags": [
          "Federation Monitoring"
        ],
        "summary": "Get Federation State Summaries",
        "description": "Returns the number of Federation members that are currently in each of the following states - HEALTHY, NOT_AVAILABLE, DELAYED, PENDING_FS, FULL_SYNC_RUNNING, ERROR, DISABLED",
        "operationId": "getFederationStateSummaries",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "federationStates": {
                      "type": "object",
                      "properties": {
                        "HEALTHY": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "NOT_AVAILABLE": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "DELAYED": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "PENDING_FS": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "FULL_SYNC_RUNNING": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "ERROR": {
                          "type": "integer",
                          "format": "int64"
                        },
                        "DISABLED": {
                          "type": "integer",
                          "format": "int64"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - The provided authentication is invalid.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have the necessary permissions to perform this action.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false
                }
              }
            }
          },
          "405": {
            "description": "Method Not Allowed - RTFS is not enabled",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false
                }
              }
            }
          },
          "500": {
            "description": "Internal Server Error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false
                }
              }
            }
          }
        }
      }
    }
  },
  "security": [
    {
      "BasicAuth": []
    },
    {
      "ApiKeyAuth": []
    },
    {
      "BearerAuth": []
    }
  ],
  "components": {
    "securitySchemes": {
      "BasicAuth": {
        "type": "http",
        "scheme": "basic"
      },
      "ApiKeyAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "X-JFrog-Art-Api"
      },
      "BearerAuth": {
        "type": "http",
        "scheme": "bearer"
      }
    }
  }
}
```