# Source: https://docs.firehydrant.com/reference/get_runbook.md

# Get a runbook

Get a runbook and all its configuration

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
      "name": "Runbooks",
      "description": "Operations related to Runbooks"
    }
  ],
  "paths": {
    "/v1/runbooks/{runbook_id}": {
      "get": {
        "tags": [
          "Runbooks"
        ],
        "summary": "Get a runbook",
        "description": "Get a runbook and all its configuration",
        "operationId": "get_runbook",
        "parameters": [
          {
            "name": "runbook_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Get a runbook and all its configuration",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RunbookEntity"
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
      "Integrations_IntegrationEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "slug": {
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
          "setup_url": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "connections": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Integrations_ConnectionEntity"
            }
          },
          "enabled": {
            "type": "boolean",
            "nullable": true
          },
          "installed": {
            "type": "boolean",
            "nullable": true
          },
          "deprecated": {
            "type": "boolean",
            "nullable": true
          },
          "logo": {
            "$ref": "#/components/schemas/NullableIntegrations_IntegrationEntity_LogoEntity"
          },
          "nat_ip": {
            "type": "string",
            "nullable": true
          }
        },
        "description": "Integrations_IntegrationEntity model"
      },
      "Integrations_ConnectionEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "integration_slug": {
            "type": "string",
            "nullable": true
          },
          "integration_id": {
            "type": "string",
            "nullable": true
          },
          "display_name": {
            "type": "string",
            "nullable": true
          },
          "configuration_url": {
            "type": "string",
            "nullable": true
          },
          "authorized_by": {
            "type": "string",
            "nullable": true
          },
          "authorized_by_id": {
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
          "details": {
            "type": "object",
            "properties": {},
            "description": "Integration-specific details of this connection. As identified by the integration_slug, this object will be represented by that integration's ConnectionEntity.",
            "nullable": true
          },
          "default_authorized_actor": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          }
        },
        "description": "Integrations_ConnectionEntity model"
      },
      "Integrations_IntegrationEntity_LogoEntity": {
        "type": "object",
        "properties": {
          "logo_url": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Runbooks_ActionsEntity": {
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
          "config": {
            "$ref": "#/components/schemas/NullableRunbooks_ActionConfigEntity"
          },
          "category": {
            "type": "string",
            "nullable": true
          },
          "prerequisites": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
          },
          "integration": {
            "$ref": "#/components/schemas/NullableIntegrations_IntegrationEntity"
          },
          "supported_runbook_types": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
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
          "automatable": {
            "type": "boolean",
            "nullable": true
          },
          "rerunnable": {
            "type": "boolean",
            "nullable": true
          },
          "repeatable": {
            "type": "boolean",
            "nullable": true
          },
          "default_logic": {
            "type": "object",
            "properties": {},
            "nullable": true
          },
          "default_rule_data": {
            "type": "object",
            "properties": {},
            "nullable": true
          }
        }
      },
      "Runbooks_ActionConfigEntity": {
        "type": "object",
        "properties": {
          "elements": {
            "type": "array",
            "description": "A list of elements that can be used in this action configuration",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Runbooks_ElementEntity"
            }
          },
          "documentation_url": {
            "type": "string",
            "description": "Location of documentation for this action",
            "nullable": true
          }
        }
      },
      "Runbooks_ElementEntity": {
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
          "markdown": {
            "$ref": "#/components/schemas/NullableRunbooks_ElementMarkdownEntity"
          },
          "textarea": {
            "$ref": "#/components/schemas/NullableRunbooks_ElementTextareaEntity"
          },
          "input": {
            "$ref": "#/components/schemas/NullableRunbooks_ElementInputEntity"
          },
          "plain_text": {
            "$ref": "#/components/schemas/NullableRunbooks_ElementMarkdownEntity"
          },
          "dynamic_select": {
            "$ref": "#/components/schemas/NullableRunbooks_ElementDynamicSelectEntity"
          }
        }
      },
      "Runbooks_ElementMarkdownEntity": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Runbooks_ElementTextareaEntity": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string",
            "nullable": true
          },
          "placeholder": {
            "type": "string",
            "nullable": true
          },
          "default_value": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Runbooks_ElementInputEntity": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string",
            "nullable": true
          },
          "placeholder": {
            "type": "string",
            "nullable": true
          },
          "default_value": {
            "type": "string",
            "nullable": true
          },
          "required": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "Runbooks_ElementDynamicSelectEntity": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string",
            "nullable": true
          },
          "placeholder": {
            "type": "string",
            "nullable": true
          },
          "async_url": {
            "type": "string",
            "nullable": true
          },
          "required": {
            "type": "boolean",
            "nullable": true
          },
          "clearable": {
            "type": "boolean",
            "nullable": true
          },
          "is_multi": {
            "type": "boolean",
            "nullable": true
          },
          "options": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Runbooks_ElementDynamicSelectEntity_SelectOptionEntity"
            }
          }
        }
      },
      "Runbooks_ElementDynamicSelectEntity_SelectOptionEntity": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "RunbookEntity": {
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
          "runbook_template_id": {
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
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "updated_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "steps": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/RunbookStepEntity"
            }
          },
          "attachment_rule": {
            "$ref": "#/components/schemas/NullableRules_RuleEntity"
          },
          "votes": {
            "$ref": "#/components/schemas/NullableEmptyVotesEntity"
          },
          "is_editable": {
            "type": "boolean",
            "nullable": true
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
          "auto_attach_to_restricted_incidents": {
            "type": "boolean",
            "nullable": true
          },
          "tutorial": {
            "type": "boolean",
            "nullable": true
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
        },
        "description": "RunbookEntity model"
      },
      "RunbookStepEntity": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "action_id": {
            "type": "string",
            "nullable": true
          },
          "step_id": {
            "type": "string",
            "nullable": true
          },
          "config": {
            "type": "object",
            "properties": {},
            "description": "An unstructured object of key/value pairs describing the config settings for the step.",
            "nullable": true
          },
          "action_elements": {
            "type": "array",
            "description": "A list of action elements",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
          },
          "step_elements": {
            "type": "array",
            "description": "A list of step elements",
            "nullable": true,
            "items": {
              "type": "object",
              "properties": {}
            }
          },
          "automatic": {
            "type": "boolean",
            "nullable": true
          },
          "delay_duration": {
            "type": "string",
            "nullable": true
          },
          "action": {
            "$ref": "#/components/schemas/NullableRunbooks_ActionsEntity"
          },
          "reruns": {
            "type": "boolean",
            "nullable": true
          },
          "repeats": {
            "type": "boolean",
            "nullable": true
          },
          "repeats_duration": {
            "type": "string",
            "nullable": true
          },
          "votes": {
            "$ref": "#/components/schemas/NullableEmptyVotesEntity"
          },
          "rule": {
            "$ref": "#/components/schemas/NullableRules_RuleEntity"
          }
        }
      },
      "EmptyVotesEntity": {
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
        }
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
      },
      "NullableIntegrations_IntegrationEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Integrations_IntegrationEntity"
          }
        ]
      },
      "NullableIntegrations_IntegrationEntity_LogoEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Integrations_IntegrationEntity_LogoEntity"
          }
        ]
      },
      "NullableRunbooks_ActionsEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ActionsEntity"
          }
        ]
      },
      "NullableRunbooks_ActionConfigEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ActionConfigEntity"
          }
        ]
      },
      "NullableRunbooks_ElementMarkdownEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ElementMarkdownEntity"
          }
        ]
      },
      "NullableRunbooks_ElementTextareaEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ElementTextareaEntity"
          }
        ]
      },
      "NullableRunbooks_ElementInputEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ElementInputEntity"
          }
        ]
      },
      "NullableRunbooks_ElementDynamicSelectEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Runbooks_ElementDynamicSelectEntity"
          }
        ]
      },
      "NullableEmptyVotesEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/EmptyVotesEntity"
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