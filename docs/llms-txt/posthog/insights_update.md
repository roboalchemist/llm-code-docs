# Source: https://posthog.com/docs/open-api-spec/insights_update.md

# insights_update

## OpenAPI

```json PUT /api/projects/{project_id}/insights/{id}/
{
  "paths": {
    "/api/projects/{project_id}/insights/{id}/": {
      "put": {
        "operationId": "insights_update",
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
            "description": "A unique integer value identifying this insight.",
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
          "insights"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Insight"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Insight"
                }
              },
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/Insight"
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
      "Insight": {
        "type": "object",
        "description": "Simplified serializer to speed response times when loading large amounts of objects.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "short_id": {
            "type": "string",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "derived_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "query": {
            "allOf": [
              {
                "$ref": "#/components/schemas/_InsightQuerySchema"
              }
            ],
            "nullable": true
          },
          "order": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "deleted": {
            "type": "boolean"
          },
          "dashboards": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "\n        DEPRECATED. Will be removed in a future release. Use dashboard_tiles instead.\n        A dashboard ID for each of the dashboards that this insight is displayed on.\n        "
          },
          "dashboard_tiles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DashboardTileBasic"
            },
            "readOnly": true,
            "description": "\n    A dashboard tile ID and dashboard_id for each of the dashboards that this insight is displayed on.\n    "
          },
          "last_refresh": {
            "type": "string",
            "readOnly": true,
            "description": "\n    The datetime this insight's results were generated.\n    If added to one or more dashboards the insight can be refreshed separately on each.\n    Returns the appropriate last_refresh datetime for the context the insight is viewed in\n    (see from_dashboard query parameter).\n    "
          },
          "cache_target_age": {
            "type": "string",
            "readOnly": true,
            "description": "The target age of the cached results for this insight."
          },
          "next_allowed_client_refresh": {
            "type": "string",
            "readOnly": true,
            "description": "\n    The earliest possible datetime at which we'll allow the cached results for this insight to be refreshed\n    by querying the database.\n    "
          },
          "result": {
            "type": "string",
            "readOnly": true
          },
          "hasMore": {
            "type": "string",
            "readOnly": true
          },
          "columns": {
            "type": "string",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "description": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "favorited": {
            "type": "boolean"
          },
          "last_modified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "last_modified_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "is_sample": {
            "type": "boolean",
            "readOnly": true
          },
          "effective_restriction_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EffectiveRestrictionLevelEnum"
              }
            ],
            "readOnly": true
          },
          "effective_privilege_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EffectivePrivilegeLevelEnum"
              }
            ],
            "readOnly": true
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          },
          "timezone": {
            "type": "string",
            "readOnly": true,
            "description": "The timezone this chart is displayed in."
          },
          "is_cached": {
            "type": "string",
            "readOnly": true
          },
          "query_status": {
            "type": "string",
            "readOnly": true
          },
          "hogql": {
            "type": "string",
            "readOnly": true
          },
          "types": {
            "type": "string",
            "readOnly": true
          },
          "resolved_date_range": {
            "type": "string",
            "readOnly": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "alerts": {
            "type": "string",
            "readOnly": true
          },
          "last_viewed_at": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "alerts",
          "cache_target_age",
          "columns",
          "created_at",
          "created_by",
          "dashboard_tiles",
          "effective_privilege_level",
          "effective_restriction_level",
          "hasMore",
          "hogql",
          "id",
          "is_cached",
          "is_sample",
          "last_modified_at",
          "last_modified_by",
          "last_refresh",
          "last_viewed_at",
          "next_allowed_client_refresh",
          "query_status",
          "resolved_date_range",
          "result",
          "short_id",
          "timezone",
          "types",
          "updated_at",
          "user_access_level"
        ]
      },
      "_InsightQuerySchema": {
        "description": "The query definition for this insight. The `kind` field determines the query type:\n- `InsightVizNode` — product analytics (trends, funnels, retention, paths, stickiness, lifecycle)\n- `DataVisualizationNode` — SQL insights using HogQL\n- `DataTableNode` — raw data tables\n- `HogQuery` — Hog language queries",
        "discriminator": {
          "mapping": {
            "DataTableNode": "#/components/schemas/DataTableNode",
            "DataVisualizationNode": "#/components/schemas/DataVisualizationNode",
            "HogQuery": "#/components/schemas/HogQuery",
            "InsightVizNode": "#/components/schemas/InsightVizNode"
          },
          "propertyName": "kind"
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/InsightVizNode"
          },
          {
            "$ref": "#/components/schemas/DataTableNode"
          },
          {
            "$ref": "#/components/schemas/DataVisualizationNode"
          },
          {
            "$ref": "#/components/schemas/HogQuery"
          }
        ],
        "title": "_InsightQuerySchema"
      },
      "DashboardTileBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "dashboard_id": {
            "type": "integer",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "nullable": true
          }
        },
        "required": [
          "dashboard_id",
          "id"
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
      "EffectiveRestrictionLevelEnum": {
        "enum": [
          21,
          37
        ],
        "type": "integer"
      },
      "EffectivePrivilegeLevelEnum": {
        "enum": [
          21,
          37
        ],
        "type": "integer"
      },
      "InsightVizNode": {
        "additionalProperties": false,
        "properties": {
          "embedded": {
            "default": null,
            "description": "Query is embedded inside another bordered component",
            "title": "Embedded",
            "type": "boolean",
            "nullable": true
          },
          "full": {
            "default": null,
            "description": "Show with most visual options enabled. Used in insight scene.",
            "title": "Full",
            "type": "boolean",
            "nullable": true
          },
          "hidePersonsModal": {
            "default": null,
            "title": "Hidepersonsmodal",
            "type": "boolean",
            "nullable": true
          },
          "hideTooltipOnScroll": {
            "default": null,
            "title": "Hidetooltiponscroll",
            "type": "boolean",
            "nullable": true
          },
          "kind": {
            "default": "InsightVizNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "InsightVizNode"
            ]
          },
          "showCorrelationTable": {
            "default": null,
            "title": "Showcorrelationtable",
            "type": "boolean",
            "nullable": true
          },
          "showFilters": {
            "default": null,
            "title": "Showfilters",
            "type": "boolean",
            "nullable": true
          },
          "showHeader": {
            "default": null,
            "title": "Showheader",
            "type": "boolean",
            "nullable": true
          },
          "showLastComputation": {
            "default": null,
            "title": "Showlastcomputation",
            "type": "boolean",
            "nullable": true
          },
          "showLastComputationRefresh": {
            "default": null,
            "title": "Showlastcomputationrefresh",
            "type": "boolean",
            "nullable": true
          },
          "showResults": {
            "default": null,
            "title": "Showresults",
            "type": "boolean",
            "nullable": true
          },
          "showTable": {
            "default": null,
            "title": "Showtable",
            "type": "boolean",
            "nullable": true
          },
          "source": {
            "discriminator": {
              "mapping": {
                "FunnelsQuery": "#/components/schemas/FunnelsQuery",
                "LifecycleQuery": "#/components/schemas/LifecycleQuery",
                "PathsQuery": "#/components/schemas/PathsQuery",
                "RetentionQuery": "#/components/schemas/RetentionQuery",
                "StickinessQuery": "#/components/schemas/StickinessQuery",
                "TrendsQuery": "#/components/schemas/TrendsQuery",
                "WebOverviewQuery": "#/components/schemas/WebOverviewQuery",
                "WebStatsTableQuery": "#/components/schemas/WebStatsTableQuery"
              },
              "propertyName": "kind"
            },
            "oneOf": [
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
            "title": "Source"
          },
          "suppressSessionAnalysisWarning": {
            "default": null,
            "title": "Suppresssessionanalysiswarning",
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          },
          "vizSpecificOptions": {
            "default": null,
            "$ref": "#/components/schemas/VizSpecificOptions",
            "nullable": true
          }
        },
        "required": [
          "source"
        ],
        "title": "InsightVizNode",
        "type": "object"
      },
      "DataTableNode": {
        "additionalProperties": false,
        "properties": {
          "allowSorting": {
            "default": null,
            "description": "Can the user click on column headers to sort the table? (default: true)",
            "title": "Allowsorting",
            "type": "boolean",
            "nullable": true
          },
          "columns": {
            "default": null,
            "description": "Columns shown in the table, unless the `source` provides them.",
            "title": "Columns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "context": {
            "default": null,
            "description": "Context for the table, used by components like ColumnConfigurator",
            "$ref": "#/components/schemas/DataTableNodeViewPropsContext",
            "nullable": true
          },
          "contextKey": {
            "default": null,
            "description": "Context key for universal column configuration (e.g., \"survey:123\")",
            "title": "Contextkey",
            "type": "string",
            "nullable": true
          },
          "defaultColumns": {
            "default": null,
            "description": "Default columns to use when resetting column configuration",
            "title": "Defaultcolumns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "embedded": {
            "default": null,
            "description": "Uses the embedded version of LemonTable",
            "title": "Embedded",
            "type": "boolean",
            "nullable": true
          },
          "expandable": {
            "default": null,
            "description": "Can expand row to show raw event data (default: true)",
            "title": "Expandable",
            "type": "boolean",
            "nullable": true
          },
          "full": {
            "default": null,
            "description": "Show with most visual options enabled. Used in scenes.",
            "title": "Full",
            "type": "boolean",
            "nullable": true
          },
          "hiddenColumns": {
            "default": null,
            "description": "Columns that aren't shown in the table, even if in columns or returned data",
            "title": "Hiddencolumns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "kind": {
            "default": "DataTableNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "DataTableNode"
            ]
          },
          "pinnedColumns": {
            "default": null,
            "description": "Columns that are sticky when scrolling horizontally",
            "title": "Pinnedcolumns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "propertiesViaUrl": {
            "default": null,
            "description": "Link properties via the URL (default: false)",
            "title": "Propertiesviaurl",
            "type": "boolean",
            "nullable": true
          },
          "response": {
            "default": null,
            "title": "Response",
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "$ref": "#/components/schemas/Response"
              },
              {
                "$ref": "#/components/schemas/Response1"
              },
              {
                "$ref": "#/components/schemas/Response2"
              },
              {
                "$ref": "#/components/schemas/Response3"
              },
              {
                "$ref": "#/components/schemas/Response4"
              },
              {
                "$ref": "#/components/schemas/Response5"
              },
              {
                "$ref": "#/components/schemas/Response6"
              },
              {
                "$ref": "#/components/schemas/Response8"
              },
              {
                "$ref": "#/components/schemas/Response9"
              },
              {
                "$ref": "#/components/schemas/Response10"
              },
              {
                "$ref": "#/components/schemas/Response11"
              },
              {
                "$ref": "#/components/schemas/Response12"
              },
              {
                "$ref": "#/components/schemas/Response13"
              },
              {
                "$ref": "#/components/schemas/Response14"
              },
              {
                "$ref": "#/components/schemas/Response15"
              },
              {
                "$ref": "#/components/schemas/Response16"
              },
              {
                "$ref": "#/components/schemas/Response18"
              },
              {
                "$ref": "#/components/schemas/Response19"
              },
              {
                "$ref": "#/components/schemas/Response20"
              },
              {
                "$ref": "#/components/schemas/Response21"
              },
              {
                "$ref": "#/components/schemas/Response22"
              },
              {
                "$ref": "#/components/schemas/Response23"
              },
              {
                "$ref": "#/components/schemas/Response24"
              },
              {
                "$ref": "#/components/schemas/Response25"
              },
              {
                "$ref": "#/components/schemas/Response26"
              }
            ],
            "nullable": true
          },
          "showActions": {
            "default": null,
            "description": "Show the kebab menu at the end of the row",
            "title": "Showactions",
            "type": "boolean",
            "nullable": true
          },
          "showColumnConfigurator": {
            "default": null,
            "description": "Show a button to configure the table's columns if possible",
            "title": "Showcolumnconfigurator",
            "type": "boolean",
            "nullable": true
          },
          "showCount": {
            "default": null,
            "description": "Show count of total and filtered results",
            "title": "Showcount",
            "type": "boolean",
            "nullable": true
          },
          "showDateRange": {
            "default": null,
            "description": "Show date range selector",
            "title": "Showdaterange",
            "type": "boolean",
            "nullable": true
          },
          "showElapsedTime": {
            "default": null,
            "description": "Show the time it takes to run a query",
            "title": "Showelapsedtime",
            "type": "boolean",
            "nullable": true
          },
          "showEventFilter": {
            "default": null,
            "description": "Include an event filter above the table (EventsNode only)",
            "title": "Showeventfilter",
            "type": "boolean",
            "nullable": true
          },
          "showEventsFilter": {
            "default": null,
            "description": "Include an events filter above the table to filter by multiple events (EventsQuery only)",
            "title": "Showeventsfilter",
            "type": "boolean",
            "nullable": true
          },
          "showExport": {
            "default": null,
            "description": "Show the export button",
            "title": "Showexport",
            "type": "boolean",
            "nullable": true
          },
          "showHogQLEditor": {
            "default": null,
            "description": "Include a HogQL query editor above HogQL tables",
            "title": "Showhogqleditor",
            "type": "boolean",
            "nullable": true
          },
          "showOpenEditorButton": {
            "default": null,
            "description": "Show a button to open the current query as a new insight. (default: true)",
            "title": "Showopeneditorbutton",
            "type": "boolean",
            "nullable": true
          },
          "showPersistentColumnConfigurator": {
            "default": null,
            "description": "Show a button to configure and persist the table's default columns if possible",
            "title": "Showpersistentcolumnconfigurator",
            "type": "boolean",
            "nullable": true
          },
          "showPropertyFilter": {
            "default": null,
            "description": "Include a property filter above the table",
            "title": "Showpropertyfilter",
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "items": {
                  "$ref": "#/components/schemas/TaxonomicFilterGroupType"
                },
                "type": "array"
              }
            ],
            "nullable": true
          },
          "showRecordingColumn": {
            "default": null,
            "description": "Show a recording column for events with session recordings",
            "title": "Showrecordingcolumn",
            "type": "boolean",
            "nullable": true
          },
          "showReload": {
            "default": null,
            "description": "Show a reload button",
            "title": "Showreload",
            "type": "boolean",
            "nullable": true
          },
          "showResultsTable": {
            "default": null,
            "description": "Show a results table",
            "title": "Showresultstable",
            "type": "boolean",
            "nullable": true
          },
          "showSavedFilters": {
            "default": null,
            "description": "Show saved filters feature for this table (requires uniqueKey)",
            "title": "Showsavedfilters",
            "type": "boolean",
            "nullable": true
          },
          "showSavedQueries": {
            "default": null,
            "description": "Shows a list of saved queries",
            "title": "Showsavedqueries",
            "type": "boolean",
            "nullable": true
          },
          "showSearch": {
            "default": null,
            "description": "Include a free text search field (PersonsNode only)",
            "title": "Showsearch",
            "type": "boolean",
            "nullable": true
          },
          "showSourceQueryOptions": {
            "default": null,
            "description": "Show actors query options and back to source",
            "title": "Showsourcequeryoptions",
            "type": "boolean",
            "nullable": true
          },
          "showTableViews": {
            "default": null,
            "description": "Show table views feature for this table (requires uniqueKey)",
            "title": "Showtableviews",
            "type": "boolean",
            "nullable": true
          },
          "showTestAccountFilters": {
            "default": null,
            "description": "Show filter to exclude test accounts",
            "title": "Showtestaccountfilters",
            "type": "boolean",
            "nullable": true
          },
          "showTimings": {
            "default": null,
            "description": "Show a detailed query timing breakdown",
            "title": "Showtimings",
            "type": "boolean",
            "nullable": true
          },
          "source": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/EventsNode"
              },
              {
                "$ref": "#/components/schemas/EventsQuery"
              },
              {
                "$ref": "#/components/schemas/PersonsNode"
              },
              {
                "$ref": "#/components/schemas/ActorsQuery"
              },
              {
                "$ref": "#/components/schemas/GroupsQuery"
              },
              {
                "$ref": "#/components/schemas/HogQLQuery"
              },
              {
                "$ref": "#/components/schemas/WebOverviewQuery"
              },
              {
                "$ref": "#/components/schemas/WebStatsTableQuery"
              },
              {
                "$ref": "#/components/schemas/WebExternalClicksTableQuery"
              },
              {
                "$ref": "#/components/schemas/WebGoalsQuery"
              },
              {
                "$ref": "#/components/schemas/WebVitalsQuery"
              },
              {
                "$ref": "#/components/schemas/WebVitalsPathBreakdownQuery"
              },
              {
                "$ref": "#/components/schemas/SessionAttributionExplorerQuery"
              },
              {
                "$ref": "#/components/schemas/SessionsQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueAnalyticsGrossRevenueQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueAnalyticsMetricsQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueAnalyticsMRRQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueAnalyticsOverviewQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueAnalyticsTopCustomersQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueExampleEventsQuery"
              },
              {
                "$ref": "#/components/schemas/RevenueExampleDataWarehouseTablesQuery"
              },
              {
                "$ref": "#/components/schemas/MarketingAnalyticsTableQuery"
              },
              {
                "$ref": "#/components/schemas/MarketingAnalyticsAggregatedQuery"
              },
              {
                "$ref": "#/components/schemas/NonIntegratedConversionsTableQuery"
              },
              {
                "$ref": "#/components/schemas/ErrorTrackingQuery"
              },
              {
                "$ref": "#/components/schemas/ErrorTrackingIssueCorrelationQuery"
              },
              {
                "$ref": "#/components/schemas/ExperimentFunnelsQuery"
              },
              {
                "$ref": "#/components/schemas/ExperimentTrendsQuery"
              },
              {
                "$ref": "#/components/schemas/TracesQuery"
              },
              {
                "$ref": "#/components/schemas/TraceQuery"
              },
              {
                "$ref": "#/components/schemas/EndpointsUsageTableQuery"
              }
            ],
            "description": "Source of the events",
            "title": "Source"
          },
          "tags": {
            "default": null,
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
          "source"
        ],
        "title": "DataTableNode",
        "type": "object"
      },
      "DataVisualizationNode": {
        "additionalProperties": false,
        "properties": {
          "chartSettings": {
            "default": null,
            "$ref": "#/components/schemas/ChartSettings",
            "nullable": true
          },
          "display": {
            "default": null,
            "$ref": "#/components/schemas/ChartDisplayType",
            "nullable": true
          },
          "kind": {
            "default": "DataVisualizationNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "DataVisualizationNode"
            ]
          },
          "source": {
            "$ref": "#/components/schemas/HogQLQuery"
          },
          "tableSettings": {
            "default": null,
            "$ref": "#/components/schemas/TableSettings",
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
          "source"
        ],
        "title": "DataVisualizationNode",
        "type": "object"
      },
      "HogQuery": {
        "additionalProperties": false,
        "properties": {
          "code": {
            "default": null,
            "title": "Code",
            "type": "string",
            "nullable": true
          },
          "kind": {
            "default": "HogQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "HogQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/HogQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "HogQuery",
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
      "VizSpecificOptions": {
        "additionalProperties": false,
        "properties": {
          "ActionsPie": {
            "default": null,
            "$ref": "#/components/schemas/ActionsPie",
            "nullable": true
          },
          "RETENTION": {
            "default": null,
            "$ref": "#/components/schemas/RETENTION",
            "nullable": true
          }
        },
        "title": "VizSpecificOptions",
        "type": "object"
      },
      "DataTableNodeViewPropsContext": {
        "additionalProperties": false,
        "properties": {
          "eventDefinitionId": {
            "default": null,
            "title": "Eventdefinitionid",
            "type": "string",
            "nullable": true
          },
          "type": {
            "$ref": "#/components/schemas/DataTableNodeViewPropsContextType"
          }
        },
        "required": [
          "type"
        ],
        "title": "DataTableNodeViewPropsContext",
        "type": "object"
      },
      "Response": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
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
          "nextCursor": {
            "default": null,
            "description": "Cursor for fetching the next page of results",
            "title": "Nextcursor",
            "type": "string",
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
            "items": {
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "results",
          "types"
        ],
        "title": "Response",
        "type": "object"
      },
      "Response1": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "missing_actors_count": {
            "default": null,
            "title": "Missing Actors Count",
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
            "title": "Offset",
            "type": "integer"
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
              "items": {},
              "type": "array"
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "columns",
          "hogql",
          "limit",
          "offset",
          "results"
        ],
        "title": "Response1",
        "type": "object"
      },
      "Response2": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
          },
          "kind": {
            "default": "GroupsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "GroupsQuery"
            ]
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
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
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "limit",
          "offset",
          "results",
          "types"
        ],
        "title": "Response2",
        "type": "object"
      },
      "Response3": {
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
        "title": "Response3",
        "type": "object"
      },
      "Response4": {
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
        "title": "Response4",
        "type": "object"
      },
      "Response5": {
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
        "title": "Response5",
        "type": "object"
      },
      "Response6": {
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
          }
        },
        "required": [
          "results"
        ],
        "title": "Response6",
        "type": "object"
      },
      "Response8": {
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
              "$ref": "#/components/schemas/WebVitalsPathBreakdownResult"
            },
            "maxItems": 1,
            "minItems": 1,
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
        "title": "Response8",
        "type": "object"
      },
      "Response9": {
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "Response9",
        "type": "object"
      },
      "Response10": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
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
            "items": {
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "results",
          "types"
        ],
        "title": "Response10",
        "type": "object"
      },
      "Response11": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
          }
        },
        "required": [
          "results"
        ],
        "title": "Response11",
        "type": "object"
      },
      "Response12": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
        "title": "Response12",
        "type": "object"
      },
      "Response13": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
              "$ref": "#/components/schemas/RevenueAnalyticsMRRQueryResultItem"
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
        "title": "Response13",
        "type": "object"
      },
      "Response14": {
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
              "$ref": "#/components/schemas/RevenueAnalyticsOverviewItem"
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
        "title": "Response14",
        "type": "object"
      },
      "Response15": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
        "title": "Response15",
        "type": "object"
      },
      "Response16": {
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "Response16",
        "type": "object"
      },
      "Response18": {
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
            "items": {
              "items": {
                "$ref": "#/components/schemas/MarketingAnalyticsItem"
              },
              "type": "array"
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
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "Response18",
        "type": "object"
      },
      "Response19": {
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
            "additionalProperties": {
              "$ref": "#/components/schemas/MarketingAnalyticsItem"
            },
            "title": "Results",
            "type": "object"
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
          }
        },
        "required": [
          "results"
        ],
        "title": "Response19",
        "type": "object"
      },
      "Response20": {
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
            "items": {
              "items": {
                "$ref": "#/components/schemas/MarketingAnalyticsItem"
              },
              "type": "array"
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
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "Response20",
        "type": "object"
      },
      "Response21": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingIssue"
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
        "title": "Response21",
        "type": "object"
      },
      "Response22": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingCorrelatedIssue"
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
        "title": "Response22",
        "type": "object"
      },
      "Response23": {
        "additionalProperties": false,
        "properties": {
          "credible_intervals": {
            "additionalProperties": {
              "items": {
                "type": "number"
              },
              "type": "array"
            },
            "title": "Credible Intervals",
            "type": "object"
          },
          "expected_loss": {
            "title": "Expected Loss",
            "type": "number"
          },
          "funnels_query": {
            "default": null,
            "$ref": "#/components/schemas/FunnelsQuery",
            "nullable": true
          },
          "insight": {
            "items": {
              "items": {
                "additionalProperties": true,
                "type": "object"
              },
              "type": "array"
            },
            "title": "Insight",
            "type": "array"
          },
          "kind": {
            "default": "ExperimentFunnelsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentFunnelsQuery"
            ]
          },
          "probability": {
            "additionalProperties": {
              "type": "number"
            },
            "title": "Probability",
            "type": "object"
          },
          "significance_code": {
            "$ref": "#/components/schemas/ExperimentSignificanceCode"
          },
          "significant": {
            "title": "Significant",
            "type": "boolean"
          },
          "stats_version": {
            "default": null,
            "title": "Stats Version",
            "type": "integer",
            "nullable": true
          },
          "variants": {
            "items": {
              "$ref": "#/components/schemas/ExperimentVariantFunnelsBaseStats"
            },
            "title": "Variants",
            "type": "array"
          }
        },
        "required": [
          "credible_intervals",
          "expected_loss",
          "insight",
          "probability",
          "significance_code",
          "significant",
          "variants"
        ],
        "title": "Response23",
        "type": "object"
      },
      "Response24": {
        "additionalProperties": false,
        "properties": {
          "count_query": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQuery",
            "nullable": true
          },
          "credible_intervals": {
            "additionalProperties": {
              "items": {
                "type": "number"
              },
              "type": "array"
            },
            "title": "Credible Intervals",
            "type": "object"
          },
          "exposure_query": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQuery",
            "nullable": true
          },
          "insight": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "title": "Insight",
            "type": "array"
          },
          "kind": {
            "default": "ExperimentTrendsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentTrendsQuery"
            ]
          },
          "p_value": {
            "title": "P Value",
            "type": "number"
          },
          "probability": {
            "additionalProperties": {
              "type": "number"
            },
            "title": "Probability",
            "type": "object"
          },
          "significance_code": {
            "$ref": "#/components/schemas/ExperimentSignificanceCode"
          },
          "significant": {
            "title": "Significant",
            "type": "boolean"
          },
          "stats_version": {
            "default": null,
            "title": "Stats Version",
            "type": "integer",
            "nullable": true
          },
          "variants": {
            "items": {
              "$ref": "#/components/schemas/ExperimentVariantTrendsBaseStats"
            },
            "title": "Variants",
            "type": "array"
          }
        },
        "required": [
          "credible_intervals",
          "insight",
          "p_value",
          "probability",
          "significance_code",
          "significant",
          "variants"
        ],
        "title": "Response24",
        "type": "object"
      },
      "Response25": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/LLMTrace"
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
        "title": "Response25",
        "type": "object"
      },
      "Response26": {
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
          }
        },
        "required": [
          "results"
        ],
        "title": "Response26",
        "type": "object"
      },
      "TaxonomicFilterGroupType": {
        "enum": [
          "metadata",
          "actions",
          "cohorts",
          "cohorts_with_all",
          "data_warehouse",
          "data_warehouse_properties",
          "data_warehouse_person_properties",
          "elements",
          "events",
          "internal_events",
          "internal_event_properties",
          "event_properties",
          "event_feature_flags",
          "event_metadata",
          "numerical_event_properties",
          "person_properties",
          "pageview_urls",
          "pageview_events",
          "screens",
          "screen_events",
          "email_addresses",
          "autocapture_events",
          "custom_events",
          "wildcard",
          "groups",
          "persons",
          "feature_flags",
          "insights",
          "experiments",
          "plugins",
          "dashboards",
          "name_groups",
          "session_properties",
          "hogql_expression",
          "notebooks",
          "log_entries",
          "error_tracking_issues",
          "logs",
          "log_attributes",
          "log_resource_attributes",
          "replay",
          "replay_saved_filters",
          "revenue_analytics_properties",
          "resources",
          "error_tracking_properties",
          "activity_log_properties",
          "max_ai_context",
          "workflow_variables",
          "suggested_filters",
          "empty"
        ],
        "title": "TaxonomicFilterGroupType",
        "type": "string"
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
      "EventsQuery": {
        "additionalProperties": false,
        "properties": {
          "actionId": {
            "default": null,
            "description": "Show events matching a given action",
            "title": "Actionid",
            "type": "integer",
            "nullable": true
          },
          "after": {
            "default": null,
            "description": "Only fetch events that happened after this timestamp",
            "title": "After",
            "type": "string",
            "nullable": true
          },
          "before": {
            "default": null,
            "description": "Only fetch events that happened before this timestamp",
            "title": "Before",
            "type": "string",
            "nullable": true
          },
          "event": {
            "default": null,
            "description": "Limit to events matching this string",
            "title": "Event",
            "type": "string",
            "nullable": true
          },
          "events": {
            "default": null,
            "description": "Filter to events matching any of these event names",
            "title": "Events",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "description": "Filter test accounts",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/PropertyGroupFilter"
                },
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
            "type": "array",
            "nullable": true
          },
          "kind": {
            "default": "EventsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "EventsQuery"
            ]
          },
          "limit": {
            "default": null,
            "description": "Number of rows to return",
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
            "description": "Number of rows to skip before returning rows",
            "title": "Offset",
            "type": "integer",
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
          "personId": {
            "default": null,
            "description": "Show events for a given person",
            "title": "Personid",
            "type": "string",
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
            "$ref": "#/components/schemas/EventsQueryResponse",
            "nullable": true
          },
          "select": {
            "description": "Return a limited set of data. Required.",
            "items": {
              "type": "string"
            },
            "title": "Select",
            "type": "array"
          },
          "source": {
            "default": null,
            "description": "source for querying events for insights",
            "$ref": "#/components/schemas/InsightActorsQuery",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          },
          "where": {
            "default": null,
            "description": "HogQL filters to apply on returned data",
            "title": "Where",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "select"
        ],
        "title": "EventsQuery",
        "type": "object"
      },
      "PersonsNode": {
        "additionalProperties": false,
        "properties": {
          "cohort": {
            "default": null,
            "title": "Cohort",
            "type": "integer",
            "nullable": true
          },
          "distinctId": {
            "default": null,
            "title": "Distinctid",
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
            "default": "PersonsNode",
            "title": "Kind",
            "type": "string",
            "enum": [
              "PersonsNode"
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
          "search": {
            "default": null,
            "title": "Search",
            "type": "string",
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "PersonsNode",
        "type": "object"
      },
      "ActorsQuery": {
        "additionalProperties": false,
        "properties": {
          "fixedProperties": {
            "default": null,
            "description": "Currently only person filters supported. No filters for querying groups. See `filter_conditions()` in actor_strategies.py.",
            "title": "Fixedproperties",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/PersonPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/CohortPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/HogQLPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/EmptyPropertyFilter"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "kind": {
            "default": "ActorsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ActorsQuery"
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
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "default": null,
            "description": "Currently only person filters supported. No filters for querying groups. See `filter_conditions()` in actor_strategies.py.",
            "title": "Properties",
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/PersonPropertyFilter"
                    },
                    {
                      "$ref": "#/components/schemas/CohortPropertyFilter"
                    },
                    {
                      "$ref": "#/components/schemas/HogQLPropertyFilter"
                    },
                    {
                      "$ref": "#/components/schemas/EmptyPropertyFilter"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "$ref": "#/components/schemas/PropertyGroupFilterValue"
              }
            ],
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ActorsQueryResponse",
            "nullable": true
          },
          "search": {
            "default": null,
            "title": "Search",
            "type": "string",
            "nullable": true
          },
          "select": {
            "default": null,
            "title": "Select",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "source": {
            "default": null,
            "title": "Source",
            "anyOf": [
              {
                "$ref": "#/components/schemas/InsightActorsQuery"
              },
              {
                "$ref": "#/components/schemas/FunnelsActorsQuery"
              },
              {
                "$ref": "#/components/schemas/FunnelCorrelationActorsQuery"
              },
              {
                "$ref": "#/components/schemas/StickinessActorsQuery"
              },
              {
                "$ref": "#/components/schemas/HogQLQuery"
              }
            ],
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "ActorsQuery",
        "type": "object"
      },
      "GroupsQuery": {
        "additionalProperties": false,
        "properties": {
          "group_type_index": {
            "title": "Group Type Index",
            "type": "integer"
          },
          "kind": {
            "default": "GroupsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "GroupsQuery"
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
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "properties": {
            "default": null,
            "title": "Properties",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/GroupPropertyFilter"
                },
                {
                  "$ref": "#/components/schemas/HogQLPropertyFilter"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/GroupsQueryResponse",
            "nullable": true
          },
          "search": {
            "default": null,
            "title": "Search",
            "type": "string",
            "nullable": true
          },
          "select": {
            "default": null,
            "title": "Select",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "group_type_index"
        ],
        "title": "GroupsQuery",
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
      "WebExternalClicksTableQuery": {
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
            "default": "WebExternalClicksTableQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebExternalClicksTableQuery"
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
            "$ref": "#/components/schemas/WebExternalClicksTableQueryResponse",
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
          "stripQueryParams": {
            "default": null,
            "title": "Stripqueryparams",
            "type": "boolean",
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
        "title": "WebExternalClicksTableQuery",
        "type": "object"
      },
      "WebGoalsQuery": {
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
            "default": "WebGoalsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebGoalsQuery"
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
            "$ref": "#/components/schemas/WebGoalsQueryResponse",
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
        "title": "WebGoalsQuery",
        "type": "object"
      },
      "WebVitalsQuery": {
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
            "default": "WebVitalsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebVitalsQuery"
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
            "$ref": "#/components/schemas/WebGoalsQueryResponse",
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
          "source": {
            "discriminator": {
              "mapping": {
                "FunnelsQuery": "#/components/schemas/FunnelsQuery",
                "LifecycleQuery": "#/components/schemas/LifecycleQuery",
                "PathsQuery": "#/components/schemas/PathsQuery",
                "RetentionQuery": "#/components/schemas/RetentionQuery",
                "StickinessQuery": "#/components/schemas/StickinessQuery",
                "TrendsQuery": "#/components/schemas/TrendsQuery",
                "WebOverviewQuery": "#/components/schemas/WebOverviewQuery",
                "WebStatsTableQuery": "#/components/schemas/WebStatsTableQuery"
              },
              "propertyName": "kind"
            },
            "oneOf": [
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
            "title": "Source"
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
          "properties",
          "source"
        ],
        "title": "WebVitalsQuery",
        "type": "object"
      },
      "WebVitalsPathBreakdownQuery": {
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
            "default": "WebVitalsPathBreakdownQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "WebVitalsPathBreakdownQuery"
            ]
          },
          "metric": {
            "$ref": "#/components/schemas/WebVitalsMetric"
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
          "percentile": {
            "$ref": "#/components/schemas/WebVitalsPercentile"
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
            "$ref": "#/components/schemas/WebVitalsPathBreakdownQueryResponse",
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
          "thresholds": {
            "items": {
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "title": "Thresholds",
            "type": "array"
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
          "metric",
          "percentile",
          "properties",
          "thresholds"
        ],
        "title": "WebVitalsPathBreakdownQuery",
        "type": "object"
      },
      "SessionAttributionExplorerQuery": {
        "additionalProperties": false,
        "properties": {
          "filters": {
            "default": null,
            "$ref": "#/components/schemas/Filters",
            "nullable": true
          },
          "groupBy": {
            "items": {
              "$ref": "#/components/schemas/SessionAttributionGroupBy"
            },
            "title": "Groupby",
            "type": "array"
          },
          "kind": {
            "default": "SessionAttributionExplorerQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "SessionAttributionExplorerQuery"
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
          "response": {
            "default": null,
            "$ref": "#/components/schemas/SessionAttributionExplorerQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "groupBy"
        ],
        "title": "SessionAttributionExplorerQuery",
        "type": "object"
      },
      "SessionsQuery": {
        "additionalProperties": false,
        "properties": {
          "actionId": {
            "default": null,
            "description": "Filter sessions by action - sessions that contain events matching this action",
            "title": "Actionid",
            "type": "integer",
            "nullable": true
          },
          "after": {
            "default": null,
            "description": "Only fetch sessions that started after this timestamp",
            "title": "After",
            "type": "string",
            "nullable": true
          },
          "before": {
            "default": null,
            "description": "Only fetch sessions that started before this timestamp",
            "title": "Before",
            "type": "string",
            "nullable": true
          },
          "event": {
            "default": null,
            "description": "Filter sessions by event name - sessions that contain this event",
            "title": "Event",
            "type": "string",
            "nullable": true
          },
          "eventProperties": {
            "default": null,
            "description": "Event property filters - only applies when event or actionId is set",
            "title": "Eventproperties",
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
          "filterTestAccounts": {
            "default": null,
            "description": "Filter test accounts",
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "fixedProperties": {
            "default": null,
            "description": "Fixed properties in the query, can't be edited in the interface (e.g. scoping down by person)",
            "title": "Fixedproperties",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/PropertyGroupFilter"
                },
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
            "type": "array",
            "nullable": true
          },
          "kind": {
            "default": "SessionsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "SessionsQuery"
            ]
          },
          "limit": {
            "default": null,
            "description": "Number of rows to return",
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
            "description": "Number of rows to skip before returning rows",
            "title": "Offset",
            "type": "integer",
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
          "personId": {
            "default": null,
            "description": "Show sessions for a given person",
            "title": "Personid",
            "type": "string",
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
            "$ref": "#/components/schemas/SessionsQueryResponse",
            "nullable": true
          },
          "select": {
            "description": "Return a limited set of data. Required.",
            "items": {
              "type": "string"
            },
            "title": "Select",
            "type": "array"
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          },
          "where": {
            "default": null,
            "description": "HogQL filters to apply on returned data",
            "title": "Where",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "select"
        ],
        "title": "SessionsQuery",
        "type": "object"
      },
      "RevenueAnalyticsGrossRevenueQuery": {
        "additionalProperties": false,
        "properties": {
          "breakdown": {
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsBreakdown"
            },
            "title": "Breakdown",
            "type": "array"
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "interval": {
            "$ref": "#/components/schemas/SimpleIntervalType"
          },
          "kind": {
            "default": "RevenueAnalyticsGrossRevenueQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueAnalyticsGrossRevenueQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueAnalyticsGrossRevenueQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "breakdown",
          "interval",
          "properties"
        ],
        "title": "RevenueAnalyticsGrossRevenueQuery",
        "type": "object"
      },
      "RevenueAnalyticsMetricsQuery": {
        "additionalProperties": false,
        "properties": {
          "breakdown": {
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsBreakdown"
            },
            "title": "Breakdown",
            "type": "array"
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "interval": {
            "$ref": "#/components/schemas/SimpleIntervalType"
          },
          "kind": {
            "default": "RevenueAnalyticsMetricsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueAnalyticsMetricsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueAnalyticsMetricsQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "breakdown",
          "interval",
          "properties"
        ],
        "title": "RevenueAnalyticsMetricsQuery",
        "type": "object"
      },
      "RevenueAnalyticsMRRQuery": {
        "additionalProperties": false,
        "properties": {
          "breakdown": {
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsBreakdown"
            },
            "title": "Breakdown",
            "type": "array"
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "interval": {
            "$ref": "#/components/schemas/SimpleIntervalType"
          },
          "kind": {
            "default": "RevenueAnalyticsMRRQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueAnalyticsMRRQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueAnalyticsMRRQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "breakdown",
          "interval",
          "properties"
        ],
        "title": "RevenueAnalyticsMRRQuery",
        "type": "object"
      },
      "RevenueAnalyticsOverviewQuery": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "kind": {
            "default": "RevenueAnalyticsOverviewQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueAnalyticsOverviewQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueAnalyticsOverviewQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "properties"
        ],
        "title": "RevenueAnalyticsOverviewQuery",
        "type": "object"
      },
      "RevenueAnalyticsTopCustomersQuery": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "groupBy": {
            "$ref": "#/components/schemas/RevenueAnalyticsTopCustomersGroupBy"
          },
          "kind": {
            "default": "RevenueAnalyticsTopCustomersQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueAnalyticsTopCustomersQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RevenueAnalyticsPropertyFilter"
            },
            "title": "Properties"
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueAnalyticsTopCustomersQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "groupBy",
          "properties"
        ],
        "title": "RevenueAnalyticsTopCustomersQuery",
        "type": "object"
      },
      "RevenueExampleEventsQuery": {
        "additionalProperties": false,
        "properties": {
          "kind": {
            "default": "RevenueExampleEventsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueExampleEventsQuery"
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
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueExampleEventsQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "RevenueExampleEventsQuery",
        "type": "object"
      },
      "RevenueExampleDataWarehouseTablesQuery": {
        "additionalProperties": false,
        "properties": {
          "kind": {
            "default": "RevenueExampleDataWarehouseTablesQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "RevenueExampleDataWarehouseTablesQuery"
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
          "response": {
            "default": null,
            "$ref": "#/components/schemas/RevenueExampleDataWarehouseTablesQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "RevenueExampleDataWarehouseTablesQuery",
        "type": "object"
      },
      "MarketingAnalyticsTableQuery": {
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
            "description": "Compare to date range",
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
          "draftConversionGoal": {
            "default": null,
            "description": "Draft conversion goal that can be set in the UI without saving",
            "title": "Draftconversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ConversionGoalFilter1"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter2"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter3"
              }
            ],
            "nullable": true
          },
          "drillDownLevel": {
            "default": null,
            "description": "Drill-down hierarchy level: channel, source, or campaign (default)",
            "$ref": "#/components/schemas/MarketingAnalyticsDrillDownLevel",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "description": "Filter test accounts",
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
          "integrationFilter": {
            "default": null,
            "description": "Filter by integration type",
            "$ref": "#/components/schemas/IntegrationFilter",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "Interval for date range calculation (affects date_to rounding for hour vs day ranges)",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "MarketingAnalyticsTableQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "MarketingAnalyticsTableQuery"
            ]
          },
          "limit": {
            "default": null,
            "description": "Number of rows to return",
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
            "description": "Number of rows to skip before returning rows",
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "description": "Columns to order by - similar to EventsQuery format",
            "title": "Orderby",
            "items": {
              "items": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "$ref": "#/components/schemas/MarketingAnalyticsOrderByEnum"
                  }
                ]
              },
              "type": "array"
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
            "$ref": "#/components/schemas/MarketingAnalyticsTableQueryResponse",
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
          "select": {
            "default": null,
            "description": "Return a limited set of data. Will use default columns if empty.",
            "title": "Select",
            "items": {
              "type": "string"
            },
            "type": "array",
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
        "title": "MarketingAnalyticsTableQuery",
        "type": "object"
      },
      "MarketingAnalyticsAggregatedQuery": {
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
          "draftConversionGoal": {
            "default": null,
            "description": "Draft conversion goal that can be set in the UI without saving",
            "title": "Draftconversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ConversionGoalFilter1"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter2"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter3"
              }
            ],
            "nullable": true
          },
          "drillDownLevel": {
            "default": null,
            "description": "Drill-down hierarchy level: channel, source, or campaign (default)",
            "$ref": "#/components/schemas/MarketingAnalyticsDrillDownLevel",
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
          "integrationFilter": {
            "default": null,
            "description": "Filter by integration IDs",
            "$ref": "#/components/schemas/IntegrationFilter",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "Interval for date range calculation (affects date_to rounding for hour vs day ranges)",
            "$ref": "#/components/schemas/IntervalType",
            "nullable": true
          },
          "kind": {
            "default": "MarketingAnalyticsAggregatedQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "MarketingAnalyticsAggregatedQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
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
            "$ref": "#/components/schemas/MarketingAnalyticsAggregatedQueryResponse",
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
          "select": {
            "default": null,
            "description": "Return a limited set of data. Will use default columns if empty.",
            "title": "Select",
            "items": {
              "type": "string"
            },
            "type": "array",
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
        "title": "MarketingAnalyticsAggregatedQuery",
        "type": "object"
      },
      "NonIntegratedConversionsTableQuery": {
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
            "description": "Compare to date range",
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
          "draftConversionGoal": {
            "default": null,
            "description": "Draft conversion goal that can be set in the UI without saving",
            "title": "Draftconversiongoal",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ConversionGoalFilter1"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter2"
              },
              {
                "$ref": "#/components/schemas/ConversionGoalFilter3"
              }
            ],
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "description": "Filter test accounts",
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
            "default": "NonIntegratedConversionsTableQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "NonIntegratedConversionsTableQuery"
            ]
          },
          "limit": {
            "default": null,
            "description": "Number of rows to return",
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
            "description": "Number of rows to skip before returning rows",
            "title": "Offset",
            "type": "integer",
            "nullable": true
          },
          "orderBy": {
            "default": null,
            "description": "Columns to order by",
            "title": "Orderby",
            "items": {
              "items": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "$ref": "#/components/schemas/MarketingAnalyticsOrderByEnum"
                  }
                ]
              },
              "type": "array"
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
            "$ref": "#/components/schemas/NonIntegratedConversionsTableQueryResponse",
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
          "select": {
            "default": null,
            "description": "Return a limited set of data. Will use default columns if empty.",
            "title": "Select",
            "items": {
              "type": "string"
            },
            "type": "array",
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
        "title": "NonIntegratedConversionsTableQuery",
        "type": "object"
      },
      "ErrorTrackingQuery": {
        "additionalProperties": false,
        "properties": {
          "assignee": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueAssignee",
            "nullable": true
          },
          "dateRange": {
            "$ref": "#/components/schemas/DateRange"
          },
          "filterGroup": {
            "default": null,
            "$ref": "#/components/schemas/PropertyGroupFilter",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "groupKey": {
            "default": null,
            "title": "Groupkey",
            "type": "string",
            "nullable": true
          },
          "groupTypeIndex": {
            "default": null,
            "title": "Grouptypeindex",
            "type": "integer",
            "nullable": true
          },
          "issueId": {
            "default": null,
            "title": "Issueid",
            "type": "string",
            "nullable": true
          },
          "kind": {
            "default": "ErrorTrackingQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ErrorTrackingQuery"
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
            "$ref": "#/components/schemas/OrderBy1"
          },
          "orderDirection": {
            "default": null,
            "$ref": "#/components/schemas/OrderDirection1",
            "nullable": true
          },
          "personId": {
            "default": null,
            "title": "Personid",
            "type": "string",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingQueryResponse",
            "nullable": true
          },
          "searchQuery": {
            "default": null,
            "title": "Searchquery",
            "type": "string",
            "nullable": true
          },
          "status": {
            "default": null,
            "title": "ErrorTrackingQueryStatus",
            "anyOf": [
              {
                "$ref": "#/components/schemas/ErrorTrackingIssueStatus"
              },
              {
                "type": "string"
              }
            ],
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "useQueryV2": {
            "default": null,
            "description": "Use V2 query path (ClickHouse postgres connector join instead of separate Postgres queries)",
            "title": "Usequeryv2",
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "default": null,
            "description": "version of the node, used for schema migrations",
            "title": "Version",
            "type": "number",
            "nullable": true
          },
          "volumeResolution": {
            "title": "Volumeresolution",
            "type": "integer"
          },
          "withAggregations": {
            "default": null,
            "title": "Withaggregations",
            "type": "boolean",
            "nullable": true
          },
          "withFirstEvent": {
            "default": null,
            "title": "Withfirstevent",
            "type": "boolean",
            "nullable": true
          },
          "withLastEvent": {
            "default": null,
            "title": "Withlastevent",
            "type": "boolean",
            "nullable": true
          }
        },
        "required": [
          "dateRange",
          "orderBy",
          "volumeResolution"
        ],
        "title": "ErrorTrackingQuery",
        "type": "object"
      },
      "ErrorTrackingIssueCorrelationQuery": {
        "additionalProperties": false,
        "properties": {
          "events": {
            "items": {
              "type": "string"
            },
            "title": "Events",
            "type": "array"
          },
          "kind": {
            "default": "ErrorTrackingIssueCorrelationQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ErrorTrackingIssueCorrelationQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueCorrelationQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "events"
        ],
        "title": "ErrorTrackingIssueCorrelationQuery",
        "type": "object"
      },
      "ExperimentFunnelsQuery": {
        "additionalProperties": false,
        "properties": {
          "experiment_id": {
            "default": null,
            "title": "Experiment Id",
            "type": "integer",
            "nullable": true
          },
          "fingerprint": {
            "default": null,
            "title": "Fingerprint",
            "type": "string",
            "nullable": true
          },
          "funnels_query": {
            "$ref": "#/components/schemas/FunnelsQuery"
          },
          "kind": {
            "default": "ExperimentFunnelsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentFunnelsQuery"
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
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ExperimentFunnelsQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "uuid": {
            "default": null,
            "title": "Uuid",
            "type": "string",
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
          "funnels_query"
        ],
        "title": "ExperimentFunnelsQuery",
        "type": "object"
      },
      "ExperimentTrendsQuery": {
        "additionalProperties": false,
        "properties": {
          "count_query": {
            "$ref": "#/components/schemas/TrendsQuery"
          },
          "experiment_id": {
            "default": null,
            "title": "Experiment Id",
            "type": "integer",
            "nullable": true
          },
          "exposure_query": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQuery",
            "nullable": true
          },
          "fingerprint": {
            "default": null,
            "title": "Fingerprint",
            "type": "string",
            "nullable": true
          },
          "kind": {
            "default": "ExperimentTrendsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentTrendsQuery"
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
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ExperimentTrendsQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "uuid": {
            "default": null,
            "title": "Uuid",
            "type": "string",
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
          "count_query"
        ],
        "title": "ExperimentTrendsQuery",
        "type": "object"
      },
      "TracesQuery": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "filterSupportTraces": {
            "default": null,
            "title": "Filtersupporttraces",
            "type": "boolean",
            "nullable": true
          },
          "filterTestAccounts": {
            "default": null,
            "title": "Filtertestaccounts",
            "type": "boolean",
            "nullable": true
          },
          "groupKey": {
            "default": null,
            "title": "Groupkey",
            "type": "string",
            "nullable": true
          },
          "groupTypeIndex": {
            "default": null,
            "title": "Grouptypeindex",
            "type": "integer",
            "nullable": true
          },
          "kind": {
            "default": "TracesQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "TracesQuery"
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
          "personId": {
            "default": null,
            "description": "Person who performed the event",
            "title": "Personid",
            "type": "string",
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
          "randomOrder": {
            "default": null,
            "description": "Use random ordering instead of timestamp DESC. Useful for representative sampling to avoid recency bias.",
            "title": "Randomorder",
            "type": "boolean",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/TracesQueryResponse",
            "nullable": true
          },
          "showColumnConfigurator": {
            "default": null,
            "title": "Showcolumnconfigurator",
            "type": "boolean",
            "nullable": true
          },
          "tags": {
            "default": null,
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
        "title": "TracesQuery",
        "type": "object"
      },
      "TraceQuery": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "kind": {
            "default": "TraceQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "TraceQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
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
            "$ref": "#/components/schemas/TraceQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
            "$ref": "#/components/schemas/QueryLogTags",
            "nullable": true
          },
          "traceId": {
            "title": "Traceid",
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
          "traceId"
        ],
        "title": "TraceQuery",
        "type": "object"
      },
      "EndpointsUsageTableQuery": {
        "additionalProperties": false,
        "properties": {
          "breakdownBy": {
            "$ref": "#/components/schemas/EndpointsUsageBreakdown"
          },
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "endpointNames": {
            "default": null,
            "description": "Filter to specific endpoints by name",
            "title": "Endpointnames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "kind": {
            "default": "EndpointsUsageTableQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "EndpointsUsageTableQuery"
            ]
          },
          "limit": {
            "default": null,
            "title": "Limit",
            "type": "integer",
            "nullable": true
          },
          "materializationType": {
            "default": null,
            "description": "Filter by materialization type",
            "$ref": "#/components/schemas/MaterializationType",
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
                  "$ref": "#/components/schemas/EndpointsUsageOrderByField"
                },
                {
                  "$ref": "#/components/schemas/EndpointsUsageOrderByDirection"
                }
              ]
            },
            "type": "array",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/EndpointsUsageTableQueryResponse",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "breakdownBy"
        ],
        "title": "EndpointsUsageTableQuery",
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
      "ChartSettings": {
        "additionalProperties": false,
        "properties": {
          "goalLines": {
            "default": null,
            "title": "Goallines",
            "items": {
              "$ref": "#/components/schemas/GoalLine"
            },
            "type": "array",
            "nullable": true
          },
          "heatmap": {
            "default": null,
            "$ref": "#/components/schemas/HeatmapSettings",
            "nullable": true
          },
          "leftYAxisSettings": {
            "default": null,
            "$ref": "#/components/schemas/YAxisSettings",
            "nullable": true
          },
          "rightYAxisSettings": {
            "default": null,
            "$ref": "#/components/schemas/YAxisSettings",
            "nullable": true
          },
          "seriesBreakdownColumn": {
            "default": null,
            "title": "Seriesbreakdowncolumn",
            "type": "string",
            "nullable": true
          },
          "showLegend": {
            "default": null,
            "title": "Showlegend",
            "type": "boolean",
            "nullable": true
          },
          "showNullsAsZero": {
            "default": null,
            "title": "Shownullsaszero",
            "type": "boolean",
            "nullable": true
          },
          "showTotalRow": {
            "default": null,
            "title": "Showtotalrow",
            "type": "boolean",
            "nullable": true
          },
          "showXAxisBorder": {
            "default": null,
            "title": "Showxaxisborder",
            "type": "boolean",
            "nullable": true
          },
          "showXAxisTicks": {
            "default": null,
            "title": "Showxaxisticks",
            "type": "boolean",
            "nullable": true
          },
          "showYAxisBorder": {
            "default": null,
            "title": "Showyaxisborder",
            "type": "boolean",
            "nullable": true
          },
          "stackBars100": {
            "default": null,
            "description": "Whether we fill the bars to 100% in stacked mode",
            "title": "Stackbars100",
            "type": "boolean",
            "nullable": true
          },
          "xAxis": {
            "default": null,
            "$ref": "#/components/schemas/ChartAxis",
            "nullable": true
          },
          "yAxis": {
            "default": null,
            "title": "Yaxis",
            "items": {
              "$ref": "#/components/schemas/ChartAxis"
            },
            "type": "array",
            "nullable": true
          },
          "yAxisAtZero": {
            "default": null,
            "description": "Deprecated: use `[left|right]YAxisSettings`. Whether the Y axis should start at zero",
            "title": "Yaxisatzero",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "ChartSettings",
        "type": "object"
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
      "TableSettings": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "$ref": "#/components/schemas/ChartAxis"
            },
            "type": "array",
            "nullable": true
          },
          "conditionalFormatting": {
            "default": null,
            "title": "Conditionalformatting",
            "items": {
              "$ref": "#/components/schemas/ConditionalFormattingRule"
            },
            "type": "array",
            "nullable": true
          },
          "pinnedColumns": {
            "default": null,
            "title": "Pinnedcolumns",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "title": "TableSettings",
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
      "HogQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "bytecode": {
            "default": null,
            "title": "Bytecode",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "coloredBytecode": {
            "default": null,
            "title": "Coloredbytecode",
            "items": {},
            "type": "array",
            "nullable": true
          },
          "results": {
            "title": "Results"
          },
          "stdout": {
            "default": null,
            "title": "Stdout",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "HogQueryResponse",
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
      "ActionsPie": {
        "additionalProperties": false,
        "properties": {
          "disableHoverOffset": {
            "default": null,
            "title": "Disablehoveroffset",
            "type": "boolean",
            "nullable": true
          },
          "hideAggregation": {
            "default": null,
            "title": "Hideaggregation",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "ActionsPie",
        "type": "object"
      },
      "RETENTION": {
        "additionalProperties": false,
        "properties": {
          "hideLineGraph": {
            "default": null,
            "title": "Hidelinegraph",
            "type": "boolean",
            "nullable": true
          },
          "hideSizeColumn": {
            "default": null,
            "title": "Hidesizecolumn",
            "type": "boolean",
            "nullable": true
          },
          "useSmallLayout": {
            "default": null,
            "title": "Usesmalllayout",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "RETENTION",
        "type": "object"
      },
      "DataTableNodeViewPropsContextType": {
        "enum": [
          "event_definition",
          "team_columns"
        ],
        "title": "DataTableNodeViewPropsContextType",
        "type": "string"
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
      "WebVitalsPathBreakdownResult": {
        "additionalProperties": false,
        "properties": {
          "good": {
            "items": {
              "$ref": "#/components/schemas/WebVitalsPathBreakdownResultItem"
            },
            "title": "Good",
            "type": "array"
          },
          "needs_improvements": {
            "items": {
              "$ref": "#/components/schemas/WebVitalsPathBreakdownResultItem"
            },
            "title": "Needs Improvements",
            "type": "array"
          },
          "poor": {
            "items": {
              "$ref": "#/components/schemas/WebVitalsPathBreakdownResultItem"
            },
            "title": "Poor",
            "type": "array"
          }
        },
        "required": [
          "good",
          "needs_improvements",
          "poor"
        ],
        "title": "WebVitalsPathBreakdownResult",
        "type": "object"
      },
      "RevenueAnalyticsMRRQueryResultItem": {
        "additionalProperties": false,
        "properties": {
          "churn": {
            "title": "Churn"
          },
          "contraction": {
            "title": "Contraction"
          },
          "expansion": {
            "title": "Expansion"
          },
          "new": {
            "title": "New"
          },
          "total": {
            "title": "Total"
          }
        },
        "required": [
          "churn",
          "contraction",
          "expansion",
          "new",
          "total"
        ],
        "title": "RevenueAnalyticsMRRQueryResultItem",
        "type": "object"
      },
      "RevenueAnalyticsOverviewItem": {
        "additionalProperties": false,
        "properties": {
          "key": {
            "$ref": "#/components/schemas/RevenueAnalyticsOverviewItemKey"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "key",
          "value"
        ],
        "title": "RevenueAnalyticsOverviewItem",
        "type": "object"
      },
      "MarketingAnalyticsItem": {
        "additionalProperties": false,
        "properties": {
          "changeFromPreviousPct": {
            "default": null,
            "title": "Changefrompreviouspct",
            "type": "number",
            "nullable": true
          },
          "hasComparison": {
            "default": null,
            "title": "Hascomparison",
            "type": "boolean",
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
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "string"
              }
            ],
            "nullable": true
          },
          "value": {
            "default": null,
            "title": "Value",
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "string"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "key",
          "kind"
        ],
        "title": "MarketingAnalyticsItem",
        "type": "object"
      },
      "ErrorTrackingIssue": {
        "additionalProperties": false,
        "properties": {
          "aggregations": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueAggregations",
            "nullable": true
          },
          "assignee": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueAssignee",
            "nullable": true
          },
          "cohort": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueCohort",
            "nullable": true
          },
          "description": {
            "default": null,
            "title": "Description",
            "type": "string",
            "nullable": true
          },
          "external_issues": {
            "default": null,
            "title": "External Issues",
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingExternalReference"
            },
            "type": "array",
            "nullable": true
          },
          "first_event": {
            "default": null,
            "$ref": "#/components/schemas/FirstEvent",
            "nullable": true
          },
          "first_seen": {
            "format": "date-time",
            "title": "First Seen",
            "type": "string"
          },
          "function": {
            "default": null,
            "title": "Function",
            "type": "string",
            "nullable": true
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "last_event": {
            "default": null,
            "$ref": "#/components/schemas/LastEvent",
            "nullable": true
          },
          "last_seen": {
            "format": "date-time",
            "title": "Last Seen",
            "type": "string"
          },
          "library": {
            "default": null,
            "title": "Library",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "source": {
            "default": null,
            "title": "Source",
            "type": "string",
            "nullable": true
          },
          "status": {
            "$ref": "#/components/schemas/ErrorTrackingIssueStatus"
          }
        },
        "required": [
          "first_seen",
          "id",
          "last_seen",
          "status"
        ],
        "title": "ErrorTrackingIssue",
        "type": "object"
      },
      "ErrorTrackingCorrelatedIssue": {
        "additionalProperties": false,
        "properties": {
          "assignee": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueAssignee",
            "nullable": true
          },
          "cohort": {
            "default": null,
            "$ref": "#/components/schemas/ErrorTrackingIssueCohort",
            "nullable": true
          },
          "description": {
            "default": null,
            "title": "Description",
            "type": "string",
            "nullable": true
          },
          "event": {
            "title": "Event",
            "type": "string"
          },
          "external_issues": {
            "default": null,
            "title": "External Issues",
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingExternalReference"
            },
            "type": "array",
            "nullable": true
          },
          "first_seen": {
            "format": "date-time",
            "title": "First Seen",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "last_seen": {
            "format": "date-time",
            "title": "Last Seen",
            "type": "string"
          },
          "library": {
            "default": null,
            "title": "Library",
            "type": "string",
            "nullable": true
          },
          "name": {
            "default": null,
            "title": "Name",
            "type": "string",
            "nullable": true
          },
          "odds_ratio": {
            "title": "Odds Ratio",
            "type": "number"
          },
          "population": {
            "$ref": "#/components/schemas/Population"
          },
          "status": {
            "$ref": "#/components/schemas/ErrorTrackingIssueStatus"
          }
        },
        "required": [
          "event",
          "first_seen",
          "id",
          "last_seen",
          "odds_ratio",
          "population",
          "status"
        ],
        "title": "ErrorTrackingCorrelatedIssue",
        "type": "object"
      },
      "ExperimentSignificanceCode": {
        "enum": [
          "significant",
          "not_enough_exposure",
          "low_win_probability",
          "high_loss",
          "high_p_value"
        ],
        "title": "ExperimentSignificanceCode",
        "type": "string"
      },
      "ExperimentVariantFunnelsBaseStats": {
        "additionalProperties": false,
        "properties": {
          "failure_count": {
            "title": "Failure Count",
            "type": "number"
          },
          "key": {
            "title": "Key",
            "type": "string"
          },
          "success_count": {
            "title": "Success Count",
            "type": "number"
          }
        },
        "required": [
          "failure_count",
          "key",
          "success_count"
        ],
        "title": "ExperimentVariantFunnelsBaseStats",
        "type": "object"
      },
      "ExperimentVariantTrendsBaseStats": {
        "additionalProperties": false,
        "properties": {
          "absolute_exposure": {
            "title": "Absolute Exposure",
            "type": "number"
          },
          "count": {
            "title": "Count",
            "type": "number"
          },
          "exposure": {
            "title": "Exposure",
            "type": "number"
          },
          "key": {
            "title": "Key",
            "type": "string"
          }
        },
        "required": [
          "absolute_exposure",
          "count",
          "exposure",
          "key"
        ],
        "title": "ExperimentVariantTrendsBaseStats",
        "type": "object"
      },
      "LLMTrace": {
        "additionalProperties": false,
        "properties": {
          "aiSessionId": {
            "default": null,
            "title": "Aisessionid",
            "type": "string",
            "nullable": true
          },
          "createdAt": {
            "title": "Createdat",
            "type": "string"
          },
          "distinctId": {
            "title": "Distinctid",
            "type": "string"
          },
          "errorCount": {
            "default": null,
            "title": "Errorcount",
            "type": "number",
            "nullable": true
          },
          "events": {
            "items": {
              "$ref": "#/components/schemas/LLMTraceEvent"
            },
            "title": "Events",
            "type": "array"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "inputCost": {
            "default": null,
            "title": "Inputcost",
            "type": "number",
            "nullable": true
          },
          "inputState": {
            "default": null,
            "title": "Inputstate",
            "nullable": true
          },
          "inputTokens": {
            "default": null,
            "title": "Inputtokens",
            "type": "number",
            "nullable": true
          },
          "isSupportTrace": {
            "default": null,
            "title": "Issupporttrace",
            "type": "boolean",
            "nullable": true
          },
          "outputCost": {
            "default": null,
            "title": "Outputcost",
            "type": "number",
            "nullable": true
          },
          "outputState": {
            "default": null,
            "title": "Outputstate",
            "nullable": true
          },
          "outputTokens": {
            "default": null,
            "title": "Outputtokens",
            "type": "number",
            "nullable": true
          },
          "person": {
            "default": null,
            "$ref": "#/components/schemas/LLMTracePerson",
            "nullable": true
          },
          "tools": {
            "default": null,
            "title": "Tools",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "totalCost": {
            "default": null,
            "title": "Totalcost",
            "type": "number",
            "nullable": true
          },
          "totalLatency": {
            "default": null,
            "title": "Totallatency",
            "type": "number",
            "nullable": true
          },
          "traceName": {
            "default": null,
            "title": "Tracename",
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "createdAt",
          "distinctId",
          "events",
          "id"
        ],
        "title": "LLMTrace",
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
      "EventsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
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
          "nextCursor": {
            "default": null,
            "description": "Cursor for fetching the next page of results",
            "title": "Nextcursor",
            "type": "string",
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
            "items": {
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "results",
          "types"
        ],
        "title": "EventsQueryResponse",
        "type": "object"
      },
      "InsightActorsQuery": {
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
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "integer"
              }
            ],
            "nullable": true
          },
          "compare": {
            "default": null,
            "$ref": "#/components/schemas/Compare",
            "nullable": true
          },
          "day": {
            "default": null,
            "title": "Day",
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
          "includeRecordings": {
            "default": null,
            "title": "Includerecordings",
            "type": "boolean",
            "nullable": true
          },
          "interval": {
            "default": null,
            "description": "An interval selected out of available intervals in source query.",
            "title": "Interval",
            "type": "integer",
            "nullable": true
          },
          "kind": {
            "default": "InsightActorsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "InsightActorsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ActorsQueryResponse",
            "nullable": true
          },
          "series": {
            "default": null,
            "title": "Series",
            "type": "integer",
            "nullable": true
          },
          "source": {
            "discriminator": {
              "mapping": {
                "FunnelsQuery": "#/components/schemas/FunnelsQuery",
                "LifecycleQuery": "#/components/schemas/LifecycleQuery",
                "PathsQuery": "#/components/schemas/PathsQuery",
                "RetentionQuery": "#/components/schemas/RetentionQuery",
                "StickinessQuery": "#/components/schemas/StickinessQuery",
                "TrendsQuery": "#/components/schemas/TrendsQuery",
                "WebOverviewQuery": "#/components/schemas/WebOverviewQuery",
                "WebStatsTableQuery": "#/components/schemas/WebStatsTableQuery"
              },
              "propertyName": "kind"
            },
            "oneOf": [
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
            "title": "Source"
          },
          "status": {
            "default": null,
            "title": "Status",
            "type": "string",
            "nullable": true
          },
          "tags": {
            "default": null,
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
          "source"
        ],
        "title": "InsightActorsQuery",
        "type": "object"
      },
      "ActorsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "missing_actors_count": {
            "default": null,
            "title": "Missing Actors Count",
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
            "title": "Offset",
            "type": "integer"
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
              "items": {},
              "type": "array"
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "columns",
          "hogql",
          "limit",
          "offset",
          "results"
        ],
        "title": "ActorsQueryResponse",
        "type": "object"
      },
      "FunnelsActorsQuery": {
        "additionalProperties": false,
        "properties": {
          "funnelStep": {
            "default": null,
            "description": "Index of the step for which we want to get the timestamp for, per person. Positive for converted persons, negative for dropped of persons.",
            "title": "Funnelstep",
            "type": "integer",
            "nullable": true
          },
          "funnelStepBreakdown": {
            "default": null,
            "description": "The breakdown value for which to get persons for. This is an array for person and event properties, a string for groups and an integer for cohorts.",
            "title": "Funnelstepbreakdown",
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "items": {
                  "anyOf": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "string"
                    },
                    {
                      "type": "number"
                    }
                  ]
                },
                "type": "array"
              }
            ],
            "nullable": true
          },
          "funnelTrendsDropOff": {
            "default": null,
            "title": "Funneltrendsdropoff",
            "type": "boolean",
            "nullable": true
          },
          "funnelTrendsEntrancePeriodStart": {
            "default": null,
            "description": "Used together with `funnelTrendsDropOff` for funnels time conversion date for the persons modal.",
            "title": "Funneltrendsentranceperiodstart",
            "type": "string",
            "nullable": true
          },
          "includeRecordings": {
            "default": null,
            "title": "Includerecordings",
            "type": "boolean",
            "nullable": true
          },
          "kind": {
            "default": "FunnelsActorsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "FunnelsActorsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ActorsQueryResponse",
            "nullable": true
          },
          "source": {
            "$ref": "#/components/schemas/FunnelsQuery"
          },
          "tags": {
            "default": null,
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
          "source"
        ],
        "title": "FunnelsActorsQuery",
        "type": "object"
      },
      "FunnelCorrelationActorsQuery": {
        "additionalProperties": false,
        "properties": {
          "funnelCorrelationPersonConverted": {
            "default": null,
            "title": "Funnelcorrelationpersonconverted",
            "type": "boolean",
            "nullable": true
          },
          "funnelCorrelationPersonEntity": {
            "default": null,
            "title": "Funnelcorrelationpersonentity",
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
            ],
            "nullable": true
          },
          "funnelCorrelationPropertyValues": {
            "default": null,
            "title": "Funnelcorrelationpropertyvalues",
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
          "includeRecordings": {
            "default": null,
            "title": "Includerecordings",
            "type": "boolean",
            "nullable": true
          },
          "kind": {
            "default": "FunnelCorrelationActorsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "FunnelCorrelationActorsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ActorsQueryResponse",
            "nullable": true
          },
          "source": {
            "$ref": "#/components/schemas/FunnelCorrelationQuery"
          },
          "tags": {
            "default": null,
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
          "source"
        ],
        "title": "FunnelCorrelationActorsQuery",
        "type": "object"
      },
      "StickinessActorsQuery": {
        "additionalProperties": false,
        "properties": {
          "compare": {
            "default": null,
            "$ref": "#/components/schemas/Compare",
            "nullable": true
          },
          "day": {
            "default": null,
            "title": "Day",
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
          "includeRecordings": {
            "default": null,
            "title": "Includerecordings",
            "type": "boolean",
            "nullable": true
          },
          "kind": {
            "default": "StickinessActorsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "StickinessActorsQuery"
            ]
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "operator": {
            "default": null,
            "$ref": "#/components/schemas/StickinessOperator",
            "nullable": true
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/ActorsQueryResponse",
            "nullable": true
          },
          "series": {
            "default": null,
            "title": "Series",
            "type": "integer",
            "nullable": true
          },
          "source": {
            "$ref": "#/components/schemas/StickinessQuery"
          },
          "tags": {
            "default": null,
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
          "source"
        ],
        "title": "StickinessActorsQuery",
        "type": "object"
      },
      "GroupsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
          },
          "kind": {
            "default": "GroupsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "GroupsQuery"
            ]
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "modifiers": {
            "default": null,
            "description": "Modifiers used when performing the query",
            "$ref": "#/components/schemas/HogQLQueryModifiers",
            "nullable": true
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
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
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "limit",
          "offset",
          "results",
          "types"
        ],
        "title": "GroupsQueryResponse",
        "type": "object"
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
      "WebExternalClicksTableQueryResponse": {
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
          }
        },
        "required": [
          "results"
        ],
        "title": "WebExternalClicksTableQueryResponse",
        "type": "object"
      },
      "WebGoalsQueryResponse": {
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
          }
        },
        "required": [
          "results"
        ],
        "title": "WebGoalsQueryResponse",
        "type": "object"
      },
      "WebVitalsMetric": {
        "enum": [
          "INP",
          "LCP",
          "CLS",
          "FCP"
        ],
        "title": "WebVitalsMetric",
        "type": "string"
      },
      "WebVitalsPercentile": {
        "enum": [
          "p75",
          "p90",
          "p99"
        ],
        "title": "WebVitalsPercentile",
        "type": "string"
      },
      "WebVitalsPathBreakdownQueryResponse": {
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
              "$ref": "#/components/schemas/WebVitalsPathBreakdownResult"
            },
            "maxItems": 1,
            "minItems": 1,
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
        "title": "WebVitalsPathBreakdownQueryResponse",
        "type": "object"
      },
      "Filters": {
        "additionalProperties": false,
        "properties": {
          "dateRange": {
            "default": null,
            "$ref": "#/components/schemas/DateRange",
            "nullable": true
          },
          "properties": {
            "default": null,
            "title": "Properties",
            "items": {
              "$ref": "#/components/schemas/SessionPropertyFilter"
            },
            "type": "array",
            "nullable": true
          }
        },
        "title": "Filters",
        "type": "object"
      },
      "SessionAttributionGroupBy": {
        "enum": [
          "ChannelType",
          "Medium",
          "Source",
          "Campaign",
          "AdIds",
          "ReferringDomain",
          "InitialURL"
        ],
        "title": "SessionAttributionGroupBy",
        "type": "string"
      },
      "SessionAttributionExplorerQueryResponse": {
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "SessionAttributionExplorerQueryResponse",
        "type": "object"
      },
      "SessionsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "items": {},
            "title": "Columns",
            "type": "array"
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
            "description": "Generated HogQL query.",
            "title": "Hogql",
            "type": "string"
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
            "items": {
              "items": {},
              "type": "array"
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
          },
          "types": {
            "items": {
              "type": "string"
            },
            "title": "Types",
            "type": "array"
          }
        },
        "required": [
          "columns",
          "hogql",
          "results",
          "types"
        ],
        "title": "SessionsQueryResponse",
        "type": "object"
      },
      "RevenueAnalyticsBreakdown": {
        "additionalProperties": false,
        "properties": {
          "property": {
            "title": "Property",
            "type": "string"
          },
          "type": {
            "default": "revenue_analytics",
            "title": "Type",
            "type": "string",
            "enum": [
              "revenue_analytics"
            ]
          }
        },
        "required": [
          "property"
        ],
        "title": "RevenueAnalyticsBreakdown",
        "type": "object"
      },
      "SimpleIntervalType": {
        "enum": [
          "day",
          "month"
        ],
        "title": "SimpleIntervalType",
        "type": "string"
      },
      "RevenueAnalyticsGrossRevenueQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
          }
        },
        "required": [
          "results"
        ],
        "title": "RevenueAnalyticsGrossRevenueQueryResponse",
        "type": "object"
      },
      "RevenueAnalyticsMetricsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
        "title": "RevenueAnalyticsMetricsQueryResponse",
        "type": "object"
      },
      "RevenueAnalyticsMRRQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
              "$ref": "#/components/schemas/RevenueAnalyticsMRRQueryResultItem"
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
        "title": "RevenueAnalyticsMRRQueryResponse",
        "type": "object"
      },
      "RevenueAnalyticsOverviewQueryResponse": {
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
              "$ref": "#/components/schemas/RevenueAnalyticsOverviewItem"
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
        "title": "RevenueAnalyticsOverviewQueryResponse",
        "type": "object"
      },
      "RevenueAnalyticsTopCustomersGroupBy": {
        "enum": [
          "month",
          "all"
        ],
        "title": "RevenueAnalyticsTopCustomersGroupBy",
        "type": "string"
      },
      "RevenueAnalyticsTopCustomersQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
        "title": "RevenueAnalyticsTopCustomersQueryResponse",
        "type": "object"
      },
      "RevenueExampleEventsQueryResponse": {
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "RevenueExampleEventsQueryResponse",
        "type": "object"
      },
      "RevenueExampleDataWarehouseTablesQueryResponse": {
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
          },
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "RevenueExampleDataWarehouseTablesQueryResponse",
        "type": "object"
      },
      "ConversionGoalFilter1": {
        "additionalProperties": false,
        "properties": {
          "conversion_goal_id": {
            "title": "Conversion Goal Id",
            "type": "string"
          },
          "conversion_goal_name": {
            "title": "Conversion Goal Name",
            "type": "string"
          },
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
          "schema_map": {
            "additionalProperties": {
              "anyOf": [
                {
                  "type": "string"
                },
                {}
              ]
            },
            "title": "Schema Map",
            "type": "object"
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
          "conversion_goal_id",
          "conversion_goal_name",
          "schema_map"
        ],
        "title": "ConversionGoalFilter1",
        "type": "object"
      },
      "ConversionGoalFilter2": {
        "additionalProperties": false,
        "properties": {
          "conversion_goal_id": {
            "title": "Conversion Goal Id",
            "type": "string"
          },
          "conversion_goal_name": {
            "title": "Conversion Goal Name",
            "type": "string"
          },
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
          "schema_map": {
            "additionalProperties": {
              "anyOf": [
                {
                  "type": "string"
                },
                {}
              ]
            },
            "title": "Schema Map",
            "type": "object"
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
          "conversion_goal_id",
          "conversion_goal_name",
          "id",
          "schema_map"
        ],
        "title": "ConversionGoalFilter2",
        "type": "object"
      },
      "ConversionGoalFilter3": {
        "additionalProperties": false,
        "properties": {
          "conversion_goal_id": {
            "title": "Conversion Goal Id",
            "type": "string"
          },
          "conversion_goal_name": {
            "title": "Conversion Goal Name",
            "type": "string"
          },
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
          "schema_map": {
            "additionalProperties": {
              "anyOf": [
                {
                  "type": "string"
                },
                {}
              ]
            },
            "title": "Schema Map",
            "type": "object"
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
          "conversion_goal_id",
          "conversion_goal_name",
          "distinct_id_field",
          "id",
          "id_field",
          "schema_map",
          "table_name",
          "timestamp_field"
        ],
        "title": "ConversionGoalFilter3",
        "type": "object"
      },
      "MarketingAnalyticsDrillDownLevel": {
        "enum": [
          "channel",
          "source",
          "campaign"
        ],
        "title": "MarketingAnalyticsDrillDownLevel",
        "type": "string"
      },
      "IntegrationFilter": {
        "additionalProperties": false,
        "properties": {
          "integrationSourceIds": {
            "default": null,
            "description": "Selected integration source IDs to filter by (e.g., table IDs or source map IDs)",
            "title": "Integrationsourceids",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          }
        },
        "title": "IntegrationFilter",
        "type": "object"
      },
      "MarketingAnalyticsOrderByEnum": {
        "enum": [
          "ASC",
          "DESC"
        ],
        "title": "MarketingAnalyticsOrderByEnum",
        "type": "string"
      },
      "MarketingAnalyticsTableQueryResponse": {
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
            "items": {
              "items": {
                "$ref": "#/components/schemas/MarketingAnalyticsItem"
              },
              "type": "array"
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
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "MarketingAnalyticsTableQueryResponse",
        "type": "object"
      },
      "MarketingAnalyticsAggregatedQueryResponse": {
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
            "additionalProperties": {
              "$ref": "#/components/schemas/MarketingAnalyticsItem"
            },
            "title": "Results",
            "type": "object"
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
          }
        },
        "required": [
          "results"
        ],
        "title": "MarketingAnalyticsAggregatedQueryResponse",
        "type": "object"
      },
      "NonIntegratedConversionsTableQueryResponse": {
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
            "items": {
              "items": {
                "$ref": "#/components/schemas/MarketingAnalyticsItem"
              },
              "type": "array"
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
          "types": {
            "default": null,
            "title": "Types",
            "items": {},
            "type": "array",
            "nullable": true
          }
        },
        "required": [
          "results"
        ],
        "title": "NonIntegratedConversionsTableQueryResponse",
        "type": "object"
      },
      "ErrorTrackingIssueAssignee": {
        "additionalProperties": false,
        "properties": {
          "id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "integer"
              }
            ],
            "title": "Id"
          },
          "type": {
            "$ref": "#/components/schemas/ErrorTrackingIssueAssigneeType"
          }
        },
        "required": [
          "id",
          "type"
        ],
        "title": "ErrorTrackingIssueAssignee",
        "type": "object"
      },
      "OrderBy1": {
        "enum": [
          "last_seen",
          "first_seen",
          "occurrences",
          "users",
          "sessions"
        ],
        "title": "OrderBy1",
        "type": "string"
      },
      "OrderDirection1": {
        "enum": [
          "ASC",
          "DESC"
        ],
        "title": "OrderDirection1",
        "type": "string"
      },
      "ErrorTrackingQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingIssue"
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
        "title": "ErrorTrackingQueryResponse",
        "type": "object"
      },
      "ErrorTrackingIssueStatus": {
        "enum": [
          "archived",
          "active",
          "resolved",
          "pending_release",
          "suppressed"
        ],
        "title": "ErrorTrackingIssueStatus",
        "type": "string"
      },
      "ErrorTrackingIssueCorrelationQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/ErrorTrackingCorrelatedIssue"
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
        "title": "ErrorTrackingIssueCorrelationQueryResponse",
        "type": "object"
      },
      "ExperimentFunnelsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "credible_intervals": {
            "additionalProperties": {
              "items": {
                "type": "number"
              },
              "type": "array"
            },
            "title": "Credible Intervals",
            "type": "object"
          },
          "expected_loss": {
            "title": "Expected Loss",
            "type": "number"
          },
          "funnels_query": {
            "default": null,
            "$ref": "#/components/schemas/FunnelsQuery",
            "nullable": true
          },
          "insight": {
            "items": {
              "items": {
                "additionalProperties": true,
                "type": "object"
              },
              "type": "array"
            },
            "title": "Insight",
            "type": "array"
          },
          "kind": {
            "default": "ExperimentFunnelsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentFunnelsQuery"
            ]
          },
          "probability": {
            "additionalProperties": {
              "type": "number"
            },
            "title": "Probability",
            "type": "object"
          },
          "significance_code": {
            "$ref": "#/components/schemas/ExperimentSignificanceCode"
          },
          "significant": {
            "title": "Significant",
            "type": "boolean"
          },
          "stats_version": {
            "default": null,
            "title": "Stats Version",
            "type": "integer",
            "nullable": true
          },
          "variants": {
            "items": {
              "$ref": "#/components/schemas/ExperimentVariantFunnelsBaseStats"
            },
            "title": "Variants",
            "type": "array"
          }
        },
        "required": [
          "credible_intervals",
          "expected_loss",
          "insight",
          "probability",
          "significance_code",
          "significant",
          "variants"
        ],
        "title": "ExperimentFunnelsQueryResponse",
        "type": "object"
      },
      "ExperimentTrendsQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "count_query": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQuery",
            "nullable": true
          },
          "credible_intervals": {
            "additionalProperties": {
              "items": {
                "type": "number"
              },
              "type": "array"
            },
            "title": "Credible Intervals",
            "type": "object"
          },
          "exposure_query": {
            "default": null,
            "$ref": "#/components/schemas/TrendsQuery",
            "nullable": true
          },
          "insight": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "title": "Insight",
            "type": "array"
          },
          "kind": {
            "default": "ExperimentTrendsQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "ExperimentTrendsQuery"
            ]
          },
          "p_value": {
            "title": "P Value",
            "type": "number"
          },
          "probability": {
            "additionalProperties": {
              "type": "number"
            },
            "title": "Probability",
            "type": "object"
          },
          "significance_code": {
            "$ref": "#/components/schemas/ExperimentSignificanceCode"
          },
          "significant": {
            "title": "Significant",
            "type": "boolean"
          },
          "stats_version": {
            "default": null,
            "title": "Stats Version",
            "type": "integer",
            "nullable": true
          },
          "variants": {
            "items": {
              "$ref": "#/components/schemas/ExperimentVariantTrendsBaseStats"
            },
            "title": "Variants",
            "type": "array"
          }
        },
        "required": [
          "credible_intervals",
          "insight",
          "p_value",
          "probability",
          "significance_code",
          "significant",
          "variants"
        ],
        "title": "ExperimentTrendsQueryResponse",
        "type": "object"
      },
      "TracesQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/LLMTrace"
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
        "title": "TracesQueryResponse",
        "type": "object"
      },
      "TraceQueryResponse": {
        "additionalProperties": false,
        "properties": {
          "columns": {
            "default": null,
            "title": "Columns",
            "items": {
              "type": "string"
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
            "items": {
              "$ref": "#/components/schemas/LLMTrace"
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
        "title": "TraceQueryResponse",
        "type": "object"
      },
      "EndpointsUsageBreakdown": {
        "enum": [
          "Endpoint",
          "MaterializationType",
          "ApiKey",
          "Status"
        ],
        "title": "EndpointsUsageBreakdown",
        "type": "string"
      },
      "MaterializationType": {
        "enum": [
          "materialized",
          "inline",
          null
        ],
        "title": "MaterializationType"
      },
      "EndpointsUsageOrderByField": {
        "enum": [
          "requests",
          "bytes_read",
          "cpu_seconds",
          "avg_query_duration_ms",
          "error_rate"
        ],
        "title": "EndpointsUsageOrderByField",
        "type": "string"
      },
      "EndpointsUsageOrderByDirection": {
        "enum": [
          "ASC",
          "DESC"
        ],
        "title": "EndpointsUsageOrderByDirection",
        "type": "string"
      },
      "EndpointsUsageTableQueryResponse": {
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
          }
        },
        "required": [
          "results"
        ],
        "title": "EndpointsUsageTableQueryResponse",
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
      "HeatmapSettings": {
        "additionalProperties": false,
        "properties": {
          "gradient": {
            "default": null,
            "title": "Gradient",
            "items": {
              "$ref": "#/components/schemas/HeatmapGradientStop"
            },
            "type": "array",
            "nullable": true
          },
          "gradientPreset": {
            "default": null,
            "title": "Gradientpreset",
            "type": "string",
            "nullable": true
          },
          "gradientScaleMode": {
            "default": null,
            "$ref": "#/components/schemas/GradientScaleMode",
            "nullable": true
          },
          "valueColumn": {
            "default": null,
            "title": "Valuecolumn",
            "type": "string",
            "nullable": true
          },
          "xAxisColumn": {
            "default": null,
            "title": "Xaxiscolumn",
            "type": "string",
            "nullable": true
          },
          "xAxisLabel": {
            "default": null,
            "title": "Xaxislabel",
            "type": "string",
            "nullable": true
          },
          "yAxisColumn": {
            "default": null,
            "title": "Yaxiscolumn",
            "type": "string",
            "nullable": true
          },
          "yAxisLabel": {
            "default": null,
            "title": "Yaxislabel",
            "type": "string",
            "nullable": true
          }
        },
        "title": "HeatmapSettings",
        "type": "object"
      },
      "YAxisSettings": {
        "additionalProperties": false,
        "properties": {
          "scale": {
            "default": null,
            "$ref": "#/components/schemas/Scale",
            "nullable": true
          },
          "showGridLines": {
            "default": null,
            "title": "Showgridlines",
            "type": "boolean",
            "nullable": true
          },
          "showTicks": {
            "default": null,
            "title": "Showticks",
            "type": "boolean",
            "nullable": true
          },
          "startAtZero": {
            "default": null,
            "description": "Whether the Y axis should start at zero",
            "title": "Startatzero",
            "type": "boolean",
            "nullable": true
          }
        },
        "title": "YAxisSettings",
        "type": "object"
      },
      "ChartAxis": {
        "additionalProperties": false,
        "properties": {
          "column": {
            "title": "Column",
            "type": "string"
          },
          "settings": {
            "default": null,
            "$ref": "#/components/schemas/Settings",
            "nullable": true
          }
        },
        "required": [
          "column"
        ],
        "title": "ChartAxis",
        "type": "object"
      },
      "ConditionalFormattingRule": {
        "additionalProperties": false,
        "properties": {
          "bytecode": {
            "items": {},
            "title": "Bytecode",
            "type": "array"
          },
          "color": {
            "title": "Color",
            "type": "string"
          },
          "colorMode": {
            "default": null,
            "$ref": "#/components/schemas/ColorMode",
            "nullable": true
          },
          "columnName": {
            "title": "Columnname",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "input": {
            "title": "Input",
            "type": "string"
          },
          "templateId": {
            "title": "Templateid",
            "type": "string"
          }
        },
        "required": [
          "bytecode",
          "color",
          "columnName",
          "id",
          "input",
          "templateId"
        ],
        "title": "ConditionalFormattingRule",
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
      "WebVitalsPathBreakdownResultItem": {
        "additionalProperties": false,
        "properties": {
          "path": {
            "title": "Path",
            "type": "string"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "path",
          "value"
        ],
        "title": "WebVitalsPathBreakdownResultItem",
        "type": "object"
      },
      "RevenueAnalyticsOverviewItemKey": {
        "enum": [
          "revenue",
          "paying_customer_count",
          "avg_revenue_per_customer"
        ],
        "title": "RevenueAnalyticsOverviewItemKey",
        "type": "string"
      },
      "ErrorTrackingIssueAggregations": {
        "additionalProperties": false,
        "properties": {
          "occurrences": {
            "title": "Occurrences",
            "type": "number"
          },
          "sessions": {
            "title": "Sessions",
            "type": "number"
          },
          "users": {
            "title": "Users",
            "type": "number"
          },
          "volumeRange": {
            "default": null,
            "title": "Volumerange",
            "items": {
              "type": "number"
            },
            "type": "array",
            "nullable": true
          },
          "volume_buckets": {
            "items": {
              "$ref": "#/components/schemas/VolumeBucket"
            },
            "title": "Volume Buckets",
            "type": "array"
          }
        },
        "required": [
          "occurrences",
          "sessions",
          "users",
          "volume_buckets"
        ],
        "title": "ErrorTrackingIssueAggregations",
        "type": "object"
      },
      "ErrorTrackingIssueCohort": {
        "additionalProperties": false,
        "properties": {
          "id": {
            "title": "Id",
            "type": "number"
          },
          "name": {
            "title": "Name",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name"
        ],
        "title": "ErrorTrackingIssueCohort",
        "type": "object"
      },
      "ErrorTrackingExternalReference": {
        "additionalProperties": false,
        "properties": {
          "external_url": {
            "title": "External Url",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "integration": {
            "$ref": "#/components/schemas/ErrorTrackingExternalReferenceIntegration"
          }
        },
        "required": [
          "external_url",
          "id",
          "integration"
        ],
        "title": "ErrorTrackingExternalReference",
        "type": "object"
      },
      "FirstEvent": {
        "additionalProperties": false,
        "properties": {
          "distinct_id": {
            "title": "Distinct Id",
            "type": "string"
          },
          "properties": {
            "type": "string",
            "title": "Properties"
          },
          "timestamp": {
            "title": "Timestamp",
            "type": "string"
          },
          "uuid": {
            "title": "Uuid",
            "type": "string"
          }
        },
        "required": [
          "distinct_id",
          "properties",
          "timestamp",
          "uuid"
        ],
        "title": "FirstEvent",
        "type": "object"
      },
      "LastEvent": {
        "additionalProperties": false,
        "properties": {
          "distinct_id": {
            "title": "Distinct Id",
            "type": "string"
          },
          "properties": {
            "type": "string",
            "title": "Properties"
          },
          "timestamp": {
            "title": "Timestamp",
            "type": "string"
          },
          "uuid": {
            "title": "Uuid",
            "type": "string"
          }
        },
        "required": [
          "distinct_id",
          "properties",
          "timestamp",
          "uuid"
        ],
        "title": "LastEvent",
        "type": "object"
      },
      "Population": {
        "additionalProperties": false,
        "properties": {
          "both": {
            "title": "Both",
            "type": "number"
          },
          "exception_only": {
            "title": "Exception Only",
            "type": "number"
          },
          "neither": {
            "title": "Neither",
            "type": "number"
          },
          "success_only": {
            "title": "Success Only",
            "type": "number"
          }
        },
        "required": [
          "both",
          "exception_only",
          "neither",
          "success_only"
        ],
        "title": "Population",
        "type": "object"
      },
      "LLMTraceEvent": {
        "additionalProperties": false,
        "properties": {
          "createdAt": {
            "title": "Createdat",
            "type": "string"
          },
          "event": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/AIEventType"
              },
              {
                "type": "string"
              }
            ],
            "title": "Event"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "title": "Properties"
          }
        },
        "required": [
          "createdAt",
          "event",
          "id",
          "properties"
        ],
        "title": "LLMTraceEvent",
        "type": "object"
      },
      "LLMTracePerson": {
        "additionalProperties": false,
        "properties": {
          "created_at": {
            "title": "Created At",
            "type": "string"
          },
          "distinct_id": {
            "title": "Distinct Id",
            "type": "string"
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "title": "Properties"
          },
          "uuid": {
            "title": "Uuid",
            "type": "string"
          }
        },
        "required": [
          "created_at",
          "distinct_id",
          "properties",
          "uuid"
        ],
        "title": "LLMTracePerson",
        "type": "object"
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
      "Compare": {
        "enum": [
          "current",
          "previous"
        ],
        "title": "Compare",
        "type": "string"
      },
      "FunnelCorrelationQuery": {
        "additionalProperties": false,
        "properties": {
          "funnelCorrelationEventExcludePropertyNames": {
            "default": null,
            "title": "Funnelcorrelationeventexcludepropertynames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "funnelCorrelationEventNames": {
            "default": null,
            "title": "Funnelcorrelationeventnames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "funnelCorrelationExcludeEventNames": {
            "default": null,
            "title": "Funnelcorrelationexcludeeventnames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "funnelCorrelationExcludeNames": {
            "default": null,
            "title": "Funnelcorrelationexcludenames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "funnelCorrelationNames": {
            "default": null,
            "title": "Funnelcorrelationnames",
            "items": {
              "type": "string"
            },
            "type": "array",
            "nullable": true
          },
          "funnelCorrelationType": {
            "$ref": "#/components/schemas/FunnelCorrelationResultsType"
          },
          "kind": {
            "default": "FunnelCorrelationQuery",
            "title": "Kind",
            "type": "string",
            "enum": [
              "FunnelCorrelationQuery"
            ]
          },
          "response": {
            "default": null,
            "$ref": "#/components/schemas/FunnelCorrelationResponse",
            "nullable": true
          },
          "source": {
            "$ref": "#/components/schemas/FunnelsActorsQuery"
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
          "funnelCorrelationType",
          "source"
        ],
        "title": "FunnelCorrelationQuery",
        "type": "object"
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
      "ErrorTrackingIssueAssigneeType": {
        "enum": [
          "user",
          "role"
        ],
        "title": "ErrorTrackingIssueAssigneeType",
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
      "HeatmapGradientStop": {
        "additionalProperties": false,
        "properties": {
          "color": {
            "title": "Color",
            "type": "string"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "color",
          "value"
        ],
        "title": "HeatmapGradientStop",
        "type": "object"
      },
      "GradientScaleMode": {
        "enum": [
          "absolute",
          "relative"
        ],
        "title": "GradientScaleMode",
        "type": "string"
      },
      "Scale": {
        "enum": [
          "linear",
          "logarithmic"
        ],
        "title": "Scale",
        "type": "string"
      },
      "Settings": {
        "additionalProperties": false,
        "properties": {
          "display": {
            "default": null,
            "$ref": "#/components/schemas/ChartSettingsDisplay",
            "nullable": true
          },
          "formatting": {
            "default": null,
            "$ref": "#/components/schemas/ChartSettingsFormatting",
            "nullable": true
          }
        },
        "title": "Settings",
        "type": "object"
      },
      "ColorMode": {
        "enum": [
          "light",
          "dark"
        ],
        "title": "ColorMode",
        "type": "string"
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
      "VolumeBucket": {
        "additionalProperties": false,
        "properties": {
          "label": {
            "title": "Label",
            "type": "string"
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
        "title": "VolumeBucket",
        "type": "object"
      },
      "ErrorTrackingExternalReferenceIntegration": {
        "additionalProperties": false,
        "properties": {
          "display_name": {
            "title": "Display Name",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "number"
          },
          "kind": {
            "$ref": "#/components/schemas/IntegrationKind"
          }
        },
        "required": [
          "display_name",
          "id",
          "kind"
        ],
        "title": "ErrorTrackingExternalReferenceIntegration",
        "type": "object"
      },
      "AIEventType": {
        "enum": [
          "$ai_generation",
          "$ai_embedding",
          "$ai_span",
          "$ai_trace",
          "$ai_metric",
          "$ai_feedback",
          "$ai_evaluation",
          "$ai_trace_summary",
          "$ai_generation_summary",
          "$ai_trace_clusters",
          "$ai_generation_clusters"
        ],
        "title": "AIEventType",
        "type": "string"
      },
      "FunnelCorrelationResultsType": {
        "enum": [
          "events",
          "properties",
          "event_with_properties"
        ],
        "title": "FunnelCorrelationResultsType",
        "type": "string"
      },
      "FunnelCorrelationResponse": {
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
            "$ref": "#/components/schemas/FunnelCorrelationResult"
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
          }
        },
        "required": [
          "results"
        ],
        "title": "FunnelCorrelationResponse",
        "type": "object"
      },
      "ChartSettingsDisplay": {
        "additionalProperties": false,
        "properties": {
          "color": {
            "default": null,
            "title": "Color",
            "type": "string",
            "nullable": true
          },
          "displayType": {
            "default": null,
            "$ref": "#/components/schemas/DisplayType",
            "nullable": true
          },
          "label": {
            "default": null,
            "title": "Label",
            "type": "string",
            "nullable": true
          },
          "trendLine": {
            "default": null,
            "title": "Trendline",
            "type": "boolean",
            "nullable": true
          },
          "yAxisPosition": {
            "default": null,
            "$ref": "#/components/schemas/YAxisPosition",
            "nullable": true
          }
        },
        "title": "ChartSettingsDisplay",
        "type": "object"
      },
      "ChartSettingsFormatting": {
        "additionalProperties": false,
        "properties": {
          "decimalPlaces": {
            "default": null,
            "title": "Decimalplaces",
            "type": "number",
            "nullable": true
          },
          "prefix": {
            "default": null,
            "title": "Prefix",
            "type": "string",
            "nullable": true
          },
          "style": {
            "default": null,
            "$ref": "#/components/schemas/Style",
            "nullable": true
          },
          "suffix": {
            "default": null,
            "title": "Suffix",
            "type": "string",
            "nullable": true
          }
        },
        "title": "ChartSettingsFormatting",
        "type": "object"
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
      },
      "IntegrationKind": {
        "enum": [
          "slack",
          "slack-posthog-code",
          "salesforce",
          "hubspot",
          "google-pubsub",
          "google-cloud-storage",
          "google-ads",
          "google-sheets",
          "linkedin-ads",
          "snapchat",
          "intercom",
          "email",
          "twilio",
          "linear",
          "github",
          "gitlab",
          "meta-ads",
          "clickup",
          "reddit-ads",
          "databricks",
          "tiktok-ads",
          "bing-ads",
          "vercel",
          "azure-blob",
          "firebase",
          "jira",
          "pinterest-ads"
        ],
        "title": "IntegrationKind",
        "type": "string"
      },
      "FunnelCorrelationResult": {
        "additionalProperties": false,
        "properties": {
          "events": {
            "items": {
              "$ref": "#/components/schemas/EventOddsRatioSerialized"
            },
            "title": "Events",
            "type": "array"
          },
          "skewed": {
            "title": "Skewed",
            "type": "boolean"
          }
        },
        "required": [
          "events",
          "skewed"
        ],
        "title": "FunnelCorrelationResult",
        "type": "object"
      },
      "DisplayType": {
        "enum": [
          "auto",
          "line",
          "bar"
        ],
        "title": "DisplayType",
        "type": "string"
      },
      "YAxisPosition": {
        "enum": [
          "left",
          "right"
        ],
        "title": "YAxisPosition",
        "type": "string"
      },
      "Style": {
        "enum": [
          "none",
          "number",
          "short",
          "percent"
        ],
        "title": "Style",
        "type": "string"
      },
      "EventOddsRatioSerialized": {
        "additionalProperties": false,
        "properties": {
          "correlation_type": {
            "$ref": "#/components/schemas/CorrelationType"
          },
          "event": {
            "$ref": "#/components/schemas/EventDefinition"
          },
          "failure_count": {
            "title": "Failure Count",
            "type": "integer"
          },
          "odds_ratio": {
            "title": "Odds Ratio",
            "type": "number"
          },
          "success_count": {
            "title": "Success Count",
            "type": "integer"
          }
        },
        "required": [
          "correlation_type",
          "event",
          "failure_count",
          "odds_ratio",
          "success_count"
        ],
        "title": "EventOddsRatioSerialized",
        "type": "object"
      },
      "CorrelationType": {
        "enum": [
          "success",
          "failure"
        ],
        "title": "CorrelationType",
        "type": "string"
      },
      "EventDefinition": {
        "additionalProperties": false,
        "properties": {
          "elements": {
            "items": {},
            "title": "Elements",
            "type": "array"
          },
          "event": {
            "title": "Event",
            "type": "string"
          },
          "properties": {
            "type": "object",
            "additionalProperties": true,
            "title": "Properties"
          }
        },
        "required": [
          "elements",
          "event",
          "properties"
        ],
        "title": "EventDefinition",
        "type": "object"
      }
    }
  }
}
```
