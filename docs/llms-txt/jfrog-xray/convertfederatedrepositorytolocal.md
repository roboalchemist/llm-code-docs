# Source: https://docs.jfrog.com/artifactory/reference/convertfederatedrepositorytolocal.md

# Convert Federated Repository to a Local Repository

Converts the specified Federated repository to a local repository. The conversion from Federated back to local is allowed only if the Federated repository is not part of an active Federation containing additional members.

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
    "/federation/convertToLocal": {
      "post": {
        "tags": [
          "Federation Management"
        ],
        "summary": "Convert Federated Repository to a Local Repository",
        "description": "Converts the specified Federated repository to a local repository. The conversion from Federated back to local is allowed only if the Federated repository is not part of an active Federation containing additional members.",
        "operationId": "convertFederatedRepositoryToLocal",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "A list of Federated repositories to convert back to local repositories"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "One or more repos converted successfully",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "object",
                      "properties": {
                        "failedConversionRepositories": {
                          "type": "object",
                          "additionalProperties": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Repos failed to convert",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "failedConversionRepositories": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "string"
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
          "404": {
            "description": "Not Found - The specified resource was not found.",
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