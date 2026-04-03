# Source: https://docs.jfrog.com/security/reference/get-operational-risk-report-content.md

# Get Operational Risk Report Content

Retrieves the content of a previously generated Operational Risk report by its ID. Results are paginated; all pagination query parameters are mandatory.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can access report content in the scope of a project by using the additional query parameter `projectKey`.

Requires a user with the Manage Reports role. Since Xray 3.49.0.


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
    "/api/v1/reports/operationalRisks/{id}": {
      "post": {
        "operationId": "get-operational-risk-report-content",
        "summary": "Get Operational Risk Report Content",
        "description": "Retrieves the content of a previously generated Operational Risk report by its ID. Results are paginated; all pagination query parameters are mandatory.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can access report content in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.49.0.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the Operational Risk report.",
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
            "description": "Field to sort by. One of: risk, artifact, component, released, is_eol, cadence, commits, committers.",
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
            "description": "OK - Operational Risk report content retrieved successfully",
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
                      "description": "List of operational risk report rows.",
                      "items": {
                        "type": "object",
                        "properties": {
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
                          "risk": {
                            "type": "string"
                          },
                          "risk_reason": {
                            "type": "string"
                          },
                          "released": {
                            "type": "string"
                          },
                          "version": {
                            "type": "string"
                          },
                          "latest_version": {
                            "type": "string"
                          },
                          "newer_versions": {
                            "type": "integer"
                          },
                          "is_eol": {
                            "type": "boolean"
                          },
                          "eol_message": {
                            "type": "string"
                          },
                          "cadence": {
                            "type": "number"
                          },
                          "commits": {
                            "type": "integer"
                          },
                          "committers": {
                            "type": "integer"
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
                      "component": "deb://debian:master:abc:2.28-10",
                      "artifact": "docker://redis:latest-07142020122937",
                      "path": "repo/dir/file",
                      "artifact_scan_time": "2021-01-01T01:00:00+02:00",
                      "risk": "High",
                      "risk_reason": "",
                      "released": "2005-01-01T03:00:00+02:00",
                      "version": "2.28-10",
                      "latest_version": "1.2.3",
                      "newer_versions": 10,
                      "is_eol": true,
                      "eol_message": "unsupported",
                      "cadence": 5,
                      "committers": 10,
                      "commits": 10,
                      "project_keys": [
                        "proj1",
                        "proj2"
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