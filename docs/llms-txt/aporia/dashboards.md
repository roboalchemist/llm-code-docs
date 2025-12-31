# Source: https://docs.aporia.com/ml-monitoring-as-code/dashboards.md

# Dashboards

This guide will show you how to automatically add dashboards to your models using the Python SDK.

{% hint style="info" %}
This functionality is currently only supported through the API SDK, and may be added to the as-code SDK in the future.
{% endhint %}

## Constructing Dashboards

To define a new dashboard, we start by constructing the widgets list.

There are various widget types to choose from, each with its own configuration and visualization.

Lets start by exploring the main concepts.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fuf0fKvW8xLyBvDNLFOas%2Fimage.png?alt=media&#x26;token=5d02eeb1-e74a-4487-b5a4-8221ae008cc1" alt=""><figcaption></figcaption></figure>

### Widget Grid

Each dashboard has a widget grid, in which the widgets reside. Widgets can't overlap, and if an overlap does occur, the dashboard will attempt to resolve it, resulting in widgets sliding downwards.

The grid has 12 columns, and is of infinite rows.

The Text widget can be of any size, while other widgets have a minimum size of 4 columns and 5 rows (Width=4, Height=5).

The position of a widget is defined as a tuple of (x,y), where x indicates the X coordinate of the widget, ranging from 0 to 11 (0 - Leftmost widget, 11 - Rightmost widget). Due to size constraints, non-text widgets X coordinate ranges from 0 to 8. Y indicates the Y coordinate of the widget, ranging from 0 onwards, with 0 being the first line. There is no size constraint, but a widget will slide upwards if there is empty space above it with no widgets in between. The size of a widget is defined in a matching tuple (width, height).

### Metric Configuration

As most widgets are designed to plot metrics, the metric configuration is consolidated into 2 classes:

#### MetricConfiguration (aporia.sdk.widgets.base.MetricConfiguration)

This is the main configuration class for metrics in the Aporia dashboards. This defines the inspected metric and any relevant parameter for it. Each metric configuration is defined first by the metric (one of `aporia.sdk.metrics.MetricType` enum), and then any relevant parameter:&#x20;

* `field` - Most metrics are calculated over specific fields. This parameter should be of type `aporia.sdk.fields.Field` and indicates the field to use for calculation. You can use `model.get_fields()` or `model.get_field_by_name()` functions to retrieve these objects.
* `custom_metric` - When using the `MetricType.CUSTOM_METRIC` metric type, the custom metric object (`aporia.sdk.custom_metrics.CustomMetric`) should be passed in to identify the chosen metric.
* `average` - For some multiclass metrics, the average method should be specified. This should be one of `aporia.sdk.metrics.AverageMethod` values.
* `threshold` - For confusion-matrix metrics with numeric predictions, the threshold indicates the cutoff threshold to decide whether a prediction is positive or negative. This should be a floating point  number between 0 and 1.
* `k` - For ranking metrics, the k parameter, indicating the top K choices being inspect, should be specified. This should be an integer between 1 and 12.
* `class_name` - For some multiclass per-class metrics, the inspected class should also be specified. This should be a string, matching the class as it appears in the database and Aporia.
* `baseline` - For drift metrics, the baseline for drift should be specified. This should be described by the `aporia.sdk.widgets.base.BaselineConfiguration` class, and contains the following fields:
  * `type` - This is one of the values of `aporia.sdk.widgets.base.BaselineType`:&#x20;
    * `BaselineType.TRAINING` - Compare the metric to the matching training dataset. No extra parameters are needed.
    * `BaselineType.RELATIVE_TIME_PERIOD` - Compare the metric to the previous time window. The time-window should be defined by the `unit` (`aporia.sdk.widgets.base.UnitType`) and `duration` parameters, where duration is a positive integer.

#### MetricOverrideConfiguration (aporia.sdk.widgets.base.MetricOverrideConfiguration)

