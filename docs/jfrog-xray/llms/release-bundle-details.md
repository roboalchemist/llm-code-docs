# Source: https://docs.jfrog.com/security/reference/release-bundle-details.md

# Release Bundle Details

Returns the scan status and optionally the license, security, and operational risk violations found in a Release Bundle.

Requires Admin or Read permission.


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
    "/api/v1/details/release_bundle/{name}/{version}": {
      "get": {
        "operationId": "release-bundle-details",
        "summary": "Release Bundle Details",
        "description": "Returns the scan status and optionally the license, security, and operational risk violations found in a Release Bundle.\n\nRequires Admin or Read permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "description": "Release bundle name.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "my-release-bundle"
          },
          {
            "name": "version",
            "in": "path",
            "description": "Release bundle version.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "1.0.0"
          },
          {
            "name": "include_violations",
            "in": "query",
            "description": "Whether to include violation details in the response. Default: true.",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Release bundle details retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "description": "Scan status of the release bundle.",
                      "example": "ALLOWED"
                    },
                    "violations": {
                      "type": "object",
                      "description": "Violation details (when include_violations is true).",
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
                  "status": "BLOCKED",
                  "violations": {
                    "license": [],
                    "security": [
                      {
                        "severity": "High",
                        "type": "security",
                        "summary": "CVE-2021-44228"
                      }
                    ],
                    "op_risk": []
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