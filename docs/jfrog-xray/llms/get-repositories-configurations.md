# Source: https://docs.jfrog.com/security/reference/get-repositories-configurations.md

# Get Repository Configuration

Returns the scanning configuration for a specific repository, including contextual analysis, exposures, retention, and path-specific settings.

Requires Read permission. Route supports project scope.


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
    "/api/v1/repos_config/{repo_name}": {
      "get": {
        "operationId": "get-repositories-configurations",
        "summary": "Get Repository Configuration",
        "description": "Returns the scanning configuration for a specific repository, including contextual analysis, exposures, retention, and path-specific settings.\n\nRequires Read permission. Route supports project scope.\n",
        "tags": [
          "Artifacts V1"
        ],
        "parameters": [
          {
            "name": "repo_name",
            "in": "path",
            "description": "Name of the repository.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "libs-release-local"
          },
          {
            "name": "projectKey",
            "in": "query",
            "description": "Scope to the specified project.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Repository configuration retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "repo_name": {
                      "type": "string"
                    },
                    "repo_config": {
                      "type": "object",
                      "properties": {
                        "vuln_contextual_analysis": {
                          "type": "boolean"
                        },
                        "retention_in_days": {
                          "type": "integer"
                        },
                        "exposures": {
                          "type": "object",
                          "properties": {
                            "scanners_category": {
                              "type": "object",
                              "properties": {
                                "services_scan": {
                                  "type": "boolean"
                                },
                                "secrets_scan": {
                                  "type": "boolean"
                                },
                                "applications_scan": {
                                  "type": "boolean"
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "repo_paths_config": {
                      "type": "object",
                      "properties": {
                        "patterns": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "include": {
                                "type": "string"
                              },
                              "exclude": {
                                "type": "string"
                              },
                              "index_new_artifacts": {
                                "type": "boolean"
                              },
                              "retention_in_days": {
                                "type": "integer"
                              }
                            }
                          }
                        },
                        "all_other_artifacts": {
                          "type": "object",
                          "properties": {
                            "index_new_artifacts": {
                              "type": "boolean"
                            },
                            "retention_in_days": {
                              "type": "integer"
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "repo_name": "libs-release-local",
                  "repo_config": {
                    "vuln_contextual_analysis": true,
                    "retention_in_days": 90
                  }
                }
              }
            }
          },
          "400": {
            "description": "Empty repository name.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
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
      "name": "Artifacts V1",
      "description": "APIs from Artifacts V1"
    }
  ]
}
```