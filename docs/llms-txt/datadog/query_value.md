# Source: https://docs.datadoghq.com/dashboards/widgets/query_value.md

---
title: Query Value Widget
description: Display an aggregated value for a given metric query
breadcrumbs: Docs > Dashboards > Widgets > Query Value Widget
---

# Query Value Widget

Query values display the current value of a given metric, APM, or log query. They come with conditional formatting (such as a green/yellow/red background) to convey whether the value is in the expected range. This can be supplemented with optional backgrounds of timeseries data. The values displayed by a query value do not require an instantaneous measurement.

The widget can display the latest value reported, or an aggregate computed from all query values across the time window. These visualizations provide a narrow but unambiguous window into your infrastructure query.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/query_value/query_value_change_indicator.9045f68ab20095ae61f69786f529aec2.png?auto=format"
   alt="Query value widget" /%}

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/query_value/query-value-widget-setup1.d4185c97ee2d82ba6ba69e81d4e14fa6.png?auto=format"
   alt="Query value widget setup" /%}

### Configuration{% #configuration %}

1. Choose the data to graph:
   - Metric: See the [Querying documentation](https://docs.datadoghq.com/dashboards/querying/#overview) to configure a metric query.
   - Indexed Spans: See the [Trace search documentation](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#search-bar) to configure an Indexed Span query.
   - Log Events: See the [Log search documentation](https://docs.datadoghq.com/logs/search_syntax/) to configure a log event query.
1. Reduce the query values to a single value, calculated as the `avg`, `min`, `sum`, `max`, or `last` value of all data points in the specified timeframe. Percentile values like `p75` or `p90` can also be used where supported.
1. Choose the units and the formatting. Autoformat scales the dashboard for you based on the units.
1. Optionally, configure a conditional format depending on the value displayed. See Visual Formatting Rules for more examples.
1. Optionally, overlay a timeseries background:
   - Min to Max: A scale graph from minimum to maximum.
   - Line: A scale graph to include zero (0).
   - Bars: Shows discrete, periodic measurements.

### Options{% #options %}

#### Visual formatting rules{% #visual-formatting-rules %}

{% alert level="info" %}
Visual formatting rules should be based on the metric's raw value. If the metric base unit is in nanoseconds, but the Query Value autoformats to seconds, your conditional rules should be based on nanoseconds.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/query_value/visual_formatting_rules_custom_img.21e19d67fc9b5b9614292d2c316f7c99.png?auto=format"
   alt="Query value widget visual formatting rules with custom image background" /%}

Customize the background of your Query Value widget with conditional rules. You have the option of adding a background color, font color, or a custom image. With custom images, you can either upload an image from your local computer or reference images from the public internet. Internal servers must be updated to support cross origin requests to reference internal images.

#### Change indicator{% #change-indicator %}

Enable the **Change Indicator** to highlight how the current value compares to a previous time frame.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/query_value/change_indicator_config.eebd92d2dd334f78b955e0b5f8738401.png?auto=format"
   alt="Query value widget change indicator configuration options" /%}

- **Display**: `Relative Change` (percentage), `Absolute Change` (raw value), `Both`, or `Off`
- **Color**: `Increases as better` (green â, red â), `Decreases as better` (red â, green â), or `Neutral`
- **Compared to**: `Previous Period`, `Previous Day/Week/Month`, or `Custom` time frame

The widget displays the difference below the primary metric, helping highlight recent trends at a glance.

#### Context links{% #context-links %}

[Context links](https://docs.datadoghq.com/dashboards/guide/context-links/) are enabled by default, and can be toggled on or off. Context links bridge dashboard widgets with other pages in Datadog, or third party applications.

#### Global time{% #global-time %}

Choose whether your widget has a custom timeframe or the dashboard's global timeframe.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptionautoscalebooleanWhether to use auto-scaling or not. custom_links[object]List of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.custom_unitstringDisplay a unit of your choice on the widget.precisionint64Number of decimals to show. If not defined, the widget uses the raw value. requests [*required*][object]Widget definition.aggregatorenumAggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile` apm_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. audit_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. conditional_formats[object]List of conditional formats.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator. event_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. formulas[object]List of formulas that operate on queries.aliasstringExpression alias.cell_display_modeenumDefine a display mode for the table cell. Allowed enum values: `number,bar,trend` cell_display_mode_optionsobjectCell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).trend_typeenumTrend type for the cell display mode options. Allowed enum values: `area,line,bars`y_scaleenumY scale for the cell display mode options. Allowed enum values: `shared,independent` conditional_formats[object]List of conditional formats.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator.formula [*required*]stringString expression built from queries, formulas, and functions. limitobjectOptions for limiting results returned.countint64Number of results to return.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
 number_formatobjectNumber format options for the widget. unit <oneOf>Number format unit. Option 1objectCanonical unit.per_unit_namestringThe name of the unit per item.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. Option 2objectCustom unit.labelstringThe label for the custom unit.typeenumThe type of custom unit. Allowed enum values: `custom_unit_label` unit_scaleobjectThe definition of `NumberFormatUnitScale` object.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. styleobjectStyling options for widget formulas.palettestringThe color palette used to display the formula. A guide to the available color palettes can be found at [https://docs.datadoghq.com/dashboards/guide/widget_colors](https://docs.datadoghq.com/dashboards/guide/widget_colors)palette_indexint64Index specifying which color to use within the palette. log_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. network_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. process_queryobjectThe process query to use in the widget.filter_by[string]List of processes.limitint64Max number of items in the filter list.metric [*required*]stringYour chosen metric.search_bystringYour chosen search term. profile_metrics_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.qstringTODO. queries[ <oneOf>]List of queries that can be returned directly or used in formulas. Option 1objectA formula and functions metrics query.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for metrics queries. Allowed enum values: `metrics`name [*required*]stringName of the query for use in formulas.query [*required*]stringMetrics query definition.semantic_modeenumSemantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native` Option 2objectA formula and functions events query. compute [*required*]objectCompute options.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`intervalint64A time interval in milliseconds.metricstringMeasurable attribute to compute.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events` group_by[object]Group by options.facet [*required*]stringEvent facet.limitint64Number of groups to return. sortobjectOptions for sorting group by results.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`metricstringMetric used for sorting group by results.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes[string]An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.name [*required*]stringName of the query for use in formulas. searchobjectSearch options.query [*required*]stringEvents search string.storagestringOption for storage location. Feature in Private Beta. Option 3objectProcess query using formulas and functions.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData sources that rely on the process backend. Allowed enum values: `process,container`is_normalized_cpubooleanWhether to normalize the CPU percentages.limitint64Number of hits to return.metric [*required*]stringProcess metric name.name [*required*]stringName of query for use in formulas.sortenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters[string]An array of tags to filter by.text_filterstringText to use as filter. Option 4objectA formula and functions APM dependency stats query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`env [*required*]stringAPM environment.is_upstreambooleanDetermines whether stats for upstream or downstream dependencies should be queried.name [*required*]stringName of query to use in formulas.operation_name [*required*]stringName of operation on service.primary_tag_namestringThe name of the second primary tag used within APM; required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog).primary_tag_valuestringFilter APM data by the second primary tag. `primary_tag_name` must also be specified.resource_name [*required*]stringAPM resource.service [*required*]stringAPM service.stat [*required*]enumAPM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count` Option 5objectAPM resource stats query using formulas and functions.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM resource stats queries. Allowed enum values: `apm_resource_stats`env [*required*]stringAPM environment.group_by[string]Array of fields to group results by.name [*required*]stringName of this query to use in formulas.operation_namestringName of operation on service.primary_tag_namestringName of the second primary tag used within APM. Required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog)primary_tag_valuestringValue of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.resource_namestringAPM resource name.service [*required*]stringAPM service name.stat [*required*]enumAPM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99` Option 6objectA formula and functions metrics query.additional_query_filtersstringAdditional filters applied to the SLO query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for SLO measures queries. Allowed enum values: `slo`group_modeenumGroup mode to query measures. Allowed enum values: `overall,components`measure [*required*]enumSLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`namestringName of the query for use in formulas.slo_id [*required*]stringID of an SLO to query measures.slo_query_typeenumName of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice` Option 7objectA formula and functions Cloud Cost query.aggregatorenumAggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for Cloud Cost queries. Allowed enum values: `cloud_cost`name [*required*]stringName of the query for use in formulas.query [*required*]stringQuery for Cloud Cost data.response_formatenumTimeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list` rum_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. security_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.text_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right` time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed` timeseries_backgroundobjectSet a timeseries on the widget background.type [*required*]enumTimeseries is made using an area or bars. Allowed enum values: `bars,area`
default: `area`
 yaxisobjectAxis controls for the widget.include_zerobooleanSet to `true` to include zero.labelstringThe label of the axis to display on the graph. Only usable on Scatterplot Widgets.maxstringSpecifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
minstringSpecifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scalestringSpecifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
titlestringTitle of your widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the query value widget. Allowed enum values: `query_value`
default: `query_value`
{% /tab %}

{% tab title="example" %}

```json
{
  "autoscale": false,
  "custom_links": [
    {
      "is_hidden": false,
      "label": "Search logs for {{host}}",
      "link": "https://app.datadoghq.com/logs?query={{host}}",
      "override_label": "logs"
    }
  ],
  "custom_unit": "string",
  "precision": "integer",
  "requests": [
    {
      "aggregator": "string",
      "apm_query": {
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
      "audit_query": {
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
      "event_query": {
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
      "network_query": {
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
      "process_query": {
        "filter_by": [],
        "limit": "integer",
        "metric": "system.load.1",
        "search_by": "string"
      },
      "profile_metrics_query": {
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
      }
    }
  ],
  "text_align": "string",
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "timeseries_background": {
    "type": "bars",
    "yaxis": {
      "include_zero": false,
      "label": "string",
      "max": "string",
      "min": "string",
      "scale": "string"
    }
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "query_value"
}
```

{% /tab %}

{% /tab %}

### Troubleshooting{% #troubleshooting %}

- If your query is using a percentile value to aggregate underlying data points, you may find that the value returned on the widget remains the same across different time ranges. This behavior can be expected with a large sample size of underlying data points. Changes in values like this can typically be more easily found across narrower time ranges. For more information on this concept, see the [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers).

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
