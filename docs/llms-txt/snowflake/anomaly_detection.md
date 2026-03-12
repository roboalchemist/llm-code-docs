# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly_detection.md

# ANOMALY_DETECTION (SNOWFLAKE.ML)

Anomaly detection allows you to detect outliers in your time series data by using a machine learning algorithm. You use [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](anomaly-detection/commands/create-anomaly-detection.md) to create
and train a detection model, and then use the [<model_name>!DETECT_ANOMALIES](anomaly-detection/methods/detect_anomalies.md) method to detect anomalies.

> **Important:**
>
> **Legal notice.** This Snowflake ML function is powered by machine learning technology, which you, not Snowflake, determine when and how to use. Machine
> learning technology and results provided may be inaccurate, inappropriate, or biased.
> Snowflake provides you with the machine learning models that you can use within your own workflows. Decisions based on machine
> learning outputs, including those built into automatic pipelines, should have human oversight and review processes
> to ensure model-generated content is accurate.
> Snowflake provides algorithms (without any pretraining) and you’re responsible for the data that you provide the algorithm (for example, for training and inference) and the decisions you make using the resulting model’s output.
> Queries for this feature or function are treated as any
> other SQL query and may be considered [metadata](../metadata.md).
>
> **Metadata.** When you use Snowflake ML functions, Snowflake logs generic error messages returned by an ML
> function. These error logs help us troubleshoot issues that arise and improve these functions to serve you better.
>
> For further information, see [Snowflake AI Trust and Safety FAQ](https://www.snowflake.com/en/legal/snowflake-ai-trust-and-safety/).

## ANOMALY_DETECTION commands

* [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](anomaly-detection/commands/create-anomaly-detection.md)
* [DROP SNOWFLAKE.ML.ANOMALY_DETECTION](anomaly-detection/commands/drop-anomaly-detection.md)
* [SHOW SNOWFLAKE.ML.ANOMALY_DETECTION](anomaly-detection/commands/show-anomaly-detection.md)

## ANOMALY_DETECTION methods

* [<model_name>!DETECT_ANOMALIES](anomaly-detection/methods/detect_anomalies.md)
* [<model_name>!EXPLAIN_FEATURE_IMPORTANCE](anomaly-detection/methods/explain_feature_importance.md)
* [<model_name>!SHOW_EVALUATION_METRICS](anomaly-detection/methods/show_evaluation_metrics.md)
* [<model_name>!SHOW_TRAINING_LOGS](anomaly-detection/methods/show_training_logs.md)
