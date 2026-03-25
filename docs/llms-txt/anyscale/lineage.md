# Source: https://docs.anyscale.com/lineage.md

# Lineage tracking

[View Markdown](/lineage.md)

# Lineage tracking

This page explains how to enable and use lineage tracking to trace datasets and models across your Anyscale workloads.

note

Lineage tracking is in private beta. Contact [Anyscale support](mailto:support@anyscale.com) to enable it for your organization.

## What is lineage tracking?[​](#what-is-lineage-tracking "Direct link to What is lineage tracking?")

Anyscale lineage tracking is an observability feature to trace relationships between artifacts and Anyscale workloads.

Lineage tracking *artifacts* are datasets and models your Anyscale workloads produce or consume. Lineage tracking focuses primarily on understanding upstream and downstream relationships relative to artifacts, but also provides insight into all artifacts produced or consumed by workloads.

Explore relationships between workloads and artifacts using an interactive lineage graph in the Anyscale Console.

Example use cases for lineage tracking include the following:

* **Reproduce runs**: Trace a model or dataset back to the exact job, inputs, and environment that produced it.
* **Debug pipelines**: Identify which upstream jobs produced a problematic artifact or which downstream services consume it.
* **Assess impact**: See what depends on an artifact before you modify or delete it.
* **Meet audit requirements**: Maintain a complete record of artifact provenance for compliance.

## How lineage tracking works[​](#how-it-works "Direct link to How lineage tracking works")

Anyscale lineage tracking builds on the OpenLineage standard, with lineage plugins for Ray Data and MLflow. These plugins load into workloads at runtime and emit OpenLineage events when you read or write data and when you log or load models.

You enable lineage tracking at the Anyscale cloud level. Anyscale captures lineage metadata for all workloads in enabled clouds that use supported APIs.

note

Anyscale lineage tracking requires Ray initialization. While most workloads don't require any code changes to support lineage tracking, you might need to run `ray.init()` in MLflow workloads before initializing experiments and runs.

