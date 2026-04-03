# Source: https://docs.jfrog.com/security/reference/release-bundle-v2-details.md

# Release Bundle V2 Details

Returns security, license, and operational risk violations found in a Release Bundle V2. Use the `operation` parameter to specify whether to check promotion or distribution violations.

Requires Admin or Read permission. Since Xray 3.82.x.


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
    "/api/v1/details/release_bundle_v2/{name}/{version}": {
      "get": {
        "operationId": "release-bundle-v2-details",
        "summary": "Release Bundle V2 Details",
        "description": "Returns security, license, and operational risk violations found in a Release Bundle V2. Use the `operation` parameter to specify whether to check promotion or distribution violations.\n\nRequires Admin or Read permission. Since Xray 3.82.x.\n",
        "tags": [
          "Artifacts V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Release bundle V2 name.",
            "example": "my-rb-v2"
          },
          {
            "name": "version",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Release bundle V2 version.",
            "example": "1.1"
          },
          {
            "name": "operation",
            "in": "query",
            "required": true,
            "description": "Which operation to check violations for.",
            "schema": {
              "type": "string",
              "enum": [
                "promotion",
                "distribution"
              ]
            }
          },
          {
            "name": "include_violations",
            "in": "query",
            "required": false,
            "description": "Include violation details in the response. Default: true.",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "Project key scope.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Release bundle details (allowed or blocked).",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string"
                    },
                    "version": {
                      "type": "string"
                    },
                    "operation": {
                      "type": "string"
                    },
                    "status": {
                      "type": "string",
                      "description": "Status: blocked, allowed."
                    },
                    "ui_violations_url": {
                      "type": "string"
                    },
                    "violations": {
                      "type": "object",
                      "properties": {
                        "license": {
                          "type": "array",
                          "items": {
                            "type": "object"
                          }
                        },
                        "security": {
                          "type": "array",
                          "items": {
                            "type": "object"
                          }
                        },
                        "op_risk": {
                          "type": "array",
                          "items": {
                            "type": "object"
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "name": "my-rb-v2",
                  "version": "1.1",
                  "operation": "promotion",
                  "status": "allowed"
                }
              }
            }
          },
          "202": {
            "description": "Scan is in progress."
          },
          "400": {
            "description": "Bad request.",
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
          "404": {
            "description": "Release bundle not found or not indexed.",
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
          "409": {
            "description": "Release bundle not marked for indexing.",
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