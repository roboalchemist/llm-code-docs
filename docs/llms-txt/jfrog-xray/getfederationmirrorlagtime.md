# Source: https://docs.jfrog.com/artifactory/reference/getfederationmirrorlagtime.md

# Get Federation Mirror Lag Time

Returns the elapsed time since the last event that was not handled on each Federation mirror for all repositories. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2.

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
    "/federation/status/mirrorsLag": {
      "get": {
        "tags": [
          "Legacy Federation Monitoring"
        ],
        "summary": "Get Federation Mirror Lag Time",
        "description": "Returns the elapsed time since the last event that was not handled on each Federation mirror for all repositories. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2.",
        "operationId": "getFederationMirrorLagTime",
        "deprecated": true,
        "parameters": [
          {
            "name": "thresholdTimeInMs",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int64"
            },
            "description": "Returns only those repositories whose lag exceeds this defined threshold (in milliseconds)"
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
                      "localRepoKey": {
                        "type": "string"
                      },
                      "remoteUrl": {
                        "type": "string"
                      },
                      "remoteRepoKey": {
                        "type": "string"
                      },
                      "lagInMS": {
                        "type": "integer",
                        "format": "int64"
                      },
                      "eventRegistrationTimeStamp": {
                        "type": "integer",
                        "format": "int64"
                      }
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