In some widget configurations, you can override certain parameters of a metric in an alternative view. This lets you edit all of the parameters mentioned above, except for the metric itself and the custom metric identifier, if chosen. The overrides will be applied, and other parameters will be maintained.

#### Timeframes

The dashboard is intended to show a picture for a given timeframe. However, some things are supposed to be relative to it. The dashboard itself has a global timeframe which is inherited by all widgets unless specified otherwise. All timeframes are a choice of 2 options:

* Relative timeframe: This is one of a predefined set of relative timeframes supported by Aporia. It will check the time for the latest X hours/days/weeks/months compared to the current time. The possible values are: "1h", "4h", "1d", "2d", "1w", "2w", "1M", "2M", "3M".
* Fixed timeframe: A specific timeframe. This is set by a specific start and end periods. This must be an instance of `aporia.sdk.widgets.base.FixedTimeframe`. This is comprised of `to` and `from` fields of type `datetime.datetime`. Due to `from` being a keyword in Python, initialize the class in the following way: `FixedTimeframe(**{"to": ..., "from": ...})`

### Compare View

Some widgets support a Compare view, which allows you to add an additional plot or data to the same widget. In most cases, this is limited to the same metric/version/segment of the Data view. This lets you edit most non-constrained parameters. Read about each individual widget to see which overrides are possible.

### Widget Types

All widgets share the following parameters:

* `position` - The position of the widget, as described above
* `size` - The size of the widget, as described above
* `title` (Not applicable for text widgets) - The title of the widget

To create a new widget, call the `widget = WidgetClass.create(...)` function, exported by each widget type (e.g: `MetricWidget.create(...)`). Some widgets support a compare functionality. This is available through the `widget = widget.compare(...)` function.

<details>

<summary>Text Widget</summary>

The **Text** widget displays a line of text, usually to split the dashboard to parts.

**Parameters:**

* **`text`** - The text to display in the widget. This can also include emojis.
* `font` (default - 24) - The font size of the widget. We recommend leaving this as the default, unless an extra large text widget is desired.

</details>

<details>

<summary>Metric Widget</summary>

The **metric** widget lets you plot a metric as a number, to highlight very important information quickly, such as the bottom-line revenue numbers.

**Parameters:**

