# Source: https://docs.jfrog.com/artifactory/reference/prioritizefederatedrepository.md

# Prioritize Federated Repository

Determines whether the queue of the specified Federated repository has priority access to system resources. Prioritizing the repository helps ensure timely synchronization of its events with other members of the Federation. There can be a maximum of 10 prioritized Federated repositories at any one time on the JPD.

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
    "/federation/prioritization/{repoKey}": {
      "put": {
        "tags": [
          "Federation Monitoring"
        ],
        "summary": "Prioritize Federated Repository",
        "description": "Determines whether the queue of the specified Federated repository has priority access to system resources. Prioritizing the repository helps ensure timely synchronization of its events with other members of the Federation. There can be a maximum of 10 prioritized Federated repositories at any one time on the JPD.",
        "operationId": "prioritizeFederatedRepository",
        "parameters": [
          {
            "name": "repoKey",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The repository key"
          },
          {
            "name": "priorityLevel",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "enum": [
                "high",
                "standard"
              ]
            },
            "description": "Defines the priority level assigned to the Federated repository"
          }
        ],
        "responses": {
          "200": {
            "description": "The repository was prioritized/deprioritized successfully",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Invalid request",
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
          "404": {
            "description": "The repository was not found",
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
            "description": "Internal error",
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