Anyscale stores lineage metadata in the control plane and displays relationships through the Anyscale console. See [View lineage in the Anyscale Console](#console).

## Requirements[​](#requirements "Direct link to Requirements")

Lineage tracking has the following requirements:

* You must enable lineage tracking at the organization and cloud level containing the workload.

* You must use an Anyscale base image with Ray version 2.53.0 or later.

* MLflow support requires version 2.19.0 or later.

* Anyscale supports lineage tracking for **Ray Data** and **MLflow** workloads only.

* You must initialize Ray before Anyscale can capture lineage metadata.

  <!-- -->

  * For Ray Data workloads, Ray initializes implicitly in most cases.
  * For MLflow workloads, initialize Ray before you create experiments or runs.

## Enable lineage tracking[​](#enable "Direct link to Enable lineage tracking")

You must enable lineage tracking for your organization before you can enable it for a cloud. To enable it for your organization, contact [Anyscale support](mailto:support@anyscale.com).

You must be an organization owner to enable lineage tracking for an Anyscale cloud.

To enable lineage tracking for a cloud:

1. Click your user icon.
2. Click **Clouds**.
3. Click the name of your cloud.
4. Click **Settings**.
5. Under **Platform services > Lineage tracking**, toggle the switch.

note

When you enable lineage tracking, Anyscale doesn't capture lineage for clusters that are already running or have terminated. Restart or redeploy your workloads to capture lineage information.

When you turn off lineage tracking, Anyscale stops capturing lineage for new clusters, but continues capturing lineage for running clusters until they terminate.

## Datasets[​](#datasets "Direct link to Datasets")

Anyscale captures lineage metadata for datasets read or written using supported Ray Data APIs. You explore lineage for tracked datasets using the **Datasets** page in the Anyscale Console.

* [Parquet read and write](https://docs.ray.io/en/latest/data/api/input_output.html#parquet)
* [CSV read and write](https://docs.ray.io/en/latest/data/api/input_output.html#csv)
* [JSON read and write](https://docs.ray.io/en/latest/data/api/input_output.html#json)
* [Text read](https://docs.ray.io/en/latest/data/api/input_output.html#text)
* [Audio read](https://docs.ray.io/en/latest/data/api/input_output.html#audio)
* [Avro read](https://docs.ray.io/en/latest/data/api/input_output.html#avro)
* [Images read and write](https://docs.ray.io/en/latest/data/api/input_output.html#images)
* [Binary read](https://docs.ray.io/en/latest/data/api/input_output.html#binary)
* [TFRecords read and write](https://docs.ray.io/en/latest/data/api/input_output.html#tfrecords)
* [Video read](https://docs.ray.io/en/latest/data/api/input_output.html#video)
* [WebDataset read](https://docs.ray.io/en/latest/data/api/input_output.html#webdataset)

note

Contact [Anyscale support](mailto:support@anyscale.com) to request coverage for other [Ray Data Input/Output APIs](https://docs.ray.io/en/latest/data/api/input_output.html) or new data sources.

The dataset naming follows the [OpenLineage convention](https://openlineage.io/docs/spec/naming/). In addition to name, the page shows dataset type, dataset URI, the datetime when Anyscale logged the dataset, and the user who created it. Anyscale infers the dataset type from metadata or file extension when available. Use the **Created by** filter to filter by user email, or the breadcrumb menu to filter by cloud and project.

Click a dataset name to see the detailed view, where you can view **Related workloads** and **Lineage**.

## Models[​](#models "Direct link to Models")

Anyscale automatically tracks models and artifacts logged or loaded using the following MLflow APIs:

* [mlflow.\<model-flavor>.load\_model](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.sklearn.html#mlflow.sklearn.load_model)
* [mlflow.\<model-flavor>.log\_model](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model)
* [mlflow.register\_model](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.register_model)
* [mlflow.log\_artifact](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=log_artifact#mlflow.log_artifact)
* [mlflow.log\_artifacts](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=log_artifact#mlflow.log_artifacts)
* [mlflow.artifacts.download\_artifacts](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.artifacts.html?highlight=download_artifact#mlflow.artifacts.download_artifacts)

The lineage metadata for these models and artifacts appears on the **Models** page.

Click a model name to see the detailed view, where you can view **Related workloads** and **Lineage**.

## View lineage in the Anyscale Console[​](#console "Direct link to View lineage in the Anyscale Console")

You interact with lineage information through the Anyscale console using the following interfaces:

| Interface         | Description                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Datasets          | Click **Datasets** in the console sidebar to see a list of datasets with lineage information.                                                                         |
| Models            | Click **Models** in the console sidebar to see a list of the models with lineage information.                                                                         |
| Artifact overview | Click on the name of a dataset or model to view the artifact overview page. This includes [artifact metadata](#metadata) and [related workloads](#related-workloads). |
| Lineage graph     | From the artifact overview, click **Lineage** to see the [lineage graph](#lineage-graph).                                                                             |
| Related artifacts | Each job, service, or workspace overview page provides a quick view for [related artifacts](#related-artifacts).                                                      |

### Lineage graph[​](#lineage-graph "Direct link to Lineage graph")

Click **Lineage** to view an expandable lineage graph for your artifact.

The default view shows the workloads directly related to the dataset or model as an upstream dependency or downstream consumer.

Nodes with a plus sign (**+**) have additional lineage information available. Click the plus sign to expand your lineage graph.

### Related workloads[​](#related-workloads "Direct link to Related workloads")

The dataset or model **Overview** page displays the **Related workloads** view. Here you can see all the **Upstream** producers and **Downstream** consumers of a given dataset or model.

Click a workload name to open the **Overview** page for that job, service, or workspace.

### Related artifacts[​](#related-artifacts "Direct link to Related artifacts")

Enabling lineage tracking adds the **Related artifacts** field to workload overview pages in the Anyscale console. The field shows the count of tracked upstream and downstream artifacts. Click the field to view summary details for each artifact. Click on a artifact name to navigate to the overview page for that dataset or model.

## Artifact lineage metadata[​](#metadata "Direct link to Artifact lineage metadata")

Anyscale captures and displays the following metadata for each dataset:

* Name
* URI
* File format

note

Anyscale attempts to infer and collect input and output schema metadata for supported datasets.

For models, Anyscale captures the model ID and URI.

note

Anyscale records and displays all lineage information for artifacts that MLflow consumes or creates as **Models**, although these artifacts can be files of any arbitrary type, including datasets.

You must read and write datasets using supported Ray Data APIs for their lineage information to appear as **Datasets** in the Anyscale console.

Each lineage entry displays the creation time for the lineage record and the identity of the user running the workload that created the lineage record.

### Dataset naming[​](#naming "Direct link to Dataset naming")

Anyscale uses the OpenLineage naming conventions when working with data stored in external sources such as cloud object storage. See the docs page for [OpenLineage dataset naming conventions](https://openlineage.io/docs/spec/naming/).

note

Anyscale only provides lineage tracking for data read or written with supported APIs. Anyscale doesn't support lineage tracking for some data sources supported by OpenLineage.

Datasets stored in Anyscale shared storage use the relative path for the dataset name. The URI provides the full ID for workload or cloud resource, allowing you to differentiate datasets that use the same relative path for cluster storage. The following table describes this behavior:

| Dataset name             | URI                                                        | Description                                                                                                    |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `/mnt/cluster_storage/*` | `file://<anyscale-workload-id>/mnt/cluster_storage/*`      | For each job, service, and workspace, Anyscale creates a directory in shared storage for persisting artifacts. |
| `/mnt/shared_storage/*`  | `file://<anyscale-cloud-resource-id>/mnt/shared_storage/*` | For each Anyscale cloud resource, Anyscale creates a directory in shared storage.                              |

Anyscale doesn't support lineage for the `/mnt/user_storage/` directory. See [Storage paths and scoping](/storage/shared.md#paths).

## Workload lineage metadata[​](#workload-details "Direct link to Workload lineage metadata")

Anyscale records the following workload metadata for lineage tracking:

* Workload type: job, service, or workspace
* Workload name
* Workload ID
* Organization ID
* Cloud ID
* Project ID
* Owner email
* Ray version
* Python version
* Operating system version

## Lineage tracking examples[​](#example "Direct link to Lineage tracking examples")

Anyscale automatically tracks lineage for supported operations for all workloads in clouds with lineage tracking enabled. The following examples demonstrate lineage tracking for a dataset and model.

* Ray Data
* MLflow

You must use supported Ray Data APIs to capture lineage for datasets on Anyscale.

The following example uses Ray Data to consume an image from a public S3 bucket. The code doesn't create a new dataset, so the lineage graph only shows the read relationship between your Anyscale workload and the source dataset:

```
import ray

ds = ray.data.read_images(
    "s3://doggos-dataset/train",
    include_paths=True,
    shuffle="files",
)

def add_class(row):
    row["class"] = row["path"].rsplit("/", 3)[-2]
    return row

ds = ds.map(add_class)

# You must materialize results to emit lineage information.
ds.materialize()

print(ds.schema())
```

Anyscale captures lineage metadata for models logged or loaded through MLflow APIs.

note

You must initialize Ray before you create your experiments or runs to collect lineage.

Run the following code to create lineage entities for a model logged with `mlflow.pytorch.log_model`:

```
import os
import shutil

import mlflow
import ray
import torch
import torch.nn as nn

# You must initialize Ray before creating MLflow experiments and runs.
ray.init(ignore_reinit_error=True)

EXPERIMENT_NAME = "doggos"
MODEL_REGISTRY = "/mnt/cluster_storage/mlflow/doggos"
ARTIFACT_LOCATION = f"{os.getenv('ANYSCALE_ARTIFACT_STORAGE')}/mlflow/doggos"

if os.path.isdir(MODEL_REGISTRY):
    shutil.rmtree(MODEL_REGISTRY)
os.makedirs(MODEL_REGISTRY, exist_ok=True)
    
mlflow.set_tracking_uri(f"file:{MODEL_REGISTRY}")

mlflow.create_experiment(
    EXPERIMENT_NAME,
    artifact_location=ARTIFACT_LOCATION,
)

class SimpleNet(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=16, output_dim=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)

mlflow.set_experiment(experiment_name=EXPERIMENT_NAME)

with mlflow.start_run() as run:
    model = SimpleNet()
    artifact_path = "simple_pytorch_model"
    mlflow.pytorch.log_model(
        pytorch_model=model,
        artifact_path=artifact_path,
    )
```

## Turn off lineage plugins[​](#turn-off-plugins "Direct link to Turn off lineage plugins")

To turn off lineage tracking for a workload, set the `ANYSCALE_LINEAGE_TRACKING_ENABLED` environment variable before Ray initializes:

```
export ANYSCALE_LINEAGE_TRACKING_ENABLED="false"
```

## Enable debug logging[​](#debug-logging "Direct link to Enable debug logging")

To enable debug logging for lineage tracking, set the `ANYSCALE_LINEAGE_LOG_LEVEL` and `ANYSCALE_LINEAGE_IGNORE_ERRORS` environment variables before Ray initializes:

```
export ANYSCALE_LINEAGE_LOG_LEVEL="DEBUG"
export ANYSCALE_LINEAGE_IGNORE_ERRORS="false"
```

You can then share error snippets or debug logs with Anyscale support for troubleshooting.
