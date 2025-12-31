# Source: https://docs.aporia.com/api-reference/api-extended-reference.md

# API Extended Reference

## Create Dataset

Complete API documentation can be found [here](https://platform.aporia.com/api/v1/docs#tag/Datasets/operation/connect_dataset_api_v1__account_name___workspace_name__datasets_post)

The `config` parameter can include the following keys:

* **header**: Applicable only to AWS S3, Google Cloud Storage, and Azure Blob. This flag indicates whether Spark should interpret the first line of the file as column names. Example: `"header": false`. Only relevant for CSV files.
* **infer\_schema**: Applicable only to AWS S3, Google Cloud Storage, and Azure Blob for CSV data. This flag determines whether the column types should be automatically inferred when reading the file. Example: `"infer_schema": false`. In most cases, this can be left out.
* **object\_format**: Applicable only to  AWS S3, Google Cloud Storage, and Azure Blob. Defines the format of the data files. Possible values are `parquet`, `csv`, `json`, `delta`. Example: `"object_format": "parquet"`.
* **query**: Specifies the dataset query used to retrieve data. Example: `"query": "SELECT f1, f2 FROM data_table"`. Applicable to all data sources. Note: Some data sources may use different SQL dialects. For blob-storage data sources, this SQL is SparkSQL and you can access the file data using `{data}` as a table name.
* **regex**: Applicable only to AWS S3, Google Cloud Storage, and Azure Blob. Defines a regular expression for the data bucket/path. Example: `"regex": "demo-data/demo-fraud-model-data.parquet"`.

## Create Monitor

Complete API documentation can be found [here](https://platform.aporia.com/api/v1/docs#tag/Monitors-\(Experimental\)/operation/create_monitor_api_v1__account_name___workspace_name__monitors_post)

* **type**: Specifies the monitor type. Possible values are: `"model_activity"`, `"missing_values"`, `"data_drift"`, `"prediction_drift"`, `"values_range"`, `"new_values"`, `"model_staleness"`, `"performance_degradation"`, `"metric_change"`, `"custom_metric"`, `"code_based_metric"`.
* **scheduling**: A CRON string that determines the monitor's execution schedule. For example setting the **scheduling string to** `0 0 * * *` will trigger the monitor every day at midnight.
* **is\_active**: A flag indicating whether the monitor is active or not.
* **configuration**: Contains all settings for the monitor. This parameter may include the following keys:
  * **identification**: Specifies the data on which the monitor should run. It may include:

    * **models**: Defines the model and its versions for monitoring. Includes `"id"` for the model ID and `"version"` for the model version ID. To monitor the "per active version," set it to `null`; for all versions, use `"all_versions"`; for the latest version, use `"latest"`. Example: `"models": {"id": "929ec979-4108-4397-ba59-ad639b7271e8", "version": "338dc00f-8e56-44b9-af90-f0e6507c9b09"}`. This field must always be set.
    * **segment**: Specifies the data segments to monitor. Includes `group` for the segment group ID and `value` for specific segment values. To include all segment values, set to `null`; for categorical or boolean values, specify the value (e.g., `"NY"`); for numeric values, provide the lower bound (e.g., for age range 18-23, use `"18"`). Example: `"group": "f2ad3ba0-9ff8-4b95-8d20-2490a06d026a", "value": 23}`.
    * **features, raw\_inputs, predictions, actuals**: Specifies which features, raw inputs, predictions, or actuals to monitor. The value should be an array of fields, each represented by an array containing the field's name and type. Example: `"features": [["age", "numeric"], ["is_insured", "boolean"], ["country", "categorical"]]`. For monitors which inspect different fields (drift, metric change, performance degradation, value ranges, new values), these fields must  be set.

    **Example of a complete identification configuration**:&#x20;

```json
{
  "identification": {
    "models": {
      "id": "7cf1a165-f321-452c-b8d7-2062e215cf37",
      "version": null
    },
    "segment": {
      "group": "f2ad3ba0-9ff8-4b95-8d20-2490a06d026a",
      "value": "AZ"
    },
    "features": [
        "age",
        "is_insured",
        "country"
    ]
  }
}
```

* **configuration**: Used to define monitor settings. It may include:

  * **focal**: Configurations for the data being analyzed. Potential keys include:
    * **source**: Data source, which can be `"SERVING"`, `"TRAINING"`, or `"TEST"`. Example: `"source": "SERVING"`.
    * **skipPeriod**: A time period, starting from the monitor execution time, to skip data calculations, formatted as a time string (e.g., `"2h"`, `"1w"`). Example: `"skipPeriod": "3h"` will skip all data records from the last 3 hours.
    * **timePeriod**: The time frame for data calculation, formatted as a time string (e.g., `"2h"`, `"1w"`). Example: `"timePeriod": "1w"` recalculates all data within the relevant week.
  * **baseline**: Configurations for the baseline data being compared against. Potential keys include:
    * **source**: Data source, which can be `"SERVING" or` `"TRAINING"`. Example: `"source": "SERVING"`.
    * **skipPeriod**: Similar to `focal`, specifies a time period from NOW to skip data calculations. Example: `"skipPeriod": "3h"`.\
      Note that it is common practice to set the skip period of the baseline equal to the time period of the focal, to match the timeframes.
    * **timePeriod**: Time frame for data calculation, formatted as a time string (e.g., `"2h"`, `"1w"`).  The time period is starting after the skip period (see sketch below). Example: `"timePeriod": "1w"`.
    * **segmentGroupId**: When comparing data between two segments, this is the segment group ID for the baseline data. Example: `"segmentGroupId": "f2ad3ba0-9ff8-4b95-8d20-2490a06d026a"`.
    * **segmentValue**: When comparing data between segments, this specifies the segment value for the baseline data. For categorical or boolean values, provide the value (e.g., `"NY"`); for numeric values, provide the lower bound (e.g., for an age range of 18-23, use `"18"`). Example: `"segmentValue": 0`.
    * **aggregationPeriod**: Defines the data aggregation period for creating a comparison timeline. Example: `"aggregationPeriod": "1d"` aggregates data into daily buckets.

      <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FZNSnys7P7j0JWNt4iH0p%2Fimage.png?alt=media&#x26;token=97085f91-4787-4338-85eb-b692f0334a79" alt=""><figcaption></figcaption></figure>

      This is needed for anomaly detection monitors for simple metrics (i.e: activity, performance degradation, metric change, custom metric, code-based-metric)
  * **logicEvaluations**: Defines the monitor's logic. Should be an array containing a single object with possible keys:
    * **name**: Name of the detection. Valid options are `APORIA_DRIFT_SCORE`, `MODEL_STALENESS`, `RANGE`, `RATIO`, `TIME_SERIES_ANOMALY`, `TIME_SERIES_RATIO_ANOMALY`, `VALUES_RANGE`. Example: `"name": "APORIA_DRIFT_SCORE"`.
    * **min**/**max**: Relevant for `MODEL_STALENESS, RANGE, RATIO, VALUES_RANGE.` Minimum or maximum threshold for the detection, if applicable. Example: `"min": 0.5`, `"max": 1.5`.
    * **thresholds**: Relevant for `APORIA_DRIFT_SCORE`. Specifies thresholds for drift detection, which can include different thresholds for numeric, categorical, or vector drifts. Example: `"thresholds": {"vector": 0.2, "numeric": 1, "categorical": 1}`.
    * **sensitivity**: Relevant for `TIME_SERIES_ANOMALY, TIME_SERIES_RATIO_ANOMALY.` Sensitivity threshold for time series anomaly detection. Example: `"sensitivity": 0.15`.
    * **testOnlyIncrease**: Relevant for `TIME_SERIES_ANOMALY`. A flag to alert only if the anomaly value exceeds the expected range (commonly set for missing values ratio detections). Default is `false`. Example: `"testOnlyIncrease": true`.
    * **new\_values\_count\_threshold**: Relevant for `VALUES_RANGE` detections. Sets the maximum allowed number of new values. Example: `"new_values_count_threshold": 1`.
    * **new\_values\_ratio\_threshold**: Relevant for `VALUES_RANGE` detections. Defines the maximum allowed ratio between new values and previously observed values. Example: `"new_values_ratio_threshold": 0.01`.
    * **distance**: Relevant for `VALUES_RANGE` detections. Defines the maximum gap between focal and baseline minimum & maximum values. For example: `"distance": 0.2.`
    * values: Relevant for VALUES\_RANGE detections. Define a list of allowed values for categorical fields. For example `"values": ["a", "b", "c"].`
  * **metric**: Configurations for the metrics being monitored. Potential keys include:
    * **type**: Specifies the metric type. Acceptable values are `count`, `column_count`, `mean`, `min`, `max`, `sum`, `squared_sum`, `missing_count`, `missing_ratio`, `squared_deviation_sum`, `histogram`, `ks_distance`, `js_distance`, `hellinger_distance`, `accuracy`, `precision`, `recall`, `f1`, `mse`, `rmse`, `mae`, `tp_count`, `fp_count`, `tn_count`, `fn_count`, `custom_metric`, `absolute_sum`, `absolute_error_sum`, `squared_error_sum`, `accuracy_at_k`, `precision_at_k`, `recall_at_k`, `mrr_at_k`, `map_at_k`, `ndcg_at_k`, `psi`, `tp_count_per_class`, `tn_count_per_class`, `fp_count_per_class`, `fn_count_per_class`, `accuracy_per_class`, `precision_per_class`, `recall_per_class`, `f1_per_class`, `min_length`, `max_length`, `mean_length`, `sketch_histogram`, `euclidean_distance`, `unique_values`, `variance`, `median`, `value_count`, `auc_roc`, `code`, `auuc`. \
      Example: `"type": "missing_ratio"`.
    * **id**: Relevant only for`code & custom_metric` type metrics. Specifies the ID of the code-based metric. Example: `"id": "929ec979-4108-4397-ba59-ad639b7271e8"`.
    * **threshold**: Applicable for metrics like `accuracy`, `f1`, `precision`, `recall`, `tp_count`, `fp_count`, `tn_count`, `fn_count`. Sets a threshold value for numeric columns. Example: `"threshold": 0.5`.
    * **metricAtK**: Applicable for metrics like `accuracy_at_k`, `precision_at_k`, `recall_at_k`, `mrr_at_k`, `map_at_k`, `ndcg_at_k`. Specifies the `k` value for the metric. Example: `"metricAtK": 3`.
    * **metricPerClass**: Relevant for metrics like `tp_count_per_class`, `tn_count_per_class`, `fp_count_per_class`, `fn_count_per_class`, `accuracy_per_class`, `precision_per_class`, `recall_per_class`, `f1_per_class`. Specifies the class name to calculate the metric on. Example: `"metricPerClass": "0"`.
    * **average**: Relevant for metrics like `recall`, `precision`, `f1`
  * **preConditions**: Defines preconditions that the data must satisfy before the logic evaluation runs. Can include a list of objects where each is a pre-condition to verify, with potential keys:
    * **name**: Specifies the name of the precondition. Options include:

      * `BASELINE_DATA_VALUE_IN_RANGE - verifies the value of the baseline data is in between given range.`
      * `FOCAL_DATA_VALUE_IN_RANGE - verifies the value of the focal is in between given range.`
      * `BASELINE_MIN_BUCKETS - verifies that the number of buckets with data in the baseline data exceed minimum quantity.`
      * `MIN_BASELINE_DATA_POINTS - verifies that the number of data points in the baseline data exceed minimum quantity.`
      * `MIN_FOCAL_DATA_POINTS - verifies that the number of data points in the focal data exceed minimum quantity.`
      * `IGNORE_TRAILING_ZEROS - removes trailing empty data buckets from baseline data and verifies the number of  number of buckets with data exceed minimum quantity.`

      Example: `"name": "MIN_FOCAL_DATA_POINTS"`.
    * **min / max**: Applicable for `BASELINE_DATA_VALUE_IN_RANGE`, `FOCAL_DATA_VALUE_IN_RANGE`. Defines the minimum or maximum values for the data. Example: `"min": 0.01`.
    * **value**: Relevant for `BASELINE_MIN_BUCKETS`, `MIN_BASELINE_DATA_POINTS`, `MIN_FOCAL_DATA_POINTS`. Specifies the minimum value for buckets with data, baseline data points, or focal data points. Example: `"value": 20`.
    * **minimumTimeWindowsInBaseline**: Relevant for `IGNORE_TRAILING_ZEROS`. Specifies the minimum required number of buckets with data in the baseline data, ignoring trailing zeros. Example: `"minimumTimeWindowsInBaseline": 3`.
    * **Example of a complete pre-conditions object**: `[{"name": "MIN_FOCAL_DATA_POINTS", "value": 20}, {"min": 0.01, "name": "FOCAL_DATA_VALUE_IN_RANGE"}, {"name": "MIN_BASELINE_DATA_POINTS", "value": 100}]`.
  * **actions**: Defines the action notifications triggered when an alert is detected. This should be an array containing a single element, with potential keys:

    * **alertType**: Specifies the alert type, affecting how it is displayed on Aporia's dashboard. Options include `feature_missing_values_threshold`, `metric_change`, `model_activity_anomaly`, `model_activity_change`, `model_activity_threshold`, `model_staleness`, `new_values`, `prediction_drift_anomaly`, `prediction_drift_segment_change`, `prediction_drift_training`, `values_range`. Example: `"alertType": "prediction_drift_anomaly"`.
    * **alertGroupByEntity**: Flag indicating whether the alert should be grouped by version, data segment, etc., or just by the monitor. Defaults to `true`.
    * **description**: A text template for the alert description displayed in the Aporia dashboard. The description can include HTML tags and placeholders, which will be replaced with actual alert data. Available placeholders include `model_id`, `model_name`, `model`, `model_version`, `field`, `importance`, `min_threshold`, `max_threshold`, `last_upper_bound`, `last_lower_bound`, `focal_value`, `baseline_value`, `focal_time_period`, `focal_times`, `baseline_time_period`, `baseline_times`, `baseline_segment`, `focal_segment`, `value_thresholds`, `unexpected_values`, `last_deployment_time`, `time_threshold`, `metric`, `drift_score`, `drift_score_text`. \
      Example: `"description": "An anomaly in the value of the <b>'{metric}'</b> of <b>{field}</b> {importance} was detected. <br /> The anomaly was observed in the <b>{model}</b> model, in version <b>{model_version}</b> for the <b>last {focal_time_period} ({focal_times})</b> <b>{focal_segment}</b>. <br /><br /> Based on metric history average and on defined threshold, the value was expected to be below <b>{max_threshold}</b>, but <b>{focal_value}</b> was received."`.
    * **alertGroupTimeUnit**: Defines the time unit to group alerts by. Possible values are `"h"`, `"d"`, or `"w"`. Example: `"alertGroupTimeUnit": "h"`.
    * **alertGroupTimeQuantity**: Specifies the time units for alert grouping (corresponding to `alertGroupTimeUnit`). Example: `"alertGroupTimeQuantity": 24"`.
    * **schema**: Should always be `"v1"`.
    * **notification**: Configurations for sending notifications for new alerts. Contains an array of objects, each with possible keys:
      * **type**: Notification type, which can be `"EMAIL"`, `"SLACK"`, `"TEAMS", "WEBHOOK"`
      * **integration\_id**: For Slack, Teams and Webhook notifications, this specifies the Slack integration ID. Example: `"integration_id": "a4b67272-2cf3-4fe1-82ff-2ac99c125215"`.
      * **emails**: For email notifications, this lists the email addresses to send the alert to. Example: `"emails": ["ben@org.com", "john@org.com"]`.
      * **Example configuration**: `[{"name": "Aporia - Teams", "type": "TEAMS", "webhook_url": "https://org.webhook.office.com/webhookb2/1234", "integration_id": "deff3bf8-a4bd-465a-887b-72f312f8d511"}, {"type": "EMAIL", "emails": ["jane@org.com"]}]`.
    * **visualization**: Specifies the graph type for visualization on Aporia's dashboard. Options include `null` (for no graph display), `'value_over_time'`, `'range_line_chart'`, `'embedding_drift_chart'`, `'values_candlestick_chart'`, `'distribution_compare_chart'`. Example: `"visualization": "distribution_compare_chart"`.
    * **severity**: Specifies the alert's severity level, which can be `"HIGH"`, `"MEDIUM"`, or `"LOW"`. Example: `"severity": "LOW"`.
    * **alertGroupByTime**: A flag indicating whether to merge similar alerts by time. Defaults to `true`.
    * **maxAlertsPerDay**: If set, defines the maximum number of alerts that can be generated per day from this monitor. Example: `"maxAlertsPerDay": 1"`.
    * **type**: Should always be `"ALERT"`.

  **Example of a complete configuration object**:&#x20;

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "focal": {
    "source": "SERVING",
    "skipPeriod": "1d",
    "timePeriod": "1d"
  },
  "metric": {
    "type": "js_distance"
  },
  "actions": [
    {
      "type": "ALERT",
      "schema": "v1",
      "severity": "MEDIUM",
      "alertType": "prediction_drift_anomaly",
      "description": "A prediction drift was detected in prediction &#x3C;b>'{field}'&#x3C;/b> {importance}.{drift_score_text}&#x3C;br /> The drift was observed in the &#x3C;b>{model}&#x3C;/b> model, in version &#x3C;b>{model_version}&#x3C;/b> for the &#x3C;b>last {focal_time_period} ({focal_times})&#x3C;/b> &#x3C;b>{focal_segment}&#x3C;/b> compared to the &#x3C;b>last {baseline_time_period} ({baseline_times})&#x3C;/b>. &#x3C;br />&#x3C;br /> Prediction drift indicates a significant change in model's behavior. In some cases, it is a strong indicator for concept drift.&#x3C;br />&#x3C;br /> Prediction drift might occur because: &#x3C;ul>&#x3C;li>Natural changes in data&#x3C;/li>&#x3C;li>Data store / provider schema changes&#x3C;/li>&#x3C;li>Data store / provider issues&#x3C;/li>&#x3C;li>Data processing issues&#x3C;/li>&#x3C;/ul>",
      "notification": [
        {
          "type": "SLACK",
          "integration_id": "df81469d-b78d-4010-94a5-8769c4f8ed3b"
        }
      ],
      "visualization": "distribution_compare_chart",
      "alertGroupByTime": true,
      "alertGroupByEntity": false,
      "alertGroupTimeUnit": "d",
      "alertGroupTimeQuantity": 1
    }
  ],
  "baseline": {
    "source": "SERVING",
    "skipPeriod": "2d",
    "timePeriod": "3w"
  },
  "preConditions": [
    {
      "name": "MIN_FOCAL_DATA_POINTS",
      "value": 1000
    }
  ],
  "logicEvaluations": [
    {
      "name": "APORIA_DRIFT_SCORE",
      "thresholds": {
        "numeric": 0.8
      }
    }
  ]
}
</code></pre>

## Create Model

Complete API documentation can be found [here](https://platform.aporia.com/api/v1/docs#tag/Models/operation/create_model_api_v1__account_name___workspace_name__models_post)

The `recalculation_schedules` parameter defines the periods for data recalculation, allowing for the configuration of multiple schedules. You can set up to 5 recalculation schedules per model. Each schedule consists of the following components:

* **skip\_period**: Specifies the duration, starting from the current time, during which data will be excluded from the calculation. The period is defined using a time string format (e.g., `"2h"` for 2 hours, `"1w"` for 1 week). For example, setting `"skip_period": "3h"` will skip data records from the last 3 hours. For daily models, hours are not applicable.
* **calculation\_window**: Defines the time frame over which the data should be recalculated. This is also specified using a time string format (e.g., `"2h"` for 2 hours, `"1w"` for 1 week). For instance, setting `"calculation_window": "1w"` will trigger a recalculation of all relevant data for the past week. For daily models, hours are not applicable.
* **calculation\_schedule**: A CRON expression that specifies when the recalculation process should be initiated. For example, `"0 0 * * *"` sets the recalculation to start every day at midnight.

For instance, setting the parameters as `{"skip_period": "3h", "calculation_window": "1w", "calculation_schedule": "0 0 * * *"}` results in a recalculation process that is triggered daily at midnight. This process will recalculate data of a week starting from 3 hours backwards. So, if the recalculation is triggered on August 20 at midnight, it will process data from August 12 at 21:00 (3 hours skipped) up to August 19 at 21:00.
