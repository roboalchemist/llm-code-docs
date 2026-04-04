# Source: https://docs.jfrog.com/artifactory/reference/getfederatedrepositorystatusv2.md

# Get Federated Repository Status (v2)

Returns the synchronization status of the Federation for a specific repository. This is the v2 version of the endpoint, which was released to offer a wider range of possible member statuses. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2. This API greatly impacts the database and should be used with care.

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
      "name": "Legacy Federation Monitoring",
      "description": "Legacy federation monitoring operations (deprecated)"
    }
  ],
  "paths": {
    "/v2/federation/status/repo/{repoKey}": {
      "get": {
        "tags": [
          "Legacy Federation Monitoring"
        ],
        "summary": "Get Federated Repository Status (v2)",
        "description": "Returns the synchronization status of the Federation for a specific repository. This is the v2 version of the endpoint, which was released to offer a wider range of possible member statuses. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2. This API greatly impacts the database and should be used with care.",
        "operationId": "getFederatedRepositoryStatusV2",
        "deprecated": true,
        "parameters": [
          {
            "name": "repoKey",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The repository key"
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
                    "localKey": {
                      "type": "string"
                    },
                    "binariesTasksInfo": {
                      "type": "object"
                    },
                    "mirrorEventsStatusInfo": {
                      "type": "array",
                      "items": {
                        "type": "object"
                      }
                    },
                    "federatedArtifactStatus": {
                      "type": "object"
                    }
                  }
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
          "404": {
            "description": "Repository not found",
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
            "description": "Method Not Allowed - RTFS is enabled",
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