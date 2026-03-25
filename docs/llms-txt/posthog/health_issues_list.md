# Source: https://posthog.com/docs/open-api-spec/health_issues_list.md

# health_issues_list

## OpenAPI

```json GET /api/environments/{project_id}/health_issues/
{
  "paths": {
    "/api/environments/{project_id}/health_issues/": {
      "get": {
        "operationId": "health_issues_list",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "health_issue:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedHealthIssueList"
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
      "PaginatedHealthIssueList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HealthIssue"
            }
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
