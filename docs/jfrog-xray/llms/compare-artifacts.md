# Source: https://docs.jfrog.com/security/reference/compare-artifacts.md

# Compare Artifacts

Compares two artifacts and produces a delta of their dependency components. Returns the source and target artifact metadata plus three component lists: added (in target only), removed (in source only), and unchanged (in both).

Requires a user with Read permission.


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
    "/api/v1/dependencyGraph/artifactDelta": {
      "post": {
        "operationId": "compare-artifacts",
        "summary": "Compare Artifacts",
        "description": "Compares two artifacts and produces a delta of their dependency components. Returns the source and target artifact metadata plus three component lists: added (in target only), removed (in source only), and unchanged (in both).\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ArtifactsCompareArtifactsRequest"
              },
              "example": {
                "source_artifact_path": "/pnnl/goss/goss-core-client/0.1.7/goss-core-client-0.1.7-sources.jar",
                "target_artifact_path": "/pnnl/goss/goss-core-client/0.1.8/goss-core-client-0.1.8-sources.jar"
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
                    "source_artifact": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        },
                        "pkg_type": {
                          "type": "string"
                        },
                        "sha256": {
                          "type": "string"
                        },
                        "sha1": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "name",
                        "path",
                        "pkg_type",
                        "sha256",
                        "sha1"
                      ]
                    },
                    "target_artifact": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        },
                        "pkg_type": {
                          "type": "string"
                        },
                        "sha256": {
                          "type": "string"
                        },
                        "sha1": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "name",
                        "path",
                        "pkg_type",
                        "sha256",
                        "sha1"
                      ]
                    },
                    "removed": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "component_name": {
                            "type": "string"
                          },
                          "component_id": {
                            "type": "string"
                          },
                          "package_type": {
                            "type": "string"
                          },
                          "version": {
                            "type": "string"
                          },
                          "created": {
                            "type": "string"
                          },
                          "modified": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "component_name",
                          "component_id",
                          "package_type",
                          "version",
                          "created",
                          "modified"
                        ]
                      }
                    },
                    "added": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "component_name": {
                            "type": "string"
                          },
                          "component_id": {
                            "type": "string"
                          },
                          "package_type": {
                            "type": "string"
                          },
                          "version": {
                            "type": "string"
                          },
                          "created": {
                            "type": "string"
                          },
                          "modified": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "component_name",
                          "component_id",
                          "package_type",
                          "version",
                          "created",
                          "modified"
                        ]
                      }
                    },
                    "unchanged": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "component_name": {
                            "type": "string"
                          },
                          "component_id": {
                            "type": "string"
                          },
                          "package_type": {
                            "type": "string"
                          },
                          "version": {
                            "type": "string"
                          },
                          "created": {
                            "type": "string"
                          },
                          "modified": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "component_name",
                          "component_id",
                          "package_type",
                          "version",
                          "created",
                          "modified"
                        ]
                      }
                    }
                  },
                  "required": [
                    "source_artifact",
                    "target_artifact",
                    "removed",
                    "added",
                    "unchanged"
                  ]
                },
                "example": {
                  "source_artifact": {
                    "name": "artifactory-pro.zip",
                    "path": "art2/ext-release-local/",
                    "pkg_type": "Generic",
                    "sha256": "d160c68ed8879ae42756e159daec1dd7ecfd53b6192321656b72715e20d46dd2",
                    "sha1": ""
                  },
                  "target_artifact": {
                    "name": "artifactory-pro.zip",
                    "path": "art2/ext-release-local/",
                    "pkg_type": "Generic",
                    "sha256": "d160c68ed8879ae42756e159daec1dd7ecfd53b6192321656b72715e20d46dd2",
                    "sha1": ""
                  },
                  "removed": [
                    {
                      "component_name": "some-component-1.1",
                      "component_id": "pip://some-component:1.1",
                      "package_type": "pip",
                      "version": "1.1",
                      "created": "2008-06-09T16:50:19Z",
                      "modified": "2015-07-26T17:49:47Z"
                    }
                  ],
                  "added": [
                    {
                      "component_name": "Jinja2.7.2",
                      "component_id": "pip://Jinja2:2.7.2",
                      "package_type": "pip",
                      "version": "2.7.2",
                      "created": "2008-06-09T16:50:19Z",
                      "modified": "2015-07-26T17:49:47Z"
                    }
                  ],
                  "unchanged": [
                    {
                      "component_name": "Apache1.4",
                      "component_id": "gav://apache:1.4",
                      "package_type": "maven",
                      "version": "1.4",
                      "created": "2008-06-09T16:50:19Z",
                      "modified": "2015-07-26T17:49:47Z"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Artifact '<PATH>' doesn't exist or isn't indexed in Xray",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse request",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
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
      "ArtifactsCompareArtifactsRequest": {
        "type": "object",
        "required": [
          "source_artifact_path",
          "target_artifact_path"
        ],
        "description": "Two artifact paths to diff (see Get Artifact Delta in Xray documentation).",
        "properties": {
          "source_artifact_path": {
            "type": "string",
            "description": "Path of the source artifact"
          },
          "target_artifact_path": {
            "type": "string",
            "description": "Path of the target artifact"
          }
        }
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