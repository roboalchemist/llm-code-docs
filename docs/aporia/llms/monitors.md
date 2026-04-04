# Source: https://docs.aporia.com/ml-monitoring-as-code/monitors.md

# Monitors

This guide will show you how to automatically add monitors to your models from code using the Python SDK. For more information on the various types of monitors in Aporia, [please refer to the documentation on monitors.](https://docs.aporia.com/monitors-and-alerts)

## Defining monitors

To define a new monitor, create an `aporia.Monitor(...)` object.

### Step 1: Choose monitor type and detection method

When designing a new monitor, the first decision you have to make is:

* **What's the monitor type you'd like to create?**
  * Examples: Data drift, Missing values, Performance degradation, etc.
  * This step is similar to the following step in the UI:

    <div align="left"><figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FfySLFhGaFfTv2BNoofY0%2FScreen%20Shot%202023-06-26%20at%202.04.14.png?alt=media&#x26;token=329bf0ea-13fc-4dc2-89c7-73c6a018c0fe" alt="" width="563"><figcaption></figcaption></figure></div>
* **What's the detection method you'd like to use?**
  * Examples: Anomaly Detection over Time, Change in Percentage, Absolute values, Compared to Training, Compared to Segment, etc.
  * This step is similar to the following step in the UI:

    <div align="left"><figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F7iOxiK9NnKG9UF34UnET%2FScreen%20Shot%202023-06-26%20at%202.04.29.png?alt=media&#x26;token=fc1c9bc3-7467-46e2-917e-d3fa3b0af4e1" alt="" width="563"><figcaption></figcaption></figure></div>

To begin, start by creating a monitor object, with your chosen `monitor_type` and `detection_method`, and add it to your model.&#x20;

See [#detection-methods-overview](#detection-methods-overview "mention") and [#supported-monitor-types-detection-methods](#supported-monitor-types-detection-methods "mention") for the an overview on different monitor types and their supported detection methods.

<pre class="language-python"><code class="lang-python">import aporia.as_code as aporia

stack = aporia.Stack(...)

data_drift = aporia.Monitor(
    "Data Drift - Last week compared to Training",
<strong>    monitor_type=aporia.MonitorType.DATA_DRIFT,
</strong><strong>    detection_method=aporia.DetectionMethod.COMPARED_TO_TRAINING,
</strong>    ...
)

my_model = aporia.Model(
    "My Model",
    type=aporia.ModelType.RANKING,
    icon=aporia.ModelIcon.RECOMMENDATIONS,
    ...,
    
<strong>    monitors=[data_drift],
</strong>)

stack.add(my_model)
</code></pre>

### Step 2: Choose focal and baseline datasets

The next step is to choose the dataset in which your monitor will be evaluated - this is called the **focal** dataset. In most detection methods, you'll also need to provide a **baseline** dataset.

For example, if you want to create a data drift monitor to compare the distribution of a feature from the last week to the training set, then focal will be "last week in serving", and baseline will be "training set".

<pre class="language-python"><code class="lang-python">data_drift = aporia.Monitor(
    "Data Drift - Last week compared to Training",
    monitor_type=aporia.MonitorType.DATA_DRIFT,
    detection_method=aporia.DetectionMethod.COMPARED_TO_TRAINING,
<strong>    focal=aporia.FocalConfiguration(
</strong><strong>        # Last week in serving
</strong><strong>        timePeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.WEEKS)
</strong><strong>    ),
</strong><strong>    baseline=aporia.BaselineConfiguration(
</strong><strong>         # Training dataset
</strong><strong>        source=aporia.SourceType.TRAINING
</strong><strong>    ),
</strong>    ...
)
</code></pre>

Baseline is required for any monitor that has a "Compared to" field like in the example below, or in any detection method that is not `DetectionMethod.ABSOLUTE`:

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F2Ygp6nlCHkLh37cSrJbj%2Fimage.png?alt=media&#x26;token=59d67998-26ef-42f4-8f6f-f5c9e47efddd" alt=""><figcaption></figcaption></figure>

Here's an example for focal / baseline in an anomaly detection over time monitor:

<pre class="language-python"><code class="lang-python">activity_anomaly_detection = aporia.Monitor(
    "Activity Anomaly Detection",
    monitor_type=aporia.MonitorType.MODEL_ACTIVITY,
    detection_method=aporia.DetectionMethod.ANOMALY,
<strong>    focal=aporia.FocalConfiguration(
</strong><strong>        # Last day
</strong><strong>        timePeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
</strong><strong>    ),
</strong><strong>    baseline=aporia.BaselineConfiguration(
</strong><strong>        # Last 2 weeks *before* the last day
</strong><strong>        source=aporia.SourceType.SERVING,
</strong><strong>        timePeriod=aporia.TimePeriod(count=2, type=aporia.PeriodType.WEEKS),
</strong><strong>        skipPeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
</strong><strong>    ),
</strong>    ...
)
</code></pre>

### Step 3: Configure monitor

Next, it is time to configure some important parameters for the monitor. For example:

<pre class="language-python"><code class="lang-python">activity_anomaly_detection = aporia.Monitor(
    "Activity Anomaly Detection",
    monitor_type=aporia.MonitorType.MODEL_ACTIVITY,
    detection_method=aporia.DetectionMethod.ANOMALY,
    focal=aporia.FocalConfiguration(
        # Last day
        timePeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
    ),
    baseline=aporia.BaselineConfiguration(
        # Last 2 weeks *before* the last day
        source=aporia.SourceType.SERVING,
        timePeriod=aporia.TimePeriod(count=2, type=aporia.PeriodType.WEEKS),
        skipPeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
    ),
<strong>    sensitivity=0.3,
</strong>    ...
)
</code></pre>

&#x20;The following table describes the required parameters for each monitor type

<table><thead><tr><th width="190.33333333333331">Monitor</th><th>Detection Method</th><th>Required Parameters</th></tr></thead><tbody><tr><td>Model Activity</td><td>Anomaly Detection</td><td><ul><li><code>sensitivity</code> (0-1)</li><li><code>baseline</code></li></ul></td></tr><tr><td>Model Activity</td><td>Change in Percentage</td><td><ul><li><code>percentage</code> (0-100)</li><li><code>baseline</code></li></ul></td></tr><tr><td>Model Activity</td><td>Absolute values</td><td><ul><li><code>min</code> (optional)</li><li><code>max</code> (optional)</li></ul></td></tr><tr><td>Data Drift</td><td>Anomaly Detection</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>features (list[str])</code></li><li><code>raw_inputs (list[str])</code></li><li><code>baseline</code></li></ul></td></tr><tr><td>Data Drift</td><td>Compared to Segment</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>features (list[str])</code></li><li><code>raw_inputs (list[str])</code></li><li><code>baseline</code> (On segment)</li></ul></td></tr><tr><td>Data Drift</td><td>Compared to Training</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>features (list[str])</code></li><li><code>raw_inputs (list[str])</code></li><li><code>baseline</code> (On Training)</li></ul></td></tr><tr><td>Prediction Drift</td><td>Anomaly Detection</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>predictions (list[str])</code> </li><li><code>baseline</code></li></ul></td></tr><tr><td>Prediction Drift</td><td>Compared to Segment</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>predictions (list[str])</code> </li><li><code>baseline</code> (On segment)</li></ul></td></tr><tr><td>Prediction Drift</td><td>Compared to Training</td><td><ul><li><code>thresholds (aporia.ThresholdConfiguration)</code></li><li><code>predictions (list[str])</code> </li><li><code>baseline</code> (On Training)</li></ul></td></tr><tr><td>Missing Values</td><td>Anomaly Detection</td><td><ul><li><code>sensitivity</code> (0-1)</li><li><code>min</code> (0-100) (Optional)</li><li><code>raw_inputs (list[str])</code></li><li><code>features (list[str])</code></li><li><code>predictions (list[str])</code></li><li><code>baseline</code></li><li><code>testOnlyIncrease</code> (Optional)</li></ul></td></tr><tr><td>Missing Values</td><td>Change in Percentage</td><td><ul><li><code>percentage</code></li><li><code>min</code> (0-100) (Optional)</li><li><code>raw_inputs (list[str])</code></li><li><code>features (list[str])</code></li><li><code>predictions (list[str])</code></li><li><code>baseline</code></li></ul></td></tr><tr><td>Missing Values</td><td>Absolute values</td><td><ul><li><code>min</code> (0-100) (Optional)</li><li><code>max</code> (0-100) (Optional)</li><li><code>raw_inputs (list[str])</code></li><li><code>features (list[str])</code></li><li><code>predictions (list[str])</code></li></ul></td></tr><tr><td>Missing Values</td><td>Compared to Segment</td><td><ul><li><code>percentage</code></li><li><code>min</code></li><li><code>raw_inputs (list[str])</code></li><li><code>features (list[str])</code></li><li><code>predictions (list[str])</code></li><li><code>baseline</code> (On segment)</li></ul></td></tr><tr><td>Model Staleness</td><td>Absolute</td><td><ul><li><code>staleness_period (aporia.TimePeriod)</code></li></ul></td></tr><tr><td>New Values</td><td>Percentage</td><td><ul><li><code>new_values_count_threshold</code> (Optional)</li><li><code>new_values_ratio_threshold</code> (Optional)</li><li><code>baseline</code></li></ul></td></tr><tr><td>New Values</td><td>Compared to Segment</td><td><ul><li><code>new_values_count_threshold</code> (Optional)</li><li><code>new_values_ratio_threshold</code> (Optional)</li><li><code>baseline</code> (on Segment)</li></ul></td></tr><tr><td>New Values</td><td>Compared to Training</td><td><ul><li><code>new_values_count_threshold</code> (Optional)</li><li><code>new_values_ratio_threshold</code> (Optional)</li><li><code>baseline</code> (on Training)</li></ul></td></tr><tr><td>Values Range</td><td>Percentage</td><td><ul><li><code>distance</code></li><li><code>baseline</code></li></ul></td></tr><tr><td>Values Range</td><td>Absolute</td><td><ul><li><code>min</code> (Optional)</li><li><code>max</code> (Optiona)</li></ul></td></tr><tr><td>Values Range</td><td>Compared to Segment</td><td><ul><li><code>distance</code></li><li><code>baseline</code> (on Segment)</li></ul></td></tr><tr><td>Values Range</td><td>Compared to Training</td><td><ul><li><code>distance</code></li><li><code>baseline</code> (on Training)</li></ul></td></tr><tr><td>Performance Degradation</td><td>Anomaly Detection</td><td><ul><li><code>metric</code></li><li><code>sensitivity</code></li><li><code>baseline</code></li><li>metric-specific parameters</li></ul></td></tr><tr><td>Performance Degradation</td><td>Absolute</td><td><ul><li><code>metric</code></li><li><code>min</code> (Optional)</li><li><code>max</code> (Optional)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Performance Degradation</td><td>Percentage</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code></li><li>metric-specific parameters</li></ul></td></tr><tr><td>Performance Degradation</td><td>Compared to Segment</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code> (Compared to Segment)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Performance Degradation</td><td>Compared to Training</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code> (Compared to Training)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Metric Change</td><td>Anomaly Detection</td><td><ul><li><code>metric</code></li><li><code>sensitivity</code></li><li><code>baseline</code></li><li>metric-specific parameters</li></ul></td></tr><tr><td>Metric Change</td><td>Absolute</td><td><ul><li><code>metric</code></li><li><code>min</code> (Optional)</li><li><code>max</code> (Optional)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Metric Change</td><td>Percentage</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code></li><li>metric-specific parameters</li></ul></td></tr><tr><td>Metric Change</td><td>Compared to Segment</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code> (Compared to Segment)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Metric Change</td><td>Compared to Training</td><td><ul><li><code>metric</code></li><li><code>percentage</code></li><li><code>baseline</code> (Compared to Training)</li><li>metric-specific parameters</li></ul></td></tr><tr><td>Custom Metric</td><td>Anomaly Detection</td><td><ul><li><code>custom_metric</code>/<code>custom_metric_id</code></li><li><code>sensitivity</code></li><li><code>baseline</code></li></ul></td></tr><tr><td>Custom Metric</td><td>Absolute</td><td><ul><li><code>custom_metric</code>/<code>custom_metric_id</code></li><li><code>min</code> (Optional)</li><li><code>max</code> (Optional)</li><li><code>baseline</code></li></ul></td></tr><tr><td>Custom Metric</td><td>Percentage</td><td><ul><li><code>custom_metric</code>/<code>custom_metric_id</code></li><li><code>percentage</code></li><li><code>baseline</code></li></ul></td></tr></tbody></table>

#### Metric-specific parameters

* `k`: Used for ranking metrics, such as NDCG, MRR, MAP etc.
* `prediction_threshold`: Used for binary confusion matrix metrics, such as accuracy, tp\_count, recall etc. Used with a numeric prediction (0-1) and a boolean actual.
* `prediction_class`: The class for which to calculate per-class metrics, such as accuracy-per-class.
* `average_method`: Used for precision/recall/f1\_score on multiclass predictions. Values are of `aporia.AverageMethod` enum (`MICRO`/`MACRO`/`WEIGHTED`)

### Step 4: Configure monitor action (e.g alert)

Finally, any monitor requires a `severity` parameter to describe the severity of the alerts generated by this monitor (low / medium / high).

You can also add an `emails` parameter for receiving the alert in mail, or the `messaging` parameter for integration with Webhooks, Datadog, Slack, Teams, etc.

<pre class="language-python"><code class="lang-python">activity_anomaly_detection = aporia.Monitor(
    "Activity Anomaly Detection",
    monitor_type=aporia.MonitorType.MODEL_ACTIVITY,
    detection_method=aporia.DetectionMethod.ANOMALY,
    focal=aporia.FocalConfiguration(
        # Last day
        timePeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
    ),
    baseline=aporia.BaselineConfiguration(
        # Last 2 weeks *before* the last day
        source=aporia.SourceType.SERVING,
        timePeriod=aporia.TimePeriod(count=2, type=aporia.PeriodType.WEEKS),
        skipPeriod=aporia.TimePeriod(count=1, type=aporia.PeriodType.DAYS)
    ),
    sensitivity=0.3,
<strong>    severity=aporia.Severity.MEDIUM,
</strong><strong>    emails=[&#x3C;EMAIL_LIST>],
</strong><strong>    messaging={"WEBHOOK": [WEBHOOK_INTEGRATION_ID], "SLACK": [SLACK_INTEGRATION_ID]}
</strong>)
</code></pre>

## Detection Methods Overview

<table><thead><tr><th width="184">Detection Method</th><th width="214.33333333333331">Enum value</th><th>Description</th><th>Exmaple</th></tr></thead><tbody><tr><td>Anomaly Detection over Time</td><td><code>DetectionMethod.ANOMALY</code></td><td>This will train an anomaly detection model to raise an alert if there's an anomaly in metric value with respect to a certain baseline</td><td>Missing value ratio of last week compared to week before that</td></tr><tr><td>Change in Percentage</td><td><code>DetectionMethod.PERCENTAGE</code></td><td>Detect change in percentage in metric value</td><td>Standard deviation changed by >20%</td></tr><tr><td>Absolute values</td><td><code>DetectionMethod.ABSOLUTE</code></td><td>Raise an alert when metric value is larger or smaller than a certain value</td><td>Accuracy is lower than 0.9</td></tr><tr><td>Compared to Segment</td><td><code>DetectionMethod.COMPARED_TO_SEGMENT</code></td><td>Detect changes in metric value between two data segments</td><td>Data drift between <code>gender=male</code> to <code>gender=female</code></td></tr><tr><td>Compared to Training</td><td><code>DetectionMethod.COMPARED_TO_TRAINING</code></td><td>Data change in metric value compared to the training set</td><td>Prediction drift of last month in serving compared to training</td></tr></tbody></table>

## Supported Monitor Types / Detection Methods

The following table describes the various monitor types and their supported detection methods:

<table><thead><tr><th width="127.33333333333331">Monitor Type</th><th width="259">Enum value</th><th>Supported detection methods</th></tr></thead><tbody><tr><td>Model Activity</td><td><code>MonitorType.MODEL_ACTIVITY</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li></ul></td></tr><tr><td>Data Drift</td><td><code>MonitorType.DATA_DRIFT</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr><tr><td>Prediction Drift</td><td><code>MonitorType.PREDICTION_DRIFT</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr><tr><td>Missing Values</td><td><code>MonitorType.MISSING_VALUES</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li></ul></td></tr><tr><td>Performance Degradation</td><td><code>MonitorType.PERFORMANCE_DEGRADATION</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr><tr><td>Metric Change</td><td><code>MonitorType.METRIC_CHANGE</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr><tr><td>Custom Metric</td><td><code>MonitorType.CUSTOM_METRIC_MONITOR</code></td><td><ul><li><code>DetectionMethod.ANOMALY</code></li><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li></ul></td></tr><tr><td>Model Staleness</td><td><code>MonitorType.MODEL_STALENESS</code></td><td><ul><li><code>DetectionMethod.ABSOLUTE</code></li></ul></td></tr><tr><td>Value Range</td><td><code>MonitorType.VALUE_RANGE</code></td><td><ul><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.ABSOLUTE</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr><tr><td>New Values</td><td><code>MonitorType.NEW_VALUES</code></td><td><ul><li><code>DetectionMethod.PERCENTAGE</code></li><li><code>DetectionMethod.COMPARED_TO_SEGMENT</code></li><li><code>DetectionMethod.COMPARED_TO_TRAINING</code></li></ul></td></tr></tbody></table>

###
