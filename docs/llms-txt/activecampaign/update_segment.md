# Source: https://developers.activecampaign.com/reference/update_segment.md

# Update a Segment

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
      "name": "Segments",
      "description": "Segment JSON structure is extremely flexible. Only segments that are supported by the segment-builder are guaranteed to work as expected. Specific Conditions types only support a subset of FieldDO and AggregateDO options. Please refer to your account's /app/segments/segment-builder page to verify what Segment JSON configurations are possible."
    }
  ],
  "paths": {
    "/segmentsV2/{segmentId}": {
      "put": {
        "tags": [
          "Segments"
        ],
        "summary": "Update a Segment",
        "operationId": "update_segment",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "description": "SegmentId",
            "required": true,
            "style": "simple",
            "explode": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "$ref": "#/components/requestBodies/RootDO"
        },
        "responses": {
          "200": {
            "description": "Successfully updated the Segment",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RootSuccessDO"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Payload did not pass validation"
          },
          "401": {
            "description": "Unauthorized"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found. For a GET, DELETE, or PUT request, if a body is present, no segments were found. If a body is not present, the path was not found"
          }
        },
        "deprecated": false
      }
    }
  },
  "components": {
    "requestBodies": {
      "RootDO": {
        "description": "Segment Request Document Object",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/RootSuccessDO"
            }
          }
        },
        "required": true
      }
    },
    "securitySchemes": {
      "Api_Key": {
        "type": "apiKey",
        "in": "header",
        "name": "Api-Token"
      }
    },
    "schemas": {
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
      "SegmentDataDO": {
        "title": "SegmentDataDO",
        "type": "object",
        "properties": {
          "attributes": {
            "$ref": "#/components/schemas/SegmentDO"
          },
          "id": {
            "type": "string",
            "example": "1ab85f0e-3b5c-4a35-bc07-242c68a7d195",
            "readOnly": true
          },
          "type": {
            "type": "string",
            "readOnly": true,
            "example": "Segment.v2"
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
            "description": "(Optional. Default False) If `external` is present and true, then the value of this FieldDO's \"value\" attribute is ignored and the externalId passed at-query time is used as the value of this FieldDO's \"value\" attribute. Segments with an `\"external\": true` value will not evaluate without and external-id defined at request time. This attribute is commonly used to ensure the same pre-determined object satisfies multiple conditions",
            "default": false
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
      "ConditionGroupDO": {
        "title": "ConditionGroupDO",
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "id's should be numeric strings",
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
      "RootSuccessDO": {
        "title": "RootSuccessDO",
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SegmentDataDO"
            }
          }
        }
      },
      "SegmentDO": {
        "title": "SegmentDO",
        "type": "object",
        "required": [
          "segment_conditions",
          "segment_condition_groups",
          "segment_condition_group_operator"
        ],
        "properties": {
          "created_date": {
            "type": "string",
            "format": "date-time",
            "example": "2024-01-30T14:56:02.952Z"
          },
          "meta": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "segment_condition_group_operator": {
            "type": "string",
            "description": "The operator that combines the condition groups",
            "enum": [
              "and",
              "or"
            ],
            "example": "and"
          },
          "segment_condition_groups": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConditionGroupDO"
            }
          },
          "segment_conditions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConditionDO"
            }
          },
          "segment_hash": {
            "type": "string",
            "readOnly": true
          },
          "segment_id": {
            "type": "string",
            "readOnly": true
          },
          "user_id": {
            "type": "string",
            "description": "The user that created this version of the segment",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "description": "Optional. Segments with this attribute are Saved Segments and will show up on the /app/audiences page. Value must be unique. Can be defined at creation time, but cannot be added to a Segment during an update operation"
          },
          "description": {
            "type": "string",
            "maxLength": 1000,
            "description": "Optional for Saved Segments"
          },
          "category": {
            "type": "string",
            "enum": [
              "AUDIENCE"
            ],
            "readOnly": true
          }
        }
      }
    }
  }
}
```