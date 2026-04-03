# Source: https://docs.jfrog.com/security/reference/get-reports-list.md

# Get Reports List

Returns a paginated list of reports that have been generated. All pagination query parameters are mandatory (direction, page_num, num_of_rows, order_by).

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get a list of reports in the scope of a project by using the additional query parameter `projectKey`.

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
    "/api/v1/reports": {
      "post": {
        "operationId": "get-reports-list",
        "summary": "Get Reports List",
        "description": "Returns a paginated list of reports that have been generated. All pagination query parameters are mandatory (direction, page_num, num_of_rows, order_by).\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get a list of reports in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.8.\n",
        "tags": [
          "Reports V1"
        ],
        "requestBody": {
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ReportsGetListRequestBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK - Reports list retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ReportsReportListResponse"
                },
                "example": {
                  "total_reports": 100,
                  "reports": [
                    {
                      "id": 1234,
                      "name": "vul_report_1",
                      "status": "completed",
                      "total_artifacts": 1000,
                      "num_of_processed_artifacts": 10,
                      "progress": 1,
                      "number_of_rows": 10,
                      "start_time": "1970-01-01T02:00:00+02:00",
                      "end_time": "1970-01-01T03:00:00+02:00",
                      "author": "admin",
                      "report_type": "vulnerability"
                    }
                  ]
                }
              }
            }
          }
        },
        "parameters": [
          {
            "name": "direction",
            "in": "query",
            "required": true,
            "description": "Sort direction: asc or desc",
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ]
            }
          },
          {
            "name": "page_num",
            "in": "query",
            "required": true,
            "description": "Page number (starting at 1)",
            "schema": {
              "type": "integer",
              "minimum": 1
            }
          },
          {
            "name": "num_of_rows",
            "in": "query",
            "required": true,
            "description": "Rows per page",
            "schema": {
              "type": "integer",
              "minimum": 1
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "required": true,
            "description": "One of: name, type, author, start_time, status",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "projectKey",
            "in": "query",
            "description": "Project scope (when Projects are enabled)",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ]
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
      "ReportsGetListRequestBody": {
        "type": "object",
        "description": "Optional request body for filtering the reports list. If omitted or empty, all reports are returned (subject to pagination).\n",
        "properties": {
          "filters": {
            "type": "object",
            "description": "Filter criteria for the reports list.",
            "properties": {
              "name": {
                "type": "string",
                "description": "Filter by report name (wildcard patterns supported).",
                "example": "vul_report*"
              },
              "type": {
                "type": "string",
                "description": "Filter by report type.",
                "example": "vulnerability"
              },
              "status": {
                "type": "array",
                "description": "Filter by report status.",
                "items": {
                  "type": "string"
                },
                "example": [
                  "completed",
                  "running"
                ]
              },
              "author": {
                "type": "string",
                "description": "Filter by report author.",
                "example": "admin"
              },
              "start_time_range": {
                "type": "object",
                "description": "Filter by report start time range.",
                "properties": {
                  "start": {
                    "type": "string",
                    "format": "date-time"
                  },
                  "end": {
                    "type": "string",
                    "format": "date-time"
                  }
                }
              }
            }
          }
        }
      },
      "ReportsReportListResponse": {
        "type": "object",
        "properties": {
          "pdf_export_limit": {
            "type": "integer",
            "description": "Maximum number of rows allowed for PDF export."
          },
          "max_saved_limit": {
            "type": "integer",
            "description": "Maximum number of saved reports allowed."
          },
          "total_reports": {
            "type": "integer",
            "description": "Total number of reports matching the filters."
          },
          "reports": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "report_type": {
                  "type": "string",
                  "description": "Report type: license, vulnerability, operational_risk, violations."
                },
                "status": {
                  "type": "string",
                  "description": "Report status: completed, running, pending, aborted, failed."
                },
                "total_artifacts": {
                  "type": "integer"
                },
                "num_of_processed_artifacts": {
                  "type": "integer"
                },
                "progress": {
                  "type": "integer"
                },
                "number_of_rows": {
                  "type": "integer"
                },
                "start_time": {
                  "type": "string"
                },
                "end_time": {
                  "type": "string"
                },
                "error": {
                  "type": "string"
                },
                "author": {
                  "type": "string"
                },
                "aborting_user": {
                  "type": "string"
                },
                "project_key": {
                  "type": "string"
                },
                "resources": {
                  "type": "object",
                  "description": "Resources scope of the report."
                },
                "cron_schedule": {
                  "type": "string",
                  "description": "Cron expression for scheduled reports."
                },
                "num_of_results": {
                  "type": "integer"
                },
                "cron_schedule_timezone": {
                  "type": "string",
                  "description": "Timezone for the cron schedule."
                }
              }
            }
          }
        }
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