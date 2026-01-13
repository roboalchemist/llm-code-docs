# Source: https://docs.datadoghq.com/api/latest/notebooks/

# Notebooks
Interact with your notebooks through the API to make it easier to organize, find, and share all of your notebooks with your team and organization. For more information, see the [Notebooks documentation](https://docs.datadoghq.com/notebooks/).
## [Create a notebook](https://docs.datadoghq.com/api/latest/notebooks/#create-a-notebook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/notebooks/#create-a-notebook-v1)


POST https://api.ap1.datadoghq.com/api/v1/notebookshttps://api.ap2.datadoghq.com/api/v1/notebookshttps://api.datadoghq.eu/api/v1/notebookshttps://api.ddog-gov.com/api/v1/notebookshttps://api.datadoghq.com/api/v1/notebookshttps://api.us3.datadoghq.com/api/v1/notebookshttps://api.us5.datadoghq.com/api/v1/notebooks
### Overview
Create a notebook using the specified options. This endpoint requires the `notebooks_write` permission.
### Request
#### Body Data (required)
The JSON description of the notebook you want to create.
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Field
Type
Description
data [_required_]
object
The data for a notebook create request.
attributes [_required_]
object
The data attributes of a notebook.
cells [_required_]
[object]
List of cells to display in the notebook.
attributes [_required_]
<oneOf>
The attributes of a notebook cell in create cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
index [_required_]
int64
The index of the formula to sort by.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to formula. Allowed enum values: `formula`
Option 2
object
The group to sort the widget by.
name [_required_]
string
The name of the group.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to group. Allowed enum values: `group`
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time [_required_]
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
```
{
  "data": {
    "attributes": {
      "cells": [
        {
          "attributes": {
            "definition": {
              "text": "## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```",
              "type": "markdown"
            }
          },
          "type": "notebook_cells"
        },
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "type": "notebook_cells"
        }
      ],
      "name": "Example-Notebook",
      "status": "published",
      "time": {
        "live_span": "1h"
      }
    },
    "type": "notebooks"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/notebooks/#CreateNotebook-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/notebooks/#CreateNotebook-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/notebooks/#CreateNotebook-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/notebooks/#CreateNotebook-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


