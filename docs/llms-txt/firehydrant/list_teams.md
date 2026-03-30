# Source: https://docs.firehydrant.com/reference/list_teams.md

# List teams

List all of the teams in the organization

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
      "name": "Teams",
      "description": "Operations related to Teams"
    }
  ],
  "paths": {
    "/v1/teams": {
      "get": {
        "tags": [
          "Teams"
        ],
        "summary": "List teams",
        "description": "List all of the teams in the organization",
        "operationId": "list_teams",
        "parameters": [
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
          },
          {
            "name": "query",
            "in": "query",
            "description": "A query to search teams by their name or description",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "name",
            "in": "query",
            "description": "A query to search teams by their name",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "services",
            "in": "query",
            "description": "A comma separated list of service IDs",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "default_incident_role",
            "in": "query",
            "description": "Filter by teams that have or do not have members with a default incident role asssigned. Value may be 'present', 'blank', or the ID of an incident role.",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "lite",
            "in": "query",
            "description": "Boolean to determine whether to return a slimified version of the teams object",
            "schema": {
              "type": "boolean",
              "nullable": true
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List all of the teams in the organization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TeamEntityPaginated"
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
      "OrganizationEntity": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "id": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "FunctionalityEntityLite": {
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
          "slug": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
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
          "labels": {
            "type": "object",
            "additionalProperties": true,
            "description": "An object of label key and values",
            "nullable": true
          },
          "active_incidents": {
            "type": "array",
            "description": "List of active incident guids",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "links": {
            "type": "array",
            "description": "List of links attached to this functionality.",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/LinksEntity"
            }
          },
          "owner": {
            "$ref": "#/components/schemas/NullableTeamEntityLite"
          },
          "service_tier": {
            "type": "integer",
            "description": "Integer representing functionality tier (0-5, lower is more critical)",
            "format": "int32",
            "nullable": true
          },
          "alert_on_add": {
            "type": "boolean",
            "nullable": true
          },
          "auto_add_responding_team": {
            "type": "boolean",
            "nullable": true
          },
          "updated_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          }
        }
      },
      "LinksEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "href_url": {
            "type": "string",
            "nullable": true
          },
          "icon_url": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "TeamEntityLite": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
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
          "signals_ical_url": {
            "type": "string",
            "nullable": true
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "in_support_hours": {
            "type": "boolean",
            "nullable": true
          },
          "restrict_signals_resource_management": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
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
      "ServiceEntityLite": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
          },
          "service_tier": {
            "type": "integer",
            "format": "int32",
            "nullable": true
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
          "allowed_params": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "labels": {
            "type": "object",
            "additionalProperties": true,
            "description": "An object of label key and values",
            "nullable": true
          },
          "alert_on_add": {
            "type": "boolean",
            "nullable": true
          },
          "auto_add_responding_team": {
            "type": "boolean",
            "nullable": true
          }
        },
        "description": "ServiceEntityLite model"
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
      "ChecklistTemplateEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "checks": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ChecklistCheckEntity"
            }
          },
          "owner": {
            "$ref": "#/components/schemas/NullableTeamEntityLite"
          },
          "connected_services": {
            "type": "array",
            "description": "List of services that use this checklist",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityChecklist"
            }
          }
        },
        "description": "ChecklistTemplateEntity model"
      },
      "ChecklistCheckEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "ServiceEntityChecklist": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
          },
          "service_tier": {
            "type": "integer",
            "format": "int32",
            "nullable": true
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
          "allowed_params": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "labels": {
            "type": "object",
            "additionalProperties": true,
            "description": "An object of label key and values",
            "nullable": true
          },
          "alert_on_add": {
            "type": "boolean",
            "nullable": true
          },
          "auto_add_responding_team": {
            "type": "boolean",
            "nullable": true
          },
          "completed_checks": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "owner": {
            "$ref": "#/components/schemas/NullableTeamEntityLite"
          },
          "service_checklist_updated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        }
      },
      "TeamEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
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
          "signals_ical_url": {
            "type": "string",
            "nullable": true
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "in_support_hours": {
            "type": "boolean",
            "nullable": true
          },
          "restrict_signals_resource_management": {
            "type": "boolean",
            "nullable": true
          },
          "slack_channel": {
            "$ref": "#/components/schemas/NullableIntegrations_Slack_SlackChannelEntity"
          },
          "ms_teams_channel": {
            "$ref": "#/components/schemas/NullableIntegrations_MicrosoftTeamsV2_ChannelEntity"
          },
          "memberships": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/MembershipEntity"
            }
          },
          "owned_checklist_templates": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ChecklistTemplateEntity"
            }
          },
          "owned_functionalities": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/FunctionalityEntityLite"
            }
          },
          "owned_services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityLite"
            }
          },
          "owned_runbooks": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SlimRunbookEntity"
            }
          },
          "responding_services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityLite"
            }
          },
          "services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityLite"
            }
          },
          "functionalities": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/FunctionalityEntityLite"
            }
          },
          "default_signals_escalation_policy": {
            "$ref": "#/components/schemas/NullableSuccinctEntity"
          }
        },
        "description": "TeamEntity model"
      },
      "Integrations_Slack_SlackChannelEntity": {
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
          "slack_channel_id": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Integrations_MicrosoftTeamsV2_ChannelEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "channel_id": {
            "type": "string",
            "nullable": true
          },
          "channel_name": {
            "type": "string",
            "nullable": true
          },
          "ms_team_id": {
            "type": "string",
            "nullable": true
          },
          "team_name": {
            "type": "string",
            "nullable": true
          },
          "channel_url": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          },
          "incident": {
            "$ref": "#/components/schemas/NullableIncidentEntity"
          }
        }
      },
      "IncidentEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "UUID of the Incident",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "Name of the incident",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "description": "The time the incident was opened",
            "format": "date-time",
            "nullable": true
          },
          "started_at": {
            "type": "string",
            "description": "The time the incident started",
            "format": "date-time",
            "nullable": true
          },
          "discarded_at": {
            "type": "string",
            "description": "The time the incident was archived",
            "format": "date-time",
            "nullable": true
          },
          "summary": {
            "type": "string",
            "nullable": true
          },
          "customer_impact_summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "current_milestone": {
            "type": "string",
            "description": "The type/slug of the current milestone. Will be one of the currently configured milestones for the given incident.",
            "nullable": true
          },
          "number": {
            "type": "integer",
            "description": "Incident number",
            "format": "int32",
            "nullable": true
          },
          "priority": {
            "type": "string",
            "nullable": true
          },
          "severity": {
            "type": "string",
            "nullable": true
          },
          "severity_color": {
            "type": "string",
            "nullable": true
          },
          "severity_impact": {
            "type": "string",
            "nullable": true
          },
          "severity_condition": {
            "type": "string",
            "nullable": true
          },
          "tag_list": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "incident_type": {
            "$ref": "#/components/schemas/NullableSuccinctEntity"
          },
          "severity_impact_object": {
            "$ref": "#/components/schemas/NullableSeverityMatrix_ImpactEntity"
          },
          "severity_condition_object": {
            "$ref": "#/components/schemas/NullableSeverityMatrix_ConditionEntity"
          },
          "private_id": {
            "type": "string",
            "nullable": true
          },
          "organization_id": {
            "type": "string",
            "nullable": true
          },
          "milestones": {
            "type": "array",
            "description": "DEPRECATED: Please use lifecycle phases instead",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_MilestoneEntity"
            }
          },
          "lifecycle_phases": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_LifecyclePhaseEntity"
            }
          },
          "lifecycle_measurements": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_LifecycleMeasurementEntity"
            }
          },
          "active": {
            "type": "boolean",
            "nullable": true
          },
          "labels": {
            "type": "object",
            "properties": {},
            "description": "A key/value of labels",
            "nullable": true
          },
          "role_assignments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_RoleAssignmentEntity"
            }
          },
          "status_pages": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_StatusPageEntity"
            }
          },
          "incident_url": {
            "type": "string",
            "nullable": true
          },
          "private_status_page_url": {
            "type": "string",
            "nullable": true
          },
          "organization": {
            "$ref": "#/components/schemas/NullableOrganizationEntity"
          },
          "customers_impacted": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "monetary_impact": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "monetary_impact_cents": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "last_update": {
            "type": "string",
            "nullable": true
          },
          "last_note": {
            "$ref": "#/components/schemas/NullableEvent_NoteEntity"
          },
          "report_id": {
            "type": "string",
            "nullable": true
          },
          "ai_incident_summary": {
            "type": "string",
            "description": "DEPRECATED: this field is deprecated and will be removed in a future version. Please use the `/v1/audiences/summaries/:incident_id` endpoint instead.",
            "nullable": true
          },
          "services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SuccinctEntity"
            }
          },
          "environments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SuccinctEntity"
            }
          },
          "functionalities": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SuccinctEntity"
            }
          },
          "channel_name": {
            "type": "string",
            "nullable": true
          },
          "channel_reference": {
            "type": "string",
            "nullable": true
          },
          "channel_id": {
            "type": "string",
            "nullable": true
          },
          "channel_status": {
            "type": "string",
            "description": "inoperative: 0, operational: 1, archived: 2",
            "nullable": true
          },
          "incident_tickets": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Ticketing_TicketEntity"
            }
          },
          "ticket": {
            "$ref": "#/components/schemas/NullableTicketing_TicketEntity"
          },
          "impacts": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_ImpactEntity"
            }
          },
          "conference_bridges": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_ConferenceBridgeEntity"
            }
          },
          "incident_channels": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_ChannelEntity"
            }
          },
          "retro_exports": {
            "type": "array",
            "description": "A list of objects attached to this item. Can be one of: LinkEntity, CustomerSupportIssueEntity, or GenericAttachmentEntity",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "context_object": {
            "$ref": "#/components/schemas/NullableIncidents_ContextObjectEntity"
          },
          "team_assignments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_TeamAssignmentEntityLite"
            }
          },
          "conversations": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Conversations_API_Entities_Reference"
            }
          },
          "custom_fields": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/CustomFields_FieldValue"
            }
          },
          "field_requirements": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentEntity_FieldRequirementEntity"
            }
          }
        },
        "description": "IncidentEntity model"
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
      "SeverityMatrix_ImpactEntity": {
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
          "affects_id": {
            "type": "string",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          }
        },
        "description": "SeverityMatrix_ImpactEntity model"
      },
      "SeverityMatrix_ConditionEntity": {
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
          "position": {
            "type": "integer",
            "description": "Position is used to determine ordering of conditions in API responses and dropdowns. The condition with the lowest position (typically 0) will be considered the Default Condition",
            "format": "int32",
            "nullable": true
          }
        },
        "description": "SeverityMatrix_ConditionEntity model"
      },
      "Incidents_MilestoneEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "description": "The milestone's type. This will be one of the currently configured milestones for the given incident.",
            "nullable": true
          },
          "duration": {
            "type": "string",
            "description": "How long the incident spent in this milestones, in ISO 8601 Duration Format. This will be null if the milestone is the incident's current milestone.",
            "nullable": true
          },
          "occurred_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
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
          }
        }
      },
      "Incidents_LifecyclePhaseEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "milestones": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_LifecycleMilestoneEntity"
            }
          }
        }
      },
      "Incidents_LifecycleMilestoneEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "occurred_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "duration": {
            "type": "string",
            "nullable": true
          },
          "updated_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        }
      },
      "Incidents_LifecycleMeasurementEntity": {
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
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
          },
          "starts_at_milestone": {
            "type": "string",
            "nullable": true
          },
          "ends_at_milestone": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "string",
            "nullable": true
          },
          "calculated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        }
      },
      "Incidents_RoleAssignmentEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true,
            "enum": [
              "active",
              "inactive"
            ]
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
          "incident_role": {
            "$ref": "#/components/schemas/NullableIncidentRoleEntity"
          },
          "user": {
            "$ref": "#/components/schemas/NullableUserEntity"
          }
        },
        "description": "Incidents_RoleAssignmentEntity model"
      },
      "IncidentRoleEntity": {
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
          "summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
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
          "discarded_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        },
        "description": "IncidentRoleEntity model"
      },
      "UserEntity": {
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
          "email": {
            "type": "string",
            "nullable": true
          },
          "slack_user_id": {
            "type": "string",
            "nullable": true
          },
          "role": {
            "type": "string",
            "nullable": true
          },
          "slack_linked?": {
            "type": "boolean",
            "nullable": true
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
          "signals_enabled_notification_types": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "signals_notification_policy_compliance": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Signals_API_NotificationPolicyItemComplianceEntity"
            }
          }
        },
        "description": "UserEntity model"
      },
      "Signals_API_NotificationPolicyItemComplianceEntity": {
        "type": "object",
        "properties": {
          "notification_policy_item_id": {
            "type": "string",
            "nullable": true
          },
          "is_compliant": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "Incidents_StatusPageEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "url": {
            "type": "string",
            "nullable": true
          },
          "external_id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "display_name": {
            "type": "string",
            "nullable": true
          },
          "integration": {
            "$ref": "#/components/schemas/NullableIntegrationEntity"
          }
        },
        "description": "Incidents_StatusPageEntity model"
      },
      "IntegrationEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "integration_name": {
            "type": "string",
            "nullable": true
          },
          "integration_slug": {
            "type": "string",
            "nullable": true
          },
          "display_name": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        }
      },
      "Event_NoteEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "body": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "status_pages": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_StatusPageEntity"
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
        "description": "Event_NoteEntity model"
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
      "Ticketing_TicketEntity": {
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
          "state": {
            "type": "string",
            "nullable": true,
            "enum": [
              "open",
              "in_progress",
              "cancelled",
              "done"
            ]
          },
          "type": {
            "type": "string",
            "nullable": true,
            "enum": [
              "incident",
              "task",
              "follow_up"
            ]
          },
          "assignees": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/AuthorEntity"
            }
          },
          "priority": {
            "$ref": "#/components/schemas/NullableTicketing_PriorityEntity"
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "attachments": {
            "type": "array",
            "description": "A list of objects attached to this item. Can be one of: LinkEntity, CustomerSupportIssueEntity, or GenericAttachmentEntity",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
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
          "tag_list": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "incident_id": {
            "type": "string",
            "description": "ID of incident that this ticket is related to",
            "nullable": true
          },
          "incident_name": {
            "type": "string",
            "description": "Name of incident that this ticket is related to",
            "nullable": true
          },
          "incident_current_milestone": {
            "type": "string",
            "description": "Milestone of incident that this ticket is related to",
            "nullable": true
          },
          "task_id": {
            "type": "string",
            "description": "ID of task that this ticket is related to",
            "nullable": true
          },
          "due_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "sync_error_message": {
            "type": "string",
            "description": "Error message from syncing this ticket to integrations",
            "nullable": true
          },
          "ticketing_custom_fields": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Ticketing_CustomFields_FieldValue"
            }
          },
          "link": {
            "$ref": "#/components/schemas/NullableAttachments_LinkEntity"
          }
        },
        "description": "Ticketing_TicketEntity model"
      },
      "Ticketing_PriorityEntity": {
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
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
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
          }
        },
        "description": "Ticketing_PriorityEntity model"
      },
      "Ticketing_CustomFields_FieldValue": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the custom field definition",
            "nullable": true
          },
          "value_type": {
            "type": "string",
            "description": "The type of the custom field definition",
            "nullable": true
          },
          "display_name": {
            "type": "string",
            "description": "The display name of the custom field definition",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "The description of the custom field definition",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "description": "The slug of the custom field definition",
            "nullable": true
          },
          "field_id": {
            "type": "string",
            "description": "The field id of the custom field definition",
            "nullable": true
          },
          "field_type": {
            "type": "string",
            "description": "The field type of the custom field definition",
            "nullable": true
          },
          "permissible_values": {
            "type": "array",
            "description": "An array of strings representing selections for single_select or multi_select fields",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "value_array": {
            "type": "array",
            "description": "The value of the custom field as an array (for select fields)",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "value_string": {
            "type": "string",
            "description": "The value of the custom field as a string (for string and datetime types)",
            "nullable": true
          },
          "value": {
            "type": "string",
            "description": "The raw value of the custom field",
            "nullable": true
          }
        }
      },
      "Attachments_LinkEntity": {
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
          "display_text": {
            "type": "string",
            "nullable": true
          },
          "href_url": {
            "type": "string",
            "nullable": true
          },
          "icon_url": {
            "type": "string",
            "nullable": true
          },
          "editable": {
            "type": "boolean",
            "description": "Link can be edited",
            "nullable": true
          },
          "deletable": {
            "type": "boolean",
            "description": "Link can be deleted",
            "nullable": true
          }
        },
        "description": "Attachments_LinkEntity model"
      },
      "Incidents_ImpactEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true,
            "enum": [
              "customer",
              "environment",
              "functionality",
              "service"
            ]
          },
          "impact": {
            "$ref": "#/components/schemas/NullableSuccinctEntity"
          },
          "condition": {
            "$ref": "#/components/schemas/NullableSeverityMatrix_ConditionEntity"
          },
          "conversations": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Conversations_API_Entities_Reference"
            }
          }
        }
      },
      "Incidents_ConferenceBridgeEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "attachments": {
            "type": "array",
            "description": "A list of objects attached to this item. Can be one of: LinkEntity, CustomerSupportIssueEntity, or GenericAttachmentEntity",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
          },
          "has_translated_transcripts": {
            "type": "boolean",
            "nullable": true
          },
          "language_codes": {
            "type": "array",
            "description": "A list of language codes that have translated transcripts for this conference bridge",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "transcription_status": {
            "type": "string",
            "nullable": true
          },
          "transcription_sub_code": {
            "type": "string",
            "nullable": true
          },
          "previous_host_assignment": {
            "type": "string",
            "nullable": true
          }
        },
        "description": "Incidents_ConferenceBridgeEntity model"
      },
      "Incidents_ChannelEntity": {
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
          "source_name": {
            "type": "string",
            "nullable": true
          },
          "source_id": {
            "type": "string",
            "nullable": true
          },
          "url": {
            "type": "string",
            "nullable": true
          },
          "icon_url": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          }
        },
        "description": "Incidents_ChannelEntity model"
      },
      "Incidents_ContextObjectEntity": {
        "type": "object",
        "properties": {
          "object_type": {
            "type": "string",
            "nullable": true
          },
          "object_id": {
            "type": "string",
            "nullable": true
          },
          "context_tag": {
            "type": "string",
            "nullable": true
          },
          "context_description": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Incidents_TeamAssignmentEntityLite": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
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
          "team": {
            "$ref": "#/components/schemas/NullableTeamEntityLite"
          }
        }
      },
      "CustomFields_FieldValue": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "value_type": {
            "type": "string",
            "nullable": true
          },
          "display_name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "nullable": true
          },
          "field_id": {
            "type": "string",
            "nullable": true
          },
          "value_array": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "value_string": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "IncidentEntity_FieldRequirementEntity": {
        "type": "object",
        "properties": {
          "field_id": {
            "type": "string",
            "description": "A unique identifier for the field.",
            "nullable": true
          },
          "required_at_milestone_id": {
            "type": "string",
            "description": "The milestone at which this field is required. If null, this field is always required.",
            "nullable": true
          }
        }
      },
      "MembershipEntity": {
        "type": "object",
        "properties": {
          "user": {
            "$ref": "#/components/schemas/NullableUserEntity"
          },
          "schedule": {
            "$ref": "#/components/schemas/NullableScheduleEntity"
          },
          "signals_on_call_schedule": {
            "$ref": "#/components/schemas/NullableSuccinctEntity"
          },
          "default_incident_role": {
            "$ref": "#/components/schemas/NullableIncidentRoleEntity"
          }
        }
      },
      "ScheduleEntity": {
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
          "integration": {
            "type": "string",
            "nullable": true
          },
          "discarded": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "SlimRunbookEntity": {
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
          "summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
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
          "attachment_rule": {
            "$ref": "#/components/schemas/NullableRules_RuleEntity"
          },
          "owner": {
            "$ref": "#/components/schemas/NullableTeamEntityLite"
          },
          "categories": {
            "type": "array",
            "description": "categories the runbook applies to",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "last_executed_at": {
            "type": "string",
            "description": "The timestamp when this runbook was last executed",
            "format": "date-time",
            "nullable": true
          },
          "last_executed_for_incident": {
            "$ref": "#/components/schemas/NullablePublicAPI_V1_Incidents_SuccinctEntity"
          }
        }
      },
      "Rules_RuleEntity": {
        "type": "object",
        "properties": {
          "logic": {
            "type": "object",
            "properties": {},
            "description": "An unstructured object of key/value pairs describing the logic for applying the rule.",
            "nullable": true
          },
          "user_data": {
            "$ref": "#/components/schemas/NullableFHTypes_GenericEntity"
          }
        }
      },
      "FHTypes_GenericEntity": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "string",
            "nullable": true
          },
          "label": {
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
      "TeamEntityPaginated": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/TeamEntity"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/NullablePaginationEntity"
          }
        },
        "description": "TeamEntityPaginated model"
      },
      "NullableOrganizationEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/OrganizationEntity"
          }
        ]
      },
      "NullableTeamEntityLite": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/TeamEntityLite"
          }
        ]
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
      "NullableIntegrations_Slack_SlackChannelEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Integrations_Slack_SlackChannelEntity"
          }
        ]
      },
      "NullableIntegrations_MicrosoftTeamsV2_ChannelEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Integrations_MicrosoftTeamsV2_ChannelEntity"
          }
        ]
      },
      "NullableIncidentEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/IncidentEntity"
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
      "NullableSeverityMatrix_ImpactEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/SeverityMatrix_ImpactEntity"
          }
        ]
      },
      "NullableSeverityMatrix_ConditionEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/SeverityMatrix_ConditionEntity"
          }
        ]
      },
      "NullableIncidentRoleEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/IncidentRoleEntity"
          }
        ]
      },
      "NullableUserEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/UserEntity"
          }
        ]
      },
      "NullableIntegrationEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/IntegrationEntity"
          }
        ]
      },
      "NullableEvent_NoteEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Event_NoteEntity"
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
      "NullableTicketing_TicketEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Ticketing_TicketEntity"
          }
        ]
      },
      "NullableTicketing_PriorityEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Ticketing_PriorityEntity"
          }
        ]
      },
      "NullableAttachments_LinkEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Attachments_LinkEntity"
          }
        ]
      },
      "NullableIncidents_ContextObjectEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Incidents_ContextObjectEntity"
          }
        ]
      },
      "NullableScheduleEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/ScheduleEntity"
          }
        ]
      },
      "NullableRules_RuleEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Rules_RuleEntity"
          }
        ]
      },
      "NullableFHTypes_GenericEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/FHTypes_GenericEntity"
          }
        ]
      },
      "NullablePublicAPI_V1_Incidents_SuccinctEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/PublicAPI_V1_Incidents_SuccinctEntity"
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