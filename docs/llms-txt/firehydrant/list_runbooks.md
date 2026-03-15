# Source: https://docs.firehydrant.com/reference/list_runbooks.md

# List runbooks

Lists all available runbooks.

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
    "/v1/runbooks": {
      "get": {
        "tags": [
          "Runbooks"
        ],
        "summary": "List runbooks",
        "description": "Lists all available runbooks.",
        "operationId": "list_runbooks",
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
            "name": "name",
            "in": "query",
            "description": "A query to search runbooks by their name",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "owners",
            "in": "query",
            "description": "A query to search runbooks by their owners",
            "schema": {
              "type": "string",
              "nullable": true
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "Sort runbooks by their updated date. Accepts 'asc', 'desc'. This parameter is deprecated in favor of 'order_by' and 'order_direction'.",
            "schema": {
              "type": "string",
              "nullable": true,
              "enum": [
                "asc",
                "desc"
              ]
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "description": "Sort runbooks by their updated date or name. Accepts 'updated_at', 'name', 'owner', 'last_executed_at', and 'created_at'.",
            "schema": {
              "type": "string",
              "nullable": true,
              "enum": [
                "updated_at",
                "name",
                "created_at",
                "last_executed_at",
                "owner"
              ]
            }
          },
          {
            "name": "order_direction",
            "in": "query",
            "description": "Allows assigning a direction to how the specified `order_by` parameter is sorted. This parameter must be paired with `order_by` and does nothing on its own.",
            "schema": {
              "type": "string",
              "nullable": true,
              "enum": [
                "asc",
                "desc"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Lists all available runbooks.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SlimRunbookEntityPaginated"
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
      "SlimRunbookEntityPaginated": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/SlimRunbookEntity"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/NullablePaginationEntity"
          }
        },
        "description": "SlimRunbookEntityPaginated model"
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