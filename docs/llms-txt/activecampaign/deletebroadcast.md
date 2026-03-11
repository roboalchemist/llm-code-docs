# Source: https://developers.activecampaign.com/reference/deletebroadcast.md

# Delete broadcast message

Performs a soft-delete on the requested message

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
    "/sms/broadcasts/{id}": {
      "delete": {
        "tags": [
          "Broadcasts"
        ],
        "summary": "Delete broadcast message",
        "description": "Performs a soft-delete on the requested message",
        "operationId": "deleteBroadcast",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "Broadcast ID",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Broadcast deleted successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastMessage"
                }
              }
            }
          },
          "403": {
            "description": "Insufficient permissions"
          },
          "404": {
            "description": "Broadcast not found"
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