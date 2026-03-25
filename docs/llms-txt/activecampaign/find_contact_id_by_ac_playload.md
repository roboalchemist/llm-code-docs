# Source: https://developers.activecampaign.com/reference/find_contact_id_by_ac_playload.md

# Finds the Contact Id's that match a Segment and the AdditionalContext payload

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
    "/api/3/segmentMatchSome/{segmentId}": {
      "post": {
        "operationId": "find_contact_id_by_ac_playload",
        "tags": [
          "Match All"
        ],
        "summary": "Create a Match Some Request",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AdditionalCriteriaRootDO"
              }
            }
          },
          "required": true
        },
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
            "example": "-field41"
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
            "description": "If present, response will return instantly without waiting for the results to be ready",
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
            "description": "Segment and contact evaluation completed",
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
            "description": "Unauthorized",
            "content": {}
          },
          "403": {
            "description": "Forbidden",
            "content": {}
          },
          "404": {
            "description": "Segment Not Found",
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
      "AdditionalCriteriaRootDO": {
        "title": "AdditionalCriteriaRootDO",
        "type": "object",
        "properties": {
          "data": {
            "type": "object",
            "$ref": "#/components/schemas/AdditionalCriteriaElementDO"
          }
        }
      },
      "AdditionalCriteriaElementDO": {
        "title": "AdditionalCriteriaElementDO",
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/AdditionalCriteriaDO"
          },
          "type": {
            "type": "string",
            "enum": [
              "additionalCriteria"
            ]
          }
        }
      },
      "AdditionalCriteriaDO": {
        "title": "AdditionalCriteriaDO",
        "type": "object",
        "required": [
          "conditions",
          "group_operator"
        ],
        "properties": {
          "external_id": {
            "type": "string",
            "description": "Value to inject for any FieldDO's that have external set to `True`",
            "example": "1504"
          },
          "limit": {
            "type": "integer",
            "description": "Maximum number of matches in the result-set",
            "minimum": 1,
            "maximum": 10000
          },
          "segment_relationship": {
            "description": "Used to determine how the conditions should be conjoined with the segment conditions. Only required when OR'ing such that: `thisAdditionalCriteriaCondition or theSegmentConditions",
            "type": "string",
            "enum": [
              "or"
            ]
          },
          "conditions": {
            "$ref": "#/components/schemas/ConditionDO"
          },
          "condition_groups": {
            "$ref": "#/components/schemas/ConditionGroupDO"
          },
          "group_operator": {
            "type": "string",
            "enum": [
              "and",
              "or"
            ]
          }
        }
      },
      "AggFieldDO": {
        "description": "Required if the aggregate objects is using the \"most_recent\" operator. This AggFieldDO defines the query logic that the most recent object must satisfy. When this field is present, the ConditionDO.fields attribute is used to specify the requirements prior to selecting the most recent record.",
        "title": "AggFieldDO",
        "required": [
          "data_type",
          "name",
          "operator",
          "value"
        ],
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "description": "Value the `name` field's value should be evaluated against. Sometimes optional based on `operator`"
          },
          "data_type": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "decimal",
              "date",
              "datetime",
              "list",
              ""
            ]
          },
          "name": {
            "type": "string",
            "description": "Field whose value will be evaluated"
          },
          "operator": {
            "type": "string",
            "enum": [
              "=",
              "<",
              ">",
              "<=",
              ">=",
              "!=",
              "contains",
              "does not contain",
              "is",
              "is not",
              "not empty",
              "empty",
              "wildcard match",
              "aggregate of",
              ""
            ]
          }
        }
      },
      "AggregateDO": {
        "title": "AggregateDO",
        "description": "(Optional) AggregateDO allows for requiring a count of discrete matches against the simple (non-aggregate part of a) condition before the entire condition is considered satisfied.",
        "type": "object",
        "example": {},
        "properties": {
          "aggregate_field_operator": {
            "type": "string",
            "description": "Compares the aggregate count of occurrences to the value of the `aggregate_field_value` field. \nDescription of Values:\n* \"\" - Entire AggregateDO object will be ignored\n* \"between\" - Aggregate must be between `aggregate_field_start_value` and `aggregate_field_end_value`\n* \"most_recent\" - Only the most recent record of the given SourceObject type will be looked at.\n* \"all\" - All records of the given SourceObject type will considered.\n* \"\" - aggregation is ignored \"aggregate_most_recent_field\" is required if \"most_recent\" is used. \n* All other values relate directly to only the aggregate_field_value field",
            "default": "",
            "enum": [
              "=",
              "!=",
              "<",
              ">",
              "<=",
              ">=",
              "between",
              "most_recent",
              "all",
              ""
            ]
          },
          "aggregate_field_start_value": {
            "type": "string",
            "example": "4"
          },
          "aggregate_field_end_value": {
            "type": "string",
            "example": "8"
          },
          "aggregate_field_value": {
            "type": "string",
            "example": "2"
          },
          "aggregate_field_time_within_unit": {
            "type": "string",
            "description": "Look for aggregations within the aggregate_field_time_within_value with units equal to this value.\nNot required if `aggregate_field_operator` is empty. If empty when `aggregate_field_operator` is not empty, \"days\" will be assumed.",
            "default": "days",
            "enum": [
              "hours",
              "days",
              "weeks",
              "months",
              ""
            ]
          },
          "aggregate_field_time_within_value": {
            "maximum": 2160,
            "type": "integer",
            "example": 90,
            "description": "Number of aggregate_field_time_within_unit to look for aggregations within. Not required if `aggregate_field_operator` is empty. When `aggregate_field_operator` is not empty, value must be greater than 0 and less than or equal to the maximum value for the unit specified, which are as follows:\n* hours - 2160\n* days - 90\n* weeks - 13\n* months - 3"
          },
          "aggregate_most_recent_field": {
            "$ref": "#/components/schemas/AggFieldDO"
          }
        }
      },
      "ConditionDO": {
        "title": "ConditionDO",
        "required": [
          "object_type",
          "source_system",
          "fields"
        ],
        "type": "object",
        "properties": {
          "field_aggregate": {
            "$ref": "#/components/schemas/AggregateDO"
          },
          "fields": {
            "type": "array",
            "description": "Defines the fields, values, types, and their operators. These act as search criteria for the Segment's condition.",
            "items": {
              "$ref": "#/components/schemas/FieldDO"
            }
          },
          "hash": {
            "type": "string",
            "description": "Sha1 Hash of the Condition's simple logic and its aggregation logic",
            "readOnly": true
          },
          "hash_simple": {
            "type": "string",
            "description": "Sha1 Hash of the Condition's simple logic",
            "readOnly": true
          },
          "id": {
            "type": "string",
            "description": "Numeric unique identifier for the Condition",
            "example": "1"
          },
          "object_type": {
            "type": "string",
            "description": "Name of the Object being evaluated",
            "enum": [
              "tag"
            ]
          },
          "source_system": {
            "type": "string",
            "description": "Namespace of Object being evaluated",
            "enum": [
              "activecampaign"
            ]
          }
        }
      },
      "ConditionGroupDO": {
        "title": "ConditionGroupDO",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "default": "id's should be numeric strings",
            "example": "1"
          },
          "operator": {
            "type": "string",
            "description": "The operator that applies to the conditions in this group",
            "enum": [
              "and",
              "or"
            ],
            "example": "and"
          },
          "values": {
            "type": "array",
            "description": "A list of conditions in the group. All items in the \"values\" array must have the same \"type\"",
            "items": {
              "$ref": "#/components/schemas/ConditionGroupFieldDO"
            }
          }
        }
      },
      "ConditionGroupFieldDO": {
        "title": "ConditionGroupFieldDO",
        "required": [
          "type"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Id of the Condition that belongs to this Condition Group. Conditions must not be in more than one group",
            "example": "1"
          },
          "type": {
            "type": "string",
            "description": "Required. Type of \"condition\" indicates that the \"id\" attribute is a condition id.",
            "enum": [
              "condition"
            ]
          }
        }
      },
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
      "FieldDO": {
        "title": "FieldDO",
        "required": [
          "data_type",
          "name",
          "operator",
          "value"
        ],
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "description": "Value the `name` field's value should be evaluated against. Sometimes optional based on `operator`",
            "example": "14"
          },
          "data_type": {
            "type": "string",
            "enum": [
              "string",
              "number",
              "decimal",
              "date",
              "datetime",
              "list",
              ""
            ],
            "example": "string"
          },
          "name": {
            "type": "string",
            "description": "Field whose value will be evaluated",
            "example": "tagid"
          },
          "operator": {
            "type": "string",
            "description": "All possible operators for evaluating the field's value against the `value` field",
            "enum": [
              "=",
              "<",
              ">",
              "<=",
              ">=",
              "!=",
              "starts with",
              "does not start with",
              "contains",
              "does not contain",
              "is",
              "is not",
              "is in any",
              "missing at least one",
              "empty",
              "not empty",
              "empty|=",
              "empty|<",
              "empty|<=",
              "wildcard match",
              "any",
              "not_previous",
              "between",
              "not between",
              "all",
              "none",
              ""
            ],
            "example": "="
          },
          "external": {
            "type": "boolean",
            "description": "(Optional. Default False) If `external` is present and True, then the value of this FieldDO's \"value\" attribute is ignored and the externalId passed at-query time is used as the value of this FieldDO's \"value\" attribute. This attribute is commonly used to ensure the same pre-determined object satisfies multiple conditions"
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