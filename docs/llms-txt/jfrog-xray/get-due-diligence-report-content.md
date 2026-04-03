# Source: https://docs.jfrog.com/security/reference/get-due-diligence-report-content.md

# Get Due Diligence Report Content

Retrieves the content of a previously generated Due Diligence (license) report by its ID. Results are paginated; all pagination query parameters are mandatory.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can access report content in the scope of a project by using the additional query parameter `projectKey`.

Requires a user with the Manage Reports role. Since Xray 3.9.


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
    "/api/v1/reports/licenses/{id}": {
      "post": {
        "operationId": "get-due-diligence-report-content",
        "summary": "Get Due Diligence Report Content",
        "description": "Retrieves the content of a previously generated Due Diligence (license) report by its ID. Results are paginated; all pagination query parameters are mandatory.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can access report content in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.9.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the Due Diligence report.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "description": "Sort direction: asc or desc.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "page_num",
            "in": "query",
            "description": "Page number (starting at 1).",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "num_of_rows",
            "in": "query",
            "description": "Number of rows per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "description": "Field to sort by. One of: license, artifact, component, unknown_license, path, unrecognized, artifact_scan_time, custom, license_name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "projectKey",
            "in": "query",
            "description": "Project scope (when Projects are enabled).",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK - Due Diligence report content retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "total_rows": {
                      "type": "integer",
                      "description": "Total number of rows in the report."
                    },
                    "rows": {
                      "type": "array",
                      "description": "List of license report rows.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "license_key": {
                            "type": "string"
                          },
                          "license_name": {
                            "type": "string"
                          },
                          "component": {
                            "type": "string"
                          },
                          "artifact": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          },
                          "artifact_scan_time": {
                            "type": "string"
                          },
                          "unknown": {
                            "type": "boolean"
                          },
                          "unrecognized": {
                            "type": "boolean"
                          },
                          "custom": {
                            "type": "boolean"
                          },
                          "package_type": {
                            "type": "string"
                          },
                          "references": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "impact_path": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "project_keys": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "total_rows": 100,
                  "rows": [
                    {
                      "license_key": "MIT",
                      "license_name": "The MIT License",
                      "component": "deb://debian:buster:glibc:2.28-10",
                      "artifact": "docker://redis:latest-07142020122937",
                      "path": "repo1/folder1/artifact",
                      "artifact_scan_time": "2020-07-14T09:32:00Z",
                      "unknown": false,
                      "unrecognized": false,
                      "custom": false,
                      "package_type": "Debian",
                      "references": [
                        "https://spdx.org/licenses/AFL-1.1.html"
                      ],
                      "project_keys": [
                        "proj1"
                      ]
                    }
                  ]
                }
              }
            }
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
            "description": "Report not found.",
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
      "name": "Reports V1",
      "description": "APIs from Reports V1"
    }
  ]
}
```