The description of a notebook response.
Field
Type
Description
data
object
The data for a notebook.
attributes [_required_]
object
The attributes of a notebook.
author
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
cells [_required_]
[object]
List of cells to display in the notebook.
attributes [_required_]
<oneOf>
The attributes of a notebook cell response. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
index [_required_]
int64
The index of the formula to sort by.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to formula. Allowed enum values: `formula`
Option 2
object
The group to sort the widget by.
name [_required_]
string
The name of the group.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to group. Allowed enum values: `group`
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
string
Notebook cell ID.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
created
date-time
UTC time stamp for when the notebook was created.
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
modified
date-time
UTC time stamp for when the notebook was last modified.
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time [_required_]
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
int64
Unique notebook ID, assigned when you create the notebook.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
```
{
  "data": {
    "attributes": {
      "author": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "status": "string",
        "title": "string",
        "verified": false
      },
      "cells": [
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "id": "abcd1234",
          "type": "notebook_cells"
        }
      ],
      "created": "2021-02-24T23:14:15.173964+00:00",
      "metadata": {
        "is_template": false,
        "take_snapshots": false,
        "type": "investigation"
      },
      "modified": "2021-02-24T23:15:23.274966+00:00",
      "name": "Example Notebook",
      "status": "published",
      "time": {
        "live_span": "5m"
      }
    },
    "id": 123456,
    "type": "notebooks"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=typescript)


#####  Create a notebook returns "OK" response
Copy
```
                          ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/notebooks" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "cells": [
        {
          "attributes": {
            "definition": {
              "text": "## Some test markdown\n\nWith some example content.",
              "type": "markdown"
            }
          },
          "type": "notebook_cells"
        },
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "type": "notebook_cells"
        }
      ],
      "name": "Example Notebook",
      "time": {
        "live_span": "1h"
      }
    },
    "type": "notebooks"
  }
}
EOF  

                        
```

#####  Create a notebook returns "OK" response
```
// Create a notebook returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	body := datadogV1.NotebookCreateRequest{
		Data: datadogV1.NotebookCreateData{
			Attributes: datadogV1.NotebookCreateDataAttributes{
				Cells: []datadogV1.NotebookCellCreateRequest{
					{
						Attributes: datadogV1.NotebookCellCreateRequestAttributes{
							NotebookMarkdownCellAttributes: &datadogV1.NotebookMarkdownCellAttributes{
								Definition: datadogV1.NotebookMarkdownCellDefinition{
									Text: `## Some test markdown

` + "```" + `
var x, y;
x = 5;
y = 6;
` + "```",
									Type: datadogV1.NOTEBOOKMARKDOWNCELLDEFINITIONTYPE_MARKDOWN,
								},
							}},
						Type: datadogV1.NOTEBOOKCELLRESOURCETYPE_NOTEBOOK_CELLS,
					},
					{
						Attributes: datadogV1.NotebookCellCreateRequestAttributes{
							NotebookTimeseriesCellAttributes: &datadogV1.NotebookTimeseriesCellAttributes{
								Definition: datadogV1.TimeseriesWidgetDefinition{
									Requests: []datadogV1.TimeseriesWidgetRequest{
										{
											DisplayType: datadogV1.WIDGETDISPLAYTYPE_LINE.Ptr(),
											Q:           datadog.PtrString("avg:system.load.1{*}"),
											Style: &datadogV1.WidgetRequestStyle{
												LineType:  datadogV1.WIDGETLINETYPE_SOLID.Ptr(),
												LineWidth: datadogV1.WIDGETLINEWIDTH_NORMAL.Ptr(),
												Palette:   datadog.PtrString("dog_classic"),
											},
										},
									},
									ShowLegend: datadog.PtrBool(true),
									Type:       datadogV1.TIMESERIESWIDGETDEFINITIONTYPE_TIMESERIES,
									Yaxis: &datadogV1.WidgetAxis{
										Scale: datadog.PtrString("linear"),
									},
								},
								GraphSize: datadogV1.NOTEBOOKGRAPHSIZE_MEDIUM.Ptr(),
								SplitBy: &datadogV1.NotebookSplitBy{
									Keys: []string{},
									Tags: []string{},
								},
								Time: *datadogV1.NewNullableNotebookCellTime(nil),
							}},
						Type: datadogV1.NOTEBOOKCELLRESOURCETYPE_NOTEBOOK_CELLS,
					},
				},
				Name:   "Example-Notebook",
				Status: datadogV1.NOTEBOOKSTATUS_PUBLISHED.Ptr(),
				Time: datadogV1.NotebookGlobalTime{
					NotebookRelativeTime: &datadogV1.NotebookRelativeTime{
						LiveSpan: datadogV1.WIDGETLIVESPAN_PAST_ONE_HOUR,
					}},
			},
			Type: datadogV1.NOTEBOOKRESOURCETYPE_NOTEBOOKS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewNotebooksApi(apiClient)
	resp, r, err := api.CreateNotebook(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotebooksApi.CreateNotebook`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NotebooksApi.CreateNotebook`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a notebook returns "OK" response
```
// Create a notebook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.NotebooksApi;
import com.datadog.api.client.v1.model.NotebookCellCreateRequest;
import com.datadog.api.client.v1.model.NotebookCellCreateRequestAttributes;
import com.datadog.api.client.v1.model.NotebookCellResourceType;
import com.datadog.api.client.v1.model.NotebookCreateData;
import com.datadog.api.client.v1.model.NotebookCreateDataAttributes;
import com.datadog.api.client.v1.model.NotebookCreateRequest;
import com.datadog.api.client.v1.model.NotebookGlobalTime;
import com.datadog.api.client.v1.model.NotebookGraphSize;
import com.datadog.api.client.v1.model.NotebookMarkdownCellAttributes;
import com.datadog.api.client.v1.model.NotebookMarkdownCellDefinition;
import com.datadog.api.client.v1.model.NotebookMarkdownCellDefinitionType;
import com.datadog.api.client.v1.model.NotebookRelativeTime;
import com.datadog.api.client.v1.model.NotebookResourceType;
import com.datadog.api.client.v1.model.NotebookResponse;
import com.datadog.api.client.v1.model.NotebookSplitBy;
import com.datadog.api.client.v1.model.NotebookStatus;
import com.datadog.api.client.v1.model.NotebookTimeseriesCellAttributes;
import com.datadog.api.client.v1.model.TimeseriesWidgetDefinition;
import com.datadog.api.client.v1.model.TimeseriesWidgetDefinitionType;
import com.datadog.api.client.v1.model.TimeseriesWidgetRequest;
import com.datadog.api.client.v1.model.WidgetAxis;
import com.datadog.api.client.v1.model.WidgetDisplayType;
import com.datadog.api.client.v1.model.WidgetLineType;
import com.datadog.api.client.v1.model.WidgetLineWidth;
import com.datadog.api.client.v1.model.WidgetLiveSpan;
import com.datadog.api.client.v1.model.WidgetRequestStyle;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NotebooksApi apiInstance = new NotebooksApi(defaultClient);

    NotebookCreateRequest body =
        new NotebookCreateRequest()
            .data(
                new NotebookCreateData()
                    .attributes(
                        new NotebookCreateDataAttributes()
                            .cells(
                                Arrays.asList(
                                    new NotebookCellCreateRequest()
                                        .attributes(
                                            new NotebookCellCreateRequestAttributes(
                                                new NotebookMarkdownCellAttributes()
                                                    .definition(
                                                        new NotebookMarkdownCellDefinition()
                                                            .text(
                                                                """
## Some test markdown

```
var x, y;
x = 5;
y = 6;
```
""")
                                                            .type(
                                                                NotebookMarkdownCellDefinitionType
                                                                    .MARKDOWN))))
                                        .type(NotebookCellResourceType.NOTEBOOK_CELLS),
                                    new NotebookCellCreateRequest()
                                        .attributes(
                                            new NotebookCellCreateRequestAttributes(
                                                new NotebookTimeseriesCellAttributes()
                                                    .definition(
                                                        new TimeseriesWidgetDefinition()
                                                            .requests(
                                                                Collections.singletonList(
                                                                    new TimeseriesWidgetRequest()
                                                                        .displayType(
                                                                            WidgetDisplayType.LINE)
                                                                        .q("avg:system.load.1{*}")
                                                                        .style(
                                                                            new WidgetRequestStyle()
                                                                                .lineType(
                                                                                    WidgetLineType
                                                                                        .SOLID)
                                                                                .lineWidth(
                                                                                    WidgetLineWidth
                                                                                        .NORMAL)
                                                                                .palette(
                                                                                    "dog_classic"))))
                                                            .showLegend(true)
                                                            .type(
                                                                TimeseriesWidgetDefinitionType
                                                                    .TIMESERIES)
                                                            .yaxis(
                                                                new WidgetAxis().scale("linear")))
                                                    .graphSize(NotebookGraphSize.MEDIUM)
                                                    .splitBy(new NotebookSplitBy())
                                                    .time(null)))
                                        .type(NotebookCellResourceType.NOTEBOOK_CELLS)))
                            .name("Example-Notebook")
                            .status(NotebookStatus.PUBLISHED)
                            .time(
                                new NotebookGlobalTime(
                                    new NotebookRelativeTime()
                                        .liveSpan(WidgetLiveSpan.PAST_ONE_HOUR))))
                    .type(NotebookResourceType.NOTEBOOKS));

    try {
      NotebookResponse result = apiInstance.createNotebook(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotebooksApi#createNotebook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a notebook returns "OK" response
```
"""
Create a notebook returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_create_data import NotebookCreateData
from datadog_api_client.v1.model.notebook_create_data_attributes import NotebookCreateDataAttributes
from datadog_api_client.v1.model.notebook_create_request import NotebookCreateRequest
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition
from datadog_api_client.v1.model.notebook_markdown_cell_definition_type import NotebookMarkdownCellDefinitionType
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

body = NotebookCreateRequest(
    data=NotebookCreateData(
        attributes=NotebookCreateDataAttributes(
            cells=[
                NotebookCellCreateRequest(
                    attributes=NotebookMarkdownCellAttributes(
                        definition=NotebookMarkdownCellDefinition(
                            text="## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```",
                            type=NotebookMarkdownCellDefinitionType.MARKDOWN,
                        ),
                    ),
                    type=NotebookCellResourceType.NOTEBOOK_CELLS,
                ),
                NotebookCellCreateRequest(
                    attributes=NotebookTimeseriesCellAttributes(
                        definition=TimeseriesWidgetDefinition(
                            requests=[
                                TimeseriesWidgetRequest(
                                    display_type=WidgetDisplayType.LINE,
                                    q="avg:system.load.1{*}",
                                    style=WidgetRequestStyle(
                                        line_type=WidgetLineType.SOLID,
                                        line_width=WidgetLineWidth.NORMAL,
                                        palette="dog_classic",
                                    ),
                                ),
                            ],
                            show_legend=True,
                            type=TimeseriesWidgetDefinitionType.TIMESERIES,
                            yaxis=WidgetAxis(
                                scale="linear",
                            ),
                        ),
                        graph_size=NotebookGraphSize.MEDIUM,
                        split_by=NotebookSplitBy(
                            keys=[],
                            tags=[],
                        ),
                        time=None,
                    ),
                    type=NotebookCellResourceType.NOTEBOOK_CELLS,
                ),
            ],
            name="Example-Notebook",
            status=NotebookStatus.PUBLISHED,
            time=NotebookRelativeTime(
                live_span=WidgetLiveSpan.PAST_ONE_HOUR,
            ),
        ),
        type=NotebookResourceType.NOTEBOOKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.create_notebook(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a notebook returns "OK" response
```
# Create a notebook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::NotebooksAPI.new

body = DatadogAPIClient::V1::NotebookCreateRequest.new({
  data: DatadogAPIClient::V1::NotebookCreateData.new({
    attributes: DatadogAPIClient::V1::NotebookCreateDataAttributes.new({
      cells: [
        DatadogAPIClient::V1::NotebookCellCreateRequest.new({
          attributes: DatadogAPIClient::V1::NotebookMarkdownCellAttributes.new({
            definition: DatadogAPIClient::V1::NotebookMarkdownCellDefinition.new({
              text: '## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```',
              type: DatadogAPIClient::V1::NotebookMarkdownCellDefinitionType::MARKDOWN,
            }),
          }),
          type: DatadogAPIClient::V1::NotebookCellResourceType::NOTEBOOK_CELLS,
        }),
        DatadogAPIClient::V1::NotebookCellCreateRequest.new({
          attributes: DatadogAPIClient::V1::NotebookTimeseriesCellAttributes.new({
            definition: DatadogAPIClient::V1::TimeseriesWidgetDefinition.new({
              requests: [
                DatadogAPIClient::V1::TimeseriesWidgetRequest.new({
                  display_type: DatadogAPIClient::V1::WidgetDisplayType::LINE,
                  q: "avg:system.load.1{*}",
                  style: DatadogAPIClient::V1::WidgetRequestStyle.new({
                    line_type: DatadogAPIClient::V1::WidgetLineType::SOLID,
                    line_width: DatadogAPIClient::V1::WidgetLineWidth::NORMAL,
                    palette: "dog_classic",
                  }),
                }),
              ],
              show_legend: true,
              type: DatadogAPIClient::V1::TimeseriesWidgetDefinitionType::TIMESERIES,
              yaxis: DatadogAPIClient::V1::WidgetAxis.new({
                scale: "linear",
              }),
            }),
            graph_size: DatadogAPIClient::V1::NotebookGraphSize::MEDIUM,
            split_by: DatadogAPIClient::V1::NotebookSplitBy.new({
              keys: [],
              tags: [],
            }),
            time: nil,
          }),
          type: DatadogAPIClient::V1::NotebookCellResourceType::NOTEBOOK_CELLS,
        }),
      ],
      name: "Example-Notebook",
      status: DatadogAPIClient::V1::NotebookStatus::PUBLISHED,
      time: DatadogAPIClient::V1::NotebookRelativeTime.new({
        live_span: DatadogAPIClient::V1::WidgetLiveSpan::PAST_ONE_HOUR,
      }),
    }),
    type: DatadogAPIClient::V1::NotebookResourceType::NOTEBOOKS,
  }),
})
p api_instance.create_notebook(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a notebook returns "OK" response
```
// Create a notebook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_notebooks::NotebooksAPI;
use datadog_api_client::datadogV1::model::NotebookCellCreateRequest;
use datadog_api_client::datadogV1::model::NotebookCellCreateRequestAttributes;
use datadog_api_client::datadogV1::model::NotebookCellResourceType;
use datadog_api_client::datadogV1::model::NotebookCreateData;
use datadog_api_client::datadogV1::model::NotebookCreateDataAttributes;
use datadog_api_client::datadogV1::model::NotebookCreateRequest;
use datadog_api_client::datadogV1::model::NotebookGlobalTime;
use datadog_api_client::datadogV1::model::NotebookGraphSize;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellAttributes;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellDefinition;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellDefinitionType;
use datadog_api_client::datadogV1::model::NotebookRelativeTime;
use datadog_api_client::datadogV1::model::NotebookResourceType;
use datadog_api_client::datadogV1::model::NotebookSplitBy;
use datadog_api_client::datadogV1::model::NotebookStatus;
use datadog_api_client::datadogV1::model::NotebookTimeseriesCellAttributes;
use datadog_api_client::datadogV1::model::TimeseriesWidgetDefinition;
use datadog_api_client::datadogV1::model::TimeseriesWidgetDefinitionType;
use datadog_api_client::datadogV1::model::TimeseriesWidgetRequest;
use datadog_api_client::datadogV1::model::WidgetAxis;
use datadog_api_client::datadogV1::model::WidgetDisplayType;
use datadog_api_client::datadogV1::model::WidgetLineType;
use datadog_api_client::datadogV1::model::WidgetLineWidth;
use datadog_api_client::datadogV1::model::WidgetLiveSpan;
use datadog_api_client::datadogV1::model::WidgetRequestStyle;

#[tokio::main]
async fn main() {
    let body = NotebookCreateRequest::new(NotebookCreateData::new(
        NotebookCreateDataAttributes::new(
            vec![
                NotebookCellCreateRequest::new(
                    NotebookCellCreateRequestAttributes::NotebookMarkdownCellAttributes(Box::new(
                        NotebookMarkdownCellAttributes::new(NotebookMarkdownCellDefinition::new(
                            r#"## Some test markdown

```
var x, y;
x = 5;
y = 6;
```"#
                                .to_string(),
                            NotebookMarkdownCellDefinitionType::MARKDOWN,
                        )),
                    )),
                    NotebookCellResourceType::NOTEBOOK_CELLS,
                ),
                NotebookCellCreateRequest::new(
                    NotebookCellCreateRequestAttributes::NotebookTimeseriesCellAttributes(
                        Box::new(
                            NotebookTimeseriesCellAttributes::new(
                                TimeseriesWidgetDefinition::new(
                                    vec![TimeseriesWidgetRequest::new()
                                        .display_type(WidgetDisplayType::LINE)
                                        .q("avg:system.load.1{*}".to_string())
                                        .style(
                                            WidgetRequestStyle::new()
                                                .line_type(WidgetLineType::SOLID)
                                                .line_width(WidgetLineWidth::NORMAL)
                                                .palette("dog_classic".to_string()),
                                        )],
                                    TimeseriesWidgetDefinitionType::TIMESERIES,
                                )
                                .show_legend(true)
                                .yaxis(WidgetAxis::new().scale("linear".to_string())),
                            )
                            .graph_size(NotebookGraphSize::MEDIUM)
                            .split_by(NotebookSplitBy::new(vec![], vec![]))
                            .time(None),
                        ),
                    ),
                    NotebookCellResourceType::NOTEBOOK_CELLS,
                ),
            ],
            "Example-Notebook".to_string(),
            NotebookGlobalTime::NotebookRelativeTime(Box::new(NotebookRelativeTime::new(
                WidgetLiveSpan::PAST_ONE_HOUR,
            ))),
        )
        .status(NotebookStatus::PUBLISHED),
        NotebookResourceType::NOTEBOOKS,
    ));
    let configuration = datadog::Configuration::new();
    let api = NotebooksAPI::with_config(configuration);
    let resp = api.create_notebook(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a notebook returns "OK" response
```
/**
 * Create a notebook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.NotebooksApi(configuration);

const params: v1.NotebooksApiCreateNotebookRequest = {
  body: {
    data: {
      attributes: {
        cells: [
          {
            attributes: {
              definition: {
                text:
                  `## Some test markdown

` +
                  "```" +
                  `
var x, y;
x = 5;
y = 6;
` +
                  "```",
                type: "markdown",
              },
            },
            type: "notebook_cells",
          },
          {
            attributes: {
              definition: {
                requests: [
                  {
                    displayType: "line",
                    q: "avg:system.load.1{*}",
                    style: {
                      lineType: "solid",
                      lineWidth: "normal",
                      palette: "dog_classic",
                    },
                  },
                ],
                showLegend: true,
                type: "timeseries",
                yaxis: {
                  scale: "linear",
                },
              },
              graphSize: "m",
              splitBy: {
                keys: [],
                tags: [],
              },
              time: undefined,
            },
            type: "notebook_cells",
          },
        ],
        name: "Example-Notebook",
        status: "published",
        time: {
          liveSpan: "1h",
        },
      },
      type: "notebooks",
    },
  },
};

apiInstance
  .createNotebook(params)
  .then((data: v1.NotebookResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get all notebooks](https://docs.datadoghq.com/api/latest/notebooks/#get-all-notebooks)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/notebooks/#get-all-notebooks-v1)


GET https://api.ap1.datadoghq.com/api/v1/notebookshttps://api.ap2.datadoghq.com/api/v1/notebookshttps://api.datadoghq.eu/api/v1/notebookshttps://api.ddog-gov.com/api/v1/notebookshttps://api.datadoghq.com/api/v1/notebookshttps://api.us3.datadoghq.com/api/v1/notebookshttps://api.us5.datadoghq.com/api/v1/notebooks
### Overview
Get all notebooks. This can also be used to search for notebooks with a particular `query` in the notebook `name` or author `handle`. This endpoint requires the `notebooks_read` permission.
### Arguments
#### Query Strings
Name
Type
Description
author_handle
string
Return notebooks created by the given `author_handle`.
exclude_author_handle
string
Return notebooks not created by the given `author_handle`.
start
integer
The index of the first notebook you want returned.
count
integer
The number of notebooks to be returned.
sort_field
string
Sort by field `modified`, `name`, or `created`.
sort_dir
string
Sort by direction `asc` or `desc`.
query
string
Return only notebooks with `query` string in notebook name or author handle.
include_cells
boolean
Value of `false` excludes the `cells` and global `time` for each notebook.
is_template
boolean
True value returns only template notebooks. Default is false (returns only non-template notebooks).
type
string
If type is provided, returns only notebooks with that metadata type. Default does not have type filtering.
### Response
  * [200](https://docs.datadoghq.com/api/latest/notebooks/#ListNotebooks-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/notebooks/#ListNotebooks-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/notebooks/#ListNotebooks-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/notebooks/#ListNotebooks-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Notebooks get all response.
Field
Type
Description
data
[object]
List of notebook definitions.
attributes [_required_]
object
The attributes of a notebook in get all response.
author
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
cells
[object]
List of cells to display in the notebook.
attributes [_required_]
<oneOf>
The attributes of a notebook cell response. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
index [_required_]
int64
The index of the formula to sort by.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to formula. Allowed enum values: `formula`
Option 2
object
The group to sort the widget by.
name [_required_]
string
The name of the group.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to group. Allowed enum values: `group`
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
string
Notebook cell ID.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
created
date-time
UTC time stamp for when the notebook was created.
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
modified
date-time
UTC time stamp for when the notebook was last modified.
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
int64
Unique notebook ID, assigned when you create the notebook.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
meta
object
Searches metadata returned by the API.
page
object
Pagination metadata returned by the API.
total_count
int64
The total number of notebooks that would be returned if the request was not filtered by `start` and `count` parameters.
total_filtered_count
int64
The total number of notebooks returned.
```
{
  "data": [
    {
      "attributes": {
        "author": {
          "created_at": "2019-09-19T10:00:00.000Z",
          "disabled": false,
          "email": "string",
          "handle": "string",
          "icon": "string",
          "name": "string",
          "status": "string",
          "title": "string",
          "verified": false
        },
        "cells": [
          {
            "attributes": {
              "definition": {
                "text": "# Example Header \nexample content",
                "type": "markdown"
              }
            },
            "id": "abcd1234",
            "type": "notebook_cells"
          }
        ],
        "created": "2021-02-24T23:14:15.173964+00:00",
        "metadata": {
          "is_template": false,
          "take_snapshots": false,
          "type": "investigation"
        },
        "modified": "2021-02-24T23:15:23.274966+00:00",
        "name": "Example Notebook",
        "status": "published",
        "time": {
          "live_span": "5m"
        }
      },
      "id": 123456,
      "type": "notebooks"
    }
  ],
  "meta": {
    "page": {
      "total_count": "integer",
      "total_filtered_count": "integer"
    }
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=typescript)


#####  Get all notebooks
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/notebooks" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all notebooks
```
"""
Get all notebooks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.list_notebooks()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get all notebooks
```
# Get all notebooks returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::NotebooksAPI.new
p api_instance.list_notebooks()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get all notebooks
```
// Get all notebooks returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewNotebooksApi(apiClient)
	resp, r, err := api.ListNotebooks(ctx, *datadogV1.NewListNotebooksOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotebooksApi.ListNotebooks`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NotebooksApi.ListNotebooks`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get all notebooks
```
// Get all notebooks returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.NotebooksApi;
import com.datadog.api.client.v1.model.NotebooksResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NotebooksApi apiInstance = new NotebooksApi(defaultClient);

    try {
      NotebooksResponse result = apiInstance.listNotebooks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotebooksApi#listNotebooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get all notebooks
```
// Get all notebooks returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_notebooks::ListNotebooksOptionalParams;
use datadog_api_client::datadogV1::api_notebooks::NotebooksAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = NotebooksAPI::with_config(configuration);
    let resp = api
        .list_notebooks(ListNotebooksOptionalParams::default())
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get all notebooks
```
/**
 * Get all notebooks returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.NotebooksApi(configuration);

apiInstance
  .listNotebooks()
  .then((data: v1.NotebooksResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Delete a notebook](https://docs.datadoghq.com/api/latest/notebooks/#delete-a-notebook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/notebooks/#delete-a-notebook-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.ap2.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.eu/api/v1/notebooks/{notebook_id}https://api.ddog-gov.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us3.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us5.datadoghq.com/api/v1/notebooks/{notebook_id}
### Overview
Delete a notebook using the specified ID. This endpoint requires the `notebooks_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
notebook_id [_required_]
integer
Unique ID, assigned when you create the notebook.
### Response
  * [204](https://docs.datadoghq.com/api/latest/notebooks/#DeleteNotebook-204-v1)
  * [400](https://docs.datadoghq.com/api/latest/notebooks/#DeleteNotebook-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/notebooks/#DeleteNotebook-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/notebooks/#DeleteNotebook-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/notebooks/#DeleteNotebook-429-v1)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=typescript)


#####  Delete a notebook
Copy
```
                  # Path parameters  
export notebook_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/notebooks/${notebook_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a notebook
```
"""
Delete a notebook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = environ["NOTEBOOK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    api_instance.delete_notebook(
        notebook_id=int(NOTEBOOK_DATA_ID),
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a notebook
```
# Delete a notebook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::NotebooksAPI.new

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = ENV["NOTEBOOK_DATA_ID"]
api_instance.delete_notebook(NOTEBOOK_DATA_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a notebook
```
// Delete a notebook returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "notebook" in the system
	NotebookDataID, _ := strconv.ParseInt(os.Getenv("NOTEBOOK_DATA_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewNotebooksApi(apiClient)
	r, err := api.DeleteNotebook(ctx, NotebookDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotebooksApi.DeleteNotebook`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Delete a notebook
```
// Delete a notebook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.NotebooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NotebooksApi apiInstance = new NotebooksApi(defaultClient);

    // there is a valid "notebook" in the system
    Long NOTEBOOK_DATA_ID = Long.parseLong(System.getenv("NOTEBOOK_DATA_ID"));

    try {
      apiInstance.deleteNotebook(NOTEBOOK_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotebooksApi#deleteNotebook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Delete a notebook
```
// Delete a notebook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_notebooks::NotebooksAPI;

#[tokio::main]
async fn main() {
    // there is a valid "notebook" in the system
    let notebook_data_id: i64 = std::env::var("NOTEBOOK_DATA_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = NotebooksAPI::with_config(configuration);
    let resp = api.delete_notebook(notebook_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Delete a notebook
```
/**
 * Delete a notebook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.NotebooksApi(configuration);

// there is a valid "notebook" in the system
const NOTEBOOK_DATA_ID = parseInt(process.env.NOTEBOOK_DATA_ID as string);

const params: v1.NotebooksApiDeleteNotebookRequest = {
  notebookId: NOTEBOOK_DATA_ID,
};

apiInstance
  .deleteNotebook(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a notebook](https://docs.datadoghq.com/api/latest/notebooks/#update-a-notebook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/notebooks/#update-a-notebook-v1)


PUT https://api.ap1.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.ap2.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.eu/api/v1/notebooks/{notebook_id}https://api.ddog-gov.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us3.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us5.datadoghq.com/api/v1/notebooks/{notebook_id}
### Overview
Update a notebook using the specified ID. This endpoint requires the `notebooks_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
notebook_id [_required_]
integer
Unique ID, assigned when you create the notebook.
### Request
#### Body Data (required)
Update notebook request body.
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Field
Type
Description
data [_required_]
object
The data for a notebook update request.
attributes [_required_]
object
The data attributes of a notebook.
cells [_required_]
[ <oneOf>]
List of cells to display in the notebook.
Option 1
object
The description of a notebook cell create request.
attributes [_required_]
<oneOf>
The attributes of a notebook cell in create cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
Option 2
object
The group to sort the widget by.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
Option 2
object
The description of a notebook cell update request.
attributes [_required_]
<oneOf>
The attributes of a notebook cell in update cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
Option 2
object
The group to sort the widget by.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
string
Notebook cell ID.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time [_required_]
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
```
{
  "data": {
    "attributes": {
      "cells": [
        {
          "attributes": {
            "definition": {
              "text": "## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```",
              "type": "markdown"
            }
          },
          "type": "notebook_cells"
        },
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "type": "notebook_cells"
        }
      ],
      "name": "Example-Notebook-updated",
      "status": "published",
      "time": {
        "live_span": "1h"
      }
    },
    "type": "notebooks"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-404-v1)
  * [409](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/notebooks/#UpdateNotebook-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


The description of a notebook response.
Field
Type
Description
data
object
The data for a notebook.
attributes [_required_]
object
The attributes of a notebook.
author
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
cells [_required_]
[object]
List of cells to display in the notebook.
attributes [_required_]
<oneOf>
The attributes of a notebook cell response. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
index [_required_]
int64
The index of the formula to sort by.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to formula. Allowed enum values: `formula`
Option 2
object
The group to sort the widget by.
name [_required_]
string
The name of the group.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to group. Allowed enum values: `group`
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
string
Notebook cell ID.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
created
date-time
UTC time stamp for when the notebook was created.
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
modified
date-time
UTC time stamp for when the notebook was last modified.
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time [_required_]
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
int64
Unique notebook ID, assigned when you create the notebook.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
```
{
  "data": {
    "attributes": {
      "author": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "status": "string",
        "title": "string",
        "verified": false
      },
      "cells": [
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "id": "abcd1234",
          "type": "notebook_cells"
        }
      ],
      "created": "2021-02-24T23:14:15.173964+00:00",
      "metadata": {
        "is_template": false,
        "take_snapshots": false,
        "type": "investigation"
      },
      "modified": "2021-02-24T23:15:23.274966+00:00",
      "name": "Example Notebook",
      "status": "published",
      "time": {
        "live_span": "5m"
      }
    },
    "id": 123456,
    "type": "notebooks"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=typescript)


#####  Update a notebook returns "OK" response
Copy
```
                          ## json-request-body
# 
  
# Path parameters  
export notebook_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/notebooks/${notebook_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "cells": [
        {
          "attributes": {
            "definition": {
              "text": "## Some updated test markdown\n\nWith some example content.",
              "type": "markdown"
            }
          },
          "type": "notebook_cells"
        },
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "bars",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "warm"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "id": "abcd1234",
          "type": "notebook_cells"
        }
      ],
      "name": "Example Notebook",
      "time": {
        "live_span": "1h"
      }
    },
    "type": "notebooks"
  }
}
EOF  

                        
```

#####  Update a notebook returns "OK" response
```
// Update a notebook returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "notebook" in the system
	NotebookDataID, _ := strconv.ParseInt(os.Getenv("NOTEBOOK_DATA_ID"), 10, 64)

	body := datadogV1.NotebookUpdateRequest{
		Data: datadogV1.NotebookUpdateData{
			Attributes: datadogV1.NotebookUpdateDataAttributes{
				Cells: []datadogV1.NotebookUpdateCell{
					datadogV1.NotebookUpdateCell{
						NotebookCellCreateRequest: &datadogV1.NotebookCellCreateRequest{
							Attributes: datadogV1.NotebookCellCreateRequestAttributes{
								NotebookMarkdownCellAttributes: &datadogV1.NotebookMarkdownCellAttributes{
									Definition: datadogV1.NotebookMarkdownCellDefinition{
										Text: `## Some test markdown

` + "```" + `
var x, y;
x = 5;
y = 6;
` + "```",
										Type: datadogV1.NOTEBOOKMARKDOWNCELLDEFINITIONTYPE_MARKDOWN,
									},
								}},
							Type: datadogV1.NOTEBOOKCELLRESOURCETYPE_NOTEBOOK_CELLS,
						}},
					datadogV1.NotebookUpdateCell{
						NotebookCellCreateRequest: &datadogV1.NotebookCellCreateRequest{
							Attributes: datadogV1.NotebookCellCreateRequestAttributes{
								NotebookTimeseriesCellAttributes: &datadogV1.NotebookTimeseriesCellAttributes{
									Definition: datadogV1.TimeseriesWidgetDefinition{
										Requests: []datadogV1.TimeseriesWidgetRequest{
											{
												DisplayType: datadogV1.WIDGETDISPLAYTYPE_LINE.Ptr(),
												Q:           datadog.PtrString("avg:system.load.1{*}"),
												Style: &datadogV1.WidgetRequestStyle{
													LineType:  datadogV1.WIDGETLINETYPE_SOLID.Ptr(),
													LineWidth: datadogV1.WIDGETLINEWIDTH_NORMAL.Ptr(),
													Palette:   datadog.PtrString("dog_classic"),
												},
											},
										},
										ShowLegend: datadog.PtrBool(true),
										Type:       datadogV1.TIMESERIESWIDGETDEFINITIONTYPE_TIMESERIES,
										Yaxis: &datadogV1.WidgetAxis{
											Scale: datadog.PtrString("linear"),
										},
									},
									GraphSize: datadogV1.NOTEBOOKGRAPHSIZE_MEDIUM.Ptr(),
									SplitBy: &datadogV1.NotebookSplitBy{
										Keys: []string{},
										Tags: []string{},
									},
									Time: *datadogV1.NewNullableNotebookCellTime(nil),
								}},
							Type: datadogV1.NOTEBOOKCELLRESOURCETYPE_NOTEBOOK_CELLS,
						}},
				},
				Name:   "Example-Notebook-updated",
				Status: datadogV1.NOTEBOOKSTATUS_PUBLISHED.Ptr(),
				Time: datadogV1.NotebookGlobalTime{
					NotebookRelativeTime: &datadogV1.NotebookRelativeTime{
						LiveSpan: datadogV1.WIDGETLIVESPAN_PAST_ONE_HOUR,
					}},
			},
			Type: datadogV1.NOTEBOOKRESOURCETYPE_NOTEBOOKS,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewNotebooksApi(apiClient)
	resp, r, err := api.UpdateNotebook(ctx, NotebookDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotebooksApi.UpdateNotebook`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NotebooksApi.UpdateNotebook`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a notebook returns "OK" response
```
// Update a notebook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.NotebooksApi;
import com.datadog.api.client.v1.model.NotebookCellCreateRequest;
import com.datadog.api.client.v1.model.NotebookCellCreateRequestAttributes;
import com.datadog.api.client.v1.model.NotebookCellResourceType;
import com.datadog.api.client.v1.model.NotebookGlobalTime;
import com.datadog.api.client.v1.model.NotebookGraphSize;
import com.datadog.api.client.v1.model.NotebookMarkdownCellAttributes;
import com.datadog.api.client.v1.model.NotebookMarkdownCellDefinition;
import com.datadog.api.client.v1.model.NotebookMarkdownCellDefinitionType;
import com.datadog.api.client.v1.model.NotebookRelativeTime;
import com.datadog.api.client.v1.model.NotebookResourceType;
import com.datadog.api.client.v1.model.NotebookResponse;
import com.datadog.api.client.v1.model.NotebookSplitBy;
import com.datadog.api.client.v1.model.NotebookStatus;
import com.datadog.api.client.v1.model.NotebookTimeseriesCellAttributes;
import com.datadog.api.client.v1.model.NotebookUpdateCell;
import com.datadog.api.client.v1.model.NotebookUpdateData;
import com.datadog.api.client.v1.model.NotebookUpdateDataAttributes;
import com.datadog.api.client.v1.model.NotebookUpdateRequest;
import com.datadog.api.client.v1.model.TimeseriesWidgetDefinition;
import com.datadog.api.client.v1.model.TimeseriesWidgetDefinitionType;
import com.datadog.api.client.v1.model.TimeseriesWidgetRequest;
import com.datadog.api.client.v1.model.WidgetAxis;
import com.datadog.api.client.v1.model.WidgetDisplayType;
import com.datadog.api.client.v1.model.WidgetLineType;
import com.datadog.api.client.v1.model.WidgetLineWidth;
import com.datadog.api.client.v1.model.WidgetLiveSpan;
import com.datadog.api.client.v1.model.WidgetRequestStyle;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NotebooksApi apiInstance = new NotebooksApi(defaultClient);

    // there is a valid "notebook" in the system
    Long NOTEBOOK_DATA_ID = Long.parseLong(System.getenv("NOTEBOOK_DATA_ID"));

    NotebookUpdateRequest body =
        new NotebookUpdateRequest()
            .data(
                new NotebookUpdateData()
                    .attributes(
                        new NotebookUpdateDataAttributes()
                            .cells(
                                Arrays.asList(
                                    new NotebookUpdateCell(
                                        new NotebookCellCreateRequest()
                                            .attributes(
                                                new NotebookCellCreateRequestAttributes(
                                                    new NotebookMarkdownCellAttributes()
                                                        .definition(
                                                            new NotebookMarkdownCellDefinition()
                                                                .text(
                                                                    """
## Some test markdown

```
var x, y;
x = 5;
y = 6;
```
""")
                                                                .type(
                                                                    NotebookMarkdownCellDefinitionType
                                                                        .MARKDOWN))))
                                            .type(NotebookCellResourceType.NOTEBOOK_CELLS)),
                                    new NotebookUpdateCell(
                                        new NotebookCellCreateRequest()
                                            .attributes(
                                                new NotebookCellCreateRequestAttributes(
                                                    new NotebookTimeseriesCellAttributes()
                                                        .definition(
                                                            new TimeseriesWidgetDefinition()
                                                                .requests(
                                                                    Collections.singletonList(
                                                                        new TimeseriesWidgetRequest()
                                                                            .displayType(
                                                                                WidgetDisplayType
                                                                                    .LINE)
                                                                            .q(
                                                                                "avg:system.load.1{*}")
                                                                            .style(
                                                                                new WidgetRequestStyle()
                                                                                    .lineType(
                                                                                        WidgetLineType
                                                                                            .SOLID)
                                                                                    .lineWidth(
                                                                                        WidgetLineWidth
                                                                                            .NORMAL)
                                                                                    .palette(
                                                                                        "dog_classic"))))
                                                                .showLegend(true)
                                                                .type(
                                                                    TimeseriesWidgetDefinitionType
                                                                        .TIMESERIES)
                                                                .yaxis(
                                                                    new WidgetAxis()
                                                                        .scale("linear")))
                                                        .graphSize(NotebookGraphSize.MEDIUM)
                                                        .splitBy(new NotebookSplitBy())
                                                        .time(null)))
                                            .type(NotebookCellResourceType.NOTEBOOK_CELLS))))
                            .name("Example-Notebook-updated")
                            .status(NotebookStatus.PUBLISHED)
                            .time(
                                new NotebookGlobalTime(
                                    new NotebookRelativeTime()
                                        .liveSpan(WidgetLiveSpan.PAST_ONE_HOUR))))
                    .type(NotebookResourceType.NOTEBOOKS));

    try {
      NotebookResponse result = apiInstance.updateNotebook(NOTEBOOK_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotebooksApi#updateNotebook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a notebook returns "OK" response
```
"""
Update a notebook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition
from datadog_api_client.v1.model.notebook_markdown_cell_definition_type import NotebookMarkdownCellDefinitionType
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
from datadog_api_client.v1.model.notebook_update_data import NotebookUpdateData
from datadog_api_client.v1.model.notebook_update_data_attributes import NotebookUpdateDataAttributes
from datadog_api_client.v1.model.notebook_update_request import NotebookUpdateRequest
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = environ["NOTEBOOK_DATA_ID"]

body = NotebookUpdateRequest(
    data=NotebookUpdateData(
        attributes=NotebookUpdateDataAttributes(
            cells=[
                NotebookCellCreateRequest(
                    attributes=NotebookMarkdownCellAttributes(
                        definition=NotebookMarkdownCellDefinition(
                            text="## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```",
                            type=NotebookMarkdownCellDefinitionType.MARKDOWN,
                        ),
                    ),
                    type=NotebookCellResourceType.NOTEBOOK_CELLS,
                ),
                NotebookCellCreateRequest(
                    attributes=NotebookTimeseriesCellAttributes(
                        definition=TimeseriesWidgetDefinition(
                            requests=[
                                TimeseriesWidgetRequest(
                                    display_type=WidgetDisplayType.LINE,
                                    q="avg:system.load.1{*}",
                                    style=WidgetRequestStyle(
                                        line_type=WidgetLineType.SOLID,
                                        line_width=WidgetLineWidth.NORMAL,
                                        palette="dog_classic",
                                    ),
                                ),
                            ],
                            show_legend=True,
                            type=TimeseriesWidgetDefinitionType.TIMESERIES,
                            yaxis=WidgetAxis(
                                scale="linear",
                            ),
                        ),
                        graph_size=NotebookGraphSize.MEDIUM,
                        split_by=NotebookSplitBy(
                            keys=[],
                            tags=[],
                        ),
                        time=None,
                    ),
                    type=NotebookCellResourceType.NOTEBOOK_CELLS,
                ),
            ],
            name="Example-Notebook-updated",
            status=NotebookStatus.PUBLISHED,
            time=NotebookRelativeTime(
                live_span=WidgetLiveSpan.PAST_ONE_HOUR,
            ),
        ),
        type=NotebookResourceType.NOTEBOOKS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.update_notebook(notebook_id=int(NOTEBOOK_DATA_ID), body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a notebook returns "OK" response
```
# Update a notebook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::NotebooksAPI.new

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = ENV["NOTEBOOK_DATA_ID"]

body = DatadogAPIClient::V1::NotebookUpdateRequest.new({
  data: DatadogAPIClient::V1::NotebookUpdateData.new({
    attributes: DatadogAPIClient::V1::NotebookUpdateDataAttributes.new({
      cells: [
        DatadogAPIClient::V1::NotebookCellCreateRequest.new({
          attributes: DatadogAPIClient::V1::NotebookMarkdownCellAttributes.new({
            definition: DatadogAPIClient::V1::NotebookMarkdownCellDefinition.new({
              text: '## Some test markdown\n\n```\nvar x, y;\nx = 5;\ny = 6;\n```',
              type: DatadogAPIClient::V1::NotebookMarkdownCellDefinitionType::MARKDOWN,
            }),
          }),
          type: DatadogAPIClient::V1::NotebookCellResourceType::NOTEBOOK_CELLS,
        }),
        DatadogAPIClient::V1::NotebookCellCreateRequest.new({
          attributes: DatadogAPIClient::V1::NotebookTimeseriesCellAttributes.new({
            definition: DatadogAPIClient::V1::TimeseriesWidgetDefinition.new({
              requests: [
                DatadogAPIClient::V1::TimeseriesWidgetRequest.new({
                  display_type: DatadogAPIClient::V1::WidgetDisplayType::LINE,
                  q: "avg:system.load.1{*}",
                  style: DatadogAPIClient::V1::WidgetRequestStyle.new({
                    line_type: DatadogAPIClient::V1::WidgetLineType::SOLID,
                    line_width: DatadogAPIClient::V1::WidgetLineWidth::NORMAL,
                    palette: "dog_classic",
                  }),
                }),
              ],
              show_legend: true,
              type: DatadogAPIClient::V1::TimeseriesWidgetDefinitionType::TIMESERIES,
              yaxis: DatadogAPIClient::V1::WidgetAxis.new({
                scale: "linear",
              }),
            }),
            graph_size: DatadogAPIClient::V1::NotebookGraphSize::MEDIUM,
            split_by: DatadogAPIClient::V1::NotebookSplitBy.new({
              keys: [],
              tags: [],
            }),
            time: nil,
          }),
          type: DatadogAPIClient::V1::NotebookCellResourceType::NOTEBOOK_CELLS,
        }),
      ],
      name: "Example-Notebook-updated",
      status: DatadogAPIClient::V1::NotebookStatus::PUBLISHED,
      time: DatadogAPIClient::V1::NotebookRelativeTime.new({
        live_span: DatadogAPIClient::V1::WidgetLiveSpan::PAST_ONE_HOUR,
      }),
    }),
    type: DatadogAPIClient::V1::NotebookResourceType::NOTEBOOKS,
  }),
})
p api_instance.update_notebook(NOTEBOOK_DATA_ID.to_i, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a notebook returns "OK" response
```
// Update a notebook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_notebooks::NotebooksAPI;
use datadog_api_client::datadogV1::model::NotebookCellCreateRequest;
use datadog_api_client::datadogV1::model::NotebookCellCreateRequestAttributes;
use datadog_api_client::datadogV1::model::NotebookCellResourceType;
use datadog_api_client::datadogV1::model::NotebookGlobalTime;
use datadog_api_client::datadogV1::model::NotebookGraphSize;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellAttributes;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellDefinition;
use datadog_api_client::datadogV1::model::NotebookMarkdownCellDefinitionType;
use datadog_api_client::datadogV1::model::NotebookRelativeTime;
use datadog_api_client::datadogV1::model::NotebookResourceType;
use datadog_api_client::datadogV1::model::NotebookSplitBy;
use datadog_api_client::datadogV1::model::NotebookStatus;
use datadog_api_client::datadogV1::model::NotebookTimeseriesCellAttributes;
use datadog_api_client::datadogV1::model::NotebookUpdateCell;
use datadog_api_client::datadogV1::model::NotebookUpdateData;
use datadog_api_client::datadogV1::model::NotebookUpdateDataAttributes;
use datadog_api_client::datadogV1::model::NotebookUpdateRequest;
use datadog_api_client::datadogV1::model::TimeseriesWidgetDefinition;
use datadog_api_client::datadogV1::model::TimeseriesWidgetDefinitionType;
use datadog_api_client::datadogV1::model::TimeseriesWidgetRequest;
use datadog_api_client::datadogV1::model::WidgetAxis;
use datadog_api_client::datadogV1::model::WidgetDisplayType;
use datadog_api_client::datadogV1::model::WidgetLineType;
use datadog_api_client::datadogV1::model::WidgetLineWidth;
use datadog_api_client::datadogV1::model::WidgetLiveSpan;
use datadog_api_client::datadogV1::model::WidgetRequestStyle;

#[tokio::main]
async fn main() {
    // there is a valid "notebook" in the system
    let notebook_data_id: i64 = std::env::var("NOTEBOOK_DATA_ID").unwrap().parse().unwrap();
    let body = NotebookUpdateRequest::new(NotebookUpdateData::new(
        NotebookUpdateDataAttributes::new(
            vec![
                NotebookUpdateCell::NotebookCellCreateRequest(Box::new(
                    NotebookCellCreateRequest::new(
                        NotebookCellCreateRequestAttributes::NotebookMarkdownCellAttributes(
                            Box::new(NotebookMarkdownCellAttributes::new(
                                NotebookMarkdownCellDefinition::new(
                                    r#"## Some test markdown

```
var x, y;
x = 5;
y = 6;
```"#
                                        .to_string(),
                                    NotebookMarkdownCellDefinitionType::MARKDOWN,
                                ),
                            )),
                        ),
                        NotebookCellResourceType::NOTEBOOK_CELLS,
                    ),
                )),
                NotebookUpdateCell::NotebookCellCreateRequest(Box::new(
                    NotebookCellCreateRequest::new(
                        NotebookCellCreateRequestAttributes::NotebookTimeseriesCellAttributes(
                            Box::new(
                                NotebookTimeseriesCellAttributes::new(
                                    TimeseriesWidgetDefinition::new(
                                        vec![TimeseriesWidgetRequest::new()
                                            .display_type(WidgetDisplayType::LINE)
                                            .q("avg:system.load.1{*}".to_string())
                                            .style(
                                                WidgetRequestStyle::new()
                                                    .line_type(WidgetLineType::SOLID)
                                                    .line_width(WidgetLineWidth::NORMAL)
                                                    .palette("dog_classic".to_string()),
                                            )],
                                        TimeseriesWidgetDefinitionType::TIMESERIES,
                                    )
                                    .show_legend(true)
                                    .yaxis(WidgetAxis::new().scale("linear".to_string())),
                                )
                                .graph_size(NotebookGraphSize::MEDIUM)
                                .split_by(NotebookSplitBy::new(vec![], vec![]))
                                .time(None),
                            ),
                        ),
                        NotebookCellResourceType::NOTEBOOK_CELLS,
                    ),
                )),
            ],
            "Example-Notebook-updated".to_string(),
            NotebookGlobalTime::NotebookRelativeTime(Box::new(NotebookRelativeTime::new(
                WidgetLiveSpan::PAST_ONE_HOUR,
            ))),
        )
        .status(NotebookStatus::PUBLISHED),
        NotebookResourceType::NOTEBOOKS,
    ));
    let configuration = datadog::Configuration::new();
    let api = NotebooksAPI::with_config(configuration);
    let resp = api.update_notebook(notebook_data_id.clone(), body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a notebook returns "OK" response
```
/**
 * Update a notebook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.NotebooksApi(configuration);

// there is a valid "notebook" in the system
const NOTEBOOK_DATA_ID = parseInt(process.env.NOTEBOOK_DATA_ID as string);

const params: v1.NotebooksApiUpdateNotebookRequest = {
  body: {
    data: {
      attributes: {
        cells: [
          {
            attributes: {
              definition: {
                text:
                  `## Some test markdown

` +
                  "```" +
                  `
var x, y;
x = 5;
y = 6;
` +
                  "```",
                type: "markdown",
              },
            },
            type: "notebook_cells",
          },
          {
            attributes: {
              definition: {
                requests: [
                  {
                    displayType: "line",
                    q: "avg:system.load.1{*}",
                    style: {
                      lineType: "solid",
                      lineWidth: "normal",
                      palette: "dog_classic",
                    },
                  },
                ],
                showLegend: true,
                type: "timeseries",
                yaxis: {
                  scale: "linear",
                },
              },
              graphSize: "m",
              splitBy: {
                keys: [],
                tags: [],
              },
              time: undefined,
            },
            type: "notebook_cells",
          },
        ],
        name: "Example-Notebook-updated",
        status: "published",
        time: {
          liveSpan: "1h",
        },
      },
      type: "notebooks",
    },
  },
  notebookId: NOTEBOOK_DATA_ID,
};

apiInstance
  .updateNotebook(params)
  .then((data: v1.NotebookResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a notebook](https://docs.datadoghq.com/api/latest/notebooks/#get-a-notebook)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/notebooks/#get-a-notebook-v1)


GET https://api.ap1.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.ap2.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.eu/api/v1/notebooks/{notebook_id}https://api.ddog-gov.com/api/v1/notebooks/{notebook_id}https://api.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us3.datadoghq.com/api/v1/notebooks/{notebook_id}https://api.us5.datadoghq.com/api/v1/notebooks/{notebook_id}
### Overview
Get a notebook using the specified notebook ID. This endpoint requires the `notebooks_read` permission.
### Arguments
#### Path Parameters
Name
Type
Description
notebook_id [_required_]
integer
Unique ID, assigned when you create the notebook.
### Response
  * [200](https://docs.datadoghq.com/api/latest/notebooks/#GetNotebook-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/notebooks/#GetNotebook-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/notebooks/#GetNotebook-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/notebooks/#GetNotebook-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/notebooks/#GetNotebook-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


The description of a notebook response.
Field
Type
Description
data
object
The data for a notebook.
attributes [_required_]
object
The attributes of a notebook.
author
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
name
string
Name of the user.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
cells [_required_]
[object]
List of cells to display in the notebook.
attributes [_required_]
<oneOf>
The attributes of a notebook cell response. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
Option 1
object
The attributes of a notebook `markdown` cell.
definition [_required_]
object
Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.
text [_required_]
string
The markdown content.
type [_required_]
enum
Type of the markdown cell. Allowed enum values: `markdown`
default: `markdown`
Option 2
object
The attributes of a notebook `timeseries` cell.
definition [_required_]
object
The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_columns
[string]
Columns displayed in the legend.
legend_layout
enum
Layout of the legend. Allowed enum values: `auto,horizontal,vertical`
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of timeseries widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
display_type
enum
Type of display to use for the request. Allowed enum values: `area,bars,line,overlay`
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
metadata
[object]
Used to define expression aliases.
alias_name
string
Expression alias.
expression [_required_]
string
Expression name.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
on_right_yaxis
boolean
Whether or not to display a second y-axis on the right.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
right_yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legend
boolean
(screenboard only) Show the legend for this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 3
object
The attributes of a notebook `toplist` cell.
definition [_required_]
object
The top list visualization enables you to display a list of Tag value like hostname or service with the most or least of any metric value, such as highest consumers of CPU, hosts with the least disk space, etc.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
requests [_required_]
[object]
List of top list widget requests.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
audit_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
sort
object
The controls for sorting the widget.
count
int64
The number of items to limit the widget to.
order_by
[ <oneOf>]
The array of items to sort the widget by in order.
Option 1
object
The formula to sort the widget by.
index [_required_]
int64
The index of the formula to sort by.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to formula. Allowed enum values: `formula`
Option 2
object
The group to sort the widget by.
name [_required_]
string
The name of the group.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
type [_required_]
enum
Set the sort type to group. Allowed enum values: `group`
style
object
Define request widget style.
line_type
enum
Type of lines displayed. Allowed enum values: `dashed,dotted,solid`
line_width
enum
Width of line displayed. Allowed enum values: `normal,thick,thin`
palette
string
Color palette to apply to the widget.
style
object
Style customization for a top list widget.
display
<oneOf>
Top list widget display options.
Option 1
object
Top list widget stacked display options.
legend
enum
Top list widget stacked legend behavior. Allowed enum values: `automatic,inline,none`
type [_required_]
enum
Top list widget stacked display type. Allowed enum values: `stacked`
default: `stacked`
Option 2
object
Top list widget flat display.
type [_required_]
enum
Top list widget flat display type. Allowed enum values: `flat`
default: `flat`
palette
string
Color palette to apply to the widget.
scaling
enum
Top list widget scaling definition. Allowed enum values: `absolute,relative`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of your widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the top list widget. Allowed enum values: `toplist`
default: `toplist`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 4
object
The attributes of a notebook `heatmap` cell.
definition [_required_]
object
The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
custom_links
[object]
List of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
events
[object]
List of widget events.
q [_required_]
string
Query definition.
tags_execution
string
The execution method for multi-value filters.
legend_size
string
Available legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto".
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
List of widget types.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
event_query
object
The event query.
search [_required_]
string
The query being made on the event.
tags_execution [_required_]
string
The execution method for multi-value filters. Can be either and or or.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
Whether or not to display the legend on this widget.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the heat map widget. Allowed enum values: `heatmap`
default: `heatmap`
xaxis
object
X Axis controls for the heat map widget.
num_buckets
int64
Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
yaxis
object
Axis controls for the widget.
include_zero
boolean
Set to `true` to include zero.
label
string
The label of the axis to display on the graph. Only usable on Scatterplot Widgets.
max
string
Specifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
min
string
Specifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 5
object
The attributes of a notebook `distribution` cell.
definition [_required_]
object
The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.
custom_links
[object]
A list of custom links.
is_hidden
boolean
The flag for toggling context menu link visibility.
label
string
The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
link
string
The URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.
override_label
string
The label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`.
legend_size
string
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
markers
[object]
List of markers.
display_type
string
Combination of:
  * A severity error, warning, ok, or info
  * A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.


label
string
Label to display over the marker.
time
string
Timestamp for the widget.
value [_required_]
string
Value to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90).
requests [_required_]
[object]
Array of one request object to display in the widget.
See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) to learn how to build the `REQUEST_SCHEMA`.
apm_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
apm_stats_query
object
The APM stats query for table and distributions widgets.
columns
[object]
Column properties used by the front end for display.
alias
string
A user-assigned alias for the column.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
name [_required_]
string
Column name.
order
enum
Widget sorting methods. Allowed enum values: `asc,desc`
env [_required_]
string
Environment name.
name [_required_]
string
Operation name associated with service.
primary_tag [_required_]
string
The organization's host group name and value.
resource
string
Resource name.
row_type [_required_]
enum
The level of detail for the request. Allowed enum values: `service,resource,span`
service [_required_]
string
Service name.
event_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
formulas
[object]
List of formulas that operate on queries.
alias
string
Expression alias.
cell_display_mode
enum
Define a display mode for the table cell. Allowed enum values: `number,bar,trend`
cell_display_mode_options
object
Cell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).
trend_type
enum
Trend type for the cell display mode options. Allowed enum values: `area,line,bars`
y_scale
enum
Y scale for the cell display mode options. Allowed enum values: `shared,independent`
conditional_formats
[object]
List of conditional formats.
comparator [_required_]
enum
Comparator to apply. Allowed enum values: `=,>,>=,<,<=`
custom_bg_color
string
Color palette to apply to the background, same values available as palette.
custom_fg_color
string
Color palette to apply to the foreground, same values available as palette.
hide_value
boolean
True hides values.
image_url
string
Displays an image as the background.
metric
string
Metric from the request to correlate this conditional format with.
palette [_required_]
enum
Color palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`
timeframe
string
Defines the displayed timeframe.
value [_required_]
double
Value for the comparator.
formula [_required_]
string
String expression built from queries, formulas, and functions.
limit
object
Options for limiting results returned.
count
int64
Number of results to return.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
number_format
object
Number format options for the widget.
unit
<oneOf>
Number format unit.
Option 1
object
Canonical unit.
Option 2
object
Custom unit.
unit_scale
object
The definition of `NumberFormatUnitScale` object.
type
enum
The type of unit scale. Allowed enum values: `canonical_unit`
unit_name
string
The name of the unit.
style
object
Styling options for widget formulas.
palette
string
The color palette used to display the formula. A guide to the available color palettes can be found at <https://docs.datadoghq.com/dashboards/guide/widget_colors>
palette_index
int64
Index specifying which color to use within the palette.
log_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
network_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
process_query
object
The process query to use in the widget.
filter_by
[string]
List of processes.
limit
int64
Max number of items in the filter list.
metric [_required_]
string
Your chosen metric.
search_by
string
Your chosen search term.
profile_metrics_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
q
string
Widget query.
queries
[ <oneOf>]
List of queries that can be returned directly or used in formulas.
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
Process query using formulas and functions.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data sources that rely on the process backend. Allowed enum values: `process,container`
is_normalized_cpu
boolean
Whether to normalize the CPU percentages.
limit
int64
Number of hits to return.
metric [_required_]
string
Process metric name.
name [_required_]
string
Name of query for use in formulas.
sort
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters
[string]
An array of tags to filter by.
text_filter
string
Text to use as filter.
Option 4
object
A formula and functions APM dependency stats query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`
env [_required_]
string
APM environment.
is_upstream
boolean
Determines whether stats for upstream or downstream dependencies should be queried.
name [_required_]
string
Name of query to use in formulas.
operation_name [_required_]
string
Name of operation on service.
primary_tag_name
string
The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>.
primary_tag_value
string
Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
resource_name [_required_]
string
APM resource.
service [_required_]
string
APM service.
stat [_required_]
enum
APM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count`
Option 5
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
Option 6
object
A formula and functions metrics query.
additional_query_filters
string
Additional filters applied to the SLO query.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for SLO measures queries. Allowed enum values: `slo`
group_mode
enum
Group mode to query measures. Allowed enum values: `overall,components`
measure [_required_]
enum
SLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`
name
string
Name of the query for use in formulas.
slo_id [_required_]
string
ID of an SLO to query measures.
slo_query_type
enum
Name of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice`
Option 7
object
A formula and functions Cloud Cost query.
aggregator
enum
Aggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for Cloud Cost queries. Allowed enum values: `cloud_cost`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Query for Cloud Cost data.
query
<oneOf>
Query definition for Distribution Widget Histogram Request
Option 1
object
A formula and functions metrics query.
aggregator
enum
The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for metrics queries. Allowed enum values: `metrics`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
Metrics query definition.
semantic_mode
enum
Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`
Option 2
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
storage
string
Option for storage location. Feature in Private Beta.
Option 3
object
APM resource stats query using formulas and functions.
cross_org_uuids
[string]
The source organization UUID for cross organization queries. Feature in Private Beta.
data_source [_required_]
enum
Data source for APM resource stats queries. Allowed enum values: `apm_resource_stats`
env [_required_]
string
APM environment.
group_by
[string]
Array of fields to group results by.
name [_required_]
string
Name of this query to use in formulas.
operation_name
string
Name of operation on service.
primary_tag_name
string
Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See <https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog>
primary_tag_value
string
Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
resource_name
string
APM resource name.
service [_required_]
string
APM service name.
stat [_required_]
enum
APM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99`
request_type
enum
Request type for the histogram request. Allowed enum values: `histogram`
response_format
enum
Timeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list`
rum_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
security_query
object
The log query.
compute
object
Define computation for a log query.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
group_by
[object]
List of tag prefixes to group by in the case of a cluster check.
facet [_required_]
string
Facet name.
limit
int64
Maximum number of items in the group.
sort
object
Define a sorting method.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
index
string
A coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes)
multi_compute
[object]
This field is mutually exclusive with `compute`.
aggregation [_required_]
string
The aggregation method.
facet
string
Facet name.
interval
int64
Define a time interval in seconds.
search
object
The query being made on the logs.
query [_required_]
string
Search value to apply.
style
object
Widget style definition.
palette
string
Color palette to apply to the widget.
show_legend
boolean
**DEPRECATED** : (Deprecated) The widget legend was replaced by a tooltip and sidebar.
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the distribution widget. Allowed enum values: `distribution`
default: `distribution`
xaxis
object
X Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
max
string
Specifies maximum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the x-axis. It takes a number, percentile (p90 === 90th percentile), or auto for default behavior.
default: `auto`
num_buckets
int64
Number of value buckets to target, also known as the resolution of the value bins.
scale
string
Specifies the scale type. Possible values are `linear`.
default: `linear`
yaxis
object
Y Axis controls for the distribution widget.
include_zero
boolean
True includes zero.
label
string
The label of the axis to display on the graph.
max
string
Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
min
string
Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.
default: `auto`
scale
string
Specifies the scale type. Possible values are `linear` or `log`.
default: `linear`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
split_by
object
Object describing how to split the graph to display multiple visualizations per request.
keys [_required_]
[string]
Keys to split on.
tags [_required_]
[string]
Tags to split on.
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
Option 6
object
The attributes of a notebook `log_stream` cell.
definition [_required_]
object
The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.
columns
[string]
Which columns to display on the widget.
indexes
[string]
An array of index names to query in the stream. Use [] to query all indexes at once.
logset
string
**DEPRECATED** : ID of the log set to use.
message_display
enum
Amount of log lines to display Allowed enum values: `inline,expanded-md,expanded-lg`
query
string
Query to filter the log stream with.
show_date_column
boolean
Whether to show the date column or not
show_message_column
boolean
Whether to show the message column or not
sort
object
Which column and order to sort by
column [_required_]
string
Facet path for the column
order [_required_]
enum
Widget sorting methods. Allowed enum values: `asc,desc`
time
<oneOf>
Time setting for the widget.
Option 1
object
Wrapper for live span
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
live_span
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Used for arbitrary live span times, such as 17 minutes or 6 hours.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
type [_required_]
enum
Type "live" denotes a live span in the new format. Allowed enum values: `live`
unit [_required_]
enum
Unit of the time span. Allowed enum values: `minute,hour,day,week,month,year`
value [_required_]
int64
Value of the time span.
Option 3
object
Used for fixed span times, such as 'March 1 to March 7'.
from [_required_]
int64
Start time in seconds since epoch.
hide_incomplete_cost_data
boolean
Whether to hide incomplete cost data in the widget.
to [_required_]
int64
End time in seconds since epoch.
type [_required_]
enum
Type "fixed" denotes a fixed span. Allowed enum values: `fixed`
title
string
Title of the widget.
title_align
enum
How to align the text on the widget. Allowed enum values: `center,left,right`
title_size
string
Size of the title.
type [_required_]
enum
Type of the log stream widget. Allowed enum values: `log_stream`
default: `log_stream`
graph_size
enum
The size of the graph. Allowed enum values: `xs,s,m,l,xl`
time
object <oneOf>
Timeframe for the notebook cell. When 'null', the notebook global time is used.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
string
Notebook cell ID.
type [_required_]
enum
Type of the Notebook Cell resource. Allowed enum values: `notebook_cells`
default: `notebook_cells`
created
date-time
UTC time stamp for when the notebook was created.
metadata
object
Metadata associated with the notebook.
is_template
boolean
Whether or not the notebook is a template.
take_snapshots
boolean
Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
type
enum
Metadata type of the notebook. Allowed enum values: `postmortem,runbook,investigation,documentation,report`
modified
date-time
UTC time stamp for when the notebook was last modified.
name [_required_]
string
The name of the notebook.
status
enum
Publication status of the notebook. For now, always "published". Allowed enum values: `published`
default: `published`
time [_required_]
<oneOf>
Notebook global timeframe.
Option 1
object
Relative timeframe.
live_span [_required_]
enum
The available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert`
Option 2
object
Absolute timeframe.
end [_required_]
date-time
The end time.
live
boolean
Indicates whether the timeframe should be shifted to end at the current time.
start [_required_]
date-time
The start time.
id [_required_]
int64
Unique notebook ID, assigned when you create the notebook.
type [_required_]
enum
Type of the Notebook resource. Allowed enum values: `notebooks`
default: `notebooks`
```
{
  "data": {
    "attributes": {
      "author": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "status": "string",
        "title": "string",
        "verified": false
      },
      "cells": [
        {
          "attributes": {
            "definition": {
              "requests": [
                {
                  "display_type": "line",
                  "q": "avg:system.load.1{*}",
                  "style": {
                    "line_type": "solid",
                    "line_width": "normal",
                    "palette": "dog_classic"
                  }
                }
              ],
              "show_legend": true,
              "type": "timeseries",
              "yaxis": {
                "scale": "linear"
              }
            },
            "graph_size": "m",
            "split_by": {
              "keys": [],
              "tags": []
            },
            "time": null
          },
          "id": "abcd1234",
          "type": "notebook_cells"
        }
      ],
      "created": "2021-02-24T23:14:15.173964+00:00",
      "metadata": {
        "is_template": false,
        "take_snapshots": false,
        "type": "investigation"
      },
      "modified": "2021-02-24T23:15:23.274966+00:00",
      "name": "Example Notebook",
      "status": "published",
      "time": {
        "live_span": "5m"
      }
    },
    "id": 123456,
    "type": "notebooks"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/notebooks/)
  * [Example](https://docs.datadoghq.com/api/latest/notebooks/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/notebooks/?code-lang=typescript)


#####  Get a notebook
Copy
```
                  # Path parameters  
export notebook_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/notebooks/${notebook_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a notebook
```
"""
Get a notebook returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = environ["NOTEBOOK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.get_notebook(
        notebook_id=int(NOTEBOOK_DATA_ID),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a notebook
```
# Get a notebook returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::NotebooksAPI.new

# there is a valid "notebook" in the system
NOTEBOOK_DATA_ID = ENV["NOTEBOOK_DATA_ID"]
p api_instance.get_notebook(NOTEBOOK_DATA_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a notebook
```
// Get a notebook returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "notebook" in the system
	NotebookDataID, _ := strconv.ParseInt(os.Getenv("NOTEBOOK_DATA_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewNotebooksApi(apiClient)
	resp, r, err := api.GetNotebook(ctx, NotebookDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotebooksApi.GetNotebook`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `NotebooksApi.GetNotebook`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a notebook
```
// Get a notebook returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.NotebooksApi;
import com.datadog.api.client.v1.model.NotebookResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    NotebooksApi apiInstance = new NotebooksApi(defaultClient);

    // there is a valid "notebook" in the system
    Long NOTEBOOK_DATA_ID = Long.parseLong(System.getenv("NOTEBOOK_DATA_ID"));

    try {
      NotebookResponse result = apiInstance.getNotebook(NOTEBOOK_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotebooksApi#getNotebook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a notebook
```
// Get a notebook returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_notebooks::NotebooksAPI;

#[tokio::main]
async fn main() {
    // there is a valid "notebook" in the system
    let notebook_data_id: i64 = std::env::var("NOTEBOOK_DATA_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = NotebooksAPI::with_config(configuration);
    let resp = api.get_notebook(notebook_data_id.clone()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a notebook
```
/**
 * Get a notebook returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.NotebooksApi(configuration);

// there is a valid "notebook" in the system
const NOTEBOOK_DATA_ID = parseInt(process.env.NOTEBOOK_DATA_ID as string);

const params: v1.NotebooksApiGetNotebookRequest = {
  notebookId: NOTEBOOK_DATA_ID,
};

apiInstance
  .getNotebook(params)
  .then((data: v1.NotebookResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=eaed3c2e-91eb-46c2-ab25-c6278ec1551f&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=3f87a4b9-8c87-482a-ace1-01f594555b83&pt=Notebooks&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnotebooks%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=eaed3c2e-91eb-46c2-ab25-c6278ec1551f&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=3f87a4b9-8c87-482a-ace1-01f594555b83&pt=Notebooks&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnotebooks%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=a20642b8-ca1e-481b-91d0-25179543606f&bo=2&sid=edd68350f0bf11f09aeaabc5684b3852&vid=edd6a2d0f0bf11f0862e6df258b5378b&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Notebooks&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fnotebooks%2F&r=&lt=6232&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=84221)
