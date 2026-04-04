# Source: https://docs.aporia.com/dashboards/overview.md

# Source: https://docs.aporia.com/data-sources/overview.md

# Source: https://docs.aporia.com/storing-your-predictions/overview.md

# Source: https://docs.aporia.com/v1/data-sources/overview.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/overview.md

# Overview

**Monitoring your Machine Learning models begins with storing their inputs and outputs in production.**&#x20;

Oftentimes, this data is used not just for model monitoring, but also for retraining, auditing, and other purposes; therefore, it is crucial that you have complete control over it.

Aporia monitors your models by connecting directly to *your* data, in *your* format. This section discusses the fundamentals of storing model predictions.

{% hint style="info" %}
If you are not storing your predictions today, you can also [log your predictions directly to Aporia](https://docs.aporia.com/v1/storing-your-predictions/logging-to-aporia-directly), although storing your predictions in your own database is highly recommended.
{% endhint %}

### Storage

Depending on your existing enterprise data lake infrastructure, performance requirements, and cloud costs constraints, storing your predictions can be done in a variety of data stores.

Here are some common options:

* [BigQuery](https://cloud.google.com/bigquery)
* [Delta Lake](https://delta.io/) / [Databricks Lakehouse](https://www.databricks.com/)
* [Snowflake](https://www.snowflake.com/)
* [Elasticsearch](https://www.elastic.co/) / [OpenSearch](https://opensearch.org/)
* Parquet files on S3 / GCS / ABS
  * If you choose this option, a metastore such as [Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) is recommended.

### Directory Structure

When storing your predictions, it's highly recommended to adopt a standardized directory structure (or SQL table structure) across all of your organization's models.

With a standardized structure, you'll be able to get all models onboarded to the monitoring system automatically.

Here is a very basic example:

```
s3://myorg-models/
├── my-model/
    ├── v1/
    │   ├── train.parquet
    │   ├── test.parquet
    │   ├── serving.parquet
    │   ├── artifact.onnx
    ├── v2/
    │   ├── train.parquet
    │   ├── test.parquet
    │   └── serving.parquet
    │   └── artifact.onnx
```

{% hint style="info" %}
Even though this section focuses on the storage of *predictions*, you should also consider saving the **training** and **test sets** of your models. They can serve as a monitoring baseline.&#x20;
{% endhint %}

### Data Structure

Recommendations:

* One row per prediction.
* One column per feature, prediction or raw input.
* Use a prefix for column names to identify their group (e.g `features.`, `raw_inputs.`, `predictions.`, `actuals.`, etc.)
* For serving, add ID and prediction timestamp columns.

Example:

```
+-----+----------------------+-------------------+---------------+----------------+-------------------+-------------------------+--------------+----------------------+------------------------+
| id  |      timestamp       | predictions.score | actuals.score | raw_inputs.age | raw_inputs.gender | features.my_embeddings  | features.age | features.gender_male | features.gender_female |
+-----+----------------------+-------------------+---------------+----------------+-------------------+-------------------------+--------------+----------------------+------------------------+
|   1 | 2022-10-19T14:21:08Z |              0.58 |          0.59 |             64 | male              | [0.58, 0.19, 0.38, ...] |           64 |                    1 |                      0 |
|   2 | 2022-10-19T14:21:08Z |              0.64 |          0.66 |             62 | woman             | [0.48, 0.20, 0.42, ...] |           62 |                    0 |                      1 |
| ... | ...                  |               ... |           ... |            ... | ...               | ...                     |          ... |                  ... |                    ... |
+-----+----------------------+-------------------+---------------+----------------+-------------------+-------------------------+--------------+----------------------+------------------------+
```
