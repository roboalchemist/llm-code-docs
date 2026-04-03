# Source: https://docs.jfrog.com/security/reference/abort.md

# Abort Report Generation

Aborts a report that is currently being generated. Use the report ID returned from a generate report request.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can abort a report in the scope of a project by using the additional query parameter `projectKey`.

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
    "/api/v1/reports/abort/{id}": {
      "post": {
        "operationId": "abort",
        "summary": "Abort Report Generation",
        "description": "Aborts a report that is currently being generated. Use the report ID returned from a generate report request.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can abort a report in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.8.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the report to abort.",
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
        "requestBody": {
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ReportsAbortRequestBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Report generation aborted successfully",
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
      "ReportsAbortRequestBody": {
        "type": "object",
        "description": "Optional payload when aborting; project scope may use query parameter projectKey.",
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