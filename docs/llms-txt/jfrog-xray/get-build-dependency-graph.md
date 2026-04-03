# Source: https://docs.jfrog.com/security/reference/get-build-dependency-graph.md

# Get Build Dependency Graph

Retrieves the complete dependency graph for a build identified by name and number. Returns the build metadata and a recursive tree of all its component dependencies.

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
    "/api/v1/dependencyGraph/build": {
      "post": {
        "operationId": "get-build-dependency-graph",
        "summary": "Get Build Dependency Graph",
        "description": "Retrieves the complete dependency graph for a build identified by name and number. Returns the build metadata and a recursive tree of all its component dependencies.\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "build_name": {
                    "type": "string",
                    "description": "The build name."
                  },
                  "build_number": {
                    "type": "string",
                    "description": "The build number/version."
                  },
                  "artifactory_id": {
                    "type": "string",
                    "description": "Optional Artifactory instance ID."
                  },
                  "build_repo": {
                    "type": "string",
                    "description": "Build repository name."
                  },
                  "project": {
                    "type": "string",
                    "description": "Project key (optional)."
                  }
                },
                "required": [
                  "build_name",
                  "build_number"
                ]
              },
              "example": {
                "build_name": "xray-test",
                "build_number": "157"
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
                    "build": {
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
                    "components": {
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
                          "created": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "component_name",
                          "component_id",
                          "package_type",
                          "created"
                        ]
                      }
                    }
                  },
                  "required": [
                    "build",
                    "components"
                  ]
                },
                "example": {
                  "build": {
                    "name": "xray-test",
                    "path": "default/test-build-info/xray-test",
                    "pkg_type": "Build",
                    "sha256": "2e3ccd8c1e952a30f2c2865c9130553bdb11b4ed49b81e6ab08f22a29f5d303b",
                    "component_id": "[test-build-info]/xray-test:157"
                  },
                  "components": [
                    {
                      "component_name": "multi1-3.7-20230730.132458-7-sources.jar",
                      "component_id": "org.jfrog.test:multi1:3.7-20230730.132458-7",
                      "package_type": "Maven",
                      "created": "2023-07-30T13:25:07Z"
                    },
                    {
                      "component_name": "multi1-3.7-20230730.132458-7-tests.jar",
                      "component_id": "org.jfrog.test:multi1:3.7-20230730.132458-7",
                      "package_type": "Maven",
                      "created": "2023-07-30T13:25:07Z"
                    },
                    {
                      "component_name": "javax.mail:mail:1.4.jar",
                      "component_id": "javax.mail:mail:1.4",
                      "package_type": "Maven",
                      "created": "2022-11-10T13:29:10Z"
                    },
                    {
                      "component_name": "hsqldb:hsqldb:1.8.0.10.jar",
                      "component_id": "hsqldb:hsqldb:1.8.0.10",
                      "package_type": "Maven",
                      "created": "2022-11-10T13:29:24Z"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Missing Artifactory ID",
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