# Source: https://docs.jfrog.com/artifactory/reference/getfederationstatedetails.md

# Get Federation State Details

Returns the current state of each repository Federation configured on your JPD.

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
    "/federation/status/stateList": {
      "get": {
        "tags": [
          "Federation Monitoring"
        ],
        "summary": "Get Federation State Details",
        "description": "Returns the current state of each repository Federation configured on your JPD.",
        "operationId": "getFederationStateDetails",
        "parameters": [
          {
            "name": "status",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "Comma-separated list of statuses to filter by (e.g., HEALTHY,ERROR)"
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
                    "federations": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "localRepoKey": {
                            "type": "string"
                          },
                          "memberInfoList": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "string"
                                },
                                "repoKey": {
                                  "type": "string"
                                },
                                "aggregatedStatus": {
                                  "type": "string"
                                },
                                "isSupported": {
                                  "type": "boolean"
                                },
                                "isDisabled": {
                                  "type": "boolean"
                                },
                                "isInLag": {
                                  "type": "boolean"
                                }
                              }
                            }
                          },
                          "priority": {
                            "type": "string",
                            "enum": [
                              "HIGH",
                              "STANDARD"
                            ]
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