# Source: https://docs.jfrog.com/security/reference/export.md

# Export Report

Exports a report and its data to a PDF, JSON, or CSV file. The response is a ZIP file stream containing the exported file with the naming convention `<file_name>.pdf|json|csv`. The report ID can be retrieved using the Get Reports List endpoint.

Two mandatory query parameters must be provided: `file_name` (desired file name without suffix) and `format` (pdf, json, or csv).

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can export a report in the scope of a project by using the additional query parameter `projectKey`.

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
    "/api/v1/reports/export/{id}": {
      "get": {
        "operationId": "export",
        "summary": "Export Report",
        "description": "Exports a report and its data to a PDF, JSON, or CSV file. The response is a ZIP file stream containing the exported file with the naming convention `<file_name>.pdf|json|csv`. The report ID can be retrieved using the Get Reports List endpoint.\n\nTwo mandatory query parameters must be provided: `file_name` (desired file name without suffix) and `format` (pdf, json, or csv).\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can export a report in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.8.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the report to export.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "file_name",
            "in": "query",
            "description": "The desired file name for download (without a suffix).",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "format",
            "in": "query",
            "description": "Export format: pdf, json, or csv.",
            "required": true,
            "schema": {
              "type": "string",
              "enum": [
                "pdf",
                "json",
                "csv"
              ]
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
            "description": "A ZIP file stream containing the exported report.",
            "content": {
              "application/zip": {
                "schema": {
                  "type": "string",
                  "format": "binary"
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