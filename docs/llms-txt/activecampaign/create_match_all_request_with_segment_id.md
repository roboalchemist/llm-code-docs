# Source: https://developers.activecampaign.com/reference/create_match_all_request_with_segment_id.md

# Create a Match ALL Request

A new match-all request will be initiated. If results are not ready within 4 seconds, a response that lacks a result-set will be returned and the response's `is_ready` attribute will be equal to `false`. Use the returned segmentId and runId to poll and check back later to see if the result-set is ready

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
  "tags": [
    {
      "name": "Match All",
      "description": "Return all Contact id's that match the given Segment and provided Additional Criteria"
    }
  ],
  "paths": {
    "/api/3/segmentMatchAll/{segmentId}": {
      "get": {
        "operationId": "create_match_all_request_with_segment_id",
        "tags": [
          "Match All"
        ],
        "summary": "Create a Match All Request",
        "description": "A new match-all request will be initiated. If results are not ready within 4 seconds, a response that lacks a result-set will be returned and the response's `is_ready` attribute will be equal to `false`. Use the returned segmentId and runId to poll and check back later to see if the result-set is ready",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "A segment id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "Comma delimited list of fields for which to sort the results. Optionally prepended with a dash sign to indicate descending order. Allowed fields: id, email, phone, first_name, last_name, full_name, cdate, udate, account_name, score, score<score-id>. The score<score-id> option will sort off of the value of a particular score.\n\nExamples: \"email\", \"-phone\", \"score2\", \"last_name,-first_name\"",
            "required": false,
            "schema": {
              "type": "string",
              "default": "id",
              "enum": [
                "id",
                "-id",
                "email",
                "-email",
                "phone",
                "-phone",
                "first_name",
                "-first_name",
                "last_name",
                "-last_name",
                "full_name",
                "-full_name",
                "cdate",
                "-cdate",
                "udate",
                "-udate",
                "account_name",
                "-account_name",
                "score",
                "-score",
                "score<score-id>",
                "-score<score-id>",
                "field<custom-field-id>",
                "-field<custom-field-id>"
              ]
            },
            "example": "-field9"
          },
          {
            "name": "page",
            "in": "query",
            "description": "Page Number",
            "required": false,
            "schema": {
              "type": "integer",
              "default": "1"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "description": "Page Size. Maximum: 10,000",
            "required": false,
            "schema": {
              "type": "integer",
              "default": "20",
              "maximum": 10000
            }
          },
          {
            "name": "instant",
            "in": "query",
            "description": "If present, API will return instantly with a runId without waiting for up to 4 seconds for the results to be ready. Useful if you want to kick off a match-all request but don't need the results immediately",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                ""
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Segment match all request started and/or completed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MatchAllResponseRootDO"
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
            "description": "Segment not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponseRootDO"
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
      "MatchAllResponseRootDO": {
        "title": "MatchAllResponseRootDO",
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MatchAllDataDO"
            }
          }
        }
      },
      "MatchAllDataDO": {
        "title": "MatchAllDataDO",
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/MatchAllAttributeDO"
          },
          "id": {
            "type": "string",
            "description": "ID of the specific request"
          },
          "type": {
            "type": "string",
            "enum": [
              "matchAll"
            ]
          }
        }
      },
      "MatchAllAttributeDO": {
        "title": "MatchAllAttributeDO",
        "required": [
          "is_ready",
          "run_id",
          "run_id_start",
          "segment_id"
        ],
        "type": "object",
        "properties": {
          "run_id": {
            "type": "string",
            "description": "The runId of the match-all request. Use this value to poll for results or lookup results at a later point in time. RunId results can be viewed for 90 days"
          },
          "run_id_start": {
            "type": "string",
            "description": "ISO 8601 datetime representing when the match-all request was made",
            "format": "date-time",
            "example": "2020-04-12T23:20:50.523Z"
          },
          "run_id_end": {
            "type": "string",
            "description": "ISO 8601 datetime representing when the match-all result-set was ready. If this date-time is present and `is_ready` is `false`, then the match-all request has ran into an error and will not finish; please try making a new match-all request or contacting support.",
            "format": "date-time",
            "example": "2020-04-12T23:20:50.523Z"
          },
          "is_ready": {
            "type": "boolean",
            "description": "True if the result-set is ready. False otherwise"
          },
          "matches": {
            "maxItems": 10000,
            "type": "array",
            "description": "One page of the result-set of Contact Id's",
            "items": {
              "type": "integer"
            }
          },
          "segment_id": {
            "type": "string"
          },
          "segment_timestamp": {
            "type": "string",
            "description": "ISO 8601 datetime representing when segment was last created or modified. This timestamp can be used to look up the definition of the Segment at the time of the match-all request",
            "format": "date-time",
            "example": "2020-04-12T23:20:50.523Z"
          },
          "page": {
            "$ref": "#/components/schemas/PageDO"
          }
        },
        "description": "Object representing the status and result of the match all request. Note that page number and total count information refer to the results in the \"matches\" attribute."
      },
      "PageDO": {
        "title": "PageDO",
        "type": "object",
        "properties": {
          "current_page": {
            "type": "integer",
            "format": "int32"
          },
          "last_page": {
            "type": "integer",
            "description": "Last page of results",
            "format": "int32"
          },
          "per_page": {
            "type": "integer",
            "format": "int32"
          },
          "total": {
            "type": "integer",
            "description": "The total number of matches",
            "format": "int32"
          }
        }
      }
    }
  }
}
```