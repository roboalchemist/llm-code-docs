# Source: https://posthog.com/docs/open-api-spec/environments_integrations_retrieve.md

# environments_integrations_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/{id}/": {
      "get": {
        "operationId": "environments_integrations_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this integration.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "integrations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "integration:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Integration"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Integration": {
        "type": "object",
        "description": "Standard Integration serializer.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "kind": {
            "$ref": "#/components/schemas/IntegrationKindEnum"
          },
          "config": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "errors": {
            "type": "string",
            "readOnly": true
          },
          "display_name": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "display_name",
          "errors",
          "id",
          "kind"
        ]
      },
      "IntegrationKindEnum": {
        "enum": [
          "slack",
          "slack-posthog-code",
          "salesforce",
          "hubspot",
          "google-pubsub",
          "google-cloud-storage",
          "google-ads",
          "google-sheets",
          "snapchat",
          "linkedin-ads",
          "reddit-ads",
          "tiktok-ads",
          "bing-ads",
          "intercom",
          "email",
          "linear",
          "github",
          "gitlab",
          "meta-ads",
          "twilio",
          "clickup",
          "vercel",
          "databricks",
          "azure-blob",
          "firebase",
          "jira",
          "pinterest-ads"
        ],
        "type": "string",
        "description": "* `slack` - Slack\n* `slack-posthog-code` - Slack Posthog Code\n* `salesforce` - Salesforce\n* `hubspot` - Hubspot\n* `google-pubsub` - Google Pubsub\n* `google-cloud-storage` - Google Cloud Storage\n* `google-ads` - Google Ads\n* `google-sheets` - Google Sheets\n* `snapchat` - Snapchat\n* `linkedin-ads` - Linkedin Ads\n* `reddit-ads` - Reddit Ads\n* `tiktok-ads` - Tiktok Ads\n* `bing-ads` - Bing Ads\n* `intercom` - Intercom\n* `email` - Email\n* `linear` - Linear\n* `github` - Github\n* `gitlab` - Gitlab\n* `meta-ads` - Meta Ads\n* `twilio` - Twilio\n* `clickup` - Clickup\n* `vercel` - Vercel\n* `databricks` - Databricks\n* `azure-blob` - Azure Blob\n* `firebase` - Firebase\n* `jira` - Jira\n* `pinterest-ads` - Pinterest Ads"
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
