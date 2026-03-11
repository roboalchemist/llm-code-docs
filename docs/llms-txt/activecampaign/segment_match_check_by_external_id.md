# Source: https://developers.activecampaign.com/reference/segment_match_check_by_external_id.md

# Check to see if a Contact matches a Segment using the given externalId

# OpenAPI definition

```json
{
  "openapi": "3.1.1",
  "info": {
    "title": "Segments",
    "description": "API for managing segments in your ActiveCampaign instance",
    "version": "2.0.0",
    "contact": {
      "name": "ActiveCampaign Support",
      "url": "https://www.activecampaign.com"
    }
  },
  "servers": [
    {
      "url": "https://{yourAccountName}.api-us1.com/api/3",
      "variables": {
        "yourAccountName": {
          "default": "yourAccountName",
          "description": "Your ActiveCampaign account name"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Match One",
      "description": "Evaluate Contact Id against the provided SegmentId. Returns `true` if Contact matches the given Segment"
    }
  ],
  "paths": {
    "/segmentMatch/{segmentId}/{contactId}/{externalId}": {
      "get": {
        "operationId": "segment_match_check_by_external_id",
        "tags": [
          "Match One"
        ],
        "summary": "Check to see if a Contact matches a Segment using the given externalId",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "SegmentId",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "contactId",
            "in": "path",
            "description": "ContactId",
            "required": true,
            "schema": {
              "type": "number"
            }
          },
          {
            "name": "externalId",
            "in": "path",
            "description": "externalId",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Segment, Contact & ExternalId evaluation completed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MatchResponseRootDO"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseRootDO"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseRootDO"
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorDetail": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "detail": {
            "type": "string"
          },
          "code": {
            "type": "string"
          }
        },
        "title": "ErrorDetail"
      },
      "MatchAttributeDO": {
        "type": "object",
        "properties": {
          "created_timestamp": {
            "type": "string",
            "format": "date-time",
            "example": "2025-04-12T23:20:50.523Z"
          },
          "entity_id": {
            "type": "string",
            "description": "The ContactId that was evaluated against the Segment",
            "example": "132"
          },
          "match": {
            "type": "boolean",
            "description": "True if the Contact matches the Segment. False otherwise"
          },
          "segment_id": {
            "type": "string",
            "description": "The SegmentId that the Contact was evaluated against",
            "example": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195"
          },
          "segment_timestamp": {
            "type": "string",
            "format": "date-time",
            "example": "2025-04-12T23:20:50.523Z"
          }
        },
        "title": "MatchAttributeDO"
      },
      "MatchDataDO": {
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/MatchAttributeDO"
          },
          "id": {
            "type": "string",
            "description": "Id that identifies the request. Consists of SegmentId + ContactId",
            "example": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195132"
          },
          "type": {
            "type": "string",
            "enum": [
              "match"
            ]
          }
        },
        "title": "MatchDataDO"
      },
      "MatchResponseRootDO": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MatchDataDO"
            }
          }
        },
        "title": "MatchResponseRootDO"
      },
      "ErrorResponseRootDO": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ErrorDetail"
            }
          }
        },
        "title": "ErrorResponseRootDO"
      }
    },
    "securitySchemes": {
      "Api_Key": {
        "type": "apiKey",
        "in": "header",
        "name": "Api-Token"
      }
    }
  },
  "security": [
    {
      "Api_Key": []
    }
  ]
}
```