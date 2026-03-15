# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_update.md

# environments_endpoints_update

## OpenAPI

```json PUT /api/environments/{environment_id}/endpoints/{name}/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/": {
      "put": {
        "operationId": "environments_endpoints_update",
        "description": "Update an existing endpoint. Parameters are optional. Pass version in body or ?version=N query param to target a specific version.",
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
                "$ref": "#/components/schemas/EndpointRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/EndpointRequest"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:write"
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
      "EndpointRequest": {
        "additionalProperties": false,
        "properties": {
          "bucket_overrides": {
            "default": null,
            "description": "Per-column bucket function overrides for range variable materialization. Keys are column names, values are bucket keys (hour, day, week, month).",
            "title": "Bucket Overrides",
            "additionalProperties": {
              "type": "string"
            },
            "type": "object",
            "nullable": true
          },
          "cache_age_seconds": {
            "default": null,
            "title": "Cache Age Seconds",
            "type": "number",
            "nullable": true
          },
          "derived_from_insight": {
            "default": null,
            "title": "Derived From Insight",
            "type": "string",
            "nullable": true
          },
          "description": {
            "default": null,
            "title": "Description",
            "type": "string",
            "nullable": true
          },
          "is_active": {
            "default": null,
            "title": "Is Active",
            "type": "boolean",
            "nullable": true
          },
          "is_materialized": {
            "default": null,
            "description": "Whether this endpoint's query results are materialized to S3",
            "title": "Is Materialized",
            "type": "boolean",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "query": {
            "default": null,
            "title": "Query",
            "anyOf": [
              {
                "$ref": "#/components/schemas/HogQLQuery"
              },
              {
                "$ref": "#/components/schemas/TrendsQuery"
              },
              {
                "$ref": "#/components/schemas/FunnelsQuery"
              },
              {
                "$ref": "#/components/schemas/RetentionQuery"
              },
              {
                "$ref": "#/components/schemas/PathsQuery"
              },
              {
                "$ref": "#/components/schemas/StickinessQuery"
              },
              {
                "$ref": "#/components/schemas/LifecycleQuery"
              },
              {
                "$ref": "#/components/schemas/WebStatsTableQuery"
              },
              {
                "$ref": "#/components/schemas/WebOverviewQuery"
              }
            ],
            "nullable": true
          },
          "sync_frequency": {
            "default": null,
            "description": "How frequently should the underlying materialized view be updated",
            "$ref": "#/components/schemas/DataWarehouseSyncInterval",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "Target a specific version for updates (optional, defaults to current version)",
            "title": "Version",
            "type": "integer",
            "nullable": true
          }
        },
        "title": "EndpointRequest",
        "type": "object"
      },
      "HogQLQuery": {
        "additionalProperties": false,
        "properties": {
          "connectionId": {
            "default": null,
            "description": "Optional direct external data source id for running against a specific source",
            "title": "Connectionid",
            "type": "string",
            "nullable": true
          },
          "explain": {
            "default": null,
            "title": "Explain",
            "type": "boolean",
            "nullable": true
          },
          "filters": {
            "default": null,
            "$ref": "#/components/schemas/HogQLFilters",
            "nullable": true
          },
          "kind": {
            "default": "HogQLQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "HogQLQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "name": {
            "default": null,
            "description": "Client provided name of the query",
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "query": {
            "title": "Query",
            "type": "string"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/HogQLQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "values": {
            "default": null,
            "description": "Constant values that can be referenced with the {placeholder} syntax in the query",
            "title": "Values",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "variables": {
            "default": null,
            "description": "Variables to be substituted into the query",
            "title": "Variables",
            "additionalProperties": {
              "$ref": "#/components/schemas/HogQLVariable"
            },
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "query"
        ],
        "title": "HogQLQuery",
        "type": "object"
      },
      "TrendsQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "breakdownFilter": {
            "default": null,
            "description": "Breakdown of the events and actions",
            "$ref": "#/components/schemas/BreakdownFilter",
            "nullable": true
          },
          "compareFilter": {
            "default": null,
            "description": "Compare to date range",
            "$ref": "#/components/schemas/CompareFilter",
            "nullable": true
          },
          "conversionGoal": {
            "default": null,
            "description": "Whether we should be comparing against a specific conversion goal",
            "title": "Conversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ActionConversionGoal"
              },
              {
                "$ref": "#/components/schemas/CustomEventConversionGoal"
              }
            ],
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": "day",
            "description": "Granularity of the response. Can be one of `hour`, `day`, `week` or `month`",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "TrendsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "TrendsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQueryResponse",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "series": {
            "description": "Events and actions to include",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/GroupNode"
                },
                {
                  "$ref": "#/components/schemas/EventsNode"
                },
                {
                  "$ref": "#/components/schemas/ActionsNode"
                },
                {
                  "$ref": "#/components/schemas/DataWarehouseNode"
                }
              ]
            },
            "title": "Series",
            "type": "array"
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "trendsFilter": {
            "default": null,
            "description": "Properties specific to the trends insight",
            "$ref": "#/components/schemas/TrendsFilter",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "series"
        ],
        "title": "TrendsQuery",
        "type": "object"
      },
      "FunnelsQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "breakdownFilter": {
            "default": null,
            "description": "Breakdown of the events and actions",
            "$ref": "#/components/schemas/BreakdownFilter",
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "funnelsFilter": {
            "default": null,
            "description": "Properties specific to the funnels insight",
            "$ref": "#/components/schemas/FunnelsFilter",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "Granularity of the response. Can be one of `hour`, `day`, `week` or `month`",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "FunnelsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "FunnelsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/FunnelsQueryResponse",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "series": {
            "description": "Events and actions to include",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/GroupNode"
                },
                {
                  "$ref": "#/components/schemas/EventsNode"
                },
                {
                  "$ref": "#/components/schemas/ActionsNode"
                },
                {
                  "$ref": "#/components/schemas/DataWarehouseNode"
                }
              ]
            },
            "title": "Series",
            "type": "array"
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "series"
        ],
        "title": "FunnelsQuery",
        "type": "object"
      },
      "RetentionQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "breakdownFilter": {
            "default": null,
            "description": "Breakdown of the events and actions",
            "$ref": "#/components/schemas/BreakdownFilter",
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "kind": {
            "default": "RetentionQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RetentionQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RetentionQueryResponse",
            "nullable": true
          },
          "retentionFilter": {
            "$ref": "#/components/schemas/RetentionFilter",
            "description": "Properties specific to the retention insight"
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "retentionFilter"
        ],
        "title": "RetentionQuery",
        "type": "object"
      },
      "PathsQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "funnelPathsFilter": {
            "default": null,
            "description": "Used for displaying paths in relation to funnel steps.",
            "$ref": "#/components/schemas/FunnelPathsFilter",
            "nullable": true
          },
          "kind": {
            "default": "PathsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "PathsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "pathsFilter": {
            "$ref": "#/components/schemas/PathsFilter",
            "description": "Properties specific to the paths insight"
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/PathsQueryResponse",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "pathsFilter"
        ],
        "title": "PathsQuery",
        "type": "object"
      },
      "StickinessQuery": {
        "additionalProperties": false,
        "properties": {
          "compareFilter": {
            "default": null,
            "description": "Compare to date range",
            "$ref": "#/components/schemas/CompareFilter",
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": "day",
            "description": "Granularity of the response. Can be one of `hour`, `day`, `week` or `month`",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "intervalCount": {
            "default": null,
            "description": "How many intervals comprise a period. Only used for cohorts, otherwise default 1.",
            "title": "Intervalcount",
            "type": "integer",
            "nullable": true
          },
          "kind": {
            "default": "StickinessQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "StickinessQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/StickinessQueryResponse",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "series": {
            "description": "Events and actions to include",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventsNode"
                },
                {
                  "$ref": "#/components/schemas/ActionsNode"
                },
                {
                  "$ref": "#/components/schemas/DataWarehouseNode"
                }
              ]
            },
            "title": "Series",
            "type": "array"
          },
          "stickinessFilter": {
            "default": null,
            "description": "Properties specific to the stickiness insight",
            "$ref": "#/components/schemas/StickinessFilter",
            "nullable": true
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "series"
        ],
        "title": "StickinessQuery",
        "type": "object"
      },
      "LifecycleQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "description": "Date range for the query",
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": false,
            "description": "Exclude internal and test users by applying the respective filters",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": "day",
            "description": "Granularity of the response. Can be one of `hour`, `day`, `week` or `month`",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "LifecycleQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "LifecycleQuery"
            ]
          },
          "lifecycleFilter": {
            "default": null,
            "description": "Properties specific to the lifecycle insight",
            "$ref": "#/components/schemas/LifecycleFilter",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "default": [],
            "description": "Property filters for all series",
            "title": "Properties",
            "anyOf": [
              {
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
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilter"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/LifecycleQueryResponse",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "series": {
            "description": "Events and actions to include",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventsNode"
                },
                {
                  "$ref": "#/components/schemas/ActionsNode"
                },
                {
                  "$ref": "#/components/schemas/DataWarehouseNode"
                }
              ]
            },
            "title": "Series",
            "type": "array"
          },
          "tags": {
            "default": null,
            "description": "Tags that will be added to the Query log comment",
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "series"
        ],
        "title": "LifecycleQuery",
        "type": "object"
      },
      "WebStatsTableQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation - not used in Web Analytics but required for type compatibility",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "breakdownBy": {
            "$ref": "#/components/schemas/WebStatsBreakdown"
          },
          "compareFilter": {
            "default": null,
            "$ref": "#/components/schemas/CompareFilter",
            "nullable": true
          },
          "conversionGoal": {
            "default": null,
            "title": "Conversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ActionConversionGoal"
              },
              {
                "$ref": "#/components/schemas/CustomEventConversionGoal"
              }
            ],
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization - not used in Web Analytics but required for type compatibility",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "doPathCleaning": {
            "default": null,
            "title": "Dopathcleaning",
            "type": "boolean",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "includeAvgTimeOnPage": {
            "default": null,
            "title": "Includeavgtimeonpage",
            "type": "boolean",
            "nullable": true
          },
          "includeBounceRate": {
            "default": null,
            "title": "Includebouncerate",
            "type": "boolean",
            "nullable": true
          },
          "includeRevenue": {
            "default": null,
            "title": "Includerevenue",
            "type": "boolean",
            "nullable": true
          },
          "includeScrollDepth": {
            "default": null,
            "title": "Includescrolldepth",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "Interval for date range calculation (affects date_to rounding for hour vs day ranges)",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "WebStatsTableQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebStatsTableQuery"
            ]
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "offset": {
            "default": null,
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "title": "Orderby",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/WebAnalyticsOrderByFields"
                },
                {
                  "$ref": "#/components/schemas/WebAnalyticsOrderByDirection"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/PersonPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/SessionPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortPropertyFilter"
                }
              ]
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/WebStatsTableQueryResponse",
            "nullable": true
          },
          "sampling": {
            "default": null,
            "$ref": "#/components/schemas/WebAnalyticsSampling",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "useSessionsTable": {
            "default": null,
            "title": "Usesessionstable",
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "breakdownBy",
          "properties"
        ],
        "title": "WebStatsTableQuery",
        "type": "object"
      },
      "WebOverviewQuery": {
        "additionalProperties": false,
        "properties": {
          "aggregation_group_type_index": {
            "default": null,
            "description": "Groups aggregation - not used in Web Analytics but required for type compatibility",
            "title": "Aggregation Group Type Index",
            "type": "integer",
            "nullable": true
          },
          "compareFilter": {
            "default": null,
            "$ref": "#/components/schemas/CompareFilter",
            "nullable": true
          },
          "conversionGoal": {
            "default": null,
            "title": "Conversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ActionConversionGoal"
              },
              {
                "$ref": "#/components/schemas/CustomEventConversionGoal"
              }
            ],
            "nullable": true
          },
          "dataColorTheme": {
            "default": null,
            "description": "Colors used in the insight's visualization - not used in Web Analytics but required for type compatibility",
            "title": "Datacolortheme",
            "type": "number",
            "nullable": true
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "doPathCleaning": {
            "default": null,
            "title": "Dopathcleaning",
            "type": "boolean",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "includeRevenue": {
            "default": null,
            "title": "Includerevenue",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "Interval for date range calculation (affects date_to rounding for hour vs day ranges)",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "WebOverviewQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebOverviewQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "title": "Orderby",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/WebAnalyticsOrderByFields"
                },
                {
                  "$ref": "#/components/schemas/WebAnalyticsOrderByDirection"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/PersonPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/SessionPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortPropertyFilter"
                }
              ]
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/WebOverviewQueryResponse",
            "nullable": true
          },
          "sampling": {
            "default": null,
            "$ref": "#/components/schemas/WebAnalyticsSampling",
            "nullable": true
          },
          "samplingFactor": {
            "default": null,
            "description": "Sampling rate",
            "title": "Samplingfactor",
            "type": "number",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "useSessionsTable": {
            "default": null,
            "title": "Usesessionstable",
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "properties"
        ],
        "title": "WebOverviewQuery",
        "type": "object"
      },
      "DataWarehouseSyncInterval": {
        "enum": [
          "5min",
          "30min",
          "1hour",
          "6hour",
          "12hour",
          "24hour",
          "7day",
          "30day"
        ],
        "title": "DataWarehouseSyncInterval",
        "type": "string"
      },
      "HogQLFilters": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "title": "Filtertestaccounts",
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
        "title": "HogQLFilters",
        "type": "object"
      },
      "HogQLQueryModifiers": {
        "additionalProperties": false,
        "properties": {
          "bounceRateDurationSeconds": {
            "default": null,
            "title": "Bounceratedurationseconds",
            "type": "number",
            "nullable": true
          },
          "bounceRatePageViewMode": {
            "default": null,
            "$ref": "#/components/schemas/BounceRatePageViewMode",
            "nullable": true
          },
          "convertToProjectTimezone": {
            "default": null,
            "title": "Converttoprojecttimezone",
            "type": "boolean",
            "nullable": true
          },
          "customChannelTypeRules": {
            "default": null,
            "title": "Customchanneltyperules",
            "items": {
              "$ref": "#/components/schemas/CustomChannelRule"
            },
            "type": "array",
            "nullable": true
          },
          "dataWarehouseEventsModifiers": {
            "default": null,
            "title": "Datawarehouseeventsmodifiers",
            "items": {
              "$ref": "#/components/schemas/DataWarehouseEventsModifier"
            },
            "type": "array",
            "nullable": true
          },
          "debug": {
            "default": null,
            "title": "Debug",
            "type": "boolean",
            "nullable": true
          },
          "forceClickhouseDataSkippingIndexes": {
            "default": null,
            "description": "If these are provided, the query will fail if these skip indexes are not used",
            "title": "Forceclickhousedataskippingindexes",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "formatCsvAllowDoubleQuotes": {
            "default": null,
            "title": "Formatcsvallowdoublequotes",
            "type": "boolean",
            "nullable": true
          },
          "inCohortVia": {
            "default": null,
            "$ref": "#/components/schemas/InCohortVia",
            "nullable": true
          },
          "inlineCohortCalculation": {
            "default": null,
            "$ref": "#/components/schemas/InlineCohortCalculation",
            "nullable": true
          },
          "materializationMode": {
            "default": null,
            "$ref": "#/components/schemas/MaterializationMode",
            "nullable": true
          },
          "materializedColumnsOptimizationMode": {
            "default": null,
            "$ref": "#/components/schemas/MaterializedColumnsOptimizationMode",
            "nullable": true
          },
          "optimizeJoinedFilters": {
            "default": null,
            "title": "Optimizejoinedfilters",
            "type": "boolean",
            "nullable": true
          },
          "optimizeProjections": {
            "default": null,
            "title": "Optimizeprojections",
            "type": "boolean",
            "nullable": true
          },
          "personsArgMaxVersion": {
            "default": null,
            "$ref": "#/components/schemas/PersonsArgMaxVersion",
            "nullable": true
          },
          "personsJoinMode": {
            "default": null,
            "$ref": "#/components/schemas/PersonsJoinMode",
            "nullable": true
          },
          "personsOnEventsMode": {
            "default": null,
            "$ref": "#/components/schemas/PersonsOnEventsMode",
            "nullable": true
          },
          "propertyGroupsMode": {
            "default": null,
            "$ref": "#/components/schemas/PropertyGroupsMode",
            "nullable": true
          },
          "s3TableUseInvalidColumns": {
            "default": null,
            "title": "S3Tableuseinvalidcolumns",
            "type": "boolean",
            "nullable": true
          },
          "sessionTableVersion": {
            "default": null,
            "$ref": "#/components/schemas/SessionTableVersion",
            "nullable": true
          },
          "sessionsV2JoinMode": {
            "default": null,
            "$ref": "#/components/schemas/SessionsV2JoinMode",
            "nullable": true
          },
          "timings": {
            "default": null,
            "title": "Timings",
            "type": "boolean",
            "nullable": true
          },
          "useMaterializedViews": {
            "default": null,
            "title": "Usematerializedviews",
            "type": "boolean",
            "nullable": true
          },
          "usePreaggregatedIntermediateResults": {
            "default": null,
            "title": "Usepreaggregatedintermediateresults",
            "type": "boolean",
            "nullable": true
          },
          "usePreaggregatedTableTransforms": {
            "default": null,
            "description": "Try to automatically convert HogQL queries to use preaggregated tables at the AST level *",
            "title": "Usepreaggregatedtabletransforms",
            "type": "boolean",
            "nullable": true
          },
          "useWebAnalyticsPreAggregatedTables": {
            "default": null,
            "title": "Usewebanalyticspreaggregatedtables",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "HogQLQueryModifiers",
        "type": "object"
      },
      "HogQLQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "clickhouse": {
            "default": null,
            "description": "Executed ClickHouse query",
            "title": "Clickhouse",
            "type": "string",
            "nullable": true
          },
          "columns": {
            "default": null,
            "description": "Returned columns",
            "title": "Columns",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "explain": {
            "default": null,
            "description": "Query explanation output",
            "title": "Explain",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "hasMore": {
            "default": null,
            "title": "Hasmore",
            "type": "boolean",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "metadata": {
            "default": null,
            "description": "Query metadata output",
            "$ref": "#/components/schemas/HogQLMetadataResponse",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "offset": {
            "default": null,
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "query": {
            "default": null,
            "description": "Input query string",
            "title": "Query",
            "type": "string",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {},
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          },
          "types": {
            "default": null,
            "description": "Types of returned columns",
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "HogQLQueryResponse",
        "type": "object"
      },
      "QueryLogTags": {
        "additionalProperties": false,
        "properties": {
          "name": {
            "default": null,
            "description": "Name of the query, preferably unique. For example web_analytics_vitals",
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "productKey": {
            "default": null,
            "description": "Product responsible for this query. Use string, there's no need to churn the Schema when we add a new product *",
            "title": "Productkey",
            "type": "string",
            "nullable": true
          },
          "scene": {
            "default": null,
            "description": "Scene where this query is shown in the UI. Use string, there's no need to churn the Schema when we add a new Scene *",
            "title": "Scene",
            "type": "string",
            "nullable": true
          }
        },
        "title": "QueryLogTags",
        "type": "object"
      },
      "HogQLVariable": {
        "additionalProperties": false,
        "properties": {
          "code_name": {
            "title": "Code Name",
            "type": "string"
          },
          "isNull": {
            "default": null,
            "title": "Isnull",
            "type": "boolean",
            "nullable": true
          },
          "value": {
            "default": null,
            "title": "Value",
            "nullable": true
          },
          "variableId": {
            "title": "Variableid",
            "type": "string"
          }
        },
        "required": [
          "code_name",
          "variableId"
        ],
        "title": "HogQLVariable",
        "type": "object"
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
      "CompareFilter": {
        "additionalProperties": false,
        "properties": {
          "compare": {
            "default": false,
            "description": "Whether to compare the current date range to a previous date range.",
            "title": "Compare",
            "type": "boolean",
            "nullable": true
          },
          "compare_to": {
            "default": null,
            "description": "The date range to compare to. The value is a relative date. Examples of relative dates are: `-1y` for 1 year ago, `-14m` for 14 months ago, `-100w` for 100 weeks ago, `-14d` for 14 days ago, `-30h` for 30 hours ago.",
            "title": "Compare To",
            "type": "string",
            "nullable": true
          }
        },
        "title": "CompareFilter",
        "type": "object"
      },
      "ActionConversionGoal": {
        "additionalProperties": false,
        "properties": {
          "actionId": {
            "title": "Actionid",
            "type": "integer"
          }
        },
        "required": [
          "actionId"
        ],
        "title": "ActionConversionGoal",
        "type": "object"
      },
      "CustomEventConversionGoal": {
        "additionalProperties": false,
        "properties": {
          "customEventName": {
            "title": "Customeventname",
            "type": "string"
          }
        },
        "required": [
          "customEventName"
        ],
        "title": "CustomEventConversionGoal",
        "type": "object"
      },
      "DateRange": {
        "additionalProperties": false,
        "properties": {
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
            "default": false,
            "description": "Whether the date_from and date_to should be used verbatim. Disables rounding to the start and end of period.",
            "title": "Explicitdate",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "DateRange",
        "type": "object"
      },
      "IntervalType": {
        "enum": [
          "second",
          "minute",
          "hour",
          "day",
          "week",
          "month"
        ],
        "title": "IntervalType",
        "type": "string"
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
      "PropertyGroupFilter": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "$ref": "#/components/schemas/FilterLogicalOperator"
          },
          "values": {
            "items": {
              "$ref": "#/components/schemas/PropertyGroupFilterValue"
            },
            "title": "Values",
            "type": "array"
          }
        },
        "required": [
          "type",
          "values"
        ],
        "title": "PropertyGroupFilter",
        "type": "object"
      },
      "TrendsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "boxplot_data": {
            "default": null,
            "description": "Box plot data when display type is BoxPlot",
            "title": "Boxplot Data",
            "items": {
              "$ref": "#/components/schemas/BoxPlotDatum"
            },
            "type": "array",
            "nullable": true
          },
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hasMore": {
            "default": null,
            "description": "Wether more breakdown values are available.",
            "title": "Hasmore",
            "type": "boolean",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "TrendsQueryResponse",
        "type": "object"
      },
      "GroupNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "kind": {
            "default": "GroupNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "GroupNode"
            ]
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "nodes": {
            "description": "Entities to combine in this group",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/EventsNode"
                },
                {
                  "$ref": "#/components/schemas/ActionsNode"
                },
                {
                  "$ref": "#/components/schemas/DataWarehouseNode"
                }
              ]
            },
            "title": "Nodes",
            "type": "array"
          },
          "operator": {
            "$ref": "#/components/schemas/FilterLogicalOperator",
            "description": "Group of entities combined with AND/OR operator"
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "description": "Columns to order by",
            "title": "Orderby",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "nodes",
          "operator"
        ],
        "title": "GroupNode",
        "type": "object"
      },
      "EventsNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "event": {
            "default": null,
            "description": "The event or `null` for all events.",
            "title": "Event",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "kind": {
            "default": "EventsNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "EventsNode"
            ]
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "description": "Columns to order by",
            "title": "Orderby",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "title": "EventsNode",
        "type": "object"
      },
      "ActionsNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "kind": {
            "default": "ActionsNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ActionsNode"
            ]
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "id"
        ],
        "title": "ActionsNode",
        "type": "object"
      },
      "DataWarehouseNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "distinct_id_field": {
            "title": "Distinct Id Field",
            "type": "string"
          },
          "dw_source_type": {
            "default": null,
            "title": "Dw Source Type",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "id_field": {
            "title": "Id Field",
            "type": "string"
          },
          "kind": {
            "default": "DataWarehouseNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "DataWarehouseNode"
            ]
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "table_name": {
            "title": "Table Name",
            "type": "string"
          },
          "timestamp_field": {
            "title": "Timestamp Field",
            "type": "string"
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "distinct_id_field",
          "id",
          "id_field",
          "table_name",
          "timestamp_field"
        ],
        "title": "DataWarehouseNode",
        "type": "object"
      },
      "TrendsFilter": {
        "additionalProperties": false,
        "properties": {
          "aggregationAxisFormat": {
            "default": "numeric",
            "$ref": "#/components/schemas/AggregationAxisFormat",
            "nullable": true
          },
          "aggregationAxisPostfix": {
            "default": null,
            "title": "Aggregationaxispostfix",
            "type": "string",
            "nullable": true
          },
          "aggregationAxisPrefix": {
            "default": null,
            "title": "Aggregationaxisprefix",
            "type": "string",
            "nullable": true
          },
          "breakdown_histogram_bin_count": {
            "default": null,
            "title": "Breakdown Histogram Bin Count",
            "type": "number",
            "nullable": true
          },
          "confidenceLevel": {
            "default": null,
            "title": "Confidencelevel",
            "type": "number",
            "nullable": true
          },
          "decimalPlaces": {
            "default": null,
            "title": "Decimalplaces",
            "type": "number",
            "nullable": true
          },
          "detailedResultsAggregationType": {
            "default": null,
            "description": "detailed results table",
            "$ref": "#/components/schemas/DetailedResultsAggregationType",
            "nullable": true
          },
          "display": {
            "default": "ActionsLineGraph",
            "$ref": "#/components/schemas/ChartDisplayType",
            "nullable": true
          },
          "formula": {
            "default": null,
            "title": "Formula",
            "type": "string",
            "nullable": true
          },
          "formulaNodes": {
            "default": null,
            "description": "List of formulas with optional custom names. Takes precedence over formula/formulas if set.",
            "title": "Formulanodes",
            "items": {
              "$ref": "#/components/schemas/TrendsFormulaNode"
            },
            "type": "array",
            "nullable": true
          },
          "formulas": {
            "default": null,
            "title": "Formulas",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "goalLines": {
            "default": null,
            "description": "Goal Lines",
            "title": "Goallines",
            "items": {
              "$ref": "#/components/schemas/GoalLine"
            },
            "type": "array",
            "nullable": true
          },
          "hiddenLegendIndexes": {
            "default": null,
            "title": "Hiddenlegendindexes",
            "items": {
              "type": "integer"
            },
            "type": "array",
            "nullable": true
          },
          "hideWeekends": {
            "default": false,
            "title": "Hideweekends",
            "type": "boolean",
            "nullable": true
          },
          "minDecimalPlaces": {
            "default": null,
            "title": "Mindecimalplaces",
            "type": "number",
            "nullable": true
          },
          "movingAverageIntervals": {
            "default": null,
            "title": "Movingaverageintervals",
            "type": "number",
            "nullable": true
          },
          "resultCustomizationBy": {
            "default": "value",
            "description": "Wether result datasets are associated by their values or by their order.",
            "$ref": "#/components/schemas/ResultCustomizationBy",
            "nullable": true
          },
          "resultCustomizations": {
            "default": null,
            "description": "Customizations for the appearance of result datasets.",
            "title": "Resultcustomizations",
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ResultCustomizationByValue"
                },
                "type": "object"
              },
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ResultCustomizationByPosition"
                },
                "type": "object"
              }
            ],
            "nullable": true
          },
          "showAlertThresholdLines": {
            "default": false,
            "title": "Showalertthresholdlines",
            "type": "boolean",
            "nullable": true
          },
          "showConfidenceIntervals": {
            "default": null,
            "title": "Showconfidenceintervals",
            "type": "boolean",
            "nullable": true
          },
          "showLabelsOnSeries": {
            "default": null,
            "title": "Showlabelsonseries",
            "type": "boolean",
            "nullable": true
          },
          "showLegend": {
            "default": false,
            "title": "Showlegend",
            "type": "boolean",
            "nullable": true
          },
          "showMovingAverage": {
            "default": null,
            "title": "Showmovingaverage",
            "type": "boolean",
            "nullable": true
          },
          "showMultipleYAxes": {
            "default": false,
            "title": "Showmultipleyaxes",
            "type": "boolean",
            "nullable": true
          },
          "showPercentStackView": {
            "default": false,
            "title": "Showpercentstackview",
            "type": "boolean",
            "nullable": true
          },
          "showTrendLines": {
            "default": null,
            "title": "Showtrendlines",
            "type": "boolean",
            "nullable": true
          },
          "showValuesOnSeries": {
            "default": false,
            "title": "Showvaluesonseries",
            "type": "boolean",
            "nullable": true
          },
          "smoothingIntervals": {
            "default": 1,
            "title": "Smoothingintervals",
            "type": "integer",
            "nullable": true
          },
          "yAxisScaleType": {
            "default": "linear",
            "$ref": "#/components/schemas/YAxisScaleType",
            "nullable": true
          }
        },
        "title": "TrendsFilter",
        "type": "object"
      },
      "FunnelsFilter": {
        "additionalProperties": false,
        "properties": {
          "binCount": {
            "default": null,
            "title": "Bincount",
            "type": "integer",
            "nullable": true
          },
          "breakdownAttributionType": {
            "default": "first_touch",
            "$ref": "#/components/schemas/BreakdownAttributionType",
            "nullable": true
          },
          "breakdownAttributionValue": {
            "default": null,
            "title": "Breakdownattributionvalue",
            "type": "integer",
            "nullable": true
          },
          "breakdownSorting": {
            "default": null,
            "description": "Breakdown table sorting. Format: 'column_key' or '-column_key' (descending)",
            "title": "Breakdownsorting",
            "type": "string",
            "nullable": true
          },
          "exclusions": {
            "default": [],
            "title": "Exclusions",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/FunnelExclusionEventsNode"
                },
                {
                  "$ref": "#/components/schemas/FunnelExclusionActionsNode"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "funnelAggregateByHogQL": {
            "default": null,
            "title": "Funnelaggregatebyhogql",
            "type": "string",
            "nullable": true
          },
          "funnelFromStep": {
            "default": null,
            "title": "Funnelfromstep",
            "type": "integer",
            "nullable": true
          },
          "funnelOrderType": {
            "default": "ordered",
            "$ref": "#/components/schemas/StepOrderValue",
            "nullable": true
          },
          "funnelStepReference": {
            "default": "total",
            "$ref": "#/components/schemas/FunnelStepReference",
            "nullable": true
          },
          "funnelToStep": {
            "default": null,
            "description": "To select the range of steps for trends & time to convert funnels, 0-indexed",
            "title": "Funneltostep",
            "type": "integer",
            "nullable": true
          },
          "funnelVizType": {
            "default": "steps",
            "$ref": "#/components/schemas/FunnelVizType",
            "nullable": true
          },
          "funnelWindowInterval": {
            "default": 14,
            "title": "Funnelwindowinterval",
            "type": "integer",
            "nullable": true
          },
          "funnelWindowIntervalUnit": {
            "default": "day",
            "$ref": "#/components/schemas/FunnelConversionWindowTimeUnit",
            "nullable": true
          },
          "goalLines": {
            "default": null,
            "description": "Goal Lines",
            "title": "Goallines",
            "items": {
              "$ref": "#/components/schemas/GoalLine"
            },
            "type": "array",
            "nullable": true
          },
          "hiddenLegendBreakdowns": {
            "default": null,
            "title": "Hiddenlegendbreakdowns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "layout": {
            "default": "vertical",
            "$ref": "#/components/schemas/FunnelLayout",
            "nullable": true
          },
          "resultCustomizations": {
            "default": null,
            "description": "Customizations for the appearance of result datasets.",
            "title": "Resultcustomizations",
            "additionalProperties": {
              "$ref": "#/components/schemas/ResultCustomizationByValue"
            },
            "type": "object",
            "nullable": true
          },
          "showTrendLines": {
            "default": null,
            "description": "Display linear regression trend lines on the chart (only for historical trends viz)",
            "title": "Showtrendlines",
            "type": "boolean",
            "nullable": true
          },
          "showValuesOnSeries": {
            "default": false,
            "title": "Showvaluesonseries",
            "type": "boolean",
            "nullable": true
          },
          "useUdf": {
            "default": null,
            "title": "Useudf",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "FunnelsFilter",
        "type": "object"
      },
      "FunnelsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "title": "Results"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "FunnelsQueryResponse",
        "type": "object"
      },
      "RetentionQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "$ref": "#/components/schemas/RetentionResult"
            },
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "RetentionQueryResponse",
        "type": "object"
      },
      "RetentionFilter": {
        "additionalProperties": false,
        "properties": {
          "aggregationProperty": {
            "default": null,
            "description": "The property to aggregate when aggregationType is sum or avg",
            "title": "Aggregationproperty",
            "type": "string",
            "nullable": true
          },
          "aggregationPropertyType": {
            "default": "event",
            "description": "The type of property to aggregate on (event or person). Defaults to event.",
            "$ref": "#/components/schemas/AggregationPropertyType",
            "nullable": true
          },
          "aggregationType": {
            "default": "count",
            "description": "The aggregation type to use for retention",
            "$ref": "#/components/schemas/AggregationType",
            "nullable": true
          },
          "cumulative": {
            "default": null,
            "title": "Cumulative",
            "type": "boolean",
            "nullable": true
          },
          "dashboardDisplay": {
            "default": null,
            "$ref": "#/components/schemas/RetentionDashboardDisplayType",
            "nullable": true
          },
          "display": {
            "default": null,
            "description": "controls the display of the retention graph",
            "$ref": "#/components/schemas/ChartDisplayType",
            "nullable": true
          },
          "goalLines": {
            "default": null,
            "title": "Goallines",
            "items": {
              "$ref": "#/components/schemas/GoalLine"
            },
            "type": "array",
            "nullable": true
          },
          "meanRetentionCalculation": {
            "default": null,
            "$ref": "#/components/schemas/MeanRetentionCalculation",
            "nullable": true
          },
          "minimumOccurrences": {
            "default": null,
            "title": "Minimumoccurrences",
            "type": "integer",
            "nullable": true
          },
          "period": {
            "default": "Day",
            "$ref": "#/components/schemas/RetentionPeriod",
            "nullable": true
          },
          "retentionCustomBrackets": {
            "default": null,
            "description": "Custom brackets for retention calculations",
            "title": "Retentioncustombrackets",
            "items": {
              "type": "number"
            },
            "type": "array",
            "nullable": true
          },
          "retentionReference": {
            "default": null,
            "description": "Whether retention is with regard to initial cohort size, or that of the previous period.",
            "$ref": "#/components/schemas/RetentionReference",
            "nullable": true
          },
          "retentionType": {
            "default": null,
            "$ref": "#/components/schemas/RetentionType",
            "nullable": true
          },
          "returningEntity": {
            "default": null,
            "$ref": "#/components/schemas/RetentionEntity",
            "nullable": true
          },
          "selectedInterval": {
            "default": null,
            "description": "The selected interval to display across all cohorts (null = show all intervals for each cohort)",
            "title": "Selectedinterval",
            "type": "integer",
            "nullable": true
          },
          "showTrendLines": {
            "default": null,
            "title": "Showtrendlines",
            "type": "boolean",
            "nullable": true
          },
          "targetEntity": {
            "default": null,
            "$ref": "#/components/schemas/RetentionEntity",
            "nullable": true
          },
          "timeWindowMode": {
            "default": null,
            "description": "The time window mode to use for retention calculations",
            "$ref": "#/components/schemas/TimeWindowMode",
            "nullable": true
          },
          "totalIntervals": {
            "default": 8,
            "title": "Totalintervals",
            "type": "integer",
            "nullable": true
          }
        },
        "title": "RetentionFilter",
        "type": "object"
      },
      "FunnelPathsFilter": {
        "additionalProperties": false,
        "properties": {
          "funnelPathType": {
            "default": null,
            "$ref": "#/components/schemas/FunnelPathType",
            "nullable": true
          },
          "funnelSource": {
            "$ref": "#/components/schemas/FunnelsQuery"
          },
          "funnelStep": {
            "default": null,
            "title": "Funnelstep",
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "funnelSource"
        ],
        "title": "FunnelPathsFilter",
        "type": "object"
      },
      "PathsFilter": {
        "additionalProperties": false,
        "properties": {
          "edgeLimit": {
            "default": 50,
            "title": "Edgelimit",
            "type": "integer",
            "nullable": true
          },
          "endPoint": {
            "default": null,
            "title": "Endpoint",
            "type": "string",
            "nullable": true
          },
          "excludeEvents": {
            "default": null,
            "title": "Excludeevents",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "includeEventTypes": {
            "default": null,
            "title": "Includeeventtypes",
            "items": {
              "$ref": "#/components/schemas/PathType"
            },
            "type": "array",
            "nullable": true
          },
          "localPathCleaningFilters": {
            "default": null,
            "title": "Localpathcleaningfilters",
            "items": {
              "$ref": "#/components/schemas/PathCleaningFilter"
            },
            "type": "array",
            "nullable": true
          },
          "maxEdgeWeight": {
            "default": null,
            "title": "Maxedgeweight",
            "type": "integer",
            "nullable": true
          },
          "minEdgeWeight": {
            "default": null,
            "title": "Minedgeweight",
            "type": "integer",
            "nullable": true
          },
          "pathDropoffKey": {
            "default": null,
            "description": "Relevant only within actors query",
            "title": "Pathdropoffkey",
            "type": "string",
            "nullable": true
          },
          "pathEndKey": {
            "default": null,
            "description": "Relevant only within actors query",
            "title": "Pathendkey",
            "type": "string",
            "nullable": true
          },
          "pathGroupings": {
            "default": null,
            "title": "Pathgroupings",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "pathReplacements": {
            "default": null,
            "title": "Pathreplacements",
            "type": "boolean",
            "nullable": true
          },
          "pathStartKey": {
            "default": null,
            "description": "Relevant only within actors query",
            "title": "Pathstartkey",
            "type": "string",
            "nullable": true
          },
          "pathsHogQLExpression": {
            "default": null,
            "title": "Pathshogqlexpression",
            "type": "string",
            "nullable": true
          },
          "showFullUrls": {
            "default": null,
            "title": "Showfullurls",
            "type": "boolean",
            "nullable": true
          },
          "startPoint": {
            "default": null,
            "title": "Startpoint",
            "type": "string",
            "nullable": true
          },
          "stepLimit": {
            "default": 5,
            "title": "Steplimit",
            "type": "integer",
            "nullable": true
          }
        },
        "title": "PathsFilter",
        "type": "object"
      },
      "PathsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "$ref": "#/components/schemas/PathsLink"
            },
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "PathsQueryResponse",
        "type": "object"
      },
      "StickinessQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "StickinessQueryResponse",
        "type": "object"
      },
      "StickinessFilter": {
        "additionalProperties": false,
        "properties": {
          "computedAs": {
            "default": null,
            "$ref": "#/components/schemas/StickinessComputationMode",
            "nullable": true
          },
          "display": {
            "default": null,
            "$ref": "#/components/schemas/ChartDisplayType",
            "nullable": true
          },
          "hiddenLegendIndexes": {
            "default": null,
            "title": "Hiddenlegendindexes",
            "items": {
              "type": "integer"
            },
            "type": "array",
            "nullable": true
          },
          "resultCustomizationBy": {
            "default": "value",
            "description": "Whether result datasets are associated by their values or by their order.",
            "$ref": "#/components/schemas/ResultCustomizationBy",
            "nullable": true
          },
          "resultCustomizations": {
            "default": null,
            "description": "Customizations for the appearance of result datasets.",
            "title": "Resultcustomizations",
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ResultCustomizationByValue"
                },
                "type": "object"
              },
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ResultCustomizationByPosition"
                },
                "type": "object"
              }
            ],
            "nullable": true
          },
          "showLegend": {
            "default": null,
            "title": "Showlegend",
            "type": "boolean",
            "nullable": true
          },
          "showMultipleYAxes": {
            "default": null,
            "title": "Showmultipleyaxes",
            "type": "boolean",
            "nullable": true
          },
          "showValuesOnSeries": {
            "default": null,
            "title": "Showvaluesonseries",
            "type": "boolean",
            "nullable": true
          },
          "stickinessCriteria": {
            "default": null,
            "$ref": "#/components/schemas/StickinessCriteria",
            "nullable": true
          }
        },
        "title": "StickinessFilter",
        "type": "object"
      },
      "LifecycleFilter": {
        "additionalProperties": false,
        "properties": {
          "showLegend": {
            "default": false,
            "title": "Showlegend",
            "type": "boolean",
            "nullable": true
          },
          "showValuesOnSeries": {
            "default": null,
            "title": "Showvaluesonseries",
            "type": "boolean",
            "nullable": true
          },
          "stacked": {
            "default": true,
            "title": "Stacked",
            "type": "boolean",
            "nullable": true
          },
          "toggledLifecycles": {
            "default": null,
            "title": "Toggledlifecycles",
            "items": {
              "$ref": "#/components/schemas/LifecycleToggle"
            },
            "type": "array",
            "nullable": true
          }
        },
        "title": "LifecycleFilter",
        "type": "object"
      },
      "LifecycleQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "title": "Results",
            "type": "array"
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "LifecycleQueryResponse",
        "type": "object"
      },
      "WebStatsBreakdown": {
        "enum": [
          "Page",
          "InitialPage",
          "ExitPage",
          "ExitClick",
          "PreviousPage",
          "ScreenName",
          "InitialChannelType",
          "InitialReferringDomain",
          "InitialReferringURL",
          "InitialUTMSource",
          "InitialUTMCampaign",
          "InitialUTMMedium",
          "InitialUTMTerm",
          "InitialUTMContent",
          "InitialUTMSourceMediumCampaign",
          "Browser",
          "OS",
          "Viewport",
          "DeviceType",
          "Country",
          "Region",
          "City",
          "Timezone",
          "Language",
          "FrustrationMetrics"
        ],
        "title": "WebStatsBreakdown",
        "type": "string"
      },
      "WebAnalyticsOrderByFields": {
        "enum": [
          "Visitors",
          "Views",
          "AvgTimeOnPage",
          "Clicks",
          "BounceRate",
          "AverageScrollPercentage",
          "ScrollGt80Percentage",
          "TotalConversions",
          "UniqueConversions",
          "ConversionRate",
          "ConvertingUsers",
          "RageClicks",
          "DeadClicks",
          "Errors"
        ],
        "title": "WebAnalyticsOrderByFields",
        "type": "string"
      },
      "WebAnalyticsOrderByDirection": {
        "enum": [
          "ASC",
          "DESC"
        ],
        "title": "WebAnalyticsOrderByDirection",
        "type": "string"
      },
      "WebStatsTableQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hasMore": {
            "default": null,
            "title": "Hasmore",
            "type": "boolean",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "offset": {
            "default": null,
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {},
            "title": "Results",
            "type": "array"
          },
          "samplingRate": {
            "default": null,
            "$ref": "#/components/schemas/SamplingRate",
            "nullable": true
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "usedPreAggregatedTables": {
            "default": null,
            "title": "Usedpreaggregatedtables",
            "type": "boolean",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "WebStatsTableQueryResponse",
        "type": "object"
      },
      "WebAnalyticsSampling": {
        "additionalProperties": false,
        "properties": {
          "enabled": {
            "default": null,
            "title": "Enabled",
            "type": "boolean",
            "nullable": true
          },
          "forceSamplingRate": {
            "default": null,
            "$ref": "#/components/schemas/SamplingRate",
            "nullable": true
          }
        },
        "title": "WebAnalyticsSampling",
        "type": "object"
      },
      "WebOverviewQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "dateFrom": {
            "default": null,
            "title": "Datefrom",
            "type": "string",
            "nullable": true
          },
          "dateTo": {
            "default": null,
            "title": "Dateto",
            "type": "string",
            "nullable": true
          },
          "error": {
            "default": null,
            "description": "Query error. Returned only if 'explain' or `modifiers.debug` is true. Throws an error otherwise.",
            "title": "Error",
            "type": "string",
            "nullable": true
          },
          "hogql": {
            "default": null,
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string",
            "nullable": true
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "query_status": {
            "default": null,
            "description": "Query status indicates whether next to the provided data, a query is still running.",
            "$ref": "#/components/schemas/QueryStatus",
            "nullable": true
          },
          "resolved_date_range": {
            "default": null,
            "description": "The date range used for the query",
            "$ref": "#/components/schemas/ResolvedDateRangeResponse",
            "nullable": true
          },
          "results": {
            "items": {
              "$ref": "#/components/schemas/WebOverviewItem"
            },
            "title": "Results",
            "type": "array"
          },
          "samplingRate": {
            "default": null,
            "$ref": "#/components/schemas/SamplingRate",
            "nullable": true
          },
          "timings": {
            "default": null,
            "description": "Measured timings for different parts of the query generation process",
            "title": "Timings",
            "items": {
              "$ref": "#/components/schemas/QueryTiming"
            },
            "type": "array",
            "nullable": true
          },
          "usedPreAggregatedTables": {
            "default": null,
            "title": "Usedpreaggregatedtables",
            "type": "boolean",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "WebOverviewQueryResponse",
        "type": "object"
      },
      "BounceRatePageViewMode": {
        "enum": [
          "count_pageviews",
          "uniq_urls",
          "uniq_page_screen_autocaptures"
        ],
        "title": "BounceRatePageViewMode",
        "type": "string"
      },
      "CustomChannelRule": {
        "additionalProperties": false,
        "properties": {
          "channel_type": {
            "title": "Channel Type",
            "type": "string"
          },
          "combiner": {
            "$ref": "#/components/schemas/FilterLogicalOperator"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "items": {
            "items": {
              "$ref": "#/components/schemas/CustomChannelCondition"
            },
            "title": "Items",
            "type": "array"
          }
        },
        "required": [
          "channel_type",
          "combiner",
          "id",
          "items"
        ],
        "title": "CustomChannelRule",
        "type": "object"
      },
      "DataWarehouseEventsModifier": {
        "additionalProperties": false,
        "properties": {
          "distinct_id_field": {
            "title": "Distinct Id Field",
            "type": "string"
          },
          "id_field": {
            "title": "Id Field",
            "type": "string"
          },
          "table_name": {
            "title": "Table Name",
            "type": "string"
          },
          "timestamp_field": {
            "title": "Timestamp Field",
            "type": "string"
          }
        },
        "required": [
          "distinct_id_field",
          "id_field",
          "table_name",
          "timestamp_field"
        ],
        "title": "DataWarehouseEventsModifier",
        "type": "object"
      },
      "InCohortVia": {
        "enum": [
          "auto",
          "leftjoin",
          "subquery",
          "leftjoin_conjoined"
        ],
        "title": "InCohortVia",
        "type": "string"
      },
      "InlineCohortCalculation": {
        "enum": [
          "off",
          "auto",
          "always"
        ],
        "title": "InlineCohortCalculation",
        "type": "string"
      },
      "MaterializationMode": {
        "enum": [
          "auto",
          "legacy_null_as_string",
          "legacy_null_as_null",
          "disabled"
        ],
        "title": "MaterializationMode",
        "type": "string"
      },
      "MaterializedColumnsOptimizationMode": {
        "enum": [
          "disabled",
          "optimized"
        ],
        "title": "MaterializedColumnsOptimizationMode",
        "type": "string"
      },
      "PersonsArgMaxVersion": {
        "enum": [
          "auto",
          "v1",
          "v2"
        ],
        "title": "PersonsArgMaxVersion",
        "type": "string"
      },
      "PersonsJoinMode": {
        "enum": [
          "inner",
          "left"
        ],
        "title": "PersonsJoinMode",
        "type": "string"
      },
      "PersonsOnEventsMode": {
        "enum": [
          "disabled",
          "person_id_no_override_properties_on_events",
          "person_id_override_properties_on_events",
          "person_id_override_properties_joined"
        ],
        "title": "PersonsOnEventsMode",
        "type": "string"
      },
      "PropertyGroupsMode": {
        "enum": [
          "enabled",
          "disabled",
          "optimized"
        ],
        "title": "PropertyGroupsMode",
        "type": "string"
      },
      "SessionTableVersion": {
        "enum": [
          "auto",
          "v1",
          "v2",
          "v3"
        ],
        "title": "SessionTableVersion",
        "type": "string"
      },
      "SessionsV2JoinMode": {
        "enum": [
          "string",
          "uuid"
        ],
        "title": "SessionsV2JoinMode",
        "type": "string"
      },
      "HogQLMetadataResponse": {
        "additionalProperties": false,
        "properties": {
          "ch_table_names": {
            "default": null,
            "title": "Ch Table Names",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "errors": {
            "items": {
              "$ref": "#/components/schemas/HogQLNotice"
            },
            "title": "Errors",
            "type": "array"
          },
          "isUsingIndices": {
            "default": null,
            "$ref": "#/components/schemas/QueryIndexUsage",
            "nullable": true
          },
          "isValid": {
            "default": null,
            "title": "Isvalid",
            "type": "boolean",
            "nullable": true
          },
          "notices": {
            "items": {
              "$ref": "#/components/schemas/HogQLNotice"
            },
            "title": "Notices",
            "type": "array"
          },
          "query": {
            "default": null,
            "title": "Query",
            "type": "string",
            "nullable": true
          },
          "table_names": {
            "default": null,
            "title": "Table Names",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "warnings": {
            "items": {
              "$ref": "#/components/schemas/HogQLNotice"
            },
            "title": "Warnings",
            "type": "array"
          }
        },
        "required": [
          "errors",
          "notices",
          "warnings"
        ],
        "title": "HogQLMetadataResponse",
        "type": "object"
      },
      "QueryStatus": {
        "additionalProperties": false,
        "properties": {
          "complete": {
            "default": false,
            "description": "Whether the query is still running. Will be true if the query is complete, even if it errored. Either result or error will be set.",
            "title": "Complete",
            "type": "boolean",
            "nullable": true
          },
          "dashboard_id": {
            "default": null,
            "title": "Dashboard Id",
            "type": "integer",
            "nullable": true
          },
          "end_time": {
            "default": null,
            "description": "When did the query execution task finish (whether successfully or not).",
            "title": "End Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "error": {
            "default": false,
            "description": "If the query failed, this will be set to true. More information can be found in the error_message field.",
            "title": "Error",
            "type": "boolean",
            "nullable": true
          },
          "error_message": {
            "default": null,
            "title": "Error Message",
            "type": "string",
            "nullable": true
          },
          "expiration_time": {
            "default": null,
            "title": "Expiration Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "insight_id": {
            "default": null,
            "title": "Insight Id",
            "type": "integer",
            "nullable": true
          },
          "labels": {
            "default": null,
            "title": "Labels",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "pickup_time": {
            "default": null,
            "description": "When was the query execution task picked up by a worker.",
            "title": "Pickup Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "query_async": {
            "default": true,
            "description": "ONLY async queries use QueryStatus.",
            "title": "Query Async",
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "query_progress": {
            "default": null,
            "$ref": "#/components/schemas/ClickhouseQueryProgress",
            "nullable": true
          },
          "results": {
            "default": null,
            "title": "Results",
            "nullable": true
          },
          "start_time": {
            "default": null,
            "description": "When was query execution task enqueued.",
            "title": "Start Time",
            "format": "date-time",
            "type": "string",
            "nullable": true
          },
          "task_id": {
            "default": null,
            "title": "Task Id",
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "title": "Team Id",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "team_id"
        ],
        "title": "QueryStatus",
        "type": "object"
      },
      "ResolvedDateRangeResponse": {
        "additionalProperties": false,
        "properties": {
          "date_from": {
            "format": "date-time",
            "title": "Date From",
            "type": "string"
          },
          "date_to": {
            "format": "date-time",
            "title": "Date To",
            "type": "string"
          }
        },
        "required": [
          "date_from",
          "date_to"
        ],
        "title": "ResolvedDateRangeResponse",
        "type": "object"
      },
      "QueryTiming": {
        "additionalProperties": false,
        "properties": {
          "k": {
            "description": "Key. Shortened to 'k' to save on data.",
            "title": "K",
            "type": "string"
          },
          "t": {
            "description": "Time in seconds. Shortened to 't' to save on data.",
            "title": "T",
            "type": "number"
          }
        },
        "required": [
          "k",
          "t"
        ],
        "title": "QueryTiming",
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
      "FilterLogicalOperator": {
        "enum": [
          "AND",
          "OR"
        ],
        "title": "FilterLogicalOperator",
        "type": "string"
      },
      "PropertyGroupFilterValue": {
        "additionalProperties": false,
        "properties": {
          "type": {
            "$ref": "#/components/schemas/FilterLogicalOperator"
          },
          "values": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/PropertyGroupFilterValue"
                },
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
            "title": "Values",
            "type": "array"
          }
        },
        "required": [
          "type",
          "values"
        ],
        "title": "PropertyGroupFilterValue",
        "type": "object"
      },
      "BoxPlotDatum": {
        "additionalProperties": false,
        "properties": {
          "day": {
            "title": "Day",
            "type": "string"
          },
          "label": {
            "title": "Label",
            "type": "string"
          },
          "max": {
            "title": "Max",
            "type": "number"
          },
          "mean": {
            "title": "Mean",
            "type": "number"
          },
          "median": {
            "title": "Median",
            "type": "number"
          },
          "min": {
            "title": "Min",
            "type": "number"
          },
          "p25": {
            "title": "P25",
            "type": "number"
          },
          "p75": {
            "title": "P75",
            "type": "number"
          },
          "series_index": {
            "default": null,
            "title": "Series Index",
            "type": "integer",
            "nullable": true
          },
          "series_label": {
            "default": null,
            "title": "Series Label",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "day",
          "label",
          "max",
          "mean",
          "median",
          "min",
          "p25",
          "p75"
        ],
        "title": "BoxPlotDatum",
        "type": "object"
      },
      "BaseMathType": {
        "enum": [
          "total",
          "dau",
          "weekly_active",
          "monthly_active",
          "unique_session",
          "first_time_for_user",
          "first_matching_event_for_user"
        ],
        "title": "BaseMathType",
        "type": "string"
      },
      "FunnelMathType": {
        "enum": [
          "total",
          "first_time_for_user",
          "first_time_for_user_with_filters"
        ],
        "title": "FunnelMathType",
        "type": "string"
      },
      "PropertyMathType": {
        "enum": [
          "avg",
          "sum",
          "min",
          "max",
          "median",
          "p75",
          "p90",
          "p95",
          "p99"
        ],
        "title": "PropertyMathType",
        "type": "string"
      },
      "CountPerActorMathType": {
        "enum": [
          "avg_count_per_actor",
          "min_count_per_actor",
          "max_count_per_actor",
          "median_count_per_actor",
          "p75_count_per_actor",
          "p90_count_per_actor",
          "p95_count_per_actor",
          "p99_count_per_actor"
        ],
        "title": "CountPerActorMathType",
        "type": "string"
      },
      "ExperimentMetricMathType": {
        "enum": [
          "total",
          "sum",
          "unique_session",
          "min",
          "max",
          "avg",
          "dau",
          "unique_group",
          "hogql"
        ],
        "title": "ExperimentMetricMathType",
        "type": "string"
      },
      "CalendarHeatmapMathType": {
        "enum": [
          "total",
          "dau"
        ],
        "title": "CalendarHeatmapMathType",
        "type": "string"
      },
      "MathGroupTypeIndex": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "title": "MathGroupTypeIndex",
        "type": "number"
      },
      "RevenueCurrencyPropertyConfig": {
        "additionalProperties": false,
        "properties": {
          "property": {
            "default": null,
            "title": "Property",
            "type": "string",
            "nullable": true
          },
          "static": {
            "default": null,
            "$ref": "#/components/schemas/CurrencyCode",
            "nullable": true
          }
        },
        "title": "RevenueCurrencyPropertyConfig",
        "type": "object"
      },
      "AggregationAxisFormat": {
        "enum": [
          "numeric",
          "duration",
          "duration_ms",
          "percentage",
          "percentage_scaled",
          "currency",
          "short"
        ],
        "title": "AggregationAxisFormat",
        "type": "string"
      },
      "DetailedResultsAggregationType": {
        "enum": [
          "total",
          "average",
          "median"
        ],
        "title": "DetailedResultsAggregationType",
        "type": "string"
      },
      "ChartDisplayType": {
        "enum": [
          "Auto",
          "ActionsLineGraph",
          "ActionsBar",
          "ActionsUnstackedBar",
          "ActionsStackedBar",
          "ActionsAreaGraph",
          "ActionsLineGraphCumulative",
          "BoldNumber",
          "ActionsPie",
          "ActionsBarValue",
          "ActionsTable",
          "WorldMap",
          "CalendarHeatmap",
          "TwoDimensionalHeatmap",
          "BoxPlot"
        ],
        "title": "ChartDisplayType",
        "type": "string"
      },
      "TrendsFormulaNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "description": "Optional user-defined name for the formula",
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "formula": {
            "title": "Formula",
            "type": "string"
          }
        },
        "required": [
          "formula"
        ],
        "title": "TrendsFormulaNode",
        "type": "object"
      },
      "GoalLine": {
        "additionalProperties": false,
        "properties": {
          "borderColor": {
            "default": null,
            "title": "Bordercolor",
            "type": "string",
            "nullable": true
          },
          "displayIfCrossed": {
            "default": null,
            "title": "Displayifcrossed",
            "type": "boolean",
            "nullable": true
          },
          "displayLabel": {
            "default": null,
            "title": "Displaylabel",
            "type": "boolean",
            "nullable": true
          },
          "label": {
            "title": "Label",
            "type": "string"
          },
          "position": {
            "default": null,
            "$ref": "#/components/schemas/Position",
            "nullable": true
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "label",
          "value"
        ],
        "title": "GoalLine",
        "type": "object"
      },
      "ResultCustomizationBy": {
        "enum": [
          "value",
          "position"
        ],
        "title": "ResultCustomizationBy",
        "type": "string"
      },
      "ResultCustomizationByValue": {
        "additionalProperties": false,
        "properties": {
          "assignmentBy": {
            "default": "value",
            "title": "Assignmentby",
            "type": "string",
            "enum": [
              "value"
            ]
          },
          "color": {
            "default": null,
            "$ref": "#/components/schemas/DataColorToken",
            "nullable": true
          },
          "hidden": {
            "default": null,
            "title": "Hidden",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "ResultCustomizationByValue",
        "type": "object"
      },
      "ResultCustomizationByPosition": {
        "additionalProperties": false,
        "properties": {
          "assignmentBy": {
            "default": "position",
            "title": "Assignmentby",
            "type": "string",
            "enum": [
              "position"
            ]
          },
          "color": {
            "default": null,
            "$ref": "#/components/schemas/DataColorToken",
            "nullable": true
          },
          "hidden": {
            "default": null,
            "title": "Hidden",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "ResultCustomizationByPosition",
        "type": "object"
      },
      "YAxisScaleType": {
        "enum": [
          "log10",
          "linear"
        ],
        "title": "YAxisScaleType",
        "type": "string"
      },
      "BreakdownAttributionType": {
        "enum": [
          "first_touch",
          "last_touch",
          "all_events",
          "step"
        ],
        "title": "BreakdownAttributionType",
        "type": "string"
      },
      "FunnelExclusionEventsNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "event": {
            "default": null,
            "description": "The event or `null` for all events.",
            "title": "Event",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "funnelFromStep": {
            "title": "Funnelfromstep",
            "type": "integer"
          },
          "funnelToStep": {
            "title": "Funneltostep",
            "type": "integer"
          },
          "kind": {
            "default": "EventsNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "EventsNode"
            ]
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "description": "Columns to order by",
            "title": "Orderby",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "funnelFromStep",
          "funnelToStep"
        ],
        "title": "FunnelExclusionEventsNode",
        "type": "object"
      },
      "FunnelExclusionActionsNode": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
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
          },
          "funnelFromStep": {
            "title": "Funnelfromstep",
            "type": "integer"
          },
          "funnelToStep": {
            "title": "Funneltostep",
            "type": "integer"
          },
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "kind": {
            "default": "ActionsNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ActionsNode"
            ]
          },
          "math": {
            "default": null,
            "title": "Math",
            "anyOf": [
              {
                "$ref": "#/components/schemas/BaseMathType"
              },
              {
                "$ref": "#/components/schemas/FunnelMathType"
              },
              {
                "$ref": "#/components/schemas/PropertyMathType"
              },
              {
                "$ref": "#/components/schemas/CountPerActorMathType"
              },
              {
                "$ref": "#/components/schemas/ExperimentMetricMathType"
              },
              {
                "$ref": "#/components/schemas/CalendarHeatmapMathType"
              },
              {
                "type": "string",
                "enum": [
                  "unique_group"
                ]
              },
              {
                "type": "string",
                "enum": [
                  "hogql"
                ]
              }
            ],
            "nullable": true
          },
          "math_group_type_index": {
            "default": null,
            "$ref": "#/components/schemas/MathGroupTypeIndex",
            "nullable": true
          },
          "math_hogql": {
            "default": null,
            "title": "Math Hogql",
            "type": "string",
            "nullable": true
          },
          "math_multiplier": {
            "default": null,
            "title": "Math Multiplier",
            "type": "number",
            "nullable": true
          },
          "math_property": {
            "default": null,
            "title": "Math Property",
            "type": "string",
            "nullable": true
          },
          "math_property_revenue_currency": {
            "default": null,
            "$ref": "#/components/schemas/RevenueCurrencyPropertyConfig",
            "nullable": true
          },
          "math_property_type": {
            "default": null,
            "title": "Math Property Type",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "optionalInFunnel": {
            "default": null,
            "title": "Optionalinfunnel",
            "type": "boolean",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Properties configurable in the interface",
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
          },
          "response": {
            "default": null,
            "title": "Response",
            "additionalProperties": true,
            "type": "object",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "funnelFromStep",
          "funnelToStep",
          "id"
        ],
        "title": "FunnelExclusionActionsNode",
        "type": "object"
      },
      "StepOrderValue": {
        "enum": [
          "strict",
          "unordered",
          "ordered"
        ],
        "title": "StepOrderValue",
        "type": "string"
      },
      "FunnelStepReference": {
        "enum": [
          "total",
          "previous"
        ],
        "title": "FunnelStepReference",
        "type": "string"
      },
      "FunnelVizType": {
        "enum": [
          "steps",
          "time_to_convert",
          "trends",
          "flow"
        ],
        "title": "FunnelVizType",
        "type": "string"
      },
      "FunnelConversionWindowTimeUnit": {
        "enum": [
          "second",
          "minute",
          "hour",
          "day",
          "week",
          "month"
        ],
        "title": "FunnelConversionWindowTimeUnit",
        "type": "string"
      },
      "FunnelLayout": {
        "enum": [
          "horizontal",
          "vertical"
        ],
        "title": "FunnelLayout",
        "type": "string"
      },
      "RetentionResult": {
        "additionalProperties": false,
        "properties": {
          "breakdown_value": {
            "default": null,
            "description": "Optional breakdown value for retention cohorts",
            "title": "Breakdown Value",
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ],
            "nullable": true
          },
          "date": {
            "format": "date-time",
            "title": "Date",
            "type": "string"
          },
          "label": {
            "title": "Label",
            "type": "string"
          },
          "values": {
            "items": {
              "$ref": "#/components/schemas/RetentionValue"
            },
            "title": "Values",
            "type": "array"
          }
        },
        "required": [
          "date",
          "label",
          "values"
        ],
        "title": "RetentionResult",
        "type": "object"
      },
      "AggregationPropertyType": {
        "enum": [
          "event",
          "person"
        ],
        "title": "AggregationPropertyType",
        "type": "string"
      },
      "AggregationType": {
        "enum": [
          "count",
          "sum",
          "avg"
        ],
        "title": "AggregationType",
        "type": "string"
      },
      "RetentionDashboardDisplayType": {
        "enum": [
          "table_only",
          "graph_only",
          "all"
        ],
        "title": "RetentionDashboardDisplayType",
        "type": "string"
      },
      "MeanRetentionCalculation": {
        "enum": [
          "simple",
          "weighted",
          "none"
        ],
        "title": "MeanRetentionCalculation",
        "type": "string"
      },
      "RetentionPeriod": {
        "enum": [
          "Hour",
          "Day",
          "Week",
          "Month"
        ],
        "title": "RetentionPeriod",
        "type": "string"
      },
      "RetentionReference": {
        "enum": [
          "total",
          "previous"
        ],
        "title": "RetentionReference",
        "type": "string"
      },
      "RetentionType": {
        "enum": [
          "retention_recurring",
          "retention_first_time",
          "retention_first_ever_occurrence"
        ],
        "title": "RetentionType",
        "type": "string"
      },
      "RetentionEntity": {
        "additionalProperties": false,
        "properties": {
          "custom_name": {
            "default": null,
            "title": "Custom Name",
            "type": "string",
            "nullable": true
          },
          "id": {
            "default": null,
            "title": "Id",
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              }
            ],
            "nullable": true
          },
          "kind": {
            "default": null,
            "$ref": "#/components/schemas/RetentionEntityKind",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "order": {
            "default": null,
            "title": "Order",
            "type": "integer",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "filters on the event",
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
          },
          "type": {
            "default": null,
            "$ref": "#/components/schemas/EntityType",
            "nullable": true
          },
          "uuid": {
            "default": null,
            "title": "Uuid",
            "type": "string",
            "nullable": true
          }
        },
        "title": "RetentionEntity",
        "type": "object"
      },
      "TimeWindowMode": {
        "enum": [
          "strict_calendar_dates",
          "24_hour_windows"
        ],
        "title": "TimeWindowMode",
        "type": "string"
      },
      "FunnelPathType": {
        "enum": [
          "funnel_path_before_step",
          "funnel_path_between_steps",
          "funnel_path_after_step"
        ],
        "title": "FunnelPathType",
        "type": "string"
      },
      "PathType": {
        "enum": [
          "$pageview",
          "$screen",
          "custom_event",
          "hogql"
        ],
        "title": "PathType",
        "type": "string"
      },
      "PathCleaningFilter": {
        "additionalProperties": false,
        "properties": {
          "alias": {
            "default": null,
            "title": "Alias",
            "type": "string",
            "nullable": true
          },
          "order": {
            "default": null,
            "title": "Order",
            "type": "number",
            "nullable": true
          },
          "regex": {
            "default": null,
            "title": "Regex",
            "type": "string",
            "nullable": true
          }
        },
        "title": "PathCleaningFilter",
        "type": "object"
      },
      "PathsLink": {
        "additionalProperties": false,
        "properties": {
          "average_conversion_time": {
            "title": "Average Conversion Time",
            "type": "number"
          },
          "source": {
            "title": "Source",
            "type": "string"
          },
          "target": {
            "title": "Target",
            "type": "string"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "average_conversion_time",
          "source",
          "target",
          "value"
        ],
        "title": "PathsLink",
        "type": "object"
      },
      "StickinessComputationMode": {
        "enum": [
          "non_cumulative",
          "cumulative"
        ],
        "title": "StickinessComputationMode",
        "type": "string"
      },
      "StickinessCriteria": {
        "additionalProperties": false,
        "properties": {
          "operator": {
            "$ref": "#/components/schemas/StickinessOperator"
          },
          "value": {
            "title": "Value",
            "type": "integer"
          }
        },
        "required": [
          "operator",
          "value"
        ],
        "title": "StickinessCriteria",
        "type": "object"
      },
      "LifecycleToggle": {
        "enum": [
          "new",
          "resurrecting",
          "returning",
          "dormant"
        ],
        "title": "LifecycleToggle",
        "type": "string"
      },
      "SamplingRate": {
        "additionalProperties": false,
        "properties": {
          "denominator": {
            "default": null,
            "title": "Denominator",
            "type": "number",
            "nullable": true
          },
          "numerator": {
            "title": "Numerator",
            "type": "number"
          }
        },
        "required": [
          "numerator"
        ],
        "title": "SamplingRate",
        "type": "object"
      },
      "WebOverviewItem": {
        "additionalProperties": false,
        "properties": {
          "changeFromPreviousPct": {
            "default": null,
            "title": "Changefrompreviouspct",
            "type": "number",
            "nullable": true
          },
          "isIncreaseBad": {
            "default": null,
            "title": "Isincreasebad",
            "type": "boolean",
            "nullable": true
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "kind": {
            "$ref": "#/components/schemas/WebAnalyticsItemKind"
          },
          "previous": {
            "default": null,
            "title": "Previous",
            "type": "number",
            "nullable": true
          },
          "usedPreAggregatedTables": {
            "default": null,
            "title": "Usedpreaggregatedtables",
            "type": "boolean",
            "nullable": true
          },
          "value": {
            "default": null,
            "title": "Value",
            "type": "number",
            "nullable": true
          }
        },
        "required": [
          "key",
          "kind"
        ],
        "title": "WebOverviewItem",
        "type": "object"
      },
      "CustomChannelCondition": {
        "additionalProperties": false,
        "properties": {
          "id": {
            "title": "Id",
            "type": "string"
          },
          "key": {
            "$ref": "#/components/schemas/CustomChannelField"
          },
          "op": {
            "$ref": "#/components/schemas/CustomChannelOperator"
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "id",
          "key",
          "op"
        ],
        "title": "CustomChannelCondition",
        "type": "object"
      },
      "HogQLNotice": {
        "additionalProperties": false,
        "properties": {
          "end": {
            "default": null,
            "title": "End",
            "type": "integer",
            "nullable": true
          },
          "fix": {
            "default": null,
            "title": "Fix",
            "type": "string",
            "nullable": true
          },
          "message": {
            "title": "Message",
            "type": "string"
          },
          "start": {
            "default": null,
            "title": "Start",
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "message"
        ],
        "title": "HogQLNotice",
        "type": "object"
      },
      "QueryIndexUsage": {
        "enum": [
          "undecisive",
          "no",
          "partial",
          "yes"
        ],
        "title": "QueryIndexUsage",
        "type": "string"
      },
      "ClickhouseQueryProgress": {
        "additionalProperties": false,
        "properties": {
          "active_cpu_time": {
            "title": "Active Cpu Time",
            "type": "integer"
          },
          "bytes_read": {
            "title": "Bytes Read",
            "type": "integer"
          },
          "estimated_rows_total": {
            "title": "Estimated Rows Total",
            "type": "integer"
          },
          "rows_read": {
            "title": "Rows Read",
            "type": "integer"
          },
          "time_elapsed": {
            "title": "Time Elapsed",
            "type": "integer"
          }
        },
        "required": [
          "active_cpu_time",
          "bytes_read",
          "estimated_rows_total",
          "rows_read",
          "time_elapsed"
        ],
        "title": "ClickhouseQueryProgress",
        "type": "object"
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
      },
      "CurrencyCode": {
        "enum": [
          "AED",
          "AFN",
          "ALL",
          "AMD",
          "ANG",
          "AOA",
          "ARS",
          "AUD",
          "AWG",
          "AZN",
          "BAM",
          "BBD",
          "BDT",
          "BGN",
          "BHD",
          "BIF",
          "BMD",
          "BND",
          "BOB",
          "BRL",
          "BSD",
          "BTC",
          "BTN",
          "BWP",
          "BYN",
          "BZD",
          "CAD",
          "CDF",
          "CHF",
          "CLP",
          "CNY",
          "COP",
          "CRC",
          "CVE",
          "CZK",
          "DJF",
          "DKK",
          "DOP",
          "DZD",
          "EGP",
          "ERN",
          "ETB",
          "EUR",
          "FJD",
          "GBP",
          "GEL",
          "GHS",
          "GIP",
          "GMD",
          "GNF",
          "GTQ",
          "GYD",
          "HKD",
          "HNL",
          "HRK",
          "HTG",
          "HUF",
          "IDR",
          "ILS",
          "INR",
          "IQD",
          "IRR",
          "ISK",
          "JMD",
          "JOD",
          "JPY",
          "KES",
          "KGS",
          "KHR",
          "KMF",
          "KRW",
          "KWD",
          "KYD",
          "KZT",
          "LAK",
          "LBP",
          "LKR",
          "LRD",
          "LTL",
          "LVL",
          "LSL",
          "LYD",
          "MAD",
          "MDL",
          "MGA",
          "MKD",
          "MMK",
          "MNT",
          "MOP",
          "MRU",
          "MTL",
          "MUR",
          "MVR",
          "MWK",
          "MXN",
          "MYR",
          "MZN",
          "NAD",
          "NGN",
          "NIO",
          "NOK",
          "NPR",
          "NZD",
          "OMR",
          "PAB",
          "PEN",
          "PGK",
          "PHP",
          "PKR",
          "PLN",
          "PYG",
          "QAR",
          "RON",
          "RSD",
          "RUB",
          "RWF",
          "SAR",
          "SBD",
          "SCR",
          "SDG",
          "SEK",
          "SGD",
          "SRD",
          "SSP",
          "STN",
          "SYP",
          "SZL",
          "THB",
          "TJS",
          "TMT",
          "TND",
          "TOP",
          "TRY",
          "TTD",
          "TWD",
          "TZS",
          "UAH",
          "UGX",
          "USD",
          "UYU",
          "UZS",
          "VES",
          "VND",
          "VUV",
          "WST",
          "XAF",
          "XCD",
          "XOF",
          "XPF",
          "YER",
          "ZAR",
          "ZMW"
        ],
        "title": "CurrencyCode",
        "type": "string"
      },
      "Position": {
        "enum": [
          "start",
          "end"
        ],
        "title": "Position",
        "type": "string"
      },
      "DataColorToken": {
        "enum": [
          "preset-1",
          "preset-2",
          "preset-3",
          "preset-4",
          "preset-5",
          "preset-6",
          "preset-7",
          "preset-8",
          "preset-9",
          "preset-10",
          "preset-11",
          "preset-12",
          "preset-13",
          "preset-14",
          "preset-15"
        ],
        "title": "DataColorToken",
        "type": "string"
      },
      "RetentionValue": {
        "additionalProperties": false,
        "properties": {
          "aggregation_value": {
            "default": null,
            "title": "Aggregation Value",
            "type": "number",
            "nullable": true
          },
          "count": {
            "title": "Count",
            "type": "number"
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "count"
        ],
        "title": "RetentionValue",
        "type": "object"
      },
      "RetentionEntityKind": {
        "enum": [
          "ActionsNode",
          "EventsNode"
        ],
        "title": "RetentionEntityKind",
        "type": "string"
      },
      "EntityType": {
        "enum": [
          "actions",
          "events",
          "data_warehouse",
          "new_entity",
          "groups"
        ],
        "title": "EntityType",
        "type": "string"
      },
      "StickinessOperator": {
        "enum": [
          "gte",
          "lte",
          "exact"
        ],
        "title": "StickinessOperator",
        "type": "string"
      },
      "WebAnalyticsItemKind": {
        "enum": [
          "unit",
          "duration_s",
          "percentage",
          "currency"
        ],
        "title": "WebAnalyticsItemKind",
        "type": "string"
      },
      "CustomChannelField": {
        "enum": [
          "utm_source",
          "utm_medium",
          "utm_campaign",
          "referring_domain",
          "url",
          "pathname",
          "hostname"
        ],
        "title": "CustomChannelField",
        "type": "string"
      },
      "CustomChannelOperator": {
        "enum": [
          "exact",
          "is_not",
          "is_set",
          "is_not_set",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex"
        ],
        "title": "CustomChannelOperator",
        "type": "string"
      }
    }
  }
}
```
