# Source: https://docs.jfrog.com/artifactory/reference/getfederationsyncstate.md

# Get Federation Sync State

Returns the synchronization state of all Federated repositories in the JPD. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2.

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
    "/federation/state": {
      "get": {
        "tags": [
          "Legacy Federation Monitoring"
        ],
        "summary": "Get Federation Sync State",
        "description": "Returns the synchronization state of all Federated repositories in the JPD. This API is not supported by the standalone Artifactory Federation service that was released in version 7.104.2.",
        "operationId": "getFederationSyncState",
        "deprecated": true,
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
                      "key": {
                        "type": "string"
                      },
                      "status": {
                        "type": "string",
                        "enum": [
                          "SYNCING",
                          "FULL_SYNC_RUNNING",
                          "DISABLED",
                          "OUT_OF_SYNC"
                        ]
                      },
                      "members": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "remoteKey": {
                              "type": "string"
                            },
                            "remoteUrl": {
                              "type": "string"
                            }
                          }
                        }
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