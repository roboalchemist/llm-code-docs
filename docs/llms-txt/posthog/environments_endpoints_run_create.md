# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_run_create.md

# environments_endpoints_run_create

## OpenAPI

```json POST /api/environments/{environment_id}/endpoints/{name}/run/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/run/": {
      "post": {
        "operationId": "environments_endpoints_run_create",
        "description": "Execute endpoint with optional materialization. Supports version parameter, runs latest version if not set.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
            },
            "required": true
          }
        ],
        "tags": [
          "endpoints",
          "endpoints"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRunRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRunRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRunRequest"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "EndpointRunRequest": {
        "additionalProperties": false,
        "properties": {
          "client_query_id": {
            "default": null,
            "description": "Client provided query ID. Can be used to retrieve the status or cancel the query.",
            "title": "Client Query Id",
            "type": "string",
            "nullable": true
          },
          "debug": {
            "default": false,
            "description": "Whether to include debug information (such as the executed HogQL) in the response.",
            "title": "Debug",
            "type": "boolean",
            "nullable": true
          },
          "filters_override": {
            "default": null,
            "$ref": "#/components/schemas/DashboardFilter",
            "nullable": true
          },
          "limit": {
            "default": null,
            "description": "Maximum number of results to return. If not provided, returns all results.",
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "offset": {
            "default": null,
            "description": "Number of results to skip. Must be used together with limit. Only supported for HogQL endpoints.",
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "refresh": {
            "default": "cache",
            "$ref": "#/components/schemas/EndpointRefreshMode",
            "nullable": true
          },
          "variables": {
            "default": null,
            "description": "Variables to parameterize the endpoint query. The key is the variable name and the value is the variable value.\n\nFor HogQL endpoints:   Keys must match a variable `code_name` defined in the query (referenced as `{variables.code_name}`).   Example: `{\"event_name\": \"$pageview\"}`\n\nFor non-materialized insight endpoints (e.g. TrendsQuery):   - `date_from` and `date_to` are built-in variables that filter the date range.     Example: `{\"date_from\": \"2024-01-01\", \"date_to\": \"2024-01-31\"}`\n\nFor materialized insight endpoints:   - Use the breakdown property name as the key to filter by breakdown value.     Example: `{\"$browser\": \"Chrome\"}`   - `date_from`/`date_to` are not supported on materialized insight endpoints.\n\nUnknown variable names will return a 400 error.",
            "title": "Variables",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "Specific endpoint version to execute. If not provided, the latest version is used.",
            "title": "Version",
            "type": "integer",
            "nullable": true
          }
        },
        "title": "EndpointRunRequest",
        "type": "object"
      },
      "DashboardFilter": {
        "additionalProperties": false,
        "properties": {
          "breakdown_filter": {
            "default": null,
            "$ref": "#/components/schemas/BreakdownFilter",
            "nullable": true
          },
          "date_from": {
            "default": null,
            "title": "Date From",
            "type": "string",
            "nullable": true
          },
          "date_to": {
            "default": null,
            "title": "Date To",
            "type": "string",
            "nullable": true
          },
          "explicitDate": {
            "default": null,
            "title": "Explicitdate",
            "type": "boolean",
            "nullable": true
          },
          "properties": {
            "default": null,
            "title": "Properties",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/PersonPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/ElementPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/EventMetadataPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/SessionPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/RecordingPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/LogEntryPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/GroupPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/FeaturePropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/FlagPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/HogQLPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/EmptyPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/DataWarehousePropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/DataWarehousePersonPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/ErrorTrackingIssueFilter"
                },
                {
                  "$ref": "#/components/schemas/LogPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
                }
              ]
            },
            "type": "array",
            "nullable": true
          }
        },
        "title": "DashboardFilter",
        "type": "object"
      },
      "EndpointRefreshMode": {
        "enum": [
          "cache",
          "force",
          "direct"
        ],
        "title": "EndpointRefreshMode",
        "type": "string"
      },
      "BreakdownFilter": {
        "additionalProperties": false,
        "properties": {
          "breakdown": {
            "default": null,
            "title": "Breakdown",
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "integer"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "integer"
              }
            ],
            "nullable": true
          },
          "breakdown_group_type_index": {
            "default": null,
            "title": "Breakdown Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "breakdown_hide_other_aggregation": {
            "default": null,
            "title": "Breakdown Hide Other Aggregation",
            "type": "boolean",
            "nullable": true
          },
          "breakdown_histogram_bin_count": {
            "default": null,
            "title": "Breakdown Histogram Bin Count",
            "type": "integer",
            "nullable": true
          },
          "breakdown_limit": {
            "default": null,
            "title": "Breakdown Limit",
            "type": "integer",
            "nullable": true
          },
          "breakdown_normalize_url": {
            "default": null,
            "title": "Breakdown Normalize Url",
            "type": "boolean",
            "nullable": true
          },
          "breakdown_path_cleaning": {
            "default": null,
            "title": "Breakdown Path Cleaning",
            "type": "boolean",
            "nullable": true
          },
          "breakdown_type": {
            "default": "event",
            "$ref": "#/components/schemas/BreakdownType",
            "nullable": true
          },
          "breakdowns": {
            "default": null,
            "title": "Breakdowns",
            "items": {
              "$ref": "#/components/schemas/Breakdown"
            },
            "maxItems": 3,
            "type": "array",
            "nullable": true
          }
        },
        "title": "BreakdownFilter",
        "type": "object"
      },
      "EventPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "default": "exact",
            "$ref": "#/components/schemas/PropertyOperator",
            "nullable": true
          },
          "type": {
            "default": "event",
            "description": "Event properties",
            "title": "Type",
            "type": "string",
            "enum": [
              "event"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key"
        ],
        "title": "EventPropertyFilter",
        "type": "object"
      },
      "PersonPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "person",
            "description": "Person properties",
            "title": "Type",
            "type": "string",
            "enum": [
              "person"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "PersonPropertyFilter",
        "type": "object"
      },
      "ElementPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "$ref": "#/components/schemas/Key"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "element",
            "title": "Type",
            "type": "string",
            "enum": [
              "element"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "ElementPropertyFilter",
        "type": "object"
      },
      "EventMetadataPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "event_metadata",
            "title": "Type",
            "type": "string",
            "enum": [
              "event_metadata"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "EventMetadataPropertyFilter",
        "type": "object"
      },
      "SessionPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "session",
            "title": "Type",
            "type": "string",
            "enum": [
              "session"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "SessionPropertyFilter",
        "type": "object"
      },
      "CohortPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "cohort_name": {
            "default": null,
            "title": "Cohort Name",
            "type": "string",
            "nullable": true
          },
          "key": {
            "default": "id",
            "title": "Key",
            "type": "string",
            "enum": [
              "id"
            ]
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "default": "in",
            "$ref": "#/components/schemas/PropertyOperator",
            "nullable": true
          },
          "type": {
            "default": "cohort",
            "title": "Type",
            "type": "string",
            "enum": [
              "cohort"
            ]
          },
          "value": {
            "title": "Value",
            "type": "integer"
          }
        },
        "required": [
          "value"
        ],
        "title": "CohortPropertyFilter",
        "type": "object"
      },
      "RecordingPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/DurationType"
              },
              {
                "type": "string"
              }
            ],
            "title": "Key"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "recording",
            "title": "Type",
            "type": "string",
            "enum": [
              "recording"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "RecordingPropertyFilter",
        "type": "object"
      },
      "LogEntryPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "log_entry",
            "title": "Type",
            "type": "string",
            "enum": [
              "log_entry"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "LogEntryPropertyFilter",
        "type": "object"
      },
      "GroupPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "group_key_names": {
            "default": null,
            "title": "Group Key Names",
            "additionalProperties": {
              "type": "string"
            },
            "type": "object",
            "nullable": true
          },
          "group_type_index": {
            "default": null,
            "title": "Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "group",
            "title": "Type",
            "type": "string",
            "enum": [
              "group"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "GroupPropertyFilter",
        "type": "object"
      },
      "FeaturePropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "feature",
            "description": "Event property with \"$feature/\" prepended",
            "title": "Type",
            "type": "string",
            "enum": [
              "feature"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "FeaturePropertyFilter",
        "type": "object"
      },
      "FlagPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "description": "The key should be the flag ID",
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "default": "flag_evaluates_to",
            "description": "Only flag_evaluates_to operator is allowed for flag dependencies",
            "title": "Operator",
            "type": "string",
            "enum": [
              "flag_evaluates_to"
            ]
          },
          "type": {
            "default": "flag",
            "description": "Feature flag dependency",
            "title": "Type",
            "type": "string",
            "enum": [
              "flag"
            ]
          },
          "value": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "string"
              }
            ],
            "description": "The value can be true, false, or a variant name",
            "title": "Value"
          }
        },
        "required": [
          "key",
          "value"
        ],
        "title": "FlagPropertyFilter",
        "type": "object"
      },
      "HogQLPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "type": {
            "default": "hogql",
            "title": "Type",
            "type": "string",
            "enum": [
              "hogql"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key"
        ],
        "title": "HogQLPropertyFilter",
        "type": "object"
      },
      "EmptyPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "default": "empty",
            "title": "Type",
            "type": "string",
            "enum": [
              "empty"
            ]
          }
        },
        "title": "EmptyPropertyFilter",
        "type": "object"
      },
      "DataWarehousePropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "data_warehouse",
            "title": "Type",
            "type": "string",
            "enum": [
              "data_warehouse"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "DataWarehousePropertyFilter",
        "type": "object"
      },
      "DataWarehousePersonPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "data_warehouse_person_property",
            "title": "Type",
            "type": "string",
            "enum": [
              "data_warehouse_person_property"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "DataWarehousePersonPropertyFilter",
        "type": "object"
      },
      "ErrorTrackingIssueFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "error_tracking_issue",
            "title": "Type",
            "type": "string",
            "enum": [
              "error_tracking_issue"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "ErrorTrackingIssueFilter",
        "type": "object"
      },
      "LogPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "$ref": "#/components/schemas/LogPropertyFilterType"
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator",
          "type"
        ],
        "title": "LogPropertyFilter",
        "type": "object"
      },
      "RevenueAnalyticsPropertyFilter": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "title": "Key",
            "type": "string"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "operator": {
            "$ref": "#/components/schemas/PropertyOperator"
          },
          "type": {
            "default": "revenue_analytics",
            "title": "Type",
            "type": "string",
            "enum": [
              "revenue_analytics"
            ]
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "operator"
        ],
        "title": "RevenueAnalyticsPropertyFilter",
        "type": "object"
      },
      "BreakdownType": {
        "enum": [
          "cohort",
          "person",
          "event",
          "event_metadata",
          "group",
          "session",
          "hogql",
          "data_warehouse",
          "data_warehouse_person_property",
          "revenue_analytics"
        ],
        "title": "BreakdownType",
        "type": "string"
      },
      "Breakdown": {
        "additionalProperties": false,
        "properties": {
          "group_type_index": {
            "default": null,
            "title": "Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "histogram_bin_count": {
            "default": null,
            "title": "Histogram Bin Count",
            "type": "integer",
            "nullable": true
          },
          "normalize_url": {
            "default": null,
            "title": "Normalize Url",
            "type": "boolean",
            "nullable": true
          },
          "property": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "integer"
              }
            ],
            "title": "Property"
          },
          "type": {
            "default": null,
            "$ref": "#/components/schemas/MultipleBreakdownType",
            "nullable": true
          }
        },
        "required": [
          "property"
        ],
        "title": "Breakdown",
        "type": "object"
      },
      "PropertyOperator": {
        "enum": [
          "exact",
          "is_not",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex",
          "gt",
          "gte",
          "lt",
          "lte",
          "is_set",
          "is_not_set",
          "is_date_exact",
          "is_date_before",
          "is_date_after",
          "between",
          "not_between",
          "min",
          "max",
          "in",
          "not_in",
          "is_cleaned_path_exact",
          "flag_evaluates_to",
          "semver_eq",
          "semver_neq",
          "semver_gt",
          "semver_gte",
          "semver_lt",
          "semver_lte",
          "semver_tilde",
          "semver_caret",
          "semver_wildcard",
          "icontains_multi",
          "not_icontains_multi"
        ],
        "title": "PropertyOperator",
        "type": "string"
      },
      "Key": {
        "enum": [
          "tag_name",
          "text",
          "href",
          "selector"
        ],
        "title": "Key",
        "type": "string"
      },
      "DurationType": {
        "enum": [
          "duration",
          "active_seconds",
          "inactive_seconds"
        ],
        "title": "DurationType",
        "type": "string"
      },
      "LogPropertyFilterType": {
        "enum": [
          "log",
          "log_attribute",
          "log_resource_attribute"
        ],
        "title": "LogPropertyFilterType",
        "type": "string"
      },
      "MultipleBreakdownType": {
        "enum": [
          "cohort",
          "person",
          "event",
          "event_metadata",
          "group",
          "session",
          "hogql",
          "revenue_analytics"
        ],
        "title": "MultipleBreakdownType",
        "type": "string"
      }
    }
  }
}
```
