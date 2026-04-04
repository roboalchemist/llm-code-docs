# Source: https://docs.jfrog.com/security/reference/scan-now_indexing-v2-openapi.md

# Scan Now

Enables you to index resources on-demand.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v2/index": {
      "post": {
        "operationId": "scan-now_indexing-v2-openapi",
        "summary": "Scan Now",
        "description": "Enables you to index resources on-demand.",
        "tags": [
          "Indexing V2"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "repo_path": {
                    "type": "string"
                  }
                },
                "required": [
                  "repo_path"
                ]
              },
              "example": {
                "repo_path": "local-maven-repo/org/jenkins-ci/main/jenkins-war/2.289.1/jenkins-war-2.289.1.war"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "sent_to_reindex": {
                      "type": "object",
                      "properties": {
                        "artifacts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "repository": {
                                "type": "string"
                              },
                              "path": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "repository",
                              "path"
                            ]
                          }
                        }
                      },
                      "required": [
                        "artifacts"
                      ]
                    }
                  },
                  "required": [
                    "sent_to_reindex"
                  ]
                },
                "example": {
                  "sent_to_reindex": {
                    "artifacts": [
                      {
                        "repository": "local-maven-repo",
                        "path": "org/jenkins-ci/main/jenkins-war/2.289.1/jenkins-war-2.289.1.war"
                      }
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
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Indexing V2",
      "description": "APIs from Indexing V2"
    }
  ]
}
```