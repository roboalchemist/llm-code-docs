# Source: https://docs.jfrog.com/artifactory/reference/getlistoffailedbinarytasks.md

# Get List of Failed Binary Tasks

Returns a list of tasks that failed because Artifactory was not able to retrieve the binary of the task. The number of attempts that Artifactory tries to retrieve the binary of the task is set by maximum, which is 10 by default.

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
    "/federation/binaries/failures/list": {
      "get": {
        "tags": [
          "Binary Tasks"
        ],
        "summary": "Get List of Failed Binary Tasks",
        "description": "Returns a list of tasks that failed because Artifactory was not able to retrieve the binary of the task. The number of attempts that Artifactory tries to retrieve the binary of the task is set by maximum, which is 10 by default.",
        "operationId": "getListOfFailedBinaryTasks",
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
            "name": "limit",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 1000
            },
            "description": "The number of tasks to be returned in the response"
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer"
            },
            "description": "The page number for a group of tasks, starting from 1"
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "sha1": {
                        "type": "string"
                      },
                      "repoKey": {
                        "type": "string"
                      },
                      "creationTime": {
                        "type": "integer",
                        "format": "int64"
                      },
                      "failuresCount": {
                        "type": "integer"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - repoKey parameter is required",
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