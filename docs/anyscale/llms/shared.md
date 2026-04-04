# Source: https://docs.anyscale.com/storage/shared.md

# Shared storage on Anyscale

[View Markdown](/storage/shared.md)

# Shared storage on Anyscale

This page provides an overview of shared storage on Anyscale.

## What is shared storage?[​](#what-is "Direct link to What is shared storage?")

*Shared storage* describes persistent storage available on all Anyscale workloads in a given Anyscale cloud resource.

You access shared storage through mount paths. Mount paths have different scoping to allow you to reuse paths across workloads reliably.

These paths appear as regular filesystem directories in your clusters.

important

Anyscale doesn't delete data stored in shared storage when workloads terminate. Discussions of persistence or scoping of shared storage paths pertain only to the aliased paths available to a workload. Anyscale doesn't delete the underlying directories or data, and all users in an Anyscale cloud resource have access to all other shared storage paths on that Anyscale cloud resource.

You're responsible for managing and cleaning up data in shared storage paths. If you use legacy shared storage configured with NFS, failure to monitor and clean up data might lead to a `No space left on device` error.

## How does shared storage work?[​](#implementation "Direct link to How does shared storage work?")

Shared storage is a virtual file system mapped back to persistent storage in your cloud provider account. Anyscale recommends configuring shared storage on top of cloud object storage, such as S3, Azure blob storage, or GCS.

### VM stack[​](#vm-stack "Direct link to VM stack")

Anyscale automatically configures shared storage for cloud resources on the VM stack. Shared storage is required for VM deployments. Shared storage paths map to the same object storage container configured for system default storage.

### Kubernetes stack[​](#kubernetes-stack "Direct link to Kubernetes stack")

Shared storage is optional for cloud resources on Kubernetes (AKS, EKS, GKE). To configure shared storage, use PVC and CSI drivers to mount a cloud object storage container.

For an example using Azure blob storage and blobfuse2, see [Configure shared storage with Azure blob PVC for AKS](/admin/azure/pvc.md).

### Legacy NFS configurations[​](#legacy-nfs-configurations "Direct link to Legacy NFS configurations")

Some existing Anyscale clouds use Network File System (NFS) for shared storage. Anyscale doesn't recommend NFS for new deployments due to storage capacity limitations and management overhead.

## Storage paths and scoping[​](#paths "Direct link to Storage paths and scoping")

Each shared storage path maps to a specific directory within your cloud's default object storage location. Anyscale doesn't manage persistence for the data in these directories or provide isolation guarantees. The following table describes the scope and persistence of each path relative to the workload, user, or cloud:

| Path                   | Scope      | Path persistence                   | Use case                                                                   |
| ---------------------- | ---------- | ---------------------------------- | -------------------------------------------------------------------------- |
| `/mnt/cluster_storage` | Cluster ID | Cluster lifecycle                  | Temporary files shared across nodes, TensorBoard logs, downloaded datasets |
| `/mnt/user_storage`    | User ID    | Across all user's clusters         | Personal scripts, configuration files, development artifacts               |
| `/mnt/shared_storage`  | Cloud ID   | Permanent (until manually deleted) | Model checkpoints, shared datasets, team resources                         |

note

For Anyscale workspaces, `/mnt/cluster_storage` persists between cluster restarts but isn't cloned when creating new workspaces. For jobs and services, each run creates a new cluster, so `/mnt/cluster_storage` doesn't persist between runs.

When you trigger a job or service from a workspace, that workload has a different `/mnt/cluster_storage` than the workspace.

### Storage path allocation by workload type[​](#path-allocation "Direct link to Storage path allocation by workload type")

You can use the workload ID to find the directory where the `/mnt/cluster_storage` path maps for each workload. The following table shows the pattern for this directory for each workload type:

| Workload type | Object storage path pattern                 |
| ------------- | ------------------------------------------- |
| Workspaces    | `workspaces/{WORKSPACE_ID}/cluster_storage` |
| Jobs          | `job/{JOB_ID}/cluster_storage`              |
| Job queues    | `job_queue/{JOB_QUEUE_ID}`                  |
| Services      | `service/{SERVICE_ID}`                      |

## Security considerations[​](#security "Direct link to Security considerations")

All files in shared storage locations are readable and writable by all users in an Anyscale cloud. Shared storage is optional on cloud resources configured on Kubernetes.

Anyscale doesn't recommend storing sensitive data, credentials, models, or code in shared storage.

* For credentials, Anyscale integrates with secrets managers in your cloud provider, such as Azure Key Vault. See [Secret management on Anyscale](/secrets.md).

* For data and models, Anyscale recommends connecting directly to cloud object storage using cloud URIs and cloud IAM mapping. See the following:

  <!-- -->

  * [Access blob storage and ADLS](/admin/azure/storage.md)
  * [Access S3 buckets](/storage/s3.md)
  * [Access Google Cloud Storage buckets](/storage/gcs.md)

* For code, build your own custom images and manage your code assets through integration with a private Git repository. See [Use container images from an external registry](/container-image/image-registry.md).
