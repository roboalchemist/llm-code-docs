# Source: https://developers.activecampaign.com/reference/get_saved_segment_summaries_by_id.md

# Retrieve a Saved Segment's Summary

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
      "description": "US-based Users",
      "variables": {
        "yourAccountName": {
          "default": "yourAccountName"
        }
      }
    }
  ],
  "security": [
    {
      "Api_Key": []
    }
  ],
  "tags": [
    {
      "name": "Saved Segment Summaries",
      "description": "Saved Segments have a name and are visible on the app/segments page. Saved Segments have Summaries"
    }
  ],
  "paths": {
    "/audiences/{segmentId}": {
      "get": {
        "tags": [
          "Saved Segment Summaries"
        ],
        "summary": "Retrieve a Saved Segment's Summary",
        "operationId": "get_saved_segment_summaries_by_id",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "SegmentId",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "example": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195132"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieve a Saved Segment's Summary",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SegmentSummarySuccessRootDO"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SegmentSummaryErrorRootDO"
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
            "description": "Segment Not Found"
          }
        },
        "deprecated": false
      }
    }
  },
  "components": {
    "securitySchemes": {
      "Api_Key": {
        "type": "apiKey",
        "in": "header",
        "name": "Api-Token"
      }
    },
    "schemas": {
      "ErrorDetailDO": {
        "title": "ErrorDetailDO",
        "type": "object",
        "properties": {
          "code": {
            "type": "string"
          },
          "detail": {
            "type": "string"
          },
          "source": {
            "$ref": "#/components/schemas/ErrorSourceDO"
          },
          "status": {
            "type": "string"
          },
          "title": {
            "type": "string"
          }
        }
      },
      "ErrorSourceDO": {
        "title": "ErrorSourceDO",
        "type": "object",
        "properties": {
          "pointer": {
            "type": "string"
          }
        }
      },
      "SegmentSummarySuccessRootDO": {
        "title": "Segment Summary RootDO",
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SegmentSummaryDataDO"
            }
          }
        }
      },
      "SegmentSummaryErrorRootDO": {
        "title": "Segment Summary RootDO",
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ErrorDetailDO"
            }
          }
        }
      },
      "SegmentSummaryDataDO": {
        "title": "Segment Summary DataDO",
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/SegmentSummaryDO"
          },
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        }
      },
      "SegmentSummaryDO": {
        "title": "Segment SummaryDO",
        "type": "object",
        "properties": {
          "segment_id": {
            "type": "string",
            "readOnly": true,
            "example": "d2c5a14a-771d-4cc0-a126-3513a5201940"
          },
          "category": {
            "type": "string",
            "enum": [
              "audience"
            ],
            "readOnly": true
          },
          "name": {
            "type": "string",
            "description": "Name of the audience segment",
            "readOnly": true
          },
          "counts": {
            "$ref": "#/components/schemas/SegmentSummaryCountsDO"
          },
          "created_date": {
            "type": "string",
            "readOnly": true,
            "format": "date-time",
            "example": "2024-01-30T14:56:02.952Z"
          },
          "updated_date": {
            "type": "string",
            "readOnly": true,
            "format": "date-time",
            "example": "2024-03-12T14:56:02.952Z"
          },
          "last_used_date": {
            "type": "string",
            "readOnly": true,
            "format": "date-time",
            "example": "2025-07-13T14:56:02.952Z"
          }
        }
      },
      "SegmentSummaryCountsDO": {
        "title": "Segment summary counts object containing all counts",
        "type": "object",
        "properties": {
          "last_total": {
            "$ref": "#/components/schemas/SegmentSummaryCountDO"
          },
          "last_active_total": {
            "$ref": "#/components/schemas/SegmentSummaryCountDO"
          }
        }
      },
      "SegmentSummaryCountDO": {
        "title": "Segment counts totals object",
        "type": "object",
        "properties": {
          "count": {
            "type": "number",
            "readOnly": false,
            "example": 1500
          },
          "last_total_updated": {
            "type": "string",
            "readOnly": false,
            "description": "Time that this last total count was requested to be updated",
            "format": "date-time",
            "example": "2024-01-30T14:56:02.952Z"
          },
          "run_id": {
            "type": "string",
            "readOnly": false,
            "example": "744390a5-208e-4c3d-b709-b3c3ea6e5948"
          },
          "run_id_start": {
            "type": "string",
            "readOnly": false,
            "description": "Time that this start time of the last run in UTC",
            "format": "date-time",
            "example": "2024-01-30T15:56:02.952Z"
          },
          "run_id_end": {
            "type": "string",
            "readOnly": false,
            "description": "Time that this end time of the last run in UTC",
            "format": "date-time",
            "example": "2024-01-30T15:56:04.952Z"
          }
        }
      }
    }
  }
}
```