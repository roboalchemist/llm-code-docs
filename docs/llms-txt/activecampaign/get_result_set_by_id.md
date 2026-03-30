# Source: https://developers.activecampaign.com/reference/get_result_set_by_id.md

# Return the result-set for the segment's given runId

If the result-set is not ready yet, the response's `is_ready` attribute will be equal to `false`. The match-all request has errored out if the `is_ready` attribute is false and the `run_id_end` attribute contains a valid timestamp`; when this occurs please try your request again or alert the support team. If either the RunId or the SegmentId have expired or otherwise do not exist, a 404 with error details will be returned.

result-sets are cached and returned in the same `sort` order that's requested. If the `sort` param is not provided it defaults to `id`. You can specify a different `sort` order than the original request, however this will break the result's cache for this `runId` and re-kick-off a new search for results using the same `runId`

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
    "/api/3/segmentMatchAll/{segmentId}/{runId}": {
      "get": {
        "operationId": "get_result_set_by_id",
        "tags": [
          "Match All"
        ],
        "summary": "Return Match All result-set",
        "description": "If the result-set is not ready yet, the response's `is_ready` attribute will be equal to `false`. The match-all request has errored out if the `is_ready` attribute is false and the `run_id_end` attribute contains a valid timestamp`; when this occurs please try your request again or alert the support team. If either the RunId or the SegmentId have expired or otherwise do not exist, a 404 with error details will be returned.\n\nresult-sets are cached and returned in the same `sort` order that's requested. If the `sort` param is not provided it defaults to `id`. You can specify a different `sort` order than the original request, however this will break the result's cache for this `runId` and re-kick-off a new search for results using the same `runId`",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "segmentId",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "runId",
            "in": "path",
            "description": "A run id",
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
            "example": "score15"
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
          }
        ],
        "responses": {
          "200": {
            "description": "Segment match all request started and/or completed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MatchAllResponseRootDO"
                },
                "examples": {
                  "Match All Evaluation Still Running": {
                    "value": {
                      "data": [
                        {
                          "id": "744390a5-208e-4c3d-b709-b3c3ea6e5948-1",
                          "type": "matchAll",
                          "attributes": {
                            "run_id": "744390a5-208e-4c3d-b709-b3c3ea6e5948",
                            "run_id_start": "2020-04-12T23:20:50.523Z",
                            "is_ready": false,
                            "segment_id": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195132",
                            "segment_timestamp": "2020-04-12T23:20:49.5523Z"
                          }
                        }
                      ]
                    }
                  },
                  "Match All Evaluation Complete": {
                    "value": {
                      "data": [
                        {
                          "id": "744390a5-208e-4c3d-b709-b3c3ea6e5948-1",
                          "type": "matchAll",
                          "attributes": {
                            "run_id": "744390a5-208e-4c3d-b709-b3c3ea6e5948",
                            "run_id_start": "2020-04-12T23:20:50.523Z",
                            "run_id_end": "2020-04-12T23:20:53.523Z",
                            "is_ready": true,
                            "matches": [
                              2345,
                              12,
                              234,
                              9837,
                              2317
                            ],
                            "segment_id": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195132",
                            "segment_timestamp": "2020-04-12T23:20:49.5523Z",
                            "page": {
                              "current_page": 1,
                              "last_page": 1,
                              "per_page": 20,
                              "total": 5
                            }
                          }
                        }
                      ]
                    }
                  }
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
            "description": "Segment or RunId not found",
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