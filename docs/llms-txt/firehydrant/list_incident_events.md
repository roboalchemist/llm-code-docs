# Source: https://docs.firehydrant.com/reference/list_incident_events.md

# List events for an incident

List all events for an incident. An event is a timeline entry. This can be filtered with params to retrieve events of a certain type.

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
      "name": "Incidents",
      "description": "Operations related to Incidents"
    }
  ],
  "paths": {
    "/v1/incidents/{incident_id}/events": {
      "get": {
        "tags": [
          "Incidents"
        ],
        "summary": "List events for an incident",
        "description": "List all events for an incident. An event is a timeline entry. This can be filtered with params to retrieve events of a certain type.",
        "operationId": "list_incident_events",
        "parameters": [
          {
            "name": "incident_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "types",
            "in": "query",
            "description": "A comma separated list of types of events to filter by. Possible values are:\n - `add_task_list`: Task list was added\n - `alert_event`: Someone was paged or took action on a linked alert\n - `alert_linked`: An alert was linked to the incident\n - `bulk_milestone_update`: When a milestone change occurs with no other changes\n - `bulk_update`: When an incident note/update is posted or when impacted components are updated. If other changes occur together with either of these changes (e.g., milestone change), they are all bundled together into a bulk_update\n - `change_type`: Updates to associated change events\n - `chat_message`: Any chat message event in a linked chat app like Slack or MS Teams\n - `children_changed`: When adding or updating child related incidents\n - `external_link`: When an external link is added or updated\n - `general_update`: Currently only describes Runbook stoppage events\n - `generic_chat_message`: When an event or message is manually added to the timeline via the web UI or API\n - `incident_attachment`: When attachments or files are added to the timeline\n - `generic_resource_change`: Any changes to individual fields within the incident, including custom fields\n - `incident_restriction`: When an incident is converted to private\n - `incident_status`: Only used when an incident starts and changes to an `active` state\n - `note`: When a message is posted to a status page directly and not via `/fh update`\n - `role_update`: Any updates to assigned roles\n - `runbook_attachment`: Any updates to a runbook\n - `runbook_step_execution_update`: Any Runbook step events\n - `task_update`: Task update events\n - `team_assignment`: Team assignment events\n - `ticket_update`: Updates to incident and follow-up tickets",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "nullable": true
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "nullable": true
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List all events for an incident. An event is a timeline entry. This can be filtered with params to retrieve events of a certain type.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IncidentEventEntityPaginated"
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
      "AuthorEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "source": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "PaginationEntity": {
        "type": "object",
        "properties": {
          "count": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "page": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "items": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "pages": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "last": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "prev": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "next": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          }
        }
      },
      "Conversations_API_Entities_Reference": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "resource_class": {
            "type": "string",
            "nullable": true
          },
          "resource_id": {
            "type": "string",
            "nullable": true
          },
          "field": {
            "type": "string",
            "nullable": true
          },
          "comments_url": {
            "type": "string",
            "nullable": true
          },
          "channel": {
            "$ref": "#/components/schemas/NullableConversations_API_Entities_Channel"
          }
        }
      },
      "Conversations_API_Entities_Channel": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "IncidentEventEntityPaginated": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentEventEntity"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/NullablePaginationEntity"
          }
        },
        "description": "IncidentEventEntityPaginated model"
      },
      "IncidentEventEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "incident_id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          },
          "context": {
            "type": "string",
            "nullable": true
          },
          "data": {
            "type": "object",
            "properties": {},
            "description": "Can be one of: NoteEntity, TourStepEntity, RootCauseEntity, ChangeTypeEntity, RoleUpdateEntity, TaskUpdateEntity, AlertLinkedEntity, ChatMessageEntity, AddTaskListEntity, ImpactUpdateEntity, TicketUpdateEntity, GeneralUpdateEntity, ChangelogEntryEntity, IncidentStatusEntity, TeamAssignmentEntity, BulkUpdateEntity",
            "nullable": true
          },
          "occurred_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "visibility": {
            "type": "string",
            "nullable": true,
            "enum": [
              "private_to_org",
              "open_to_public",
              "internal_status_page"
            ]
          },
          "author": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "votes": {
            "$ref": "#/components/schemas/NullableVotesEntity"
          },
          "conversations": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Conversations_API_Entities_Reference"
            }
          }
        },
        "description": "IncidentEventEntity model"
      },
      "VotesEntity": {
        "type": "object",
        "properties": {
          "voted": {
            "type": "boolean",
            "description": "Whether or not the current actor has voted",
            "nullable": true
          },
          "liked": {
            "type": "boolean",
            "description": "Whether or not the current actor has voted positively",
            "nullable": true
          },
          "disliked": {
            "type": "boolean",
            "description": "Whether or not the current actor has voted negatively",
            "nullable": true
          },
          "likes": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "dislikes": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          }
        },
        "description": "VotesEntity model"
      },
      "NullableAuthorEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/AuthorEntity"
          }
        ]
      },
      "NullablePaginationEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/PaginationEntity"
          }
        ]
      },
      "NullableConversations_API_Entities_Channel": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Conversations_API_Entities_Channel"
          }
        ]
      },
      "NullableVotesEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/VotesEntity"
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