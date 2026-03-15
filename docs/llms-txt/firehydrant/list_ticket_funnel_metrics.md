# Source: https://docs.firehydrant.com/reference/list_ticket_funnel_metrics.md

# List ticket task and follow up creation and completion metrics

Returns a report with task and follow up creation and completion data

# OpenAPI definition

````json
{
  "openapi": "3.0.1",
  "info": {
    "title": "FireHydrant API",
    "description": "The FireHydrant API is based around REST. It uses Bearer token authentication and returns JSON responses. You can use the FireHydrant API to configure integrations, define incidents, and set up webhooks--anything you can do on the FireHydrant UI.\n\n* [Dig into our API endpoints](https://developers.firehydrant.io/docs/api)\n* [View your bot users](https://app.firehydrant.io/organizations/bots)\n\n## Base API endpoint\n\n[https://api.firehydrant.io/v1](https://api.firehydrant.io/v1)\n\n## Current version\n\nv1\n\n## Authentication\n\nAll requests to the FireHydrant API require an `Authorization` header with the value set to `Bearer {token}`. FireHydrant supports bot tokens to act on behalf of a computer instead of a user's account. This prevents integrations from breaking when people leave your organization or their token is revoked. See the Bot tokens section (below) for more information on this.\n\nAn example of a header to authenticate against FireHydrant would look like:\n\n```\nAuthorization: Bearer fhb-thisismytoken\n```\n\n## Bot tokens\n\nTo access the FireHydrant API, you must authenticate with a bot token. (You must have owner permissions on your organization to see bot tokens.) Bot users allow you to interact with the FireHydrant API by using token-based authentication. To create bot tokens, log in to your organization and refer to the **Bot users** [page](https://app.firehydrant.io/organizations/bots).\n\nBot tokens enable you to create a bot that has no ties to any user. Normally, all actions associated with an API token are associated with the user who created it. Bot tokens attribute all actions to the bot user itself. This way, all data associated with the token actions can be performed against the FireHydrant API without a user.\n\nEvery request to the API is authenticated unless specified otherwise.\n\n### Rate Limiting\n\nCurrently, requests made with bot tokens are rate limited on a per-account level. If your account has multiple bot token then the rate limit is shared across all of them. As of February 7th, 2023, the rate limit is at least 50 requests per account every 10 seconds, or 300 requests per minute.\n\nRate limited responses will be served with a `429` status code and a JSON body of:\n\n```json\n{\"error\": \"rate limit exceeded\"}\n```\nand headers of:\n```\n\"RateLimit-Limit\" -> the maximum number of requests in the rate limit pool\n\"Retry-After\" -> the number of seconds to wait before trying again\n```\n\n## How lists are returned\n\nAPI lists are returned as arrays. A paginated entity in FireHydrant will return two top-level keys in the response object: a data key and a pagination key.\n\n### Paginated requests\n\nThe `data` key is returned as an array. Each item in the array includes all of the entity data specified in the API endpoint. (The per-page default for the array is 20 items.)\n\nPagination is the second key (`pagination`) returned in the overall response body. It includes medtadata around the current page, total count of items, and options to go to the next and previous page. All of the specifications returned in the pagination object are available as URL parameters. So if you want to specify, for example, going to the second page of a response, you can send a request to the same endpoint but pass the URL parameter **page=2**.\n\nFor example, you might request **https://api.firehydrant.io/v1/environments/** to retrieve environments data. The JSON returned contains the above-mentioned data section and pagination section. The data section includes various details about an incident, such as the environment name, description, and when it was created.\n\n```\n{\n  \"data\": [\n    {\n      \"id\": \"f8125cf4-b3a7-4f88-b5ab-57a60b9ed89b\",\n      \"name\": \"Production - GCP\",\n      \"description\": \"\",\n      \"created_at\": \"2021-02-17T20:02:10.679Z\"\n    },\n    {\n      \"id\": \"a69f1f58-af77-4708-802d-7e73c0bf261c\",\n      \"name\": \"Staging\",\n      \"description\": \"\",\n      \"created_at\": \"2021-04-16T13:41:59.418Z\"\n    }\n  ],\n  \"pagination\": {\n    \"count\": 2,\n    \"page\": 1,\n    \"items\": 2,\n    \"pages\": 1,\n    \"last\": 1,\n    \"prev\": null,\n    \"next\": null\n  }\n}\n```\n\nTo request the second page, you'd request the same endpoint with the additional query parameter of `page` in the URL:\n\n```\nGET https://api.firehydrant.io/v1/environments?page=2\n```\n\nIf you need to modify the number of records coming back from FireHydrant, you can use the `per_page` parameter (max is 200):\n\n```\nGET https://api.firehydrant.io/v1/environments?per_page=50\n```",
    "version": "0.0.1"
  },
  "servers": [
    {
      "url": "https://api.firehydrant.io/"
    }
  ],
  "security": [
    {
      "api_key": []
    }
  ],
  "tags": [
    {
      "name": "Metrics/Reporting",
      "description": "Operations related to Metrics & Reporting"
    }
  ],
  "paths": {
    "/v1/metrics/ticket_funnel": {
      "get": {
        "tags": [
          "Metrics/Reporting"
        ],
        "summary": "List ticket task and follow up creation and completion metrics",
        "description": "Returns a report with task and follow up creation and completion data",
        "operationId": "list_ticket_funnel_metrics",
        "parameters": [
          {
            "name": "conditions",
            "in": "query",
            "description": "A JSON string that defines 'logic' and 'user_data'",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "environments",
            "in": "query",
            "description": "A comma separated list of environment IDs or 'is_empty' to filter for incidents with no impacted environments",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "services",
            "in": "query",
            "description": "A comma separated list of service IDs or 'is_empty' to filter for incidents with no impacted services",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "functionalities",
            "in": "query",
            "description": "A comma separated list of functionality IDs or 'is_empty' to filter for incidents with no impacted functionalities",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "excluded_infrastructure_ids",
            "in": "query",
            "description": "A comma separated list of infrastructure IDs. Returns incidents that do not have the following infrastructure ids associated with them.",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "teams",
            "in": "query",
            "description": "A comma separated list of team IDs",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "assigned_teams",
            "in": "query",
            "description": "A comma separated list of IDs for assigned teams or 'is_empty' to filter for incidents with no active team assignments",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "status",
            "in": "query",
            "description": "Incident status",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "description": "Filters for incidents that started on or after this date",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "Filters for incidents that started on or before this date",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "resolved_at_or_after",
            "in": "query",
            "description": "Filters for incidents that were resolved at or after this time. Combine this with the `current_milestones` parameter if you wish to omit incidents that were re-opened and are still active.",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "resolved_at_or_before",
            "in": "query",
            "description": "Filters for incidents that were resolved at or before this time. Combine this with the `current_milestones` parameter if you wish to omit incidents that were re-opened and are still active.",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "closed_at_or_after",
            "in": "query",
            "description": "Filters for incidents that were closed at or after this time",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "closed_at_or_before",
            "in": "query",
            "description": "Filters for incidents that were closed at or before this time",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "created_at_or_after",
            "in": "query",
            "description": "Filters for incidents that were created at or after this time",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "created_at_or_before",
            "in": "query",
            "description": "Filters for incidents that were created at or before this time",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "query",
            "in": "query",
            "description": "A text query for an incident that searches on name, summary, and desciption",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "name",
            "in": "query",
            "description": "A query to search incidents by their name",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "saved_search_id",
            "in": "query",
            "description": "The id of a previously saved search.",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "priorities",
            "in": "query",
            "description": "A text value of priority",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "priority_not_set",
            "in": "query",
            "description": "Flag for including incidents where priority has not been set",
            "schema": {
              "type": "boolean",
              "nullable": true
            }
          },
          {
            "name": "severities",
            "in": "query",
            "description": "A text value of severity",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "severity_not_set",
            "in": "query",
            "description": "Flag for including incidents where severity has not been set",
            "schema": {
              "type": "boolean",
              "nullable": true
            }
          },
          {
            "name": "current_milestones",
            "in": "query",
            "description": "A comma separated list of current milestones",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "tags",
            "in": "query",
            "description": "A comma separated list of tags",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "tag_match_strategy",
            "in": "query",
            "description": "A matching strategy for the tags provided",
            "schema": {
              "type": "string",
              "nullable": true,
              "enum": [
                "any",
                "match_all",
                "exclude"
              ]
            }
          },
          {
            "name": "archived",
            "in": "query",
            "description": "Return archived incidents",
            "schema": {
              "type": "boolean",
              "nullable": true
            }
          },
          {
            "name": "updated_after",
            "in": "query",
            "description": "Filters for incidents that were updated after this date",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "updated_before",
            "in": "query",
            "description": "Filters for incidents that were updated before this date",
            "schema": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            }
          },
          {
            "name": "incident_type_id",
            "in": "query",
            "description": "A comma separated list of incident type IDs or 'is_empty' to filter for incidents with no incident type",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "custom_fields[field_id]",
            "in": "query",
            "description": "Custom field ID to filter on",
            "style": "form",
            "explode": false,
            "schema": {
              "type": "array",
              "nullable": true,
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "custom_fields[value]",
            "in": "query",
            "description": "Custom field value (empty means no value set)",
            "style": "form",
            "explode": false,
            "schema": {
              "type": "array",
              "nullable": true,
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "retrospective_templates",
            "in": "query",
            "description": "A comma separated list of retrospective template IDs",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "attached_runbooks",
            "in": "query",
            "description": "A comma separated list of runbook IDs",
            "schema": {
              "type": "string",
              "nullable": true
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "properties": {
                  "group_by": {
                    "type": "array",
                    "nullable": true,
                    "items": {
                      "type": "string",
                      "enum": [
                        "started_day",
                        "started_week",
                        "started_month",
                        "all_time"
                      ]
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Returns a report with task and follow up creation and completion data",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Metrics_TicketFunnelMetricsEntity"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Metrics_TicketFunnelMetricsEntity": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Metrics_TicketFunnelMetricsEntity_DataBucketEntity"
            }
          },
          "groupings": {
            "$ref": "#/components/schemas/NullableMetrics_TicketFunnelMetricsEntity_GroupingsEntity"
          }
        },
        "description": "Metrics_TicketFunnelMetricsEntity model"
      },
      "Metrics_TicketFunnelMetricsEntity_DataBucketEntity": {
        "type": "object",
        "properties": {
          "time_bucket": {
            "type": "string",
            "description": "The start datetime for the period",
            "format": "date-time",
            "nullable": true
          },
          "filter_params": {
            "$ref": "#/components/schemas/NullableMetrics_TicketFunnelMetricsEntity_DataBucketFilterParamsEntity"
          },
          "tasks_created": {
            "type": "integer",
            "description": "The number of tasks created",
            "format": "int32",
            "nullable": true
          },
          "tasks_done": {
            "type": "integer",
            "description": "The number of tasks completed",
            "format": "int32",
            "nullable": true
          },
          "follow_ups_created": {
            "type": "integer",
            "description": "The number of follow ups created",
            "format": "int32",
            "nullable": true
          },
          "follow_ups_done": {
            "type": "integer",
            "description": "The number of follow ups completed",
            "format": "int32",
            "nullable": true
          }
        }
      },
      "Metrics_TicketFunnelMetricsEntity_DataBucketFilterParamsEntity": {
        "type": "object",
        "properties": {
          "start_date": {
            "type": "string",
            "description": "The start datetime for the period",
            "format": "date-time",
            "nullable": true
          },
          "end_date": {
            "type": "string",
            "description": "The end datetime for the period not inclusive",
            "format": "date",
            "nullable": true
          }
        }
      },
      "Metrics_TicketFunnelMetricsEntity_GroupingsEntity": {
        "type": "object",
        "properties": {
          "bucket_size": {
            "type": "string",
            "description": "The bucket size for the data",
            "nullable": true
          }
        }
      },
      "NullableMetrics_TicketFunnelMetricsEntity_DataBucketFilterParamsEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Metrics_TicketFunnelMetricsEntity_DataBucketFilterParamsEntity"
          }
        ]
      },
      "NullableMetrics_TicketFunnelMetricsEntity_GroupingsEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Metrics_TicketFunnelMetricsEntity_GroupingsEntity"
          }
        ]
      }
    },
    "securitySchemes": {
      "api_key": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
      }
    }
  },
  "x-original-swagger-version": "2.0"
}
````