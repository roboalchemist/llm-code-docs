# Source: https://docs.jfrog.com/artifactory/reference/getfederationconnectiondetails.md

# Get Federation Connection Details

Returns the connection status of a Federated repository with other members of its Federation. This status indicates whether metadata events are being synchronized promptly between each source and each target within the Federation.

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
    "/federation/status/connectionStates/{repoKey}": {
      "get": {
        "tags": [
          "Federation Monitoring"
        ],
        "summary": "Get Federation Connection Details",
        "description": "Returns the connection status of a Federated repository with other members of its Federation. This status indicates whether metadata events are being synchronized promptly between each source and each target within the Federation.",
        "operationId": "getFederationConnectionDetails",
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
                    "memberConnections": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "localRepoKey": {
                            "type": "string"
                          },
                          "localPlatformUrl": {
                            "type": "string"
                          },
                          "remoteRepoKey": {
                            "type": "string"
                          },
                          "remotePlatformUrl": {
                            "type": "string"
                          },
                          "status": {
                            "type": "string"
                          },
                          "lagInMs": {
                            "type": "integer",
                            "format": "int64"
                          },
                          "queuedEvents": {
                            "type": "integer",
                            "format": "int64"
                          },
                          "disabled": {
                            "type": "boolean"
                          },
                          "supported": {
                            "type": "boolean"
                          }
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