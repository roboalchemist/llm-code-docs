# Source: https://posthog.com/docs/open-api-spec/actions_update.md

# actions_update

## OpenAPI

```json PUT /api/projects/{project_id}/actions/{id}/
{
  "paths": {
    "/api/projects/{project_id}/actions/{id}/": {
      "put": {
        "operationId": "actions_update",
        "parameters": [
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this action.",
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "actions",
          "actions"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Action"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Action"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Action"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "action:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Action"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/Action"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "actions"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Action": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Name of the action (must be unique within the project).",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "description": "Human-readable description of what this action represents."
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "post_to_slack": {
            "type": "boolean",
            "description": "Whether to post a notification to Slack when this action is triggered."
          },
          "slack_message_format": {
            "type": "string",
            "description": "Custom Slack message format. Supports templates with event properties.",
            "maxLength": 1200
          },
          "steps": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ActionStepJSON"
            },
            "description": "Action steps defining trigger conditions. Each step matches events by name, properties, URL, or element attributes. Multiple steps are OR-ed together."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "deleted": {
            "type": "boolean"
          },
          "is_calculating": {
            "type": "boolean",
            "readOnly": true
          },
          "last_calculated_at": {
            "type": "string",
            "format": "date-time"
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          },
          "is_action": {
            "type": "boolean",
            "readOnly": true,
            "default": true
          },
          "bytecode_error": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "pinned_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "ISO 8601 timestamp when the action was pinned, or null if not pinned. Set any value to pin, null to unpin."
          },
          "creation_context": {
            "type": "string",
            "readOnly": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          }
        },
        "required": [
          "bytecode_error",
          "created_at",
          "created_by",
          "creation_context",
          "id",
          "is_action",
          "is_calculating",
          "team_id",
          "user_access_level"
        ]
      },
      "ActionStepJSON": {
        "type": "object",
        "properties": {
          "event": {
            "type": "string",
            "nullable": true,
            "description": "Event name to match (e.g. '$pageview', '$autocapture', or a custom event name)."
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ActionStepPropertyFilter"
            },
            "nullable": true,
            "description": "Event or person property filters. Each item should have 'key' (string), 'value' (string, number, boolean, or array), optional 'operator' (exact, is_not, is_set, is_not_set, icontains, not_icontains, regex, not_regex, gt, gte, lt, lte), and optional 'type' (event, person)."
          },
          "selector": {
            "type": "string",
            "nullable": true,
            "description": "CSS selector to match the target element (e.g. 'div > button.cta')."
          },
          "selector_regex": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "tag_name": {
            "type": "string",
            "nullable": true,
            "description": "HTML tag name to match (e.g. \"button\", \"a\", \"input\")."
          },
          "text": {
            "type": "string",
            "nullable": true,
            "description": "Element text content to match."
          },
          "text_matching": {
            "nullable": true,
            "description": "How to match the text value. Defaults to exact.\n\n* `contains` - contains\n* `regex` - regex\n* `exact` - exact",
            "oneOf": [
              {
                "$ref": "#/components/schemas/UrlMatchingEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "href": {
            "type": "string",
            "nullable": true,
            "description": "Link href attribute to match."
          },
          "href_matching": {
            "nullable": true,
            "description": "How to match the href value. Defaults to exact.\n\n* `contains` - contains\n* `regex` - regex\n* `exact` - exact",
            "oneOf": [
              {
                "$ref": "#/components/schemas/UrlMatchingEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "url": {
            "type": "string",
            "nullable": true,
            "description": "Page URL to match."
          },
          "url_matching": {
            "nullable": true,
            "description": "How to match the URL value. Defaults to contains.\n\n* `contains` - contains\n* `regex` - regex\n* `exact` - exact",
            "oneOf": [
              {
                "$ref": "#/components/schemas/UrlMatchingEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "selector_regex"
        ]
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "ActionStepPropertyFilter": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/StringPropertyFilter"
          },
          {
            "$ref": "#/components/schemas/NumericPropertyFilter"
          },
          {
            "$ref": "#/components/schemas/ArrayPropertyFilter"
          },
          {
            "$ref": "#/components/schemas/DatePropertyFilter"
          },
          {
            "$ref": "#/components/schemas/ExistencePropertyFilter"
          }
        ]
      },
      "UrlMatchingEnum": {
        "enum": [
          "contains",
          "regex",
          "exact"
        ],
        "type": "string",
        "description": "* `contains` - contains\n* `regex` - regex\n* `exact` - exact"
      },
      "NullEnum": {
        "enum": [
          null
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "StringPropertyFilter": {
        "type": "object",
        "description": "Matches string values with text-oriented operators.",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              }
            ],
            "default": "event",
            "description": "Property type (event, person, session, etc.).\n\n* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
          },
          "value": {
            "type": "string",
            "description": "String value to match against."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/StringPropertyFilterOperatorEnum"
              }
            ],
            "default": "exact",
            "description": "String comparison operator.\n\n* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "NumericPropertyFilter": {
        "type": "object",
        "description": "Matches numeric values with comparison operators.",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              }
            ],
            "default": "event",
            "description": "Property type (event, person, session, etc.).\n\n* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
          },
          "value": {
            "type": "number",
            "format": "double",
            "description": "Numeric value to compare against."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/NumericPropertyFilterOperatorEnum"
              }
            ],
            "default": "exact",
            "description": "Numeric comparison operator.\n\n* `exact` - exact\n* `is_not` - is_not\n* `gt` - gt\n* `lt` - lt\n* `gte` - gte\n* `lte` - lte"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "ArrayPropertyFilter": {
        "type": "object",
        "description": "Matches against a list of values (OR semantics for exact/is_not, set membership for in/not_in).",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              }
            ],
            "default": "event",
            "description": "Property type (event, person, session, etc.).\n\n* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
          },
          "value": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of values to match. For example `[\"test@example.com\", \"ok@example.com\"]`."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ArrayPropertyFilterOperatorEnum"
              }
            ],
            "default": "exact",
            "description": "Array comparison operator.\n\n* `exact` - exact\n* `is_not` - is_not\n* `in` - in\n* `not_in` - not_in"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "DatePropertyFilter": {
        "type": "object",
        "description": "Matches date/datetime values with date-specific operators.",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              }
            ],
            "default": "event",
            "description": "Property type (event, person, session, etc.).\n\n* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
          },
          "value": {
            "type": "string",
            "description": "Date or datetime string in ISO 8601 format (e.g. '2024-01-15' or '2024-01-15T10:30:00Z')."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DatePropertyFilterOperatorEnum"
              }
            ],
            "default": "is_date_exact",
            "description": "Date comparison operator.\n\n* `is_date_exact` - is_date_exact\n* `is_date_before` - is_date_before\n* `is_date_after` - is_date_after"
          }
        },
        "required": [
          "key",
          "value"
        ]
      },
      "ExistencePropertyFilter": {
        "type": "object",
        "description": "Checks whether a property is set or not, without comparing values.",
        "properties": {
          "key": {
            "type": "string",
            "description": "Key of the property you're filtering on. For example `email` or `$current_url`."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type19aEnum"
              }
            ],
            "default": "event",
            "description": "Property type (event, person, session, etc.).\n\n* `event` - event\n* `event_metadata` - event_metadata\n* `feature` - feature\n* `person` - person\n* `cohort` - cohort\n* `element` - element\n* `static-cohort` - static-cohort\n* `dynamic-cohort` - dynamic-cohort\n* `precalculated-cohort` - precalculated-cohort\n* `group` - group\n* `recording` - recording\n* `log_entry` - log_entry\n* `behavioral` - behavioral\n* `session` - session\n* `hogql` - hogql\n* `data_warehouse` - data_warehouse\n* `data_warehouse_person_property` - data_warehouse_person_property\n* `error_tracking_issue` - error_tracking_issue\n* `log` - log\n* `log_attribute` - log_attribute\n* `log_resource_attribute` - log_resource_attribute\n* `revenue_analytics` - revenue_analytics\n* `flag` - flag\n* `workflow_variable` - workflow_variable"
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Operator3e6Enum"
              }
            ],
            "description": "Existence check operator.\n\n* `is_set` - is_set\n* `is_not_set` - is_not_set"
          }
        },
        "required": [
          "key",
          "operator"
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
      },
      "StringPropertyFilterOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex"
      },
      "NumericPropertyFilterOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "gt",
          "lt",
          "gte",
          "lte"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `gt` - gt\n* `lt` - lt\n* `gte` - gte\n* `lte` - lte"
      },
      "ArrayPropertyFilterOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "in",
          "not_in"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `in` - in\n* `not_in` - not_in"
      },
      "DatePropertyFilterOperatorEnum": {
        "enum": [
          "is_date_exact",
          "is_date_before",
          "is_date_after"
        ],
        "type": "string",
        "description": "* `is_date_exact` - is_date_exact\n* `is_date_before` - is_date_before\n* `is_date_after` - is_date_after"
      },
      "Operator3e6Enum": {
        "enum": [
          "is_set",
          "is_not_set"
        ],
        "type": "string",
        "description": "* `is_set` - is_set\n* `is_not_set` - is_not_set"
      }
    }
  }
}
```
