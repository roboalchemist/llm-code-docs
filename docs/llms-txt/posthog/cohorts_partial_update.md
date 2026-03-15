# Source: https://posthog.com/docs/open-api-spec/cohorts_partial_update.md

# cohorts_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/cohorts/{id}/
{
  "paths": {
    "/api/projects/{project_id}/cohorts/{id}/": {
      "patch": {
        "operationId": "cohorts_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this cohort.",
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
          "core",
          "cohorts"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCohort"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCohort"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCohort"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "cohort:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Cohort"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedCohort": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "maxLength": 1000
          },
          "groups": {},
          "deleted": {
            "type": "boolean"
          },
          "filters": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CohortFilters"
              }
            ],
            "nullable": true
          },
          "query": {
            "nullable": true
          },
          "version": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "pending_version": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_calculating": {
            "type": "boolean",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_calculation": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "errors_calculating": {
            "type": "integer",
            "readOnly": true
          },
          "last_error_message": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_static": {
            "type": "boolean"
          },
          "cohort_type": {
            "nullable": true,
            "description": "Type of cohort based on filter complexity\n\n* `static` - static\n* `person_property` - person_property\n* `behavioral` - behavioral\n* `realtime` - realtime\n* `analytical` - analytical",
            "oneOf": [
              {
                "$ref": "#/components/schemas/CohortTypeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "experiment_set": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "readOnly": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "_create_static_person_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "writeOnly": true,
            "default": [],
            "title": " create static person ids"
          }
        }
      },
      "Cohort": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "maxLength": 1000
          },
          "groups": {},
          "deleted": {
            "type": "boolean"
          },
          "filters": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CohortFilters"
              }
            ],
            "nullable": true
          },
          "query": {
            "nullable": true
          },
          "version": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "pending_version": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_calculating": {
            "type": "boolean",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_calculation": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "errors_calculating": {
            "type": "integer",
            "readOnly": true
          },
          "last_error_message": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "count": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_static": {
            "type": "boolean"
          },
          "cohort_type": {
            "nullable": true,
            "description": "Type of cohort based on filter complexity\n\n* `static` - static\n* `person_property` - person_property\n* `behavioral` - behavioral\n* `realtime` - realtime\n* `analytical` - analytical",
            "oneOf": [
              {
                "$ref": "#/components/schemas/CohortTypeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "experiment_set": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "readOnly": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "_create_static_person_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "writeOnly": true,
            "default": [],
            "title": " create static person ids"
          }
        },
        "required": [
          "count",
          "created_at",
          "created_by",
          "errors_calculating",
          "experiment_set",
          "id",
          "is_calculating",
          "last_calculation",
          "last_error_message",
          "pending_version",
          "version"
        ]
      },
      "CohortFilters": {
        "additionalProperties": false,
        "properties": {
          "properties": {
            "$ref": "#/components/schemas/CohortFilterGroup"
          }
        },
        "required": [
          "properties"
        ],
        "title": "CohortFilters",
        "type": "object"
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
      "CohortTypeEnum": {
        "enum": [
          "static",
          "person_property",
          "behavioral",
          "realtime",
          "analytical"
        ],
        "type": "string",
        "description": "* `static` - static\n* `person_property` - person_property\n* `behavioral` - behavioral\n* `realtime` - realtime\n* `analytical` - analytical"
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
      "CohortFilterGroup": {
        "additionalProperties": false,
        "description": "AND/OR group containing cohort filters. Named to avoid collision with analytics Group model.",
        "properties": {
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PropertyGroupOperator"
              }
            ],
            "title": "Type"
          },
          "values": {
            "items": {
              "discriminator": {
                "mapping": {
                  "AND": "#/components/schemas/CohortFilterGroup",
                  "OR": "#/components/schemas/CohortFilterGroup",
                  "behavioral": "#/components/schemas/BehavioralFilter",
                  "cohort": "#/components/schemas/CohortFilter",
                  "person": "#/components/schemas/PersonFilter"
                },
                "propertyName": "type"
              },
              "oneOf": [
                {
                  "$ref": "#/components/schemas/BehavioralFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortFilter"
                },
                {
                  "$ref": "#/components/schemas/PersonFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortFilterGroup"
                }
              ]
            },
            "title": "Values",
            "type": "array"
          }
        },
        "required": [
          "type",
          "values"
        ],
        "title": "CohortFilterGroup",
        "type": "object"
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
      "PropertyGroupOperator": {
        "enum": [
          "AND",
          "OR"
        ],
        "type": "string"
      },
      "BehavioralFilter": {
        "additionalProperties": false,
        "properties": {
          "bytecode": {
            "default": null,
            "title": "Bytecode",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "bytecode_error": {
            "default": null,
            "title": "Bytecode Error",
            "type": "string",
            "nullable": true
          },
          "conditionHash": {
            "default": null,
            "title": "Conditionhash",
            "type": "string",
            "nullable": true
          },
          "type": {
            "title": "Type",
            "type": "string",
            "enum": [
              "behavioral"
            ]
          },
          "key": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "integer"
              }
            ],
            "title": "Key"
          },
          "value": {
            "title": "Value",
            "type": "string"
          },
          "event_type": {
            "title": "Event Type",
            "type": "string"
          },
          "time_value": {
            "default": null,
            "title": "Time Value",
            "type": "integer",
            "nullable": true
          },
          "time_interval": {
            "default": null,
            "title": "Time Interval",
            "type": "string",
            "nullable": true
          },
          "negation": {
            "default": false,
            "title": "Negation",
            "type": "boolean"
          },
          "operator": {
            "default": null,
            "title": "Operator",
            "type": "string",
            "nullable": true
          },
          "operator_value": {
            "default": null,
            "title": "Operator Value",
            "type": "integer",
            "nullable": true
          },
          "seq_time_interval": {
            "default": null,
            "title": "Seq Time Interval",
            "type": "string",
            "nullable": true
          },
          "seq_time_value": {
            "default": null,
            "title": "Seq Time Value",
            "type": "integer",
            "nullable": true
          },
          "seq_event": {
            "default": null,
            "title": "Seq Event",
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "integer"
              }
            ],
            "nullable": true
          },
          "seq_event_type": {
            "default": null,
            "title": "Seq Event Type",
            "type": "string",
            "nullable": true
          },
          "total_periods": {
            "default": null,
            "title": "Total Periods",
            "type": "integer",
            "nullable": true
          },
          "min_periods": {
            "default": null,
            "title": "Min Periods",
            "type": "integer",
            "nullable": true
          },
          "event_filters": {
            "default": null,
            "title": "Event Filters",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventPropFilter"
                },
                {
                  "$ref": "#/components/schemas/HogQLFilter"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "explicit_datetime": {
            "default": null,
            "title": "Explicit Datetime",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "type",
          "key",
          "value",
          "event_type"
        ],
        "title": "BehavioralFilter",
        "type": "object"
      },
      "CohortFilter": {
        "additionalProperties": false,
        "properties": {
          "bytecode": {
            "default": null,
            "title": "Bytecode",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "bytecode_error": {
            "default": null,
            "title": "Bytecode Error",
            "type": "string",
            "nullable": true
          },
          "conditionHash": {
            "default": null,
            "title": "Conditionhash",
            "type": "string",
            "nullable": true
          },
          "type": {
            "title": "Type",
            "type": "string",
            "enum": [
              "cohort"
            ]
          },
          "key": {
            "title": "Key",
            "type": "string",
            "enum": [
              "id"
            ]
          },
          "value": {
            "title": "Value",
            "type": "integer"
          },
          "negation": {
            "default": false,
            "title": "Negation",
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "key",
          "value"
        ],
        "title": "CohortFilter",
        "type": "object"
      },
      "PersonFilter": {
        "additionalProperties": false,
        "properties": {
          "bytecode": {
            "default": null,
            "title": "Bytecode",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "bytecode_error": {
            "default": null,
            "title": "Bytecode Error",
            "type": "string",
            "nullable": true
          },
          "conditionHash": {
            "default": null,
            "title": "Conditionhash",
            "type": "string",
            "nullable": true
          },
          "type": {
            "title": "Type",
            "type": "string",
            "enum": [
              "person"
            ]
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "operator": {
            "default": null,
            "title": "Operator",
            "type": "string",
            "nullable": true
          },
          "value": {
            "default": null,
            "title": "Value",
            "nullable": true
          },
          "negation": {
            "default": false,
            "title": "Negation",
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "key"
        ],
        "title": "PersonFilter",
        "type": "object"
      },
      "EventPropFilter": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EventPropFilterTypeEnum"
              }
            ],
            "title": "Type"
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "value": {
            "title": "Value"
          },
          "operator": {
            "default": null,
            "title": "Operator",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "type",
          "key",
          "value"
        ],
        "title": "EventPropFilter",
        "type": "object"
      },
      "HogQLFilter": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "title": "Type",
            "type": "string",
            "enum": [
              "hogql"
            ]
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "value": {
            "default": null,
            "title": "Value",
            "nullable": true
          }
        },
        "required": [
          "type",
          "key"
        ],
        "title": "HogQLFilter",
        "type": "object"
      },
      "EventPropFilterTypeEnum": {
        "enum": [
          "event",
          "element"
        ],
        "type": "string"
      }
    }
  }
}
```
