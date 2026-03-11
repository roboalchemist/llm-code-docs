# Source: https://docs.anyscale.com/administration/cloud-deployment/leverage-cloud-tpus-on-kubernetes.md

# Leverage Cloud TPUs on GKE

[View Markdown](/administration/cloud-deployment/leverage-cloud-tpus-on-kubernetes.md)

# Leverage Cloud TPUs on GKE

info

TPUs on Anyscale are only supported on Anyscale operator deployments on Google Kubernetes Engine.

## Overview[​](#overview "Direct link to Overview")

This page describes how to use Cloud TPUs on Anyscale.

Before proceeding, we recommend becoming familiar with [how Cloud TPU works with Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus) and the [terminology related to TPUs in GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology).

This walkthrough has been tested using [GKE Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview). If using GKE Standard, you must ensure that your GKE cluster is properly configured to use Cloud TPUs, which will require [creating one or more TPU node groups](https://cloud.google.com/kubernetes-engine/docs/how-to/tpus).

### Using Single-Host TPUs[​](#using-single-host-tpus "Direct link to Using Single-Host TPUs")

To use single-host TPUs on Anyscale, add an instance type to the Anyscale operator's Helm chart `values.yaml` file as follows. Note that the `resources` may need to be adjusted based on the target TPU topology.

```
workloads:
  instanceTypes:
    additional:
      # This instance type defines a single-host TPU.
      # 
      # Note that the CPU, TPU, and memory values here
      # may be adjusted based on the shape of the TPU
      # and the TPU host.
      8CPU-16GB-TPU-V5E-2x2-SINGLEHOST:
        resources:
          CPU: 8
          TPU: 4
          memory: 16Gi
          accelerators:
            - TPU-V5E
          # This is a hint to Anyscale that this is a single-host deployment.
          'anyscale/tpu_hosts': 1
        nodeSelector:
          cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
          cloud.google.com/gke-tpu-topology: 2x2
          # Force this instance type to always request SPOT instances.
          # TPUs are generally more available on SPOT instances.
          cloud.google.com/gke-spot: "true"
```

Then, use this instance type in an Anyscale workload.

```
# tpu_singlehost_job.yaml
name: tpu_singlehost_job
working_dir: .
entrypoint: python tpu_singlehost.py
compute_config:
  cloud: CLOUD_NAME
  head_node:
    instance_type: 4CPU-16GB
  worker_nodes:
  - instance_type: 8CPU-16GB-TPU-V5E-2x2-SINGLEHOST
    min_nodes: 1
    max_nodes: 1
    market_type: SPOT
```

```
# tpu_singlehost.py
import os
import ray
import jax
import time

from jax.experimental import multihost_utils

ray.init()

@ray.remote(resources={"TPU": 4})
def tpu_cores():
    cores = "TPU cores:" + str(jax.device_count())
    return cores

result = ray.get(tpu_cores.remote())
print(result)
```

```
anyscale job submit -f tpu_singlehost_job.yaml
```

### Using Multi-Host TPUs[​](#using-multi-host-tpus "Direct link to Using Multi-Host TPUs")

To use multi-host TPUs on Anyscale, add an instance type to the Anyscale operator's Helm chart `values.yaml` file as follows. Note that the `resources` may need to be adjusted based on the target TPU topology.

```
workloads:
  instanceTypes:
    additional:
      # This instance type defines a multi-host TPU slice.
      #
      # Note that the CPU, TPU, and memory values here
      # may be adjusted based on the shape of the TPU
      # and the TPU hosts.
      8CPU-16GB-TPU-V5E-4x4-MULTIHOST:
        resources:
          CPU: 8
          TPU: 4
          memory: 16Gi
          accelerators:
            - TPU-V5E
          # Hint to Anyscale that this is a multi-host deployment,
          # and so we need to set the TPU_WORKER_HOSTNAMES environment
          # variable to link together all of the hosts in this TPU slice.
          #
          # Anyscale automatically sets this environment variable on
          # all hosts.
          'anyscale/tpu_hosts': 4
        nodeSelector:
          cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
          cloud.google.com/gke-tpu-topology: 4x4
          # Force this instance type to always request SPOT instances.
          # TPUs are generally more available on SPOT instances.
          cloud.google.com/gke-spot: "true"
```

Then, use this instance type in an Anyscale workload.

```
# tpu_multihost_job.yaml
name: tpu_multihost_job
working_dir: .
entrypoint: python tpu_multihost.py
compute_config:
  cloud: CLOUD_NAME
  head_node:
    instance_type: 4CPU-16GB
  worker_nodes:
  - instance_type: 8CPU-16GB-TPU-V5E-4x4-MULTIHOST
    min_nodes: 4
    max_nodes: 4
    market_type: SPOT
```

```
# tpu_multihost.py
import os
import ray
import jax
import time

from jax.experimental import multihost_utils

ray.init()

@ray.remote(resources={"TPU": 4})
def tpu_cores():
    multihost_utils.sync_global_devices("sync")
    cores = "TPU cores:" + str(jax.device_count())
    print("TPU Worker: " + os.environ.get("TPU_WORKER_ID"))
    return cores

num_workers = int(ray.available_resources()["TPU"]) // 4
print(f"Number of TPU Workers: {num_workers}")
result = [tpu_cores.remote() for _ in range(num_workers)]
print(ray.get(result))
```

```
anyscale job submit -f tpu_multihost_job.yaml
```
