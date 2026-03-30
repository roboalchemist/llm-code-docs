# Source: https://posthog.com/docs/open-api-spec/error_tracking_issues_bulk_create.md

# error_tracking_issues_bulk_create

## OpenAPI

```json POST /api/environments/{project_id}/error_tracking/issues/bulk/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/issues/bulk/": {
      "post": {
        "operationId": "error_tracking_issues_bulk_create",
        "parameters": [
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
          "error_tracking",
          "error_tracking"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingIssueFull"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingIssueFull"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingIssueFull"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "error_tracking"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorTrackingIssueFull": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "status": {
            "$ref": "#/components/schemas/ErrorTrackingIssueFullStatusEnum"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "first_seen": {
            "type": "string",
            "format": "date-time"
          },
          "assignee": {
            "$ref": "#/components/schemas/ErrorTrackingIssueAssignment"
          },
          "external_issues": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingExternalReference"
            }
          },
          "cohort": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "assignee",
          "cohort",
          "external_issues",
          "first_seen",
          "id"
        ]
      },
      "ErrorTrackingIssueFullStatusEnum": {
        "enum": [
          "archived",
          "active",
          "resolved",
          "pending_release",
          "suppressed"
        ],
        "type": "string",
        "description": "* `archived` - Archived\n* `active` - Active\n* `resolved` - Resolved\n* `pending_release` - Pending release\n* `suppressed` - Suppressed"
      },
      "ErrorTrackingIssueAssignment": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "type": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "id",
          "type"
        ]
      },
      "ErrorTrackingExternalReference": {
        "additionalProperties": false,
        "properties": {
          "external_url": {
            "title": "External Url",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "integration": {
            "$ref": "#/components/schemas/ErrorTrackingExternalReferenceIntegration"
          }
        },
        "required": [
          "external_url",
          "id",
          "integration"
        ],
        "title": "ErrorTrackingExternalReference",
        "type": "object"
      },
      "ErrorTrackingExternalReferenceIntegration": {
        "additionalProperties": false,
        "properties": {
          "display_name": {
            "title": "Display Name",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "number"
          },
          "kind": {
            "$ref": "#/components/schemas/IntegrationKind"
          }
        },
        "required": [
          "display_name",
          "id",
          "kind"
        ],
        "title": "ErrorTrackingExternalReferenceIntegration",
        "type": "object"
      },
      "IntegrationKind": {
        "enum": [
          "slack",
          "slack-posthog-code",
          "salesforce",
          "hubspot",
          "google-pubsub",
          "google-cloud-storage",
          "google-ads",
          "google-sheets",
          "linkedin-ads",
          "snapchat",
          "intercom",
          "email",
          "twilio",
          "linear",
          "github",
          "gitlab",
          "meta-ads",
          "clickup",
          "reddit-ads",
          "databricks",
          "tiktok-ads",
          "bing-ads",
          "vercel",
          "azure-blob",
          "firebase",
          "jira",
          "pinterest-ads"
        ],
        "title": "IntegrationKind",
        "type": "string"
      }
    }
  }
}
```
