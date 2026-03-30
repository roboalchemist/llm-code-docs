# Source: https://posthog.com/docs/open-api-spec/environments_external_data_sources_refresh_schemas_create.md

# environments_external_data_sources_refresh_schemas_create

## OpenAPI

```json POST /api/environments/{environment_id}/external_data_sources/{id}/refresh_schemas/
{
  "paths": {
    "/api/environments/{environment_id}/external_data_sources/{id}/refresh_schemas/": {
      "post": {
        "operationId": "environments_external_data_sources_refresh_schemas_create",
        "description": "Fetch current schema/table list from the source and create any new ExternalDataSchema rows (no data sync).",
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
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this external data source.",
            "required": true
          }
        ],
        "tags": [
          "data_warehouse",
          "external_data_sources"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ExternalDataSourceSerializers"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ExternalDataSourceSerializers"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ExternalDataSourceSerializers"
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
        "deprecated": true,
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "ExternalDataSourceSerializers": {
        "type": "object",
        "description": "Mixin for serializers to add user access control fields",
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
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "status": {
            "type": "string",
            "readOnly": true
          },
          "client_secret": {
            "type": "string",
            "writeOnly": true
          },
          "account_id": {
            "type": "string",
            "writeOnly": true
          },
          "source_type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SourceTypeE09Enum"
              }
            ],
            "readOnly": true
          },
          "latest_error": {
            "type": "string",
            "readOnly": true
          },
          "prefix": {
            "type": "string",
            "nullable": true,
            "maxLength": 100
          },
          "description": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "access_method": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AccessMethodEnum"
              }
            ],
            "readOnly": true
          },
          "last_run_at": {
            "type": "string",
            "readOnly": true
          },
          "schemas": {
            "type": "string",
            "readOnly": true
          },
          "job_inputs": {
            "nullable": true
          },
          "revenue_analytics_config": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ExternalDataSourceRevenueAnalyticsConfig"
              }
            ],
            "readOnly": true
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          }
        },
        "required": [
          "access_method",
          "account_id",
          "client_secret",
          "created_at",
          "created_by",
          "id",
          "last_run_at",
          "latest_error",
          "revenue_analytics_config",
          "schemas",
          "source_type",
          "status",
          "user_access_level"
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
      },
      "AccessMethodEnum": {
        "enum": [
          "warehouse",
          "direct"
        ],
        "type": "string",
        "description": "* `warehouse` - warehouse\n* `direct` - direct"
      },
      "ExternalDataSourceRevenueAnalyticsConfig": {
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean"
          },
          "include_invoiceless_charges": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
