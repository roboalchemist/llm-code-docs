# Source: https://docs.jfrog.com/security/reference/update-repositories-configurations.md

# Update Repositories Configurations

Updates the scanning configuration for a specific repository, including contextual analysis settings, exposures scanning, retention period, and path-specific configurations.

Requires Admin or Index Resources permission.


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
    "/api/v1/repos_config": {
      "put": {
        "operationId": "update-repositories-configurations",
        "summary": "Update Repositories Configurations",
        "description": "Updates the scanning configuration for a specific repository, including contextual analysis settings, exposures scanning, retention period, and path-specific configurations.\n\nRequires Admin or Index Resources permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "repo_name"
                ],
                "properties": {
                  "repo_name": {
                    "type": "string",
                    "description": "Name of the repository to configure.",
                    "example": "libs-release-local"
                  },
                  "repo_config": {
                    "type": "object",
                    "description": "Repository-level configuration.",
                    "properties": {
                      "vuln_contextual_analysis": {
                        "type": "boolean",
                        "description": "Enable contextual analysis for vulnerabilities."
                      },
                      "retention_in_days": {
                        "type": "integer",
                        "description": "Number of days to retain scan results."
                      },
                      "exposures": {
                        "type": "object",
                        "description": "Exposures scanning configuration.",
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
                    "description": "Path-specific configurations.",
                    "properties": {
                      "patterns": {
                        "type": "array",
                        "description": "Path pattern rules.",
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
                        "description": "Configuration for artifacts not matching any pattern.",
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
                  "retention_in_days": 90,
                  "exposures": {
                    "scanners_category": {
                      "services_scan": true,
                      "secrets_scan": true,
                      "applications_scan": false
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Repository configuration updated successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "info": "Repository configuration has been updated successfully"
                }
              }
            }
          },
          "400": {
            "description": "Failed to decode request or invalid configuration.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to decode request"
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