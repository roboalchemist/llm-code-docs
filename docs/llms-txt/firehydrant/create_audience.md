# Source: https://docs.firehydrant.com/reference/create_audience.md

# Create audience

Create a new audience

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
      "name": "Audiences",
      "description": "Operations related to Audiences"
    }
  ],
  "paths": {
    "/v1/audiences": {
      "post": {
        "tags": [
          "Audiences"
        ],
        "summary": "Create audience",
        "description": "Create a new audience",
        "operationId": "create_audience",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/create_audience"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Create a new audience",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Audiences_Entities_AudienceEntity"
                }
              }
            }
          }
        },
        "x-codegen-request-body-name": "create_audience"
      }
    }
  },
  "components": {
    "schemas": {
      "Audiences_Entities_AudienceEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the audience",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "Name of the audience (maximum 255 characters)",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "description": "Slug of the audience, unique and autogenerated",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "Description of the audience and its purpose (maximum 4000 characters)",
            "nullable": true
          },
          "default": {
            "type": "boolean",
            "description": "Whether this is the organization's default audience",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "description": "When the audience was created",
            "format": "date-time",
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "description": "When the audience was last updated",
            "format": "date-time",
            "nullable": true
          },
          "discarded_at": {
            "type": "string",
            "description": "When the audience was discarded (soft deleted)",
            "format": "date-time",
            "nullable": true
          },
          "details": {
            "type": "array",
            "description": "List of incident details for this audience",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Audiences_Entities_DetailEntity"
            }
          }
        },
        "description": "Audiences_Entities_AudienceEntity model"
      },
      "Audiences_Entities_DetailEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the detail item",
            "nullable": true
          },
          "question": {
            "type": "string",
            "description": "The need-to-know question (maximum 255 characters)",
            "nullable": true
          },
          "prompt": {
            "type": "string",
            "description": "AI prompt used to gather this information",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "description": "Order position of this item in the list",
            "format": "int32",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "description": "Slug of the detail, unique and autogenerated",
            "nullable": true
          }
        }
      },
      "create_audience": {
        "required": [
          "description",
          "name"
        ],
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the audience (max 255 characters)"
          },
          "description": {
            "type": "string",
            "description": "Description of the audience (max 4000 characters)"
          },
          "default": {
            "type": "boolean",
            "description": "Whether this is the default audience",
            "nullable": true,
            "default": false
          },
          "details": {
            "type": "array",
            "nullable": true,
            "items": {
              "required": [
                "prompt",
                "question"
              ],
              "type": "object",
              "properties": {
                "question": {
                  "type": "string",
                  "description": "The incident detail question (max 255 characters)"
                },
                "prompt": {
                  "type": "string",
                  "description": "The prompt to display when collecting this detail"
                },
                "slug": {
                  "type": "string",
                  "description": "Optional unique identifier for this detail",
                  "nullable": true
                }
              }
            }
          },
          "settings": {
            "required": [
              "alerts",
              "communications",
              "current_milestone",
              "custom_fields",
              "customer_impact_summary",
              "description",
              "high_value_events",
              "id",
              "medium_value_events",
              "name",
              "responders",
              "services",
              "severity",
              "started_at",
              "status",
              "timeline",
              "work_items"
            ],
            "type": "object",
            "properties": {
              "id": {
                "type": "boolean",
                "description": "Include the incident's id in summarization"
              },
              "name": {
                "type": "boolean",
                "description": "Include the incident's name in summarization"
              },
              "started_at": {
                "type": "boolean",
                "description": "Include the datetime the incident started in summarization"
              },
              "status": {
                "type": "boolean",
                "description": "Include the incident's status in summarization"
              },
              "severity": {
                "type": "boolean",
                "description": "Include the incident's severity in summarization"
              },
              "description": {
                "type": "boolean",
                "description": "Include the incident's description in summarization"
              },
              "customer_impact_summary": {
                "type": "boolean",
                "description": "Include the incident's customer impact summary in summarization"
              },
              "current_milestone": {
                "type": "boolean",
                "description": "Include the incident's current milestone in summarization"
              },
              "timeline": {
                "type": "boolean",
                "description": "Include each milestone change and any high or medium value event in summarization"
              },
              "communications": {
                "type": "boolean",
                "description": "Include all communication (starred or not) in summarization"
              },
              "work_items": {
                "type": "boolean",
                "description": "Include all tickets and tasks in summarization"
              },
              "services": {
                "type": "boolean",
                "description": "Include all impacted catalog items in summarization"
              },
              "custom_fields": {
                "type": "boolean",
                "description": "Include all custom fields for the incident in summarization"
              },
              "alerts": {
                "type": "boolean",
                "description": "Include all alerts related to the incident in summarization"
              },
              "responders": {
                "type": "boolean",
                "description": "Include all information on responders, their roles, and any assigned teams"
              },
              "high_value_events": {
                "required": [
                  "add_task_list",
                  "bulk_milestone_update",
                  "external_link",
                  "handoff",
                  "impact_update",
                  "incident_status"
                ],
                "type": "object",
                "properties": {
                  "incident_status": {
                    "type": "boolean",
                    "description": "Include incident status change events in the timeline"
                  },
                  "bulk_milestone_update": {
                    "type": "boolean",
                    "description": "Include bulk updates (including runbook or automation events) in the timeline"
                  },
                  "impact_update": {
                    "type": "boolean",
                    "description": "Include any catalog item impact events in the timeline"
                  },
                  "handoff": {
                    "type": "boolean",
                    "description": "Include any handoff events in the timeline"
                  },
                  "add_task_list": {
                    "type": "boolean",
                    "description": "Include any additions to the task list in the timeline"
                  },
                  "external_link": {
                    "type": "boolean",
                    "description": "Include any external link events in the timeline"
                  }
                }
              },
              "medium_value_events": {
                "required": [
                  "change_type",
                  "child_changed",
                  "new_related_change_event",
                  "parent_changed",
                  "runbook_step_execution_update"
                ],
                "type": "object",
                "properties": {
                  "parent_changed": {
                    "type": "boolean",
                    "description": "Include any events where the incident's parent changes in the timeline"
                  },
                  "child_changed": {
                    "type": "boolean",
                    "description": "Include any events where the incident's children change in the timeline"
                  },
                  "new_related_change_event": {
                    "type": "boolean",
                    "description": "Include any related change events in the timeline"
                  },
                  "runbook_step_execution_update": {
                    "type": "boolean",
                    "description": "Include any runbook step updates in the timeline"
                  },
                  "change_type": {
                    "type": "boolean",
                    "description": "Include any incident type change events in the timeline"
                  }
                }
              }
            },
            "description": "audience settings for initial audience creation",
            "nullable": true
          }
        },
        "description": "Create a new audience"
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