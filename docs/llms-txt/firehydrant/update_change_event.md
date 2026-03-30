# Source: https://docs.firehydrant.com/reference/update_change_event.md

# Update a change event

Update a change event

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
      "name": "Changes",
      "description": "Operations related to Changes"
    }
  ],
  "paths": {
    "/v1/changes/events/{change_event_id}": {
      "patch": {
        "tags": [
          "Changes"
        ],
        "summary": "Update a change event",
        "description": "Update a change event",
        "operationId": "update_change_event",
        "parameters": [
          {
            "name": "change_event_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/update_change_event"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Update a change event",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ChangeEventEntity"
                }
              }
            }
          }
        },
        "x-codegen-request-body-name": "update_change_event"
      }
    }
  },
  "components": {
    "schemas": {
      "EnvironmentEntryEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "UUID of the Environment",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "Name of the Environment",
            "nullable": true
          },
          "slug": {
            "type": "string",
            "description": "Slug of the Environment",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "Description of the Environment",
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "description": "The time the environment was updated",
            "format": "date-time",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "description": "The time the environment was created",
            "format": "date-time",
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
          "external_resources": {
            "type": "array",
            "description": "Information about known linkages to representations of services outside of FireHydrant.",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ExternalResourceEntity"
            }
          },
          "functionalities": {
            "type": "array",
            "description": "Functionalities related to this environment",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/FunctionalityEntityLite"
            }
          },
          "services": {
            "type": "array",
            "description": "Services related to this environment",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityLite"
            }
          }
        },
        "description": "EnvironmentEntryEntity model"
      },
      "ExternalResourceEntity": {
        "type": "object",
        "properties": {
          "connection_type": {
            "type": "string",
            "nullable": true
          },
          "connection_name": {
            "type": "string",
            "nullable": true
          },
          "connection_full_favicon_url": {
            "type": "string",
            "nullable": true
          },
          "connection_id": {
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
          "name": {
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
      "ChangeEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "UUID of the Change",
            "nullable": true
          },
          "summary": {
            "type": "string",
            "description": "Description of the Change",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "description": "The time the change entry was created",
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
            "properties": {},
            "description": "Arbitrary key/value pairs of labels.",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "Description of the Change",
            "nullable": true
          }
        },
        "description": "ChangeEntity model"
      },
      "ChangeIdentityEntity": {
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
          "value": {
            "type": "string",
            "nullable": true
          },
          "change_id": {
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
          }
        },
        "description": "ChangeIdentityEntity model"
      },
      "ChangeEventEntity": {
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
          "external_id": {
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
          "environments": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/EnvironmentEntryEntity"
            }
          },
          "related_changes": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ChangeEntity"
            }
          },
          "identities": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ChangeIdentityEntity"
            }
          },
          "authors": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/AuthorEntity"
            }
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
          "labels": {
            "type": "object",
            "properties": {},
            "description": "An object of label key and values",
            "nullable": true
          },
          "services": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ServiceEntityLite"
            }
          }
        },
        "description": "ChangeEventEntity model"
      },
      "update_change_event": {
        "type": "object",
        "properties": {
          "summary": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "labels": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
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
          "environments": {
            "type": "array",
            "description": "An array of environment IDs (setting this will overwrite the current environments)",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "services": {
            "type": "array",
            "description": "An array of service IDs (setting this will overwrite the current services)",
            "nullable": true,
            "items": {
              "type": "string"
            }
          },
          "attachments": {
            "type": "array",
            "description": "JSON objects representing attachments, see attachments documentation for the schema",
            "nullable": true,
            "items": {
              "required": [
                "type"
              ],
              "type": "object",
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "link"
                  ]
                }
              }
            }
          }
        },
        "description": "Update a change event"
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