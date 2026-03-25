# Source: https://docs.anyscale.com/storage/local.md

# Local storage on Anyscale

[View Markdown](/storage/local.md)

# Local storage on Anyscale

This page provides an overview of local storage on Anyscale.

## What is local storage?[​](#what-is "Direct link to What is local storage?")

Local storage provides high-performance block storage attached directly to each node in your Anyscale cluster. You access local storage at `/mnt/local_storage`. Each node has its own local storage that isn't shared with other nodes.

important

Local storage is ephemeral. All data stored in `/mnt/local_storage` is permanently deleted when the cluster terminates. For persistent storage, use shared storage paths or cloud object storage.

## Configuration options[​](#configuration "Direct link to Configuration options")

Configuration options differ by deployment type.

### VM stack[​](#vm-stack "Direct link to VM stack")

When using the VM stack on AWS or Google Cloud, you can configure block storage settings in your compute configuration. The specific options vary by cloud provider.

#### AWS block storage[​](#aws-block-storage "Direct link to AWS block storage")

Configure EBS volumes with options for volume type, volume size, performance settings, and instance storage options. See [AWS block storage settings](/configuration/compute/aws.md#disk-size).

#### Google Cloud block storage[​](#google-cloud-block-storage "Direct link to Google Cloud block storage")

Configure persistent disks with options for disk type, disk size, and local SSD options. See [Google Cloud block storage settings](/configuration/compute/gcp.md#disk-size).

#### NVMe storage[​](#nvme-storage "Direct link to NVMe storage")

For workloads with intensive I/O requirements, Anyscale supports Non-Volatile Memory Express (NVMe) instance storage. NVMe provides low latency and high throughput, and is available on instance types with local NVMe drives. Anyscale automatically mounts NVMe storage at `/mnt/local_storage`.

Anyscale recommends configuring NVMe storage for workloads that rely on any of the following:

* Frequent random reads and writes.
* Large datasets that don't fit in memory.
* Sustained high IOPS.
* Extensive Ray object spilling.

### Kubernetes stack[​](#k8s-configuration "Direct link to Kubernetes stack")

Your Kubernetes administrator controls local storage configuration through instance type settings and Helm chart configuration. Anyscale uses ephemeral volumes with the disks configured for your machine types.

## How Ray uses local storage[​](#ray-usage "Direct link to How Ray uses local storage")

Ray automatically uses local storage for logs, temporary files, and session data. By default, Ray stores these files in the Ray session directory (for example, `/tmp/ray/session_latest/`). On Anyscale, you can configure Ray to use `/mnt/local_storage` for better performance.

## Configure Ray object spilling[​](#object-spilling "Direct link to Configure Ray object spilling")

Use local storage for object spilling to improve performance when the object store is full. By default, Ray spills objects to the temporary directory, but configuring object spilling to use `/mnt/local_storage` provides better I/O performance.

The following example configures object spilling:

```
import ray

# Configure object spilling to use local storage
ray.init(object_spilling_directory="/mnt/local_storage/spill")
```

## Stage checkpoints before uploading[​](#checkpoint-staging "Direct link to Stage checkpoints before uploading")

Use local storage as temporary staging for checkpoints before uploading to persistent storage. This pattern improves training performance by saving checkpoints to fast local storage first, then uploading to cloud storage asynchronously.

The following example demonstrates the checkpoint staging pattern:

```
import tempfile
from ray.train import Checkpoint
import ray.train

def train_fn(config):
    for epoch in range(10):
        # Training logic
        metrics = {"loss": ...}
        
        # Save checkpoint to temporary local directory
        with tempfile.TemporaryDirectory() as temp_checkpoint_dir:
            model.save(temp_checkpoint_dir)
            # Ray Train uploads to persistent storage automatically
            ray.train.report(
                metrics,
                checkpoint=Checkpoint.from_directory(temp_checkpoint_dir)
            )
```

warning

For multi-node Ray clusters, don't use local storage for the `storage_path` parameter in `RunConfig`. Use cloud object storage (S3, Azure blob storage, GCS) or shared storage (`/mnt/cluster_storage`) instead. Ray Train requires all workers to access the same persistent storage location for checkpoints.
