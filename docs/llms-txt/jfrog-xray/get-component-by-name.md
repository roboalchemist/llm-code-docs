# Source: https://docs.jfrog.com/security/reference/get-component-by-name.md

# Find Component by Name

Search for a component by name. This API is applicable only for components synced from the JFrog Global database to Xray. Requires Read permission.

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
    "/api/v1/component/{name}": {
      "get": {
        "operationId": "get-component-by-name",
        "summary": "Find Component by Name",
        "description": "Search for a component by name. This API is applicable only for components synced from the JFrog Global database to Xray. Requires Read permission.",
        "tags": [
          "Components V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The component name to search for."
          }
        ],
        "responses": {
          "200": {
            "description": "Component details returned successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "component": {
                      "type": "string",
                      "description": "Component identifier including package type prefix."
                    },
                    "package_type": {
                      "type": "string",
                      "description": "Package type (e.g. rpm, maven, npm)."
                    },
                    "name": {
                      "type": "string",
                      "description": "Component name."
                    },
                    "description": {
                      "type": "string",
                      "description": "Component description."
                    },
                    "created": {
                      "type": "string",
                      "description": "Timestamp when the component was created."
                    },
                    "modified": {
                      "type": "string",
                      "description": "Timestamp when the component was last modified."
                    },
                    "sources": {
                      "type": "array",
                      "description": "List of sources where this component was found.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "Source name."
                          },
                          "url": {
                            "type": "string",
                            "description": "Source URL."
                          },
                          "updated": {
                            "type": "string",
                            "description": "Timestamp when the source was last updated."
                          }
                        }
                      }
                    },
                    "versions": {
                      "type": "array",
                      "description": "List of known versions for this component.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "version": {
                            "type": "string",
                            "description": "Version string."
                          },
                          "released": {
                            "type": "string",
                            "description": "Release timestamp."
                          },
                          "Licenses": {
                            "type": "array",
                            "description": "List of licenses for this version.",
                            "items": {
                              "type": "string"
                            }
                          },
                          "files": {
                            "type": "array",
                            "description": "List of files for this version.",
                            "items": {
                              "type": "object",
                              "properties": {
                                "name": {
                                  "type": "string",
                                  "description": "File name."
                                },
                                "sha256": {
                                  "type": "string",
                                  "description": "SHA-256 checksum."
                                },
                                "sha1": {
                                  "type": "string",
                                  "description": "SHA-1 checksum."
                                },
                                "md5": {
                                  "type": "string",
                                  "description": "MD5 checksum."
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "component": "4:kdegames-devel",
                  "package_type": "rpm",
                  "name": "kdegames-devel",
                  "description": "Development files for the KDE gaming libraries. Install kdegames-devel if you wish to develop or compile games for the KDE desktop.",
                  "created": "2017-11-19T09:24:12.065Z",
                  "modified": "2017-11-19T10:13:19.946Z",
                  "sources": [
                    {
                      "name": "archive-centos",
                      "url": "http://vault.centos.org/",
                      "updated": "2017-11-19T09:24:11.995Z"
                    }
                  ],
                  "versions": [
                    {
                      "version": "6:3.3.1-2",
                      "released": "0001-01-01T00:00:00Z",
                      "Licenses": [
                        "GPL-3.0"
                      ],
                      "files": [
                        {
                          "name": "kdegames-devel-3.3.1-2.i386.rpm",
                          "sha256": "f256373977e2705e521e06c85f6f49cefcd6c74c8a0fa18dec2eb1bcefe7e4b4",
                          "sha1": "d184ba4bd8e205fda0ba29b7f1db39b91174b1ef",
                          "md5": "7b246aecf791ad549e78cda2c3c72a48"
                        }
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Missing component name parameter."
          },
          "404": {
            "description": "Component not found."
          },
          "500": {
            "description": "Internal server error."
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
      "name": "Components V1",
      "description": "APIs from Components V1"
    }
  ]
}
```