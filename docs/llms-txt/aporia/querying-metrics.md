# Source: https://docs.aporia.com/ml-monitoring-as-code/querying-metrics.md

# Querying metrics

To query metrics from Aporia, initialize a new client and call the `query_metrics` API:

```python
from datetime import datetime, timedelta
from aporia import (
    Aporia,
    MetricDataset,
    MetricParameters,
    TimeRange,
)
from aporia.sdk.datasets import DatasetType

aporia_token = os.environ["APORIA_TOKEN"]
aporia_account = os.environ["APORIA_ACCOUNT"]
aporia_workspace = os.environ["APORIA_WORKSPACE"]

aporia_client = Aporia(
    base_url="https://platform.aporia.com",  # or "https://platform-eu.aporia.com"
    token=aporia_token,
    account_name=aporia_account,
    workspace_name=aporia_workspace,
)

last_week_dataset = MetricDataset(
    dataset_type=DatasetType.SERVING,
    time_range=TimeRange(
        start=datetime.datetime.now() - datetime.timedelta(days=7),
        end=datetime.datetime.now(),
    ),
)

res = metrics.query_batch(
    model_id=model_id,
    metrics=[
        MetricParameters(
            dataset=last_week_dataset,
            name="count",
        ),
    ],
)

print(f"The model had {metrics[0]} predictions last week")

```

## Parameters

The `query_metrics` API has the following parameters:

<table><thead><tr><th width="153">Parameter</th><th width="280">Type</th><th>Description</th></tr></thead><tbody><tr><td>model_id</td><td><code>str</code></td><td>Model ID to query metrics for.</td></tr><tr><td>metrics</td><td><code>List[MetricParameters]</code></td><td>List of metrics to query. </td></tr></tbody></table>

The API can request values for multiple metrics concurrently.&#x20;

### MetricParameters

Here are different fields for the `MetricParameters` object:

<table><thead><tr><th width="186">Field</th><th width="178.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>name</td><td><code>str</code></td><td>Metric name (see <a data-mention href="../../api-reference/custom-metric-syntax#supported-functions">#supported-functions</a>). Required.</td></tr><tr><td>dataset</td><td><code>MetricDataset</code></td><td>Specifies what data to query (training / serving), what segment, and what timeframe. Required.</td></tr><tr><td>column</td><td><code>str</code></td><td>Name of the column to calculate the metric for.<br><br>Required except for the <code>count</code> metric. For performance metrics, this should be the name of the <em>prediction</em>, not the actual.</td></tr><tr><td>k</td><td><code>int</code></td><td>K value for ranking metrics such as nDCG.<br><br>Required only for <code>ndcg_at_k</code>, <code>map_at_k</code>, <code>mrr_at_k</code>, <code>accuracy_at_k</code>, <code>precision_at_k</code>, and <code>recall_at_k</code>. </td></tr><tr><td>threshold</td><td><code>float</code></td><td><p>Threshold to use when calculating binary performance metrics. </p><p></p><p>Required only if the prediction is <code>numeric</code> and the actual is <code>boolean</code>, and the metric is a binary performance metric such as <code>accuracy</code>, <code>recall</code>, <code>precision</code>, <code>f1_score</code>, etc.</p></td></tr><tr><td>custom_metric_id</td><td><code>str</code></td><td><p>Custom metric ID.</p><p></p><p>Required only if you want to query a custom metric.</p></td></tr><tr><td>baseline</td><td><code>MetricDataset</code></td><td><p>Specifies what data to use as baseline. </p><p></p><p>Required only for statistical distances such as <code>js_distance</code>, <code>ks_distance</code>, <code>psi</code>, and <code>hellinger_distance</code>. </p></td></tr></tbody></table>

### MetricDataset

The `MetricDataset` object contains the following fields:

<table><thead><tr><th width="159.33333333333331">Field</th><th width="174">Type</th><th>Description</th></tr></thead><tbody><tr><td>dataset_type</td><td><code>DatasetType</code></td><td>Can be either <code>DatasetType.SERVING</code> or <code>DatasetType.TRAINING</code>. Required.</td></tr><tr><td>time_range</td><td><code>TimeRange</code></td><td>Time range (contains <code>start</code> and <code>end</code> fields). Do not pass this for training.</td></tr><tr><td>model_version</td><td><code>str</code></td><td>Model version to filter by. Optional.</td></tr><tr><td>segment</td><td><code>MetricSegment</code></td><td>Used to query metrics in a specific data segment. Contains <code>id</code> and <code>value</code> fields.</td></tr></tbody></table>
