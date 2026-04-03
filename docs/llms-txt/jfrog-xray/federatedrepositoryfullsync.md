# Source: https://docs.jfrog.com/artifactory/reference/federatedrepositoryfullsync.md

# Federated Repository Full Sync

Runs a full synchronization between the Federated repository members. Starting with Artifactory 7.104.2, there is an option to use the Federation Comparison tool, which uses the isDry query parameter to generate a JSON file listing the binaries requiring synchronization without carrying out the operation.

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
      "name": "Federation Management",
      "description": "Federation repository management operations"
    }
  ],
  "paths": {
    "/federation/fullSync/{repoKey}": {
      "post": {
        "tags": [
          "Federation Management"
        ],
        "summary": "Federated Repository Full Sync",
        "description": "Runs a full synchronization between the Federated repository members. Starting with Artifactory 7.104.2, there is an option to use the Federation Comparison tool, which uses the isDry query parameter to generate a JSON file listing the binaries requiring synchronization without carrying out the operation.",
        "operationId": "federatedRepositoryFullSync",
        "parameters": [
          {
            "name": "repoKey",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The name of the repository"
          },
          {
            "name": "mirror",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "The URL of the specific Federation member on which you want to run the Full Sync. If this parameter is not set, the Full Sync is run against all remote Federation members."
          },
          {
            "name": "isDry",
            "in": "query",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "When set to true, runs the Federation Comparison tool to determine which files on the local member are missing on the remote members."
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
                    "message": {
                      "type": "string"
                    },
                    "resultPaths": {
                      "type": "array",
                      "items": {
                        "type": "string"
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