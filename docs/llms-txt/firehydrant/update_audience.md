# Source: https://docs.firehydrant.com/reference/update_audience.md

# Update audience

Update an existing audience

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
    "/v1/audiences/{audience_id}": {
      "patch": {
        "tags": [
          "Audiences"
        ],
        "summary": "Update audience",
        "description": "Update an existing audience",
        "operationId": "update_audience",
        "parameters": [
          {
            "name": "audience_id",
            "in": "path",
            "description": "Unique identifier of the audience",
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
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the audience (max 255 characters)",
                    "nullable": true
                  },
                  "description": {
                    "type": "string",
                    "description": "Description of the audience (max 4000 characters)",
                    "nullable": true
                  },
                  "default": {
                    "type": "boolean",
                    "description": "Whether this is the default audience",
                    "nullable": true
                  },
                  "active": {
                    "type": "boolean",
                    "description": "Whether the audience is active or discarded",
                    "nullable": true
                  },
                  "details[question]": {
                    "type": "array",
                    "description": "The incident detail question (max 255 characters)",
                    "nullable": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "details[prompt]": {
                    "type": "array",
                    "description": "The prompt to display when collecting this detail",
                    "nullable": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "details[slug]": {
                    "type": "array",
                    "description": "Optional unique identifier for this detail",
                    "nullable": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "details[position]": {
                    "type": "array",
                    "description": "Position of the question in the list (1-based indexing)",
                    "nullable": true,
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Update an existing audience",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Audiences_Entities_AudienceEntity"
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