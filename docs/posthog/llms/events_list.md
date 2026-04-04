# Source: https://posthog.com/docs/open-api-spec/events_list.md

# events_list

## OpenAPI

```json GET /api/projects/{project_id}/events/
{
  "paths": {
    "/api/projects/{project_id}/events/": {
      "get": {
        "operationId": "events_list",
        "description": "\n        This endpoint allows you to list and filter events.\n        It is effectively deprecated and is kept only for backwards compatibility.\n        If you ever ask about it you will be advised to not use it...\n        If you want to ad-hoc list or aggregate events, use the Query endpoint instead.\n        If you want to export all events or many pages of events you should use our CDP/Batch Exports products instead.\n        ",
        "parameters": [
          {
            "in": "query",
            "name": "after",
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Only return events with a timestamp after this time. Default: now() - 24 hours."
          },
          {
            "in": "query",
            "name": "before",
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Only return events with a timestamp before this time. Default: now() + 5 seconds."
          },
          {
            "in": "query",
            "name": "distinct_id",
            "schema": {
              "type": "integer"
            },
            "description": "Filter list by distinct id."
          },
          {
            "in": "query",
            "name": "event",
            "schema": {
              "type": "string"
            },
            "description": "Filter list by event. For example `user sign up` or `$pageview`."
          },
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
            }
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer"
            },
            "description": "The maximum number of results to return"
          },
          {
            "in": "query",
            "name": "offset",
            "schema": {
              "type": "integer"
            },
            "description": "Allows to skip first offset rows. Will fail for value larger than 100000. Read about proper way of paginating: https://posthog.com/docs/api/queries#5-use-timestamp-based-pagination-instead-of-offset",
            "deprecated": true
          },
          {
            "in": "query",
            "name": "person_id",
            "schema": {
              "type": "integer"
            },
            "description": "Filter list by person id."
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          },
          {
            "in": "query",
            "name": "properties",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Property"
              }
            },
            "description": "Filter events by event property, person property, cohort, groups and more."
          },
          {
            "in": "query",
            "name": "select",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "(Experimental) JSON-serialized array of HogQL expressions to return"
          },
          {
            "in": "query",
            "name": "where",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "(Experimental) JSON-serialized array of HogQL expressions that must pass"
          }
        ],
        "tags": [
          "events"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedClickhouseEventList"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedClickhouseEventList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "Property": {
        "type": "object",
        "properties": {
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PropertyGroupOperator"
              }
            ],
            "default": "AND",
            "description": "\n You can use a simplified version:\n```json\n{\n    \"properties\": [\n        {\n            \"key\": \"email\",\n            \"value\": \"x@y.com\",\n            \"operator\": \"exact\",\n            \"type\": \"event\"\n        }\n    ]\n}\n```\n\nOr you can create more complicated queries with AND and OR:\n```json\n{\n    \"properties\": {\n        \"type\": \"AND\",\n        \"values\": [\n            {\n                \"type\": \"OR\",\n                \"values\": [\n                    {\"key\": \"email\", ...},\n                    {\"key\": \"email\", ...}\n                ]\n            },\n            {\n                \"type\": \"AND\",\n                \"values\": [\n                    {\"key\": \"email\", ...},\n                    {\"key\": \"email\", ...}\n                ]\n            }\n        ]\n    ]\n}\n```\n\n\n* `AND` - AND\n* `OR` - OR"
          },
          "values": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PropertyItem"
            }
          }
        },
        "required": [
          "values"
        ]
      },
      "PaginatedClickhouseEventList": {
        "type": "object",
        "properties": {
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ClickhouseEvent"
            }
          }
        }
      },
      "PropertyGroupOperator": {
        "enum": [
          "AND",
          "OR"
        ],
        "type": "string"
      },
      "PropertyItem": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`"
          },
          "value": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              },
              {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    }
                  ]
                }
              }
            ],
            "description": "Value of your filter. For example `test@example.com` or `https://example.com/test/`. Can be an array for an OR query, like `[\"test@example.com\",\"ok@example.com\"]`"
          },
          "operator": {
            "nullable": true,
            "default": "exact",
            "oneOf": [
              {
                "$ref": "#/components/schemas/PropertyItemOperatorEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "type": {
            "default": "event",
            "oneOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              }
            ]
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "ClickhouseEvent": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true
          },
          "properties": {
            "type": "string",
            "readOnly": true
          },
          "event": {
            "type": "string",
            "readOnly": true
          },
          "timestamp": {
            "type": "string",
            "readOnly": true
          },
          "person": {
            "type": "string",
            "readOnly": true
          },
          "elements": {
            "type": "string",
            "readOnly": true
          },
          "elements_chain": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "distinct_id",
          "elements",
          "elements_chain",
          "event",
          "id",
          "person",
          "properties",
          "timestamp"
        ]
      },
      "PropertyItemOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex",
          "gt",
          "lt",
          "gte",
          "lte",
          "is_set",
          "is_not_set",
          "is_date_exact",
          "is_date_after",
          "is_date_before",
          "in",
          "not_in"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex\n* `gt` - gt\n* `lt` - lt\n* `gte` - gte\n* `lte` - lte\n* `is_set` - is_set\n* `is_not_set` - is_not_set\n* `is_date_exact` - is_date_exact\n* `is_date_after` - is_date_after\n* `is_date_before` - is_date_before\n* `in` - in\n* `not_in` - not_in"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      },
      "Type19aEnum": {
        "enum": [
          "event",
          "event_metadata",
          "feature",
          "person",
          "cohort",
          "element",
          "static-cohort",
          "dynamic-cohort",
          "precalculated-cohort",
          "group",
          "recording",
          "log_entry",
          "behavioral",
          "session",
          "hogql",
          "data_warehouse",
          "data_warehouse_person_property",
          "error_tracking_issue",
          "log",
          "log_attribute",
          "log_resource_attribute",
          "revenue_analytics",
          "flag",
          "workflow_variable"
        ],
        "type": "string",
        "description": "* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
      }
    }
  }
}
```
