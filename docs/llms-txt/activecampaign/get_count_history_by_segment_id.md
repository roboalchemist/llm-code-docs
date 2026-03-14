# Source: https://developers.activecampaign.com/reference/get_count_history_by_segment_id.md

# Retrieve all result counts for the given segment that were ran without an AdditionalCriteria

Up to 50 results will be returned at once. To get the next page, request again with the last result's timestamp formatted as an EPOCH seconds value

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
      "url": "https://{yourAccountName}.api-us1.com",
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
  "paths": {
    "/api/3/segmentsV2/{segmentId}/count-history": {
      "get": {
        "operationId": "get_count_history_by_segment_id",
        "tags": [
          "Count History"
        ],
        "summary": "Retrieve all result counts for the given segment that were ran without an AdditionalCriteria",
        "description": "Up to 50 results will be returned at once. To get the next page, request again with the last result's timestamp formatted as an EPOCH seconds value",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "A segment id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "An array of segment count history results",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SegmentCountHistoryResponseRootDO"
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
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponseRootDO": {
        "title": "ErrorResponseRootDO",
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
      "SegmentCountHistoryResponseRootDO": {
        "title": "SegmentCountHistoryResponseRootDO",
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SegmentCountHistoryDataDO"
            }
          },
          "errors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ErrorDetailDO"
            }
          }
        }
      },
      "SegmentCountHistoryDataDO": {
        "title": "SegmentCountHistoryDataDO",
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/SegmentCountHistoryAttributeDO"
          },
          "id": {
            "type": "string",
            "description": "Epoch timestamp the count was recorded at"
          },
          "type": {
            "type": "string",
            "enum": [
              "SegmentCountHistory"
            ]
          }
        }
      },
      "SegmentCountHistoryAttributeDO": {
        "title": "SegmentCountHistoryAttributeDO",
        "required": [
          "timestamp",
          "segment_id",
          "segment_hash",
          "run_id",
          "result_count"
        ],
        "type": "object",
        "properties": {
          "timestamp": {
            "type": "string",
            "description": "ISO 8601 datetime representing when the when the result count wos recorded",
            "format": "date-time",
            "example": "2020-04-12T23:20:50.523Z"
          },
          "segment_id": {
            "type": "string"
          },
          "segment_hash": {
            "type": "string",
            "description": "A hash of the segment's logic. A changes in the hash over time indicate when the segment was modified",
            "format": "string",
            "example": "97f75f368e9908fd88f4543a9c61a2812915b62e70bf3a7edef01acdeb81b4c5"
          },
          "run_id": {
            "type": "string",
            "description": "A unique value that identifies a segment's evaluation request",
            "example": "52701258-d47e-4e5a-81e5-cff878c69bf8"
          },
          "result_count": {
            "type": "number",
            "description": "The number of matches found for this segment's evaluation request"
          },
          "active_result_count": {
            "type": "number",
            "description": "The number of matches found for this segment's evaluation request AND are subscribed to at least one list"
          },
          "count_updating_with_runid": {
            "type": "string",
            "description": "if the current count is being updated, this is the runid that update is waiting on",
            "example": "52701258-d47e-4e5a-81e5-cff878c69bf8"
          }
        },
        "description": "Object that summarises the results of a segment's evaluation request"
      }
    }
  }
}
```