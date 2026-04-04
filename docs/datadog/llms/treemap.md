# Source: https://docs.datadoghq.com/dashboards/widgets/treemap.md

---
title: Treemap Widget
description: Graph proportions of one or more datasets
breadcrumbs: Docs > Dashboards > Widgets > Treemap Widget
---

# Treemap Widget

The treemap widget allows you to display proportions of one or more datasets. This widget can display a single dataset with corresponding proportions, or multiple datasets with nested proportions.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/treemap/treemap_overview.1f18f0c0ed018f1dc26ff12da51e1130.png?auto=format"
   alt="A treemap widget with unique page views stemming from the Real User Monitoring (RUM) dataset are shown at both the country and browser level. The outer groups - distinguished by color - shows the user's country." /%}

## Configuration{% #configuration %}

1. Select from the available data sources.
1. Configure the query, see the following resources for more information:
   - Metrics: See the [querying ](https://docs.datadoghq.com/dashboards/querying)documentation to configure a metric query.
   - Events: See the [log search](https://docs.datadoghq.com/logs/explorer/search_syntax/) documentation to configure a log event query.
1. (Optional) Modify query with a [formula](https://docs.datadoghq.com/dashboards/functions/).
1. Customize your graph.

## Customization{% #customization %}

### Context links{% #context-links %}

[Context links](https://docs.datadoghq.com/dashboards/guide/context-links/) are enabled by default, and can be toggled on or off. Context links bridge dashboard widgets with other pages (in Datadog, or third-party).

## Display and interaction{% #display-and-interaction %}

### Filter and focus{% #filter-and-focus %}

In the case where multiple groups of data are plotted at once, you can filter the widget to a single category and view proportions within it.

To filter and focus on a single category, hover over the outer portion of the category, and click. To go back to the previous view, click the **back** button on the top left header of the widget.

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/widgets/treemap/focus_animation.mp4" /%}

### Accessing the context menu{% #accessing-the-context-menu %}

To access the context menu, first hover over an individual category: this can be a nested category, or group - such as **Canada**, or **Canada > Edge** in the following example. This reveals a dropdown button in the top right corner. When clicked, the context menu appears.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/treemap/context_menu_dropdown.2cc386d8ba4796950e4175d8d5d317a5.png?auto=format"
   alt="The dropdown arrow button is revealed when hovering over a category" /%}

### Full-screen{% #full-screen %}

Viewing the treemap widget in full-screen reveals the standard set of [full-screen options](https://docs.datadoghq.com/dashboards/widgets/#full-screen).

## Pie chart widget{% #pie-chart-widget %}

Like the treemap widget, the [pie chart widget](https://docs.datadoghq.com/dashboards/widgets/pie_chart/) can also be used to display nested proportions. The primary difference between the two is that the pie chart displays proportions in radial slices, and the treemap displays nested rectangles.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptioncolor_byenum**DEPRECATED**: (deprecated) The attribute formerly used to determine color in the widget. Allowed enum values: `user`
default: `user`
 custom_links[object]List of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.group_byenum**DEPRECATED**: (deprecated) The attribute formerly used to group elements in the widget. Allowed enum values: `user,family,process` requests [*required*][object]List of treemap widget requests. formulas[object]List of formulas that operate on queries.aliasstringExpression alias.cell_display_modeenumDefine a display mode for the table cell. Allowed enum values: `number,bar,trend` cell_display_mode_optionsobjectCell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).trend_typeenumTrend type for the cell display mode options. Allowed enum values: `area,line,bars`y_scaleenumY scale for the cell display mode options. Allowed enum values: `shared,independent` conditional_formats[object]List of conditional formats.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator.formula [*required*]stringString expression built from queries, formulas, and functions. limitobjectOptions for limiting results returned.countint64Number of results to return.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
 number_formatobjectNumber format options for the widget. unit <oneOf>Number format unit. Option 1objectCanonical unit.per_unit_namestringThe name of the unit per item.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. Option 2objectCustom unit.labelstringThe label for the custom unit.typeenumThe type of custom unit. Allowed enum values: `custom_unit_label` unit_scaleobjectThe definition of `NumberFormatUnitScale` object.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. styleobjectStyling options for widget formulas.palettestringThe color palette used to display the formula. A guide to the available color palettes can be found at [https://docs.datadoghq.com/dashboards/guide/widget_colors](https://docs.datadoghq.com/dashboards/guide/widget_colors)palette_indexint64Index specifying which color to use within the palette.qstringThe widget metrics query. queries[ <oneOf>]List of queries that can be returned directly or used in formulas. Option 1objectA formula and functions metrics query.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for metrics queries. Allowed enum values: `metrics`name [*required*]stringName of the query for use in formulas.query [*required*]stringMetrics query definition.semantic_modeenumSemantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native` Option 2objectA formula and functions events query. compute [*required*]objectCompute options.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`intervalint64A time interval in milliseconds.metricstringMeasurable attribute to compute.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events` group_by[object]Group by options.facet [*required*]stringEvent facet.limitint64Number of groups to return. sortobjectOptions for sorting group by results.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`metricstringMetric used for sorting group by results.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes[string]An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.name [*required*]stringName of the query for use in formulas. searchobjectSearch options.query [*required*]stringEvents search string.storagestringOption for storage location. Feature in Private Beta. Option 3objectProcess query using formulas and functions.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData sources that rely on the process backend. Allowed enum values: `process,container`is_normalized_cpubooleanWhether to normalize the CPU percentages.limitint64Number of hits to return.metric [*required*]stringProcess metric name.name [*required*]stringName of query for use in formulas.sortenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters[string]An array of tags to filter by.text_filterstringText to use as filter. Option 4objectA formula and functions APM dependency stats query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`env [*required*]stringAPM environment.is_upstreambooleanDetermines whether stats for upstream or downstream dependencies should be queried.name [*required*]stringName of query to use in formulas.operation_name [*required*]stringName of operation on service.primary_tag_namestringThe name of the second primary tag used within APM; required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog).primary_tag_valuestringFilter APM data by the second primary tag. `primary_tag_name` must also be specified.resource_name [*required*]stringAPM resource.service [*required*]stringAPM service.stat [*required*]enumAPM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count` Option 5objectAPM resource stats query using formulas and functions.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM resource stats queries. Allowed enum values: `apm_resource_stats`env [*required*]stringAPM environment.group_by[string]Array of fields to group results by.name [*required*]stringName of this query to use in formulas.operation_namestringName of operation on service.primary_tag_namestringName of the second primary tag used within APM. Required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog)primary_tag_valuestringValue of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.resource_namestringAPM resource name.service [*required*]stringAPM service name.stat [*required*]enumAPM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99` Option 6objectA formula and functions metrics query.additional_query_filtersstringAdditional filters applied to the SLO query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for SLO measures queries. Allowed enum values: `slo`group_modeenumGroup mode to query measures. Allowed enum values: `overall,components`measure [*required*]enumSLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`namestringName of the query for use in formulas.slo_id [*required*]stringID of an SLO to query measures.slo_query_typeenumName of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice` Option 7objectA formula and functions Cloud Cost query.aggregatorenumAggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for Cloud Cost queries. Allowed enum values: `cloud_cost`name [*required*]stringName of the query for use in formulas.query [*required*]stringQuery for Cloud Cost data.response_formatenumTimeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`size_byenum**DEPRECATED**: (deprecated) The attribute formerly used to determine size in the widget. Allowed enum values: `pct_cpu,pct_mem` time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringTitle of your widget.type [*required*]enumType of the treemap widget. Allowed enum values: `treemap`
default: `treemap`
{% /tab %}

{% tab title="example" %}

```json
{
  "color_by": "user",
  "custom_links": [
    {
      "is_hidden": false,
      "label": "Search logs for {{host}}",
      "link": "https://app.datadoghq.com/logs?query={{host}}",
      "override_label": "logs"
    }
  ],
  "group_by": "user",
  "requests": [
    {
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
      "q": "string",
      "queries": [],
      "response_format": "timeseries"
    }
  ],
  "size_by": "pct_cpu",
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "type": "treemap"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Pie Chart Widget](https://docs.datadoghq.com/dashboards/widgets/pie_chart/)
- [Top List Widget](https://docs.datadoghq.com/dashboards/widgets/top_list/)
- [Bar Chart Widget](https://docs.datadoghq.com/dashboards/widgets/bar_chart/)
