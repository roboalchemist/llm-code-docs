# Source: https://docs.datadoghq.com/dashboards/widgets/geomap.md

---
title: Geomap Widget
description: >-
  Visualize geographic data with shaded regions or points to display
  location-based metrics and patterns.
breadcrumbs: Docs > Dashboards > Widgets > Geomap Widget
---

# Geomap Widget

The geomap widget visualizes geographic data with shaded regions or points. It can be used to:

- View user sessions by country.
- Filter to see a list of all sessions in a new tab.
- View user sessions filtered by employee.
- Monitor performance metrics like load time, core web vitals, and percent of views with errors.

{% video
   url="https://datadog-docs.imgix.net/images//dashboards/widgets/geomap/geomap_zoom_region.mp4" /%}

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/geomap/geomap_setup3.b99a670cd1d84ad1ba1c35120e745650.png?auto=format"
   alt="Geomap Graph your data section of widget configuration" /%}

### Configuration{% #configuration %}

1. Choose the visualization layer:

   - **Regions**: Aggregate measures at a country or country subdivisions level.
   - **Points**: Overlay events as points on the map to display geographic event data.

1. Choose the data to graph:**Note**: Support for data sources varies based on the visualization layer you select.

   {% tab title="Regions" %}

| Data source                                       | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Log Events                                        | The group by tag must include a country ISO Code (alpha-2 ISO format) or a country subdivision ISO Code (ISO-3166-2 format). You can use the [GeoIP Processor](https://docs.datadoghq.com/logs/log_configuration/processors/#geoip-parser) to do this, or manually include the [tags on ingest](https://docs.datadoghq.com/getting_started/tagging/#define-tags). See the [Log search documentation](https://docs.datadoghq.com/logs/search_syntax/) to configure a log event query. |
| Metric                                            | The group by tag must include a country ISO Code (alpha-2 ISO format) or a country subdivision ISO Code (ISO-3166-2 format). You can [generate metrics from ingested logs](https://docs.datadoghq.com/logs/logs_to_metrics/), or manually include the [tags on ingest](https://docs.datadoghq.com/getting_started/tagging/#define-tags). See the [querying documentation](https://docs.datadoghq.com/dashboards/querying/) to configure a metric query.                              |
| RUM                                               | See the [RUM documentation](https://docs.datadoghq.com/real_user_monitoring/explorer/search_syntax/) to configure a RUM query.                                                                                                                                                                                                                                                                                                                                                       |
| SLO                                               | See the [SLO search documentation](https://docs.datadoghq.com/service_level_objectives/#searching-slos) to configure an SLO query.                                                                                                                                                                                                                                                                                                                                                   |
| Security SignalsApp and API ProtectionAudit Trail | See the [Log search documentation](https://docs.datadoghq.com/logs/search_syntax/) to configure a query.                                                                                                                                                                                                                                                                                                                                                                             |

   {% /tab %}

   {% tab title="Points" %}
   
| Data source | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Log Events  | The group by tag must include a country ISO Code following the alpha-2 ISO format. You can use the [GeoIP Processor](https://docs.datadoghq.com/logs/log_configuration/processors/#geoip-parser) to do this, or manually include the [tags on ingest](https://docs.datadoghq.com/getting_started/tagging/#define-tags). See the [Log search documentation](https://docs.datadoghq.com/logs/search_syntax/) to configure a log event query. |
| RUM         | See the [RUM documentation](https://docs.datadoghq.com/real_user_monitoring/explorer/search_syntax/) to configure a RUM query.                                                                                                                                                                                                                                                                                                             |

**Note**: The Points layer shows a maximum of 100,000 events at a time.
   {% /tab %}



1. (Optional) Under **Visual Options**, use the **Set widget default view** dropdown to select where to initially focus the map. Select **Custom** to define a custom region, or search for the name of a country, state, or province.

### Options{% #options %}

#### Context links{% #context-links %}

[Context links](https://docs.datadoghq.com/dashboards/guide/context-links/) are enabled by default, you can toggle them on or off. Context links connect dashboard widgets with other pages (in Datadog, or third-party).

#### Visual formatting rules{% #visual-formatting-rules %}

Customize the region layer color of your Geomap widget with conditional rules.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription custom_links[object]A list of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`. requests [*required*][object]Array of request objects to display in the widget. May include an optional request for the region layer and/or an optional request for the points layer. Region layer requests must contain a `group-by` tag whose value is a country ISO code. See the [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) for information about building the `REQUEST_SCHEMA`. columns[object]Widget columns.field [*required*]stringWidget column field.width [*required*]enumWidget column width. Allowed enum values: `auto,compact,full` conditional_formats[object]Threshold (numeric) conditional formatting rules may be used by a regions layer.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator. formulas[object]List of formulas that operate on queries.aliasstringExpression alias.cell_display_modeenumDefine a display mode for the table cell. Allowed enum values: `number,bar,trend` cell_display_mode_optionsobjectCell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).trend_typeenumTrend type for the cell display mode options. Allowed enum values: `area,line,bars`y_scaleenumY scale for the cell display mode options. Allowed enum values: `shared,independent` conditional_formats[object]List of conditional formats.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator.formula [*required*]stringString expression built from queries, formulas, and functions. limitobjectOptions for limiting results returned.countint64Number of results to return.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
 number_formatobjectNumber format options for the widget. unit <oneOf>Number format unit. Option 1objectCanonical unit.per_unit_namestringThe name of the unit per item.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. Option 2objectCustom unit.labelstringThe label for the custom unit.typeenumThe type of custom unit. Allowed enum values: `custom_unit_label` unit_scaleobjectThe definition of `NumberFormatUnitScale` object.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. styleobjectStyling options for widget formulas.palettestringThe color palette used to display the formula. A guide to the available color palettes can be found at [https://docs.datadoghq.com/dashboards/guide/widget_colors](https://docs.datadoghq.com/dashboards/guide/widget_colors)palette_indexint64Index specifying which color to use within the palette. log_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.qstringThe widget metrics query. queries[ <oneOf>]List of queries that can be returned directly or used in formulas. Option 1objectA formula and functions metrics query.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for metrics queries. Allowed enum values: `metrics`name [*required*]stringName of the query for use in formulas.query [*required*]stringMetrics query definition.semantic_modeenumSemantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native` Option 2objectA formula and functions events query. compute [*required*]objectCompute options.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`intervalint64A time interval in milliseconds.metricstringMeasurable attribute to compute.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events` group_by[object]Group by options.facet [*required*]stringEvent facet.limitint64Number of groups to return. sortobjectOptions for sorting group by results.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`metricstringMetric used for sorting group by results.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes[string]An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.name [*required*]stringName of the query for use in formulas. searchobjectSearch options.query [*required*]stringEvents search string.storagestringOption for storage location. Feature in Private Beta. Option 3objectProcess query using formulas and functions.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData sources that rely on the process backend. Allowed enum values: `process,container`is_normalized_cpubooleanWhether to normalize the CPU percentages.limitint64Number of hits to return.metric [*required*]stringProcess metric name.name [*required*]stringName of query for use in formulas.sortenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters[string]An array of tags to filter by.text_filterstringText to use as filter. Option 4objectA formula and functions APM dependency stats query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`env [*required*]stringAPM environment.is_upstreambooleanDetermines whether stats for upstream or downstream dependencies should be queried.name [*required*]stringName of query to use in formulas.operation_name [*required*]stringName of operation on service.primary_tag_namestringThe name of the second primary tag used within APM; required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog).primary_tag_valuestringFilter APM data by the second primary tag. `primary_tag_name` must also be specified.resource_name [*required*]stringAPM resource.service [*required*]stringAPM service.stat [*required*]enumAPM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count` Option 5objectAPM resource stats query using formulas and functions.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM resource stats queries. Allowed enum values: `apm_resource_stats`env [*required*]stringAPM environment.group_by[string]Array of fields to group results by.name [*required*]stringName of this query to use in formulas.operation_namestringName of operation on service.primary_tag_namestringName of the second primary tag used within APM. Required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog)primary_tag_valuestringValue of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.resource_namestringAPM resource name.service [*required*]stringAPM service name.stat [*required*]enumAPM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99` Option 6objectA formula and functions metrics query.additional_query_filtersstringAdditional filters applied to the SLO query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for SLO measures queries. Allowed enum values: `slo`group_modeenumGroup mode to query measures. Allowed enum values: `overall,components`measure [*required*]enumSLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`namestringName of the query for use in formulas.slo_id [*required*]stringID of an SLO to query measures.slo_query_typeenumName of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice` Option 7objectA formula and functions Cloud Cost query.aggregatorenumAggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for Cloud Cost queries. Allowed enum values: `cloud_cost`name [*required*]stringName of the query for use in formulas.query [*required*]stringQuery for Cloud Cost data. queryobjectUpdated list stream widget.clustering_pattern_field_pathstringSpecifies the field for logs pattern clustering. Usable only with logs_pattern_stream. compute[object]Compute configuration for the List Stream Widget. Compute can be used only with the logs_transaction_stream (from 1 to 5 items) list stream source.aggregation [*required*]enumAggregation value. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,earliest,latest,most_frequent`facetstringFacet name.data_source [*required*]enumSource from which to query items to display in the stream. Allowed enum values: `logs_stream,audit_stream,ci_pipeline_stream,ci_test_stream,rum_issue_stream,apm_issue_stream,trace_stream,logs_issue_stream,logs_pattern_stream,logs_transaction_stream,event_stream,rum_stream,llm_observability_stream`
default: `apm_issue_stream`
event_sizeenumSize to use to display an event. Allowed enum values: `s,l` group_by[object]Group by configuration for the List Stream Widget. Group by can be used only with logs_pattern_stream (up to 4 items) or logs_transaction_stream (one group by item is required) list stream source.facet [*required*]stringFacet name.indexes[string]List of indexes.query_string [*required*]stringWidget query. sortobjectWhich column and order to sort bycolumn [*required*]stringFacet path for the columnorder [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`storagestringOption for storage location. Feature in Private Beta.response_formatenumTimeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list` rum_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. security_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. sortobjectThe controls for sorting the widget.countint64The number of items to limit the widget to. order_by[ <oneOf>]The array of items to sort the widget by in order. Option 1objectThe formula to sort the widget by.index [*required*]int64The index of the formula to sort by.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`type [*required*]enumSet the sort type to formula. Allowed enum values: `formula` Option 2objectThe group to sort the widget by.name [*required*]stringThe name of the group.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`type [*required*]enumSet the sort type to group. Allowed enum values: `group` styleobjectThe style to apply to the request for points layer.color_bystringThe category to color the points by. text_formats[object]Text formatting rules may be used by a points layer.custom_bg_colorstringHex representation of the custom background color. Used with custom background palette option.custom_fg_colorstringHex representation of the custom text color. Used with custom text palette option. match [*required*]objectMatch rule for the table widget text format.type [*required*]enumMatch or compare option. Allowed enum values: `is,is_not,contains,does_not_contain,starts_with,ends_with`value [*required*]stringTable Widget Match String.paletteenumColor-on-color palette to highlight replaced text. Allowed enum values: `white_on_red,white_on_yellow,white_on_green,black_on_light_red,black_on_light_yellow,black_on_light_green,red_on_white,yellow_on_white,green_on_white,custom_bg,custom_text`
default: `white_on_green`
 replace <oneOf>Replace rule for the table widget text format. Option 1objectMatch All definition.type [*required*]enumTable widget text format replace all type. Allowed enum values: `all`with [*required*]stringReplace All type. Option 2objectMatch Sub-string definition.substring [*required*]stringText that will be replaced.type [*required*]enumTable widget text format replace sub-string type. Allowed enum values: `substring`with [*required*]stringText that will replace original sub-string. style [*required*]objectThe style to apply to the widget.palette [*required*]stringThe color palette to apply to the widget.palette_flip [*required*]booleanWhether to flip the palette tones. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringThe title of your widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringThe size of the title.type [*required*]enumType of the geomap widget. Allowed enum values: `geomap`
default: `geomap`
 view [*required*]objectThe view of the world that the map should render.focus [*required*]stringThe 2-letter ISO code of a country to focus the map on, or `WORLD` for global view, or a region (`EMEA`, `APAC`, `LATAM`), or a continent (`NORTH_AMERICA`, `SOUTH_AMERICA`, `EUROPE`, `AFRICA`, `ASIA`, `OCEANIA`).
{% /tab %}

{% tab title="example" %}

```json
{
  "custom_links": [
    {
      "is_hidden": false,
      "label": "Search logs for {{host}}",
      "link": "https://app.datadoghq.com/logs?query={{host}}",
      "override_label": "logs"
    }
  ],
  "requests": [
    {
      "columns": [
        {
          "field": "content",
          "width": "compact"
        }
      ],
      "conditional_formats": [
        {
          "comparator": ">",
          "custom_bg_color": "string",
          "custom_fg_color": "string",
          "hide_value": false,
          "image_url": "string",
          "metric": "string",
          "palette": "blue",
          "timeframe": "string",
          "value": 0
        }
      ],
      "formulas": [
        {
          "alias": "string",
          "cell_display_mode": "number",
          "cell_display_mode_options": {
            "trend_type": "area",
            "y_scale": "shared"
          },
          "conditional_formats": [
            {
              "comparator": ">",
              "custom_bg_color": "string",
              "custom_fg_color": "string",
              "hide_value": false,
              "image_url": "string",
              "metric": "string",
              "palette": "blue",
              "timeframe": "string",
              "value": 0
            }
          ],
          "formula": "func(a) + b",
          "limit": {
            "count": "integer",
            "order": "string"
          },
          "number_format": {
            "unit": {
              "per_unit_name": "bytes",
              "type": "canonical_unit",
              "unit_name": "bytes"
            },
            "unit_scale": {
              "type": "canonical_unit",
              "unit_name": "bytes"
            }
          },
          "style": {
            "palette": "classic",
            "palette_index": 1
          }
        }
      ],
      "log_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "q": "string",
      "queries": [],
      "query": {
        "clustering_pattern_field_path": "message",
        "compute": [
          {
            "aggregation": "count",
            "facet": "resource_name"
          }
        ],
        "data_source": "apm_issue_stream",
        "event_size": "string",
        "group_by": [
          {
            "facet": "resource_name"
          }
        ],
        "indexes": [],
        "query_string": "@service:app",
        "sort": {
          "column": "",
          "order": "desc"
        },
        "storage": "indexes"
      },
      "response_format": "timeseries",
      "rum_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "security_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "sort": {
        "count": "integer",
        "order_by": [
          {
            "index": 0,
            "order": "desc",
            "type": "formula"
          }
        ]
      },
      "style": {
        "color_by": "status"
      },
      "text_formats": [
        {
          "custom_bg_color": "#632ca6",
          "custom_fg_color": "#632ca6",
          "match": {
            "type": "is",
            "value": "Match Value"
          },
          "palette": "string",
          "replace": {
            "type": "all",
            "with": "all"
          }
        }
      ]
    }
  ],
  "style": {
    "palette": "hostmap_blues",
    "palette_flip": false
  },
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "geomap",
  "view": {
    "focus": "WORLD"
  }
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Notebooks](https://docs.datadoghq.com/notebooks/)
