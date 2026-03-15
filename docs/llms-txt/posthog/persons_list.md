# Source: https://posthog.com/docs/open-api-spec/persons_list.md

# persons_list

## OpenAPI

```json GET /api/projects/{project_id}/persons/
{
  "paths": {
    "/api/projects/{project_id}/persons/": {
      "get": {
        "operationId": "persons_list",
        "description": "This endpoint is meant for reading and deleting persons. To create or update persons, we recommend using the [capture API](https://posthog.com/docs/api/capture), the `$set` and `$unset` [properties](https://posthog.com/docs/product-analytics/user-properties), or one of our SDKs.",
        "parameters": [
          {
            "in": "query",
            "name": "distinct_id",
            "schema": {
              "type": "string"
            },
            "description": "Filter list by distinct id."
          },
          {
            "in": "query",
            "name": "email",
            "schema": {
              "type": "string"
            },
            "description": "Filter persons by email (exact match)",
            "examples": {
              "Email": {
                "value": "test@test.com",
                "summary": "email"
              }
            }
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
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
            "description": "Filter Persons by person properties."
          },
          {
            "in": "query",
            "name": "search",
            "schema": {
              "type": "string"
            },
            "description": "Search persons, either by email (full text search) or distinct_id (exact match)."
          }
        ],
        "tags": [
          "persons",
          "persons"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "person:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedPersonList"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedPersonList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "persons"
        ]
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
      "PaginatedPersonList": {
        "type": "object",
        "properties": {
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "https://app.posthog.com/api/projects/{project_id}/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "https://app.posthog.com/api/projects/{project_id}/accounts/?offset=400&limit=100"
          },
          "count": {
            "type": "integer",
            "example": 400
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Person"
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
      "Person": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "distinct_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "properties": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "last_seen_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "distinct_ids",
          "id",
          "last_seen_at",
          "name",
          "uuid"
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
