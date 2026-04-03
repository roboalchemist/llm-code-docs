# Source: https://docs.jfrog.com/security/reference/generate-exposures-report-by-id.md

# Get Exposures Report Content

Retrieves the content of a previously generated Exposures report by its ID. Results are paginated; all pagination query parameters are mandatory.

Requires a user with the Manage Reports role.


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
    "/api/v1/reports/exposures/{id}": {
      "post": {
        "operationId": "generate-exposures-report-by-id",
        "summary": "Get Exposures Report Content",
        "description": "Retrieves the content of a previously generated Exposures report by its ID. Results are paginated; all pagination query parameters are mandatory.\n\nRequires a user with the Manage Reports role.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the Exposures report.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "description": "Sort direction: asc or desc.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "page_num",
            "in": "query",
            "description": "Page number (starting at 1).",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "num_of_rows",
            "in": "query",
            "description": "Number of rows per page.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "description": "Field to sort by.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ReportsReportContentFiltersBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK - Exposures report content retrieved successfully",
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
                      "description": "List of exposure report rows.",
                      "items": {
                        "type": "object"
                      }
                    }
                  }
                },
                "example": {
                  "total_rows": 2,
                  "rows": [
                    {
                      "category": "secrets",
                      "jfrog_severity": "high",
                      "exposures_id": "EXP-1235-00001",
                      "description": "Plaintext API keys found",
                      "file_path": "/exposures/req.secret.keys.py",
                      "location": "Line Number: 2",
                      "repository": "louis-vv18-exposures-report",
                      "impacted_artifact": "docker://xnas:regular_louis_f42172",
                      "cwe": "CWE-256",
                      "evidence": "$gcyD6**********",
                      "origin": "jfrog",
                      "provider": "aws_access"
                    },
                    {
                      "category": "secrets",
                      "jfrog_severity": "high",
                      "exposures_id": "EXP-1235-00002",
                      "description": "Plaintext API keys found",
                      "file_path": "/exposures/req.secret.keys.py",
                      "location": "Line Number: 3",
                      "repository": "louis-vv18-exposures-report",
                      "impacted_artifact": "docker://xnas:regular_louis_f42172",
                      "cwe": "CWE-256",
                      "evidence": "gho_D6**********",
                      "origin": "jfrog",
                      "provider": "github"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Bad request - Required fields are missing",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "404": {
            "description": "Report not found",
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
      "ReportsReportContentFiltersBody": {
        "type": "object",
        "description": "Optional filters for report table content; pagination is usually via query parameters.",
        "additionalProperties": true
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