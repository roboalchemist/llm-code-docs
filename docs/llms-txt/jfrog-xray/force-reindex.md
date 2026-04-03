# Source: https://docs.jfrog.com/security/reference/force-reindex.md

# Force Reindex

Triggers a reindex of specified artifacts and/or builds. Use this to reindex existing resources that may have missing component data. The total number of entities (artifacts + builds) cannot exceed the configured maximum (default 1000).

Requires Admin permission.


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
    "/api/v1/forceReindex": {
      "post": {
        "operationId": "force-reindex",
        "summary": "Force Reindex",
        "description": "Triggers a reindex of specified artifacts and/or builds. Use this to reindex existing resources that may have missing component data. The total number of entities (artifacts + builds) cannot exceed the configured maximum (default 1000).\n\nRequires Admin permission.\n",
        "tags": [
          "Indexing V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/IndexingForceReindexRequest"
              },
              "example": {
                "artifactory_id": "",
                "artifacts": [
                  {
                    "repository": "libs-release-local",
                    "path": "org/acme/app/1.0/app-1.0.jar",
                    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
                  }
                ],
                "builds": [
                  {
                    "name": "my-build",
                    "number": "42"
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Reindex completed. Check sent_to_reindex for successfully queued items. If failed_send_to_reindex is present, some items could not be processed.\n",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "sent_to_reindex": {
                      "type": "object",
                      "description": "Items successfully queued for reindexing.",
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
                              },
                              "sha256": {
                                "type": "string"
                              }
                            }
                          }
                        },
                        "builds": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string"
                              },
                              "number": {
                                "type": "string"
                              },
                              "build_repo": {
                                "type": "string"
                              }
                            }
                          }
                        }
                      }
                    },
                    "failed_send_to_reindex": {
                      "type": "object",
                      "description": "Items that failed to be queued. Only present if there were failures. Each item includes an error field.\n",
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
                              },
                              "sha256": {
                                "type": "string"
                              },
                              "error": {
                                "type": "string"
                              }
                            }
                          }
                        },
                        "builds": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string"
                              },
                              "number": {
                                "type": "string"
                              },
                              "build_repo": {
                                "type": "string"
                              },
                              "error": {
                                "type": "string"
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "sent_to_reindex": {
                    "artifacts": [
                      {
                        "repository": "libs-release-local",
                        "path": "org/acme/app/1.0/app-1.0.jar",
                        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
                      }
                    ],
                    "builds": [
                      {
                        "name": "my-build",
                        "number": "42"
                      }
                    ]
                  }
                }
              }
            }
          },
          "400": {
            "description": "Too many entities to reindex, or failed to get artifactory data.\n",
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
                  "error": "Total number of entities to reindex can't be greater than 1000"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse the request body.",
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
                  "error": "Failed to parse force reindex request"
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
                },
                "example": {
                  "error": "Failed to get artifactory data"
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
    },
    "schemas": {
      "IndexingForceReindexRequest": {
        "type": "object",
        "description": "Specifies which artifacts and/or builds to reindex. Provide at least one artifact or build.\n",
        "properties": {
          "artifactory_id": {
            "type": "string",
            "description": "Optional Artifactory instance ID. If omitted, the configured instance is used automatically.\n"
          },
          "artifacts": {
            "type": "array",
            "description": "List of artifacts to reindex.",
            "items": {
              "type": "object",
              "properties": {
                "repository": {
                  "type": "string",
                  "description": "Repository name.",
                  "example": "libs-release-local"
                },
                "path": {
                  "type": "string",
                  "description": "Artifact path within the repository.",
                  "example": "org/acme/app/1.0/app-1.0.jar"
                },
                "sha256": {
                  "type": "string",
                  "description": "SHA256 checksum of the artifact.",
                  "example": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
                }
              }
            }
          },
          "builds": {
            "type": "array",
            "description": "List of builds to reindex.",
            "items": {
              "type": "object",
              "required": [
                "name",
                "number"
              ],
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Build name.",
                  "example": "my-build"
                },
                "number": {
                  "type": "string",
                  "description": "Build number/version.",
                  "example": "42"
                },
                "build_repo": {
                  "type": "string",
                  "description": "Build repository name."
                },
                "project": {
                  "type": "string",
                  "description": "Project key. When set, the build repo is resolved from the project."
                }
              }
            }
          },
          "is_non_indexed_repo_allowed": {
            "type": "boolean",
            "description": "If true, allows reindexing artifacts from non-indexed repositories."
          }
        },
        "additionalProperties": true
      }
    }
  },
  "tags": [
    {
      "name": "Indexing V1",
      "description": "APIs from Indexing V1"
    }
  ]
}
```