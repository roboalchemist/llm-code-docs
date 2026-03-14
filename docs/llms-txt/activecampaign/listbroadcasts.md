# Source: https://developers.activecampaign.com/reference/listbroadcasts.md

# Get all broadcast messages

Gets a paged list of all of a customer's broadcast messages with optional filtering

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "SMS Broadcast API",
    "description": "API for managing SMS broadcasts, lists, metrics, and AI-powered content generation in ActiveCampaign",
    "version": "3.0.0",
    "contact": {
      "name": "ActiveCampaign Support",
      "url": "https://www.activecampaign.com"
    }
  },
  "servers": [
    {
      "url": "https://{yourAccountName}.api-us1.com/api/3",
      "description": "US-based Users",
      "variables": {
        "yourAccountName": {
          "default": "yourAccountName"
        }
      }
    }
  ],
  "paths": {
    "/sms/broadcasts": {
      "get": {
        "tags": [
          "Broadcasts"
        ],
        "summary": "Get all broadcast messages",
        "description": "Gets a paged list of all of a customer's broadcast messages with optional filtering",
        "operationId": "listBroadcasts",
        "parameters": [
          {
            "name": "offset",
            "in": "query",
            "description": "Offset for pagination",
            "schema": {
              "type": "integer",
              "default": 0
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of items to return",
            "schema": {
              "type": "integer",
              "default": 20
            }
          },
          {
            "name": "filters[name]",
            "in": "query",
            "description": "Filter by broadcast name",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[status]",
            "in": "query",
            "description": "Filter by broadcast status",
            "schema": {
              "type": "string",
              "enum": [
                "draft",
                "scheduled",
                "sent",
                "pending_review",
                "sending"
              ]
            }
          },
          {
            "name": "filters[type]",
            "in": "query",
            "description": "Filter by broadcast type (future feature)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "orders[field]",
            "in": "query",
            "description": "Order results by field (ASC or DESC)",
            "schema": {
              "type": "string",
              "enum": [
                "ASC",
                "DESC"
              ]
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "description": "Filter by start date (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "Filter by end date (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastListResponse"
                }
              }
            }
          },
          "403": {
            "description": "Insufficient permissions"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BroadcastMessage": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the broadcast"
          },
          "name": {
            "type": "string",
            "description": "Name of the broadcast"
          },
          "address_id": {
            "type": "integer",
            "nullable": true,
            "description": "ID used to get sender name"
          },
          "body": {
            "type": "string",
            "description": "SMS message content"
          },
          "media_urls": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uri"
            },
            "description": "Media URLs for MMS messages"
          },
          "preview_url": {
            "type": "string",
            "format": "uri",
            "description": "URL for message preview"
          },
          "shorten_track_links_enabled": {
            "type": "boolean",
            "description": "Whether link shortening is enabled"
          },
          "status": {
            "type": "string",
            "enum": [
              "draft",
              "scheduled",
              "sent",
              "pending_review",
              "sending"
            ],
            "description": "Current status of the broadcast"
          },
          "sent_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "Date when broadcast was sent"
          },
          "scheduled_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "Scheduled send date (UTC)"
          },
          "custom_run_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "custom run id generated from segmentMatchSome endpoint"
          },
          "custom_segment_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "custom segment id generated from segmentsV2 endpoint and passing in a valid audience"
          },
          "scheduled_by": {
            "type": "integer",
            "nullable": true,
            "description": "User ID who scheduled the broadcast"
          },
          "sent_to_count": {
            "type": "integer",
            "nullable": true,
            "description": "Number of recipients"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Creation timestamp"
          },
          "created_by": {
            "type": "integer",
            "description": "User ID who created the broadcast"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "Last update timestamp"
          },
          "updated_by": {
            "type": "integer",
            "description": "User ID who last updated"
          },
          "deleted_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "Deletion timestamp (for soft deletes)"
          },
          "sift_approved": {
            "type": "integer",
            "description": "Sift approval status"
          },
          "arc_approved": {
            "type": "integer",
            "description": "ARC approval status"
          },
          "quiet_hours_enabled": {
            "type": "integer",
            "nullable": true,
            "description": "Whether quiet hours are enabled"
          },
          "list_ids": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "Associated list IDs"
          },
          "segment_id": {
            "type": "string",
            "nullable": true,
            "description": "Segment ID (can be UUID or integer string)"
          },
          "label_ids": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "nullable": true,
            "description": "Associated label IDs"
          }
        }
      },
      "BroadcastListResponse": {
        "type": "object",
        "properties": {
          "broadcasts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BroadcastMessage"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "total": {
                "type": "integer",
                "description": "Total number of broadcasts"
              }
            }
          }
        }
      }
    },
    "securitySchemes": {
      "ApiToken": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "description": "Your ActiveCampaign API token"
      }
    }
  },
  "security": [
    {
      "ApiToken": []
    }
  ]
}
```