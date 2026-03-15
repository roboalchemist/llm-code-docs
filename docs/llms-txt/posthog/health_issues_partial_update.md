# Source: https://posthog.com/docs/open-api-spec/health_issues_partial_update.md

# health_issues_partial_update

## OpenAPI

```json PATCH /api/environments/{project_id}/health_issues/{id}/
{
  "paths": {
    "/api/environments/{project_id}/health_issues/{id}/": {
      "patch": {
        "operationId": "health_issues_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this health issue.",
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "health_issues"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedHealthIssue"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedHealthIssue"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedHealthIssue"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "health_issue:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HealthIssue"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedHealthIssue": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "kind": {
            "type": "string",
            "readOnly": true
          },
          "severity": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SeverityEnum"
              }
            ],
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HealthIssueStatusEnum"
              }
            ],
            "readOnly": true
          },
          "dismissed": {
            "type": "boolean"
          },
          "payload": {
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "resolved_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "HealthIssue": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "kind": {
            "type": "string",
            "readOnly": true
          },
          "severity": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SeverityEnum"
              }
            ],
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HealthIssueStatusEnum"
              }
            ],
            "readOnly": true
          },
          "dismissed": {
            "type": "boolean"
          },
          "payload": {
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "resolved_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "id",
          "kind",
          "payload",
          "resolved_at",
          "severity",
          "status",
          "updated_at"
        ]
      },
      "SeverityEnum": {
        "enum": [
          "critical",
          "warning",
          "info"
        ],
        "type": "string",
        "description": "* `critical` - Critical\n* `warning` - Warning\n* `info` - Info"
      },
      "HealthIssueStatusEnum": {
        "enum": [
          "active",
          "resolved"
        ],
        "type": "string",
        "description": "* `active` - Active\n* `resolved` - Resolved"
      }
    }
  }
}
```
