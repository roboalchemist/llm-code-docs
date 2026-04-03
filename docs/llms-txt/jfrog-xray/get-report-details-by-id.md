# Source: https://docs.jfrog.com/security/reference/get-report-details-by-id.md

# Get Report Details By ID

Returns the metadata and status of a report by its unique ID, including progress, row count, start/end times, and report type.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get report details in the scope of a project by using the additional query parameter `projectKey`.

Requires a user with the Manage Reports role. Since Xray 3.8.


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
    "/api/v1/reports/{id}": {
      "get": {
        "operationId": "get-report-details-by-id",
        "summary": "Get Report Details By ID",
        "description": "Returns the metadata and status of a report by its unique ID, including progress, row count, start/end times, and report type.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get report details in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.8.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the report.",
            "required": true,
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
            "description": "OK - Report details retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "Report identifier."
                    },
                    "name": {
                      "type": "string",
                      "description": "Report name."
                    },
                    "status": {
                      "type": "string",
                      "description": "Report status, e.g. pending, running, completed, failed."
                    },
                    "total_artifacts": {
                      "type": "integer",
                      "description": "Total number of artifacts in the report scope."
                    },
                    "num_of_processed_artifacts": {
                      "type": "integer",
                      "description": "Number of artifacts processed so far."
                    },
                    "progress": {
                      "type": "integer",
                      "description": "Progress percentage (0-100)."
                    },
                    "number_of_rows": {
                      "type": "integer",
                      "description": "Number of result rows."
                    },
                    "start_time": {
                      "type": "string",
                      "description": "Report generation start time."
                    },
                    "end_time_estimation": {
                      "type": "string",
                      "description": "Estimated end time."
                    },
                    "error": {
                      "type": "string",
                      "description": "Error message in case of failure."
                    },
                    "author": {
                      "type": "string",
                      "description": "User who initiated the report."
                    },
                    "report_type": {
                      "type": "string",
                      "description": "Type of report, e.g. license, vulnerability, operational_risk."
                    }
                  }
                },
                "example": {
                  "id": 1234,
                  "name": "vul_report_1",
                  "status": "completed",
                  "total_artifacts": 1000,
                  "num_of_processed_artifacts": 10,
                  "progress": 1,
                  "number_of_rows": 10,
                  "start_time": "1970-01-01T02:00:00+02:00",
                  "end_time_estimation": "1970-01-01T03:00:00+02:00",
                  "author": "admin",
                  "report_type": "vulnerability"
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