# Source: https://docs.fiddler.ai/api/rest-api/rest-api/custom-metrics.md

# Source: https://docs.fiddler.ai/reference/glossary/custom-metrics.md

# Source: https://docs.fiddler.ai/observability/platform/custom-metrics.md

# Custom Metrics

### Overview

Custom metrics offer the capability to define metrics that align precisely with your machine learning requirements. Whether it's tracking business KPIs, crafting specialized performance assessments, or computing weighted averages, custom metrics empower you to tailor measurements to your specific needs. Seamlessly integrate these custom metrics throughout Fiddler, leveraging them in dashboards, alerting, and performance tracking.

Create user-defined metrics by employing a simple query language we call [Fiddler Query Language (FQL)](https://docs.fiddler.ai/observability/platform/fiddler-query-language). FQL enables you to leverage your model's features, metadata, predictions, and outcomes for new data fields using a rich array of aggregations, operators, and metric functions, thereby expanding the depth of your analytical insights.

### How to Define a Custom Metric

Build custom metrics effortlessly with Fiddler's intuitive Excel-formula-like syntax. Once a custom metric is defined, Fiddler distinguishes itself by seamlessly managing time granularity and ranges within the charting, dashboarding, and analytics experience. This empowers you to effortlessly adjust time range and granularity without the need to modify your query, ensuring a smooth and efficient analytical experience.

### Adding a Custom Metric

From the model schema page, you can access the model's custom metrics by clicking the **Custom Metrics** tab at the top of the page. Then click **Add Custom Metric** to add a new Custom Metric. Finally, enter the name, description, and FQL definition for your custom metric and click **Save**.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-e2ed380f23ae958c92778437d58c2a35d1974fe6%2F1614146-image.png?alt=media)

### Accessing Custom Metrics in Charts and Alerts

After your custom metric is saved, you can use it in your chart and alert definitions.

#### Charts

Set `Metric Type` to `Custom Metric` and select your desired custom metric.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-96b1636c208730edd1af8c1a6b4eed8ea5109eb1%2F94a09f8-image.png?alt=media)

#### Alerts

When creating a new alert rule, set `Metric Type` to `Custom Metric`, and under the `Metric` field select your desired custom metric or author a new metric to use.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-078f9c513e83d9af6d4c5794d46b4cc1f688e8bc%2Feaa46b0-image.png?alt=media)

### Modifying Custom Metrics

Since alerts can be set on Custom Metrics, making modifications to a metric may introduce inconsistencies in alerts.

> 🚧 Therefore, custom metrics cannot be modified once they are created.

If you'd like to try out a new metric, you can create a new one with a different name and definition.

### Deleting Custom Metrics

To delete a custom metric using the Python client, see [CustomMetric.delete()](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-python-client-sdk). Alternatively, from the custom metrics tab, you can delete a metric by clicking the trash icon next to the metric record.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-d29e1b0603abd1bd96d0a0272422a9c77fcbad25%2Fcb4a4bd-image.png?alt=media)

### Examples

> 📘 Custom metrics must return either:
>
> * an aggregate (produced by aggregate functions or built-in metric functions)
> * a combination of aggregates

#### Simple Metric

Given this example use case:

> If an event is a false negative, assign a value of -40. If the event is a false positive, assign a value of -400. If the event is a true positive or true negative, then assign a value of 250.

Create a new Custom Metric with the following FQL formula:

```python
average(if(fn(), -40, if(fp(), -400, 250)))
```

Fiddler offers many convenience functions such as `fp()` and `fn()`.\
Alternatively, we could also identify false positives and false negatives the old fashioned way.

```python
average(if(Prediction < 0.5 and Target == 1, -40, if(Prediction >= 0.5 and Target == 0, -400, 250)))
```

Here, we assume `Prediction` is the name of the output column for a binary classifier and `Target` is the name of our label column.

#### Tweedie Loss

In our next example, we provide an example implementation of the Tweedie Loss Function. Here, `Target` is the name of the target column and `Prediction` is the name of the prediction/output column.

```python
average((Target \* Prediction ^ (1 - 0.5)) / (1 - 0.5) + Prediction ^ (2 - 0.5) / (2 - 0.5))
```

#### Quantile/Percentile Metrics

Quantile metrics are essential for understanding the distribution of your data and tracking percentile-based performance indicators. Unlike averages, which can be skewed by outliers, quantiles provide robust insights into the actual behavior of your model across different percentiles.

**Use Case: Monitoring ML Model Latency**

Track the median (50th percentile) inference time to understand typical model performance:

```python
quantile(inference_time_ms, level=0.5)
```

**Use Case: SLA Compliance Tracking**

Monitor 95th percentile latency to ensure most requests meet performance SLAs:

```python
quantile(response_time_ms, level=0.95)
```

**Use Case: Outlier Detection**

Track the 99th percentile of prediction scores to identify extreme predictions:

```python
quantile(prediction_score, level=0.99)
```

**Use Case: Statistical Distribution Analysis**

Compute quartiles to understand the distribution of a feature or prediction:

```python
quantile(feature_value, level=0.25)  # First quartile (Q1)
quantile(feature_value, level=0.5)   # Median (Q2)
quantile(feature_value, level=0.75)  # Third quartile (Q3)
```

> 📘 **Why use quantiles instead of averages?**
>
> Quantiles provide a more complete picture of your data's distribution. While averages can be heavily influenced by outliers, percentiles show you the actual values at specific points in your distribution. For example, a 95th percentile latency of 500ms means 95% of your requests complete in 500ms or less, regardless of how slow the remaining 5% might be.

### Modifying Custom Metrics

Since alerts can be set on Custom Metrics, modifying a metric may introduce inconsistencies in those alerts.

> 🚧 Therefore, custom metrics cannot be modified once they are created.

If you'd like to try out a new metric, you can create a new one with a different name and definition.
