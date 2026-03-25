# Source: https://docs.anyscale.com/platform/workspaces/workspaces-large-dataset-best-practices.md

# Best practices for handling large datasets

[View Markdown](/platform/workspaces/workspaces-large-dataset-best-practices.md)

# Best practices for handling large datasets

This guide highlights best practices when using a distributed cluster such as the Anyscale workspace. Understanding the difference between developing locally and using an Anyscale workspace sets the context for these recommendations.

In traditional development, you might:

* Keep all data files alongside your code
* Load entire datasets into memory
* Run everything on a single machine

Anyscale's distributed environment works differently:

* Your code runs across multiple machines called nodes
* The head node orchestrates work across worker nodes
* Data needs to be accessible to all nodes efficiently

## Data storage options: When to use what[​](#data-storage-options-when-to-use-what "Direct link to Data storage options: When to use what")

### Option 1: Working directory of workspace (good for small files)[​](#option-1-working-directory-of-workspace-good-for-small-files "Direct link to Option 1: Working directory of workspace (good for small files)")

For small files such as code, configs, and small datasets, storing directly in your workspace works well:

```
import ray
from ray.data import read_csv

# Reading a small CSV file from workspace.
dataset = read_csv("/home/ray/default/data/small_config.csv")
```

The working directory of a workspace is typically best for:

* Configuration files
* Small datasets (up to a few hundred MB)
* Temporary results
* Quick experiments

The following are considerations for choosing workspace storage:

* Workspace storage limits depend on your cluster configuration.
* Anyscale snapshots all files every 5 minutes (unless ignored).
* Add large or temporary files to `.anyscaleignore` to prevent snapshot bloat.
* For persistence, Ray packs the default working directory with a limit of \~10GB.
* For task submission, Ray packs the CURRENT working directory, and the limit is 500MiB. This is a Ray Core limit.

```
  # .anyscaleignore
  temp_results/
  *.tmp
  intermediate_data/
```

### Cloud object storage (best for larger datasets)[​](#cloud-object-storage-best-for-larger-datasets "Direct link to Cloud object storage (best for larger datasets)")

For workloads with substantial data, use object storage:

```
import ray
from ray.data import read_parquet

# Reading from cloud storage.
dataset = read_parquet("s3://your-bucket/large-dataset/")
```

Cloud object storage is typically best for:

* Large datasets (GB or TB scale)
* Data that needs to persist beyond workspace lifecycle
* Shared datasets used by multiple workspaces
* Production pipelines

note

New Anyscale clouds use cloud object storage by default for shared storage locations.

Shared storage locations on cloud object storage are convenient for storing data files of any scale, but lack security controls for sensitive data. See [Security considerations](/storage/shared.md#security).

### NFS storage[​](#nfs-storage "Direct link to NFS storage")

note

This section describes NFS storage behavior for legacy Anyscale cloud deployments. NFS storage is now optional for all Anyscale clouds and off by default.

NFS provides shared storage that all nodes can access:

```
# Reading from NFS storage
dataset = read_csv("/mnt/cluster_storage/medium_dataset.csv")
```

NFS storage is typically best for:

* Medium-sized datasets (up to 10GB)
* Files shared across workspaces, jobs, or services
* Development and iteration workflows
* Temporary storage of model weights
* Scenarios where object storage setup isn't necessary

The following are considerations for choosing NFS:

* Performance may degrade with high disk I/O operations
* Access from /mnt/cluster\_storage on all nodes
* Better suited for development than production workloads

## Common pitfalls[​](#common-pitfalls "Direct link to Common pitfalls")

### Pitfall 1: Memory limitations[​](#pitfall-1-memory-limitations "Direct link to Pitfall 1: Memory limitations")

**Problem**: Loading a large dataset into the head node memory.

```
# DON'T DO THIS with large datasets.
import pandas as pd
df = pd.read_csv("/home/ray/default/huge_dataset.csv")  # Could crash your workspace.
```

**Solution**: Use Ray Data to stream and process data.

```
# DO THIS instead.
import ray
from ray.data import read_csv
dataset = read_csv("s3://your-bucket/huge_dataset.csv")
```

### Pitfall 2: Workspace snapshot limits[​](#pitfall-2-workspace-snapshot-limits "Direct link to Pitfall 2: Workspace snapshot limits")

**Problem**: Including large temporary files in snapshots.

```
# This generates a large file that Anyscale includes in snapshots.
with open("/home/ray/default/large_temp_file.dat", "wb") as f:
    f.write(b"\0" * 5_000_000_000)  # 5GB file
```

**Solution**: Use `.anyscaleignore` or store in the object storage.

```
# In .anyscaleignore
large_temp_file.dat
```

### Pitfall 3: Data transfer bottlenecks[​](#pitfall-3-data-transfer-bottlenecks "Direct link to Pitfall 3: Data transfer bottlenecks")

**Problem**: Transferring data from head to workers in inefficient ways.

```
# DON'T DO THIS with large data.
@ray.remote
def process(data):
    # Data gets serialized and sent to each worker.
    return process_func(data)

big_data = load_big_dataset()  # On the head node.
futures = [process.remote(big_data) for _ in range(10)]  # Copies sent to each worker.
```

**Solution**: Use Ray Data for efficient distribution.

```
# DO THIS instead.
dataset = ray.data.read_parquet("s3://your-bucket/data/")
processed = dataset.map_batches(process_func)
```

## Conclusion[​](#conclusion "Direct link to Conclusion")

* Small files can live in your workspace-just manage them with `.anyscaleignore`
* Larger datasets belong in cloud object storage
* Let Ray Data handle the heavy lifting of distributed data processing
