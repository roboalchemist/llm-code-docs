# Source: https://docs.fiddler.ai/reference/ml-metrics-reference.md

# ML Metrics Reference

Fiddler provides 35 built-in metrics for monitoring ML models in production. These metrics cover model performance, data drift, data integrity, traffic, and statistics. You can also define [custom metrics](https://docs.fiddler.ai/observability/platform/custom-metrics) using the [Fiddler Query Language](https://docs.fiddler.ai/observability/platform/fiddler-query-language).

{% hint style="info" %}
For LLM and GenAI application metrics, see the [LLM Observability Metrics Reference](https://docs.fiddler.ai/reference/llm-observability-metrics).
{% endhint %}

## Performance metrics

Performance metrics measure how well a model performs on its task. The available metrics depend on the model task type. For more details on performance monitoring workflows, see [Performance Tracking](https://docs.fiddler.ai/observability/platform/performance-tracking-platform).

### Binary classification

| Metric                      | API ID                       | Score Range   | Description                                                                                                        |
| --------------------------- | ---------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------ |
| Accuracy                    | `accuracy`                   | 0 -- 1        | (TP + TN) / (TP + TN + FP + FN)                                                                                    |
| Log Loss                    | `log_loss`                   | 0 -- infinity | Measures the difference between the predicted probability distribution and the true distribution                   |
| Precision                   | `precision`                  | 0 -- 1        | TP / (TP + FP). Requires a decision threshold.                                                                     |
| Recall / True Positive Rate | `recall`                     | 0 -- 1        | TP / (TP + FN). Requires a decision threshold.                                                                     |
| F1 Score                    | `f1_score`                   | 0 -- 1        | 2 \* (Precision \* Recall) / (Precision + Recall). Requires a decision threshold.                                  |
| False Positive Rate         | `fpr`                        | 0 -- 1        | FP / (FP + TN). Requires a decision threshold.                                                                     |
| AUC                         | `auc`                        | 0 -- 1        | Area Under the ROC Curve (histogram-based calculation). See also AUROC.                                            |
| AUROC                       | `auroc`                      | 0 -- 1        | Area Under the Receiver Operating Characteristic curve, plotting true positive rate against false positive rate    |
| Expected Calibration Error  | `expected_calibration_error` | 0 -- 1        | Measures the difference between predicted probabilities and empirical probabilities                                |
| Geometric Mean              | `geometric_mean`             | 0 -- 1        | Square root of (Precision \* Recall). Requires a decision threshold.                                               |
| Calibrated Threshold        | `calibrated_threshold`       | 0 -- 1        | A threshold that balances precision and recall at a particular operating point                                     |
| Data Count                  | `data_count`                 | 0 -- infinity | The number of events where target and output are both not NULL. Used as the denominator for accuracy calculations. |

### Multi-class classification

| Metric         | API ID           | Score Range   | Description                                                                                                              |
| -------------- | ---------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Accuracy       | `accuracy`       | 0 -- 1        | (Number of correctly classified samples) / Data Count                                                                    |
| Log Loss       | `log_loss`       | 0 -- infinity | Measures the difference between the predicted probability distribution and the true distribution, on a logarithmic scale |
| Log Loss Count | `log_loss_count` | 0 -- infinity | Count of events used in the Log Loss calculation                                                                         |

### Regression

| Metric                                          | API ID  | Score Range    | Description                                                                               |
| ----------------------------------------------- | ------- | -------------- | ----------------------------------------------------------------------------------------- |
| Mean Absolute Error (MAE)                       | `mae`   | 0 -- infinity  | Average of the absolute differences between predicted and true values                     |
| Mean Squared Error (MSE)                        | `mse`   | 0 -- infinity  | Average of the squared differences between predicted and true values                      |
| Mean Absolute Percentage Error (MAPE)           | `mape`  | 0 -- infinity  | Average of the absolute percentage differences between predicted and true values          |
| Weighted Mean Absolute Percentage Error (WMAPE) | `wmape` | 0 -- infinity  | Weighted average of the absolute percentage differences between predicted and true values |
| R-squared (R²)                                  | `r2`    | -infinity -- 1 | Proportion of variance in the dependent variable explained by the independent variables   |

### Ranking

| Metric                                       | API ID        | Score Range   | Description                                                                                                                 |
| -------------------------------------------- | ------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Mean Average Precision (MAP)                 | `map`         | 0 -- 1        | Average precision of relevant items in the top-k results. For binary relevance ranking only. Supports configurable `top_k`. |
| Normalized Discounted Cumulative Gain (NDCG) | `ndcg_mean`   | 0 -- 1        | Quality of the ranking by discounting relevance scores at lower ranks. Supports configurable `top_k`.                       |
| Query Count                                  | `query_count` | 0 -- infinity | Number of ranking queries in the time period                                                                                |

## Drift metrics

Drift metrics measure distributional changes between your baseline dataset and production data. High drift can indicate data pipeline issues or genuine shifts in the data distribution. Both metrics require a [baseline](https://docs.fiddler.ai/reference/glossary/baseline) dataset. For more details, see [Data Drift](https://docs.fiddler.ai/observability/platform/data-drift-platform).

| Metric                           | API ID | Score Range   | Description                                                                                                               |
| -------------------------------- | ------ | ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Jensen-Shannon Distance (JSD)    | `jsd`  | 0 -- 1        | Distance between the baseline distribution and the production distribution for a given field                              |
| Population Stability Index (PSI) | `psi`  | 0 -- infinity | Drift metric based on multinomial classification of a variable into bins, comparing baseline and production distributions |

{% hint style="info" %}
The drift analytics table also provides **Feature Impact**, **Feature Drift**, and **Prediction Drift Impact** as derived values to help identify which features contribute most to prediction drift.
{% endhint %}

## Data integrity metrics

Data integrity metrics detect violations in production data compared to the schema established during model onboarding. Fiddler tracks three violation types: missing values, type mismatches, and range violations. Both raw counts and percentages are available. For more details, see [Data Integrity](https://docs.fiddler.ai/observability/platform/data-integrity-platform).

### Count-based

| Metric                  | API ID                  | Description                                               |
| ----------------------- | ----------------------- | --------------------------------------------------------- |
| Any Violation           | `any_violation_count`   | Count of any data integrity violation across all features |
| Missing Value Violation | `null_violation_count`  | Count of missing value violations across all features     |
| Range Violation         | `range_violation_count` | Count of range violations across all features             |
| Type Violation          | `type_violation_count`  | Count of data type violations across all features         |

### Percentage-based

| Metric                    | API ID                       | Description                                            |
| ------------------------- | ---------------------------- | ------------------------------------------------------ |
| % Any Violation           | `any_violation_percentage`   | Percentage of events with any data integrity violation |
| % Missing Value Violation | `null_violation_percentage`  | Percentage of events with missing value violations     |
| % Range Violation         | `range_violation_percentage` | Percentage of events with range violations             |
| % Type Violation          | `type_violation_percentage`  | Percentage of events with data type violations         |

## Traffic metrics

Traffic metrics provide visibility into the operational health of your model service. For more details, see [Traffic](https://docs.fiddler.ai/observability/platform/traffic-platform).

| Metric  | API ID    | Description                                                  |
| ------- | --------- | ------------------------------------------------------------ |
| Traffic | `traffic` | Volume of inference requests received by the model over time |

## Statistics metrics

Statistics metrics provide basic aggregations over columns. These are useful for monitoring custom metadata fields over time. For more details, see [Statistics](https://docs.fiddler.ai/observability/platform/statistics).

| Metric    | API ID      | Applies To                    | Description                         |
| --------- | ----------- | ----------------------------- | ----------------------------------- |
| Average   | `average`   | Numeric columns               | Arithmetic mean of a numeric column |
| Sum       | `sum`       | Numeric columns               | Sum of a numeric column             |
| Frequency | `frequency` | Categorical / Boolean columns | Count of occurrences for each value |

## Custom metrics

In addition to the built-in metrics above, you can define custom metrics using the [Fiddler Query Language (FQL)](https://docs.fiddler.ai/observability/platform/fiddler-query-language). Custom metrics support aggregations, operators, and metric functions to create business-specific KPIs.

For details on creating and managing custom metrics, see:

* [Custom Metrics Guide](https://docs.fiddler.ai/observability/platform/custom-metrics)
* [CustomMetric SDK Reference](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-python-client-sdk/entities/custom-metric)
* [Custom Metrics REST API](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/rest-api/rest-api/custom-metrics)

## Related resources

* [LLM Observability Metrics Reference](https://docs.fiddler.ai/reference/llm-observability-metrics) — Enrichments for LLM application monitoring
* [Performance Tracking](https://docs.fiddler.ai/observability/platform/performance-tracking-platform) — Performance monitoring workflows
* [Data Drift](https://docs.fiddler.ai/observability/platform/data-drift-platform) — Drift monitoring and analysis
* [Data Integrity](https://docs.fiddler.ai/observability/platform/data-integrity-platform) — Data quality monitoring
* [Custom Metrics Guide](https://docs.fiddler.ai/observability/platform/custom-metrics) — Creating custom metrics with FQL
