# Source: https://docs.firehydrant.com/reference/list_incident_types.md

# List incident types

List all of the incident types in the organization

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
      "name": "Incident Settings",
      "description": "Operations related to Incident Settings"
    }
  ],
  "paths": {
    "/v1/incident_types": {
      "get": {
        "tags": [
          "Incident Settings"
        ],
        "summary": "List incident types",
        "description": "List all of the incident types in the organization",
        "operationId": "list_incident_types",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "description": "A query to search incident types by their name",
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
            "description": "List all of the incident types in the organization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IncidentTypeEntityPaginated"
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
      "IncidentTypeEntity": {
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
          "allowed_role_ids": {
            "type": "array",
            "description": "IDs of roles allowed to create incidents of this type. Empty array means all roles are allowed.",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "template": {
            "$ref": "#/components/schemas/NullableIncidentTypeEntity_TemplateEntity"
          },
          "template_values": {
            "$ref": "#/components/schemas/NullableIncidentTypeEntity_TemplateValuesEntity"
          },
          "required_fields": {
            "type": "array",
            "description": "A list of fields that are required on incidents of this type.",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Incidents_RequiredFieldEntity"
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
          }
        },
        "description": "IncidentTypeEntity model"
      },
      "IncidentTypeEntity_TemplateEntity": {
        "type": "object",
        "properties": {
          "incident_name": {
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
          "customer_impact_summary": {
            "type": "string",
            "nullable": true
          },
          "labels": {
            "type": "object",
            "additionalProperties": true,
            "description": "Arbitrary key:value pairs of labels for your incidents.",
            "nullable": true
          },
          "severity": {
            "type": "string",
            "nullable": true
          },
          "priority": {
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
          "runbook_ids": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "team_ids": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "private_incident": {
            "type": "boolean",
            "nullable": true
          },
          "custom_fields": {
            "type": "string",
            "nullable": true
          },
          "impacts": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentTypeEntity_TemplateImpactEntity"
            }
          }
        }
      },
      "IncidentTypeEntity_TemplateImpactEntity": {
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
          "condition_id": {
            "type": "string",
            "nullable": true
          },
          "condition_name": {
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
          }
        }
      },
      "IncidentTypeEntity_TemplateValuesEntity": {
        "type": "object",
        "properties": {
          "services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentTypeEntity_TemplateImpactEntity"
            }
          },
          "functionalities": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentTypeEntity_TemplateImpactEntity"
            }
          },
          "environments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentTypeEntity_TemplateImpactEntity"
            }
          },
          "runbooks": {
            "type": "object",
            "properties": {},
            "description": "A hash mapping runbook IDs to runbook names.",
            "nullable": true
          },
          "teams": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/TeamEntityLite"
            }
          }
        }
      },
      "Incidents_RequiredFieldEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "A unique identifier for the field. For built-in fields, this will be human-readable. For custom fields or milestone timestamps, it will be a prefixed version of the field or milestone's UUID.",
            "nullable": true
          },
          "required_at_milestone_id": {
            "type": "string",
            "description": "The milestone at which this field is required. If null, this field is always required.",
            "nullable": true
          }
        }
      },
      "IncidentTypeEntityPaginated": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/IncidentTypeEntity"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/NullablePaginationEntity"
          }
        },
        "description": "IncidentTypeEntityPaginated model"
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
      "NullableIncidentTypeEntity_TemplateEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/IncidentTypeEntity_TemplateEntity"
          }
        ]
      },
      "NullableIncidentTypeEntity_TemplateValuesEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/IncidentTypeEntity_TemplateValuesEntity"
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