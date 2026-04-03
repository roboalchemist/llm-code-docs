# Source: https://docs.jfrog.com/artifactory/reference/replayfailedbinarytasks.md

# Replay Failed Binary Tasks

This API marks binary tasks that previously failed to be processed again. This can be done for the entire repository or for a particular binary task in the repository.

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
      "name": "Binary Tasks",
      "description": "Binary task management operations"
    }
  ],
  "paths": {
    "/federation/binaries/failures/replay": {
      "put": {
        "tags": [
          "Binary Tasks"
        ],
        "summary": "Replay Failed Binary Tasks",
        "description": "This API marks binary tasks that previously failed to be processed again. This can be done for the entire repository or for a particular binary task in the repository.",
        "operationId": "replayFailedBinaryTasks",
        "parameters": [
          {
            "name": "repoKey",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The name of the repository"
          },
          {
            "name": "sha1",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "The SHA1 of the artifact. If not provided, all failed tasks for the repository will be replayed."
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "replayTasks": {
                      "type": "integer"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - repoKey parameter is required or invalid request",
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