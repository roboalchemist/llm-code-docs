# Source: https://docs.jfrog.com/security/reference/compare-builds.md

# Compare Builds

Compares two builds and produces a delta of their dependency components. Returns the source and target build metadata plus three component lists: added (in target only), removed (in source only), and unchanged (in both).

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
    "/api/v1/dependencyGraph/buildDelta": {
      "post": {
        "operationId": "compare-builds",
        "summary": "Compare Builds",
        "description": "Compares two builds and produces a delta of their dependency components. Returns the source and target build metadata plus three component lists: added (in target only), removed (in source only), and unchanged (in both).\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ArtifactsCompareBuildsRequest"
              },
              "example": {
                "source_artifactory_id": "default",
                "source_build_name": "my-build",
                "source_build_number": "1",
                "target_artifactory_id": "default",
                "target_build_name": "my-build",
                "target_build_number": "2"
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
                    "source_build": {
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
                        "component_id": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "name",
                        "path",
                        "pkg_type",
                        "sha256",
                        "component_id"
                      ]
                    },
                    "target_build": {
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
                        "component_id": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "name",
                        "path",
                        "pkg_type",
                        "sha256",
                        "component_id"
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
                    "source_build",
                    "target_build",
                    "removed",
                    "added",
                    "unchanged"
                  ]
                },
                "example": {
                  "source_build": {
                    "name": "my-build",
                    "path": "art2/ext-release-local/",
                    "pkg_type": "Generic",
                    "sha256": "d160c68ed8879ae42756e159daec1dd7ecfd53b6192321656b72715e20d46dd2",
                    "component_id": "gav://org.artifactory.pro:artifactory-pro-war:4.14.0"
                  },
                  "target_build": {
                    "name": "my-build",
                    "path": "art2/ext-release-local/",
                    "pkg_type": "Generic",
                    "sha256": "d160c68ed8879ae42756e159daec1dd7ecfd53b6192321656b72715e20d46dd2",
                    "component_id": "gav://org.artifactory.pro:artifactory-pro-war:4.14.0"
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
            "description": "The build with the provided identifier doesn't exist or isn't indexed in Xray",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "401": {
            "description": "Bad credentials",
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
      "ArtifactsCompareBuildsRequest": {
        "type": "object",
        "description": "Two builds to compare (see Compare Builds / build delta in Xray REST API documentation).",
        "required": [
          "source_artifactory_id",
          "source_build_name",
          "source_build_number",
          "target_artifactory_id",
          "target_build_name",
          "target_build_number"
        ],
        "properties": {
          "source_artifactory_id": {
            "type": "string",
            "description": "Name of the first Artifactory instance"
          },
          "source_build_name": {
            "type": "string",
            "description": "Name of the first build"
          },
          "source_build_number": {
            "type": "string",
            "description": "Number of the first build"
          },
          "target_artifactory_id": {
            "type": "string",
            "description": "Name of the second Artifactory instance"
          },
          "target_build_name": {
            "type": "string",
            "description": "Name of the second build"
          },
          "target_build_number": {
            "type": "string",
            "description": "Number of the second build"
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