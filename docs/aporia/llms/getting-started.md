# Source: https://docs.aporia.com/ml-monitoring-as-code/getting-started.md

# Getting started

{% hint style="info" %}
**BETA FEATURE**

**The monitoring-as-code is in experimental beta and details may change**
{% endhint %}

Aporia's Python SDK is a powerful tool designed to streamline ML monitoring and observability.

Define your models, monitors, dashboards, segments, custom metrics, and other ML Observability resources *as code*, just like in Terraform or Pulumi. The SDK also enables you to query metrics from Aporia to integrate with other platforms.

## Key Features

* **ML Monitoring as Code:** Make it easier to manage and track changes by managing your models, dashboards, segments, and other ML Observability resources as code.
* **CI/CD Integration:** Integrate with your CI/CD pipeline to automatically monitor all your models with Aporia.
* **Query Metrics:** Fetch metrics directly from Aporia's platform to inform decisions or to use in other applications.
* **Data Source Integration:** You can define and integrate multiple types of data sources, like S3, Snowflake, Glue Data Catalog, Databricks, and others. This allows your models to leverage a wide range of data for training and inference.
* **Pythonic Interface:** Use the familiar Python programming paradigm to interact with Aporia.

## Installation

You can install the Aporia SDK using pip:

```python
pip install aporia --upgrade
```

Please make sure you have Python 3.8+.

## Use-cases

### Define models as code

A common use-case of the SDK is to define models, monitors, dashboards, custom metrics and other Aporia resources as code.

```python
import datetime
import os

from aporia import Aporia, MetricDataset, MetricParameters, TimeRange
import aporia.as_code as aporia

aporia_token = os.environ["APORIA_TOKEN"]
aporia_account = os.environ["APORIA_ACCOUNT"]
aporia_workspace = os.environ["APORIA_WORKSPACE"]

stack = aporia.Stack(
    token=aporia_token,
    account=aporia_account,
    workspace=aporia_workspace,
)

# Your model definition code goes here

stack.apply(yes=True, rollback=False, config_path="config.json")

```

Similarly to frameworks like Pulumi and Terraform, resources are defined ***declaratively***. This means that if you run the script twice, models or monitors won't be created twice.&#x20;

Instead, the SDK diffs the current state vs. the desired state, and make sure to apply changes in Aporia. This is especially useful if you have a CI/CD pipeline to deploy models to staging / production, you can also add the model to Aporia for monitoring as an additional step.&#x20;

{% hint style="info" %}
If you are using Aporia's European cluster, please make sure to add the following argument:

`aporia.Stack(host="https://platform-eu.aporia.com", ...)`
{% endhint %}

### Query Metrics using the SDK

This example shows how you can use the Aporia SDK to query metrics from a model. It can be used to integrate data from Aporia to your internal systems:

```python
from datetime import datetime
from aporia import (
    Aporia,
    MetricDataset,
    MetricParameters,
    TimeRange,
    DatasetType,
)

aporia_token = os.environ["APORIA_TOKEN"]
aporia_account = os.environ["APORIA_ACCOUNT"]
aporia_workspace = os.environ["APORIA_WORKSPACE"]

aporia_client = Aporia(
    token=aporia_token,
    account_name=aporia_account,
    workspace_name=aporia_workspace,
)

last_week_dataset = MetricDataset(
    dataset_type=DatasetType.SERVING,
    time_range=TimeRange(
        start=datetime.now() - datetime.timedelta(days=7),
        end=datetime.now(),
    ),
)

metrics = aporia_client.query_metrics(
    model_id=model_id,
    metrics=[
        MetricParameters(
            dataset=MetricDataset(dataset_type=DatasetType.SERVING),
            name="count",
        ),
    ],
)

print(f"The model had {metrics[0]} predictions last week")

```

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><a href="adding-new-models"><strong>Adding new models</strong></a></td><td>Monitor models automatically by creating models in Aporia and connecting them to your data.</td><td></td></tr><tr><td><a href="data-segments"><strong>Data Segments</strong></a></td><td>Automatically monitor various slices of the data in production.</td><td></td></tr><tr><td><a href="custom-metrics"><strong>Custom Metrics</strong></a></td><td>Extend Aporia's monitoring capabilities by adding your own custom metrics.</td><td></td></tr><tr><td><a href="querying-metrics"><strong>Querying metrics</strong></a></td><td>Use the SDK to fetch metrics from Aporia and bridge ML Observability with other systems in your organization.</td><td></td></tr></tbody></table>
