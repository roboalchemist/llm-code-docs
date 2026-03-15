# Source: https://docs.firehydrant.com/reference/list_incident_alerts.md

# List alerts for an incident

List alerts that have been attached to an incident

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
      "name": "Alerts",
      "description": "Operations related to Alerts"
    }
  ],
  "paths": {
    "/v1/incidents/{incident_id}/alerts": {
      "get": {
        "tags": [
          "Alerts"
        ],
        "summary": "List alerts for an incident",
        "description": "List alerts that have been attached to an incident",
        "operationId": "list_incident_alerts",
        "parameters": [
          {
            "name": "incident_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List alerts that have been attached to an incident",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Incidents_AlertEntityPaginated"
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
      "SuccinctEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
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
      "PublicAPI_V1_Incidents_SuccinctEntity": {
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
          "number": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          }
        }
      },
      "Signals_API_TargetEntity": {
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
          "type": {
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "type": "string",
            "nullable": true
          },
          "is_pageable": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "Signals_API_RuleEntity": {
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
          "expression": {
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "type": "string",
            "nullable": true
          },
          "target": {
            "$ref": "#/components/schemas/NullableSignals_API_TargetEntity"
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "incident_type": {
            "$ref": "#/components/schemas/NullableSuccinctEntity"
          },
          "notification_priority_override": {
            "type": "string",
            "nullable": true,
            "enum": [
              "HIGH",
              "MEDIUM",
              "LOW",
              ""
            ]
          },
          "create_incident_condition_when": {
            "type": "string",
            "nullable": true,
            "enum": [
              "WHEN_UNSPECIFIED",
              "WHEN_ALWAYS"
            ]
          },
          "deduplication_expiry": {
            "type": "string",
            "description": "Duration for deduplicating similar alerts (ISO8601 duration format e.g., 'PT30M', 'PT2H', 'P1D')",
            "nullable": true,
            "example": "PT1H"
          }
        },
        "description": "Signals_API_RuleEntity model"
      },
      "Incidents_AlertEntityPaginated": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_AlertEntity"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/NullablePaginationEntity"
          }
        },
        "description": "Incidents_AlertEntityPaginated model"
      },
      "Incidents_AlertEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "alert": {
            "$ref": "#/components/schemas/NullableAlerts_AlertEntity"
          },
          "primary": {
            "type": "boolean",
            "description": "whether or not this is the primary alert for this incident",
            "nullable": true
          }
        },
        "description": "Incidents_AlertEntity model"
      },
      "Alerts_AlertEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "priority": {
            "type": "string",
            "nullable": true
          },
          "integration_name": {
            "type": "string",
            "nullable": true
          },
          "starts_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "ends_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "duration_ms": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "duration_iso8601": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          },
          "remote_id": {
            "type": "string",
            "nullable": true
          },
          "remote_url": {
            "type": "string",
            "nullable": true
          },
          "labels": {
            "type": "object",
            "properties": {},
            "description": "Arbitrary key:value pairs of labels.",
            "nullable": true
          },
          "environments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SuccinctEntity"
            }
          },
          "services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SuccinctEntity"
            }
          },
          "tags": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "source_icon": {
            "type": "string",
            "nullable": true
          },
          "signal_id": {
            "type": "string",
            "nullable": true
          },
          "signal_rule": {
            "$ref": "#/components/schemas/NullableSignals_API_RuleEntity"
          },
          "signal_target": {
            "$ref": "#/components/schemas/NullableSignals_API_TargetEntity"
          },
          "team_name": {
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "type": "string",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "notification_priority": {
            "type": "string",
            "nullable": true
          },
          "incidents": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/PublicAPI_V1_Incidents_SuccinctEntity"
            }
          },
          "events": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Alerts_SirenEventEntity"
            }
          },
          "is_expired": {
            "type": "boolean",
            "nullable": true
          },
          "is_noise": {
            "type": "boolean",
            "nullable": true
          },
          "parent_alerts": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Alerts_SirenAlertEntity"
            }
          },
          "child_alerts": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Alerts_SirenAlertEntity"
            }
          },
          "conversations": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Conversations_API_Entities_Reference"
            }
          }
        },
        "description": "Alerts_AlertEntity model"
      },
      "Alerts_SirenEventEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          },
          "data": {
            "type": "object",
            "properties": {},
            "description": "The event's payload",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        }
      },
      "Alerts_SirenAlertEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "starts_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "ends_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          },
          "remote_id": {
            "type": "string",
            "nullable": true
          },
          "remote_url": {
            "type": "string",
            "nullable": true
          },
          "labels": {
            "type": "object",
            "properties": {},
            "description": "Arbitrary key:value pairs of labels.",
            "nullable": true
          },
          "tags": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "signal_id": {
            "type": "string",
            "nullable": true
          },
          "signal_rule": {
            "$ref": "#/components/schemas/NullableSignals_API_RuleEntity"
          }
        }
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
      "NullableSuccinctEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/SuccinctEntity"
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
      "NullableSignals_API_TargetEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Signals_API_TargetEntity"
          }
        ]
      },
      "NullableSignals_API_RuleEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Signals_API_RuleEntity"
          }
        ]
      },
      "NullableAlerts_AlertEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Alerts_AlertEntity"
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