* **`metric`** - A MetricConfiguration class describing the metric to plot
* `timeframe`(Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* `segment`(Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value`(Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.

**Compare Parameters:**

* `metric_overrides` (Default - None) - metric overrides to apply on the original metric in the compare view.
* `timeframe` (Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version` (Default - None) - The Aporia version identifier to plot metric for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* `segment` (Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.

</details>

<details>

<summary>Metric by Segment Widget</summary>

The **metric by segment** widget lets you plot a metric over multiple segment values as a bar plot. This is useful to highlight areas of interest across different segments.

**Parameters:**

* **`metric`** - A MetricConfiguration class describing the metric to plot
* `timeframe`(Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* **`segment`**-  The Aporia segment identifier to plot metric for. This should be a specific `aporia.sdk.segments.Segment`object. This is inherited by the Compare view, if used.
* **`segment_values`** - A list of the segment values to plot. For categorical and custom segments, it should be the specific values. For numeric segments, it should be the lower bound numbers of each value.

**Compare Parameters:**

* `metric` (Default - None) - Alternative MetricConfiguration object to plot for the compare view. Mutually exclusive with `metric_overrides`.
* `metric_overrides` (Default - None) - metric overrides to apply on the original metric in the compare view. Mutually exclusive with `metric`.
* `timeframe` (Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version` (Default - None) - The Aporia version identifier to plot metric for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"

</details>

<details>

<summary>Metric Correlation Widget</summary>

The **metric correlation** widget lets you plot two metric over multiple segments or versions to look for correlation between the two.

You can choose between splitting view between different versions, or between different segments, but not both. The Compare view allows adding a different view selection.

**Parameters:**

* **`x_axis_metric`** - A MetricConfiguration class describing the metric to plot on the X axis
* **`y_axis_metric`** - A MetricConfiguration class describing the metric to plot on the Y axis
* `timeframe`(Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can a specific `aporia.sdk.versions.Version` object or `None`. Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `versions`(Default - None) - A list of Aporia version identifiers to plot metric for. This can a a list of specific `aporia.sdk.versions.Version` objects or have `None` as a list member to indicate "All versions". Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `segment` (Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number. This is only applicable if the `versions` parameter is used.
* `segment_values` - If a segment was chosen, this is a list of the segment values to plot. For categorical and custom segments, it should be the specific values. For numeric segments, it should be the lower bound numbers of each value. This is only applicable if the `version` parameter is used, or both `version` and `versions` are `None`. If `segment_value` and `segment_values` are both `None` and a single version is used, `segment_values` is automatically set to all values of `segment`.

**Compare Parameters:**

* `x_axis_metric_overrides` (Default - None) - metric overrides to apply on the original X axis metric in the compare view.
* `y_axis_metric_overrides` (Default - None) - metric overrides to apply on the original Y axis metric in the compare view.
* `timeframe` (Default - None) - An alternative timeframe for the metric. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate metric for (DatasetType.SERVING or DatasetType.TRAINING)
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can a specific `aporia.sdk.versions.Version` object or `None`. Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `versions`(Default - None) - A list of Aporia version identifiers to plot metric for. This can a a list of specific `aporia.sdk.versions.Version` objects or have `None` as a list member to indicate "All versions". Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `segment` (Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number. This is only applicable if the `versions` parameter is used.
* `segment_values` - If a segment was chosen, this is a list of the segment values to plot. For categorical and custom segments, it should be the specific values. For numeric segments, it should be the lower bound numbers of each value. This is only applicable if the `version` parameter is used, or both `version` and `versions` are `None`. If `segment_value` and `segment_values` are both `None` and a single version is used, `segment_values` is automatically set to all values of `segment`.

</details>

<details>

<summary>Distribution Widget</summary>

The **distribution** widget lets you plot a histogram of any column.

**Parameters:**

* **`field`**- The Aporia field to plot the distribution for. This parameter should be of type `aporia.sdk.fields.Field`
* `timeframe`(Default - None) - An alternative timeframe for the distribution. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate distribution for (DatasetType.SERVING or DatasetType.TRAINING)
* `version`(Default - None) - The Aporia version identifier to plot distribution for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* `segment`(Default - None) -  The Aporia segment identifier to plot distribution for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value`(Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.

**Compare Parameters:**

* `timeframe` (Default - None) - An alternative timeframe for the distribution. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate distribution for (DatasetType.SERVING or DatasetType.TRAINING)
* `version` (Default - None) - The Aporia version identifier to plot distribution for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* `segment` (Default - None) -  The Aporia segment identifier to plot distribution for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.

</details>

<details>

<summary>Time-Series Widget</summary>

The **time-series** widget lets you plot a metric over multiple segments or versions as a line plot over time. This is useful to track interesting metrics for changes or peaks.

**Parameters:**

* **`metric`** - A MetricConfiguration class describing the metric to plot
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can a specific `aporia.sdk.versions.Version` object or `None`. Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `versions`(Default - None) - A list of Aporia version identifiers to plot metric for. This can a a list of specific `aporia.sdk.versions.Version` objects or have `None` as a list member to indicate "All versions". Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `segment` (Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` (Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number. This is only applicable if the `versions` parameter is used.
* `segment_values` (Default - None) - If a segment was chosen, this is a list of the segment values to plot. For categorical and custom segments, it should be the specific values. For numeric segments, it should be the lower bound numbers of each value. This is only applicable if the `version` parameter is used, or both `version` and `versions` are `None`. If `segment_value` and `segment_values` are both `None` and a single version is used, `segment_values` is automatically set to all values of `segment`.
* `granularity` (Default - None) - The timeframe granularity to plot the line in. This can be `1d`, `1w`, `1M` to indicate daily, weekly or monthly, respectively. Pass `None` to indicate Aporia should divide the timeframes automatically for the best presentation.

**Compare Parameters:**

* `metric_overrides` (Default - None) - metric overrides to apply on the original metric in the compare view.&#x20;
* `version`(Default - None) - The Aporia version identifier to plot metric for. This can a specific `aporia.sdk.versions.Version` object or `None`. Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `versions`(Default - None) - A list of Aporia version identifiers to plot metric for. This can a a list of specific `aporia.sdk.versions.Version` objects or have `None` as a list member to indicate "All versions". Mutually exclusive with `versions`. If both are `None`, this is equivalent to a single version of "All Versions".
* `segment` (Default - None) -  The Aporia segment identifier to plot metric for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` (Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number. This is only applicable if the `versions` parameter is used.
* `segment_values` (Default - None) - If a segment was chosen, this is a list of the segment values to plot. For categorical and custom segments, it should be the specific values. For numeric segments, it should be the lower bound numbers of each value. This is only applicable if the `version` parameter is used, or both `version` and `versions` are `None`. If `segment_value` and `segment_values` are both `None` and a single version is used, `segment_values` is automatically set to all values of `segment`.

</details>

<details>

<summary>Histogram over Time Widget</summary>

The **histogram-over-time** widget lets you plot an area chart of a column over time. Currently only categorical and boolean columns are supported.

**Parameters:**

* **`field`**- The Aporia field to plot the distribution for. This parameter should be of type `aporia.sdk.fields.Field`
* `version`(Default - None) - The Aporia version identifier to plot distribution for. This can be either a specific `aporia.sdk.versions.Version` object or `None` to indicate "All Versions"
* `segment`(Default - None) -  The Aporia segment identifier to plot distribution for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value`(Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.
* `granularity` (Default - None) - The timeframe granularity to plot the line in. This can be `1d`, `1w`, `1M` to indicate daily, weekly or monthly, respectively. Pass `None` to indicate Aporia should divide the timeframes automatically for the best presentation.

</details>

<details>

<summary>Data Health Table Widget</summary>

The **data-health table** widget lets you plot a table of the most drifting/most missing features of your model. This easily highlights the main features needed to investigate or track. A common practice is to compare to training or a previous timeframe.

**Parameters:**

* `timeframe`(Default - None) - An alternative timeframe for the distribution. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate distribution for (DatasetType.SERVING or DatasetType.TRAINING)
* **`version`** - The Aporia version identifier to plot distribution for. This must be a specific `aporia.sdk.versions.Version` object
* `segment`(Default - None) -  The Aporia segment identifier to plot distribution for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value`(Default - None) - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.
* `sort_by` (Default - SortType.DRIFT\_SCORE) - Whether to highlight the top drifted features or features with highest missing ratio. Must be a value of `aporia.sdk.widgets.data_health_table_widget.SortType`
* `sort_direction` (Default - SortDirection.DESCENDING) - Whether to sort in an ascending or descending direction. Must be a value of `aporia.sdk.widgets.data_health_table_widget.SortDirection`

**Compare Parameters:**

* `timeframe` (Default - None) - An alternative timeframe for the distribution. Pass `None` to inherit the dashboard global timeframe.
* `phase` (Default - DatasetType.SERVING) - The version dataset to calculate distribution for (DatasetType.SERVING or DatasetType.TRAINING)
* `segment` (Default - None) -  The Aporia segment identifier to plot distribution for. This can be either a specific `aporia.sdk.segments.Segment`object or `None` to indicate "All Data"
* `segment_value` - If a segment was chosen, this is one of the segment values to plot for. For categorical and custom segments, it should be the specific value. For numeric segments, it should be the lower bound number.

</details>

Usage example:

```python
from aporia.sdk.metrics import MetricType
from aporia.sdk.widgets import MetricWidget, TextWidget
from aporia.sdk.widgets.base import MetricConfiguration

widgets = [
    TextWidget.create(position=(0, 0), size=(12, 1), text="This is my new dashboard!"),
    MetricWidget.create(
        position=(0, 1),
        size=(4, 5),
        title="Model activity",
        metric=MetricConfiguration(metric=MetricType.COUNT),
    ).compare(),  # This will display the same number twice
]
```

### Dashboard Configuration

The next step is to define the dashboard itself.

A dashboard is built of a list of widgets and global filters. The global filters includes the dashboard timeframe and other specific filters. This is defined by `aporia.sdk.dashboards.DashboardGlobalFilters`.  The fields are:

* **`timeframe`** - The global dashboard timeframe. See [#timeframes](#timeframes "mention") for more information.
* `version_id` - An optional version ID to filter by. All widget views configured for "All Versions" will use this version instead. Other views aren't affected.
* `data_segment_id` - An optional segment ID to filter by. All widget views configured for "All Data" will use this segment instead. Other views showing other segments will show the cross between the two segments, and views showing data for a different value of the same segment won't be affected. If this parameter is passed, `data_segment_value` must also be set.
* `data_segment_value` - The segment value to filter by, if `data_segment_id` is not `None`.

```python
from aporia.sdk.dashboards import DashboardConfiguration, DashboardGlobalFilters

dashboard_configuration = DashboardConfiguration(
    widgets=widgets,
    global_filters=DashboardGlobalFilters(
        timeframe="7d",  # Display data for last week
    ),
)
```

## Usage

### Reading & Updating Dashboards

You can use the `model.get_dashboards()` function to list all dashboards for a model. You will then get a list of objects you can filter by name, id, or other variables to find the relevant dashboard you want.

You can then edit these dashboards using the `update` function.

### Creating Dashboards

You can create new dashboards using the `model.create_dashboard(...)` function.

### Usage with as\_code SDK

In order to use the dashboard functionality with the as-code objects, you can call the `stack.get_resource_id()` function on the as-code resource name to get it's resource ID. You can then use this ID using the API SDK to get the relevant object.

### Example

```python
import os

from aporia import Aporia
from aporia.sdk.dashboards import DashboardConfiguration, DashboardGlobalFilters
from aporia.sdk.datasets import DatasetType
from aporia.sdk.metrics import MetricType
from aporia.sdk.widgets import DistributionWidget, MetricWidget, TextWidget, TimeSeriesWidget
from aporia.sdk.widgets.base import MetricConfiguration

apr = Aporia(
    account_name=os.environ["APORIA_ACCOUNT"],
    workspace_name=os.environ["APORIA_WORKSPACE"],
    token=os.environ["APORIA_TOKEN"],
)

MODEL_ID = "..."  # This can be retrieved through the model URL or through the as-code get_resource_id function

model = [model for model in apr.get_models() if model.id == MODEL_ID][0]

version = [version for version in model.get_versions() if version.name == "My version"][0]
field = model.get_field_by_name("my_prediction")

dashboard = model.create_dashboard(
    "My SDK dashboard",
    definition=DashboardConfiguration(
        global_filters=DashboardGlobalFilters(timeframe="7d"),
        widgets=[
            TextWidget.create(position=(0, 0), size=(12, 1), text="🔎 Model Overview"),
            # Show prediction volume of all versions compared to "My version"
            MetricWidget.create(
                position=(0, 1),
                size=(4, 5),
                title="Model Usage Volume by Version",
                metric=MetricConfiguration(metric=MetricType.COUNT),
            ).compare(version=version),
            # Plot prediction distribution of my_prediction in serving compared to training datasets across all versions
            DistributionWidget.create(
                position=(4, 1),
                size=(4, 5),
                title="Prediction Distribution - Serving VS Training",
                field=field,
            ).compare(phase=DatasetType.TRAINING),
            TimeSeriesWidget.create(
                position=(8, 1),
                size=(4, 5),
                title="Average Prediction",
                metric=MetricConfiguration(
                    metric=MetricType.MEAN,
                    field=field,
                ),
                granularity="1d",
                # Plot one line for "All Versions" and one line for "My version"
                versions=[None, version],
            ),
        ],
    ),
)
```
