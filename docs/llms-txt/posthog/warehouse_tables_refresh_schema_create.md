# Source: https://posthog.com/docs/open-api-spec/warehouse_tables_refresh_schema_create.md

# warehouse_tables_refresh_schema_create

## OpenAPI

```json POST /api/projects/{project_id}/warehouse_tables/{id}/refresh_schema/
{
  "paths": {
    "/api/projects/{project_id}/warehouse_tables/{id}/refresh_schema/": {
      "post": {
        "operationId": "warehouse_tables_refresh_schema_create",
        "description": "Create, Read, Update and Delete Warehouse Tables.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this data warehouse table.",
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
          "warehouse_tables"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Table"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Table"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Table"
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
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "Table": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "nullable": true
          },
          "name": {
            "type": "string",
            "maxLength": 128
          },
          "format": {
            "$ref": "#/components/schemas/TableFormatEnum"
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "url_pattern": {
            "type": "string",
            "maxLength": 500
          },
          "credential": {
            "$ref": "#/components/schemas/Credential"
          },
          "columns": {
            "type": "string",
            "readOnly": true
          },
          "external_data_source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleExternalDataSourceSerializers"
              }
            ],
            "readOnly": true
          },
          "external_schema": {
            "type": "string",
            "readOnly": true
          },
          "options": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "columns",
          "created_at",
          "created_by",
          "credential",
          "external_data_source",
          "external_schema",
          "format",
          "id",
          "name",
          "url_pattern"
        ]
      },
      "TableFormatEnum": {
        "enum": [
          "CSV",
          "CSVWithNames",
          "Parquet",
          "JSONEachRow",
          "Delta",
          "DeltaS3Wrapper"
        ],
        "type": "string",
        "description": "* `CSV` - CSV\n* `CSVWithNames` - CSVWithNames\n* `Parquet` - Parquet\n* `JSONEachRow` - JSON\n* `Delta` - Delta\n* `DeltaS3Wrapper` - DeltaS3Wrapper"
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
      "Credential": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "access_key": {
            "type": "string",
            "writeOnly": true,
            "maxLength": 500
          },
          "access_secret": {
            "type": "string",
            "writeOnly": true,
            "maxLength": 500
          }
        },
        "required": [
          "access_key",
          "access_secret",
          "created_at",
          "created_by",
          "id"
        ]
      },
      "SimpleExternalDataSourceSerializers": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "status": {
            "type": "string",
            "readOnly": true
          },
          "source_type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SourceTypeE09Enum"
              }
            ],
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "id",
          "source_type",
          "status"
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
      },
      "SourceTypeE09Enum": {
        "enum": [
          "Ashby",
          "Supabase",
          "CustomerIO",
          "Github",
          "Stripe",
          "Hubspot",
          "Postgres",
          "Zendesk",
          "Snowflake",
          "Salesforce",
          "MySQL",
          "MongoDB",
          "MSSQL",
          "Vitally",
          "BigQuery",
          "Chargebee",
          "Clerk",
          "GoogleAds",
          "TemporalIO",
          "DoIt",
          "GoogleSheets",
          "MetaAds",
          "Klaviyo",
          "Mailchimp",
          "Braze",
          "Mailjet",
          "Redshift",
          "Polar",
          "RevenueCat",
          "LinkedinAds",
          "RedditAds",
          "TikTokAds",
          "BingAds",
          "Shopify",
          "Attio",
          "SnapchatAds",
          "Linear",
          "Intercom",
          "Amplitude",
          "Mixpanel",
          "Jira",
          "ActiveCampaign",
          "Marketo",
          "Adjust",
          "AppsFlyer",
          "Freshdesk",
          "GoogleAnalytics",
          "Pipedrive",
          "SendGrid",
          "Slack",
          "PagerDuty",
          "Asana",
          "Notion",
          "Airtable",
          "Greenhouse",
          "BambooHR",
          "Lever",
          "GitLab",
          "Datadog",
          "Sentry",
          "Pendo",
          "FullStory",
          "AmazonAds",
          "PinterestAds",
          "AppleSearchAds",
          "QuickBooks",
          "Xero",
          "NetSuite",
          "WooCommerce",
          "BigCommerce",
          "PayPal",
          "Square",
          "Zoom",
          "Trello",
          "Monday",
          "ClickUp",
          "Confluence",
          "Recurly",
          "SalesLoft",
          "Outreach",
          "Gong",
          "Calendly",
          "Typeform",
          "Iterable",
          "ZohoCRM",
          "Close",
          "Oracle",
          "DynamoDB",
          "Elasticsearch",
          "Kafka",
          "LaunchDarkly",
          "Braintree",
          "Recharge",
          "HelpScout",
          "Gorgias",
          "Instagram",
          "YouTubeAnalytics",
          "FacebookPages",
          "TwitterAds",
          "Workday",
          "ServiceNow",
          "Pardot",
          "Copper",
          "Front",
          "ChartMogul",
          "Zuora",
          "Paddle",
          "CircleCI",
          "CockroachDB",
          "Firebase",
          "AzureBlob",
          "GoogleDrive",
          "OneDrive",
          "SharePoint",
          "Box",
          "SFTP",
          "MicrosoftTeams",
          "Aircall",
          "Webflow",
          "Okta",
          "Auth0",
          "Productboard",
          "Smartsheet",
          "Wrike",
          "Plaid",
          "SurveyMonkey",
          "Eventbrite",
          "RingCentral",
          "Twilio",
          "Freshsales",
          "Shortcut",
          "ConvertKit",
          "Drip",
          "CampaignMonitor",
          "MailerLite",
          "Omnisend",
          "Brevo",
          "Postmark",
          "Granola",
          "BuildBetter"
        ],
        "type": "string",
        "description": "* `Ashby` - Ashby\n* `Supabase` - Supabase\n* `CustomerIO` - CustomerIO\n* `Github` - Github\n* `Stripe` - Stripe\n* `Hubspot` - Hubspot\n* `Postgres` - Postgres\n* `Zendesk` - Zendesk\n* `Snowflake` - Snowflake\n* `Salesforce` - Salesforce\n* `MySQL` - MySQL\n* `MongoDB` - MongoDB\n* `MSSQL` - MSSQL\n* `Vitally` - Vitally\n* `BigQuery` - BigQuery\n* `Chargebee` - Chargebee\n* `Clerk` - Clerk\n* `GoogleAds` - GoogleAds\n* `TemporalIO` - TemporalIO\n* `DoIt` - DoIt\n* `GoogleSheets` - GoogleSheets\n* `MetaAds` - MetaAds\n* `Klaviyo` - Klaviyo\n* `Mailchimp` - Mailchimp\n* `Braze` - Braze\n* `Mailjet` - Mailjet\n* `Redshift` - Redshift\n* `Polar` - Polar\n* `RevenueCat` - RevenueCat\n* `LinkedinAds` - LinkedinAds\n* `RedditAds` - RedditAds\n* `TikTokAds` - TikTokAds\n* `BingAds` - BingAds\n* `Shopify` - Shopify\n* `Attio` - Attio\n* `SnapchatAds` - SnapchatAds\n* `Linear` - Linear\n* `Intercom` - Intercom\n* `Amplitude` - Amplitude\n* `Mixpanel` - Mixpanel\n* `Jira` - Jira\n* `ActiveCampaign` - ActiveCampaign\n* `Marketo` - Marketo\n* `Adjust` - Adjust\n* `AppsFlyer` - AppsFlyer\n* `Freshdesk` - Freshdesk\n* `GoogleAnalytics` - GoogleAnalytics\n* `Pipedrive` - Pipedrive\n* `SendGrid` - SendGrid\n* `Slack` - Slack\n* `PagerDuty` - PagerDuty\n* `Asana` - Asana\n* `Notion` - Notion\n* `Airtable` - Airtable\n* `Greenhouse` - Greenhouse\n* `BambooHR` - BambooHR\n* `Lever` - Lever\n* `GitLab` - GitLab\n* `Datadog` - Datadog\n* `Sentry` - Sentry\n* `Pendo` - Pendo\n* `FullStory` - FullStory\n* `AmazonAds` - AmazonAds\n* `PinterestAds` - PinterestAds\n* `AppleSearchAds` - AppleSearchAds\n* `QuickBooks` - QuickBooks\n* `Xero` - Xero\n* `NetSuite` - NetSuite\n* `WooCommerce` - WooCommerce\n* `BigCommerce` - BigCommerce\n* `PayPal` - PayPal\n* `Square` - Square\n* `Zoom` - Zoom\n* `Trello` - Trello\n* `Monday` - Monday\n* `ClickUp` - ClickUp\n* `Confluence` - Confluence\n* `Recurly` - Recurly\n* `SalesLoft` - SalesLoft\n* `Outreach` - Outreach\n* `Gong` - Gong\n* `Calendly` - Calendly\n* `Typeform` - Typeform\n* `Iterable` - Iterable\n* `ZohoCRM` - ZohoCRM\n* `Close` - Close\n* `Oracle` - Oracle\n* `DynamoDB` - DynamoDB\n* `Elasticsearch` - Elasticsearch\n* `Kafka` - Kafka\n* `LaunchDarkly` - LaunchDarkly\n* `Braintree` - Braintree\n* `Recharge` - Recharge\n* `HelpScout` - HelpScout\n* `Gorgias` - Gorgias\n* `Instagram` - Instagram\n* `YouTubeAnalytics` - YouTubeAnalytics\n* `FacebookPages` - FacebookPages\n* `TwitterAds` - TwitterAds\n* `Workday` - Workday\n* `ServiceNow` - ServiceNow\n* `Pardot` - Pardot\n* `Copper` - Copper\n* `Front` - Front\n* `ChartMogul` - ChartMogul\n* `Zuora` - Zuora\n* `Paddle` - Paddle\n* `CircleCI` - CircleCI\n* `CockroachDB` - CockroachDB\n* `Firebase` - Firebase\n* `AzureBlob` - AzureBlob\n* `GoogleDrive` - GoogleDrive\n* `OneDrive` - OneDrive\n* `SharePoint` - SharePoint\n* `Box` - Box\n* `SFTP` - SFTP\n* `MicrosoftTeams` - MicrosoftTeams\n* `Aircall` - Aircall\n* `Webflow` - Webflow\n* `Okta` - Okta\n* `Auth0` - Auth0\n* `Productboard` - Productboard\n* `Smartsheet` - Smartsheet\n* `Wrike` - Wrike\n* `Plaid` - Plaid\n* `SurveyMonkey` - SurveyMonkey\n* `Eventbrite` - Eventbrite\n* `RingCentral` - RingCentral\n* `Twilio` - Twilio\n* `Freshsales` - Freshsales\n* `Shortcut` - Shortcut\n* `ConvertKit` - ConvertKit\n* `Drip` - Drip\n* `CampaignMonitor` - CampaignMonitor\n* `MailerLite` - MailerLite\n* `Omnisend` - Omnisend\n* `Brevo` - Brevo\n* `Postmark` - Postmark\n* `Granola` - Granola\n* `BuildBetter` - BuildBetter"
      }
    }
  }
}
```
