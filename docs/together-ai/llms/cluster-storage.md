# Source: https://docs.together.ai/docs/cluster-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cluster Storage

Together Managed GPU Clusters supports long-lived, resizable in-DC shared storage with user data persistence.

You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.

All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.

[Learn more about GPU Clusters →](/docs/gpu-clusters-overview)

## Upload Your Data

To upload data to the cluster from your local machine, follow these steps:

1. Create a PVC using the shared volume name as the VolumeName as well as a pod to mount the volume
2. Run `kubectl cp LOCAL_FILENAME YOUR_POD_NAME:/data/`

Note: This method is suitable for smaller datasets, for larger datasets we recommend scheduling a pod on the cluster that can download from S3.

## Storage Types

A Together GPU Cluster has 3 types of storage:

### 1. Local disks

Each server has NVME drives which can be used for high speed local read/writes.

### 2. Shared `/home` folder for Slurm cluster

The `/home` folder is shared across all nodes, mounted as an NFS volume from the head node. This should be used for code, configs, logs, etc. It should also be used for training data or checkpointing.

We recommend logging into the Slurm head node first to properly set up your user folder with the right permissions.

### 3. Shared remote attached storage

The GPU nodes all have a mounted shared volume that you created during clsuter create (or attached an existing shared storage volume) from a high-speed storage cluster. This storage volume is useful for reading training data and writing checkpoints to/from a central location.

In the kubernetes clusters, we provide a static PersistentVolume with the same name as your shared volume. As long as you use the static PV, your data would persist.

Note: If you wish your data to persist beyond the lifecycle of the cluster, or would like to share the data/volume across clusters, you should use the static PV above which carries the same name as the shared storage volume that you provisioned. [Learn more about how to use this static PV →](/docs/gpu-clusters-management)


Built with [Mintlify](https://mintlify.com).