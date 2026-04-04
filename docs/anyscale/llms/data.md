# Source: https://docs.anyscale.com/runtime/data.md

# Ray Data

[View Markdown](/runtime/data.md)

# Ray Data

[Ray Data](https://docs.ray.io/en/latest/data/data.html) is an open-source scalable data processing library designed for machine learning workloads. Ray Data provides flexible and performant APIs for distributed data processing and uses streaming execution to efficiently process large datasets. It's particularly suited for offline batch inference and data preprocessing and ingest for ML training.

The Anyscale Runtime provides optimizations and additional features on top of Ray Data that improve performance and production reliability for unstructured data processing such as images, video, and audio. The Anyscale Runtime includes both user-configurable features and automatic optimizations that work without configuration.

Key features include the following:

* Improved autoscaling.
* Job-level checkpointing.
* Proactive issue detection.
* Automatic performance optimizations.

## Improved autoscaling[​](#autoscaling "Direct link to Improved autoscaling")

The Anyscale Runtime provides an enhanced autoscaling implementation that delivers more responsive scaling for data processing workloads.

The actor pool autoscaler enables jobs to start immediately without waiting for the full cluster to launch by dynamically scaling the number of actors within the cluster. Actor pools scale up aggressively when utilization is high and scale down gradually when work completes. This allows jobs to adapt quickly to changing resource availability and handle node preemptions gracefully by continuing execution with fewer workers.

Actor pool autoscaling works with the cluster autoscaler. See [Worker nodes scaling config](/configuration/compute.md#scaling).

## Job-level checkpointing[​](#checkpointing "Direct link to Job-level checkpointing")

Open source Ray Data fault tolerance can recover from worker failures, retrying tasks that failed. However, it doesn't support checkpointing the entire job, which is useful for handling failure scenarios such as:

* Driver, head node, or entire cluster failures.
* Unexpected exceptions, for example, rows with malformed values trigger unhandled exceptions in the UDF.

Ray Data in the Anyscale Runtime offers job-level checkpointing to checkpoint the job execution progress. When a job fails, the restarted job can resume from the previous state without reprocessing already-completed data.

### When to use job-level checkpointing[​](#when-to-use-job-level-checkpointing "Direct link to When to use job-level checkpointing")

Job-level checkpointing is particularly valuable for the following:

* Long-running batch inference jobs on spot instances with potential preemption.
* Processing petabyte-scale datasets where restarting from the beginning is costly.
* Pipelines processing data with quality issues that might trigger occasional exceptions.
* Jobs running on infrastructure with reliability concerns.

### Limitations[​](#limitations "Direct link to Limitations")

warning

Passing the `override_num_blocks` parameter to a Ray Data read API turns off all Anyscale Runtime optimizations. Omit this parameter from your Anyscale code to make sure you're using built-in optimizations.

warning

A known bug exists that in some retries after failure, job-level checkpointing might produce duplicate outputs. Contact [Anyscale support](mailto:support@anyscale.com) if you encounter this issue.

This feature supports only datasets with the following characteristics:

* Start with a read operation.
* End with a write operation.
* Contain only map-based operators such as `map`, `map_batches`, `filter`, and `flat_map`.
* Don't use aggregations, joins, or other operators that shuffle or combine data across partitions.

### Enable job-level checkpointing[​](#enable-job-level-checkpointing "Direct link to Enable job-level checkpointing")

To enable checkpointing, do the following:

1. Set `DataContext.checkpoint_config` for the dataset.
2. Set an ID column with the `id_column` config to uniquely identify each row. This column must not change across the entire job.

```
from ray.anyscale.data.checkpoint import CheckpointConfig

DataContext.get_current().checkpoint_config =  CheckpointConfig(
    id_column="id",
    checkpoint_path="s3://my_bucket/checkpoint",
)

ds = ray.data.read_parquet("...")
ds = ds.map(...)
ds.write_parquet("...")
```

### Configuration options[​](#config-options "Direct link to Configuration options")

Configurable attributes include:

* `id_column` (str): Name of the ID column in the input dataset. ID values must be unique across all rows in the dataset and must not change across the entire job.

* `checkpoint_path` (str): Path to store the checkpoint data. It can be a path to a cloud object storage such as `s3://bucket/path`, or a file system path. If the latter, the path must be a network-mounted file system such as `/mnt/cluster_storage/` that's accessible to the entire cluster. If not set, defaults to `${ANYSCALE_ARTIFACT_STORAGE}/ray_data_checkpoint`.

Additional attributes for advanced usages:

* `delete_checkpoint_on_success` (bool): If true, automatically deletes checkpoint data when the dataset execution succeeds. True by default.

* `override_filesystem` (`pyarrow.fs.FileSystem`): Overrides the `pyarrow.fs.FileSystem` object used to read or write checkpoint data. Set this option to use custom credentials.

* `override_backend` (CheckpointBackend): Overrides the CheckpointBackend object used to access the checkpoint backend storage. Set this option only if you want to use the row-based checkpoint backends. By default, the Anyscale Runtime uses batch-based backends.

## Proactive issue detection[​](#issue-detection "Direct link to Proactive issue detection")

The Anyscale Runtime includes a proactive issue detection system that monitors Ray Data pipelines for common problems before they cause failures. This system helps prevent pipeline failures by detecting issues early and emitting warnings that help you identify and resolve problems.

The issue detection system automatically monitors for the following:

* **Hanging operators**: Detects operators that stop making progress, which can indicate deadlocks or resource starvation.
* **High memory usage**: Identifies operators consuming excessive memory before out-of-memory failures occur.

The system runs by default and requires no configuration. When the system detects issues, it emits warnings with operator-specific context to help you diagnose the problem.

### Turn off issue detection[​](#turn-off-issue-detection "Direct link to Turn off issue detection")

To turn off issue detection, configure the `DataContext`:

```
from ray.data import DataContext

# Disable all issue detectors
ctx = DataContext.get_current()
ctx.issue_detectors_config.detectors = []
```

## Automatic optimizations[​](#automatic-optimizations "Direct link to Automatic optimizations")

Beyond the features described in this document, the Anyscale Runtime includes numerous automatic optimizations for Ray Data that work without configuration. These optimizations improve performance, reduce memory usage, and enhance reliability across a wide range of data processing workloads.

The Anyscale Runtime applies the following optimizations automatically:

* **Intelligent autoscaling & resource allocation**: Automatically allocating resources for operations to maximize throughput while maintaining high utilization & efficiency.
* **Vectorized operations**: Uses optimized vectorized implementations for common ops like aggregations, substantially accelerating them by reducing runtime overhead.
* **Advanced query planning & optimizations**: Optimizes execution plans for complex data pipelines through operator & transformations fusion.
* **Enhanced data sources/sinks performance**: Provides optimized readers & writers for various file formats and cloud storage systems with intelligent file splitting to maximize throughput.
* **Highly optimized partitioning**: Uses highly optimized implementations of common paths like partitioning to reduce latency and maximize compute efficiency.

The Anyscale Runtime enables these optimizations by default and they require no changes to your code. They complement the user-configurable features to provide comprehensive performance improvements for Ray Data workloads.

## Ray Data dashboard[​](#ray-data-dashboard "Direct link to Ray Data dashboard")

The Data dashboard is a centralized tool for debugging Ray Data workloads. It's a proprietary replacement for the open source data dashboard that enables users to monitor and debug Ray Data workloads more efficiently.

See [Ray Data dashboard](/monitoring/workload-debugging/data-dashboard.md).
