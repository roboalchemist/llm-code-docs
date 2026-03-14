# Source: https://docs.anyscale.com/storage/configure.md

# Configure storage for Anyscale

[View Markdown](/storage/configure.md)

# Configure storage for Anyscale

This page provides an overview of configuring storage for Anyscale clouds. Configuration requirements differ by cloud provider and whether you deploy your cloud using Kubernetes or the virtual machine (VM) stack.

## Configure default system storage[​](#default-storage "Direct link to Configure default system storage")

*Default system storage* is an object storage container that Anyscale uses for platform operations, including logs, checkpoints, and other system files. You must specify this container when configuring an Anyscale cloud resource.

The container resides in your cloud provider account (your data plane). On the Kubernetes stack, the Anyscale operator handles IAM patterns for accessing system storage.

Anyscale recommends using a dedicated object storage container for each cloud resource. When deploying an Anyscale cloud using the `anyscale cloud deploy` CLI command, Anyscale can automatically create and configure a storage container with the required permissions.

If you create and configure your own storage container, you must configure permissions to allow Anyscale to write and read artifacts in this location. Required permissions differ by cloud provider:

* **VM stack**: Configure IAM roles for the Anyscale control plane and cluster role.
* **Kubernetes stack**: Configure IAM roles mapped to Kubernetes service accounts for the Anyscale operator and cluster role.

caution

Don't modify or delete Anyscale-managed files in the default system storage container. This can cause feature degradation or data loss.

note

You can update this storage container after configuring your cloud, but Anyscale doesn't automatically migrate legacy system files. Contact [Anyscale support](mailto:support@anyscale.com) if you need to change your system default storage.

## Configure shared storage[​](#shared-storage "Direct link to Configure shared storage")

Shared storage provides persistent storage accessible through aliased paths at different scopes, such as `/mnt/cluster_storage` and `/mnt/shared_storage`. See [Shared storage on Anyscale](/storage/shared.md).

### VM stack[​](#vm-stack "Direct link to VM stack")

Anyscale automatically configures shared storage for cloud resources on the VM stack. Shared storage uses the same object storage container as system default storage.

note

If you need to disable shared storage for your VM-backed cloud, contact [Anyscale support](mailto:support@anyscale.com).

### Kubernetes stack[​](#kubernetes-stack "Direct link to Kubernetes stack")

Shared storage is optional for cloud resources on Kubernetes (AKS, EKS, GKE). To configure shared storage, use PVC and CSI drivers to mount a cloud object storage container.

For an example using Azure blob storage and blobfuse2, see [Configure shared storage with Azure blob PVC for AKS](/admin/azure/pvc.md).

## Configure IAM permissions[​](#iam "Direct link to Configure IAM permissions")

When you register an Anyscale cloud resource, you configure default identity and access management (IAM) permissions that include access to system storage and shared storage.

AWS, Azure, Google Cloud, other cloud providers, and Kubernetes each use different terminology and models for managing IAM. See [IAM on Anyscale](/iam.md).

On the VM stack, you configure default IAM roles for the Anyscale control plane and Anyscale clusters. On the Kubernetes stack, you configure default IAM roles mapped to Kubernetes service accounts for the Anyscale operator and Anyscale clusters.

All IAM roles used by Anyscale must include access to the default storage container used for system storage. Additional IAM requirements and configuration details vary by cloud provider and whether your cloud resources use the VM or Kubernetes stack.

### Grant access to additional storage[​](#grant-access-to-additional-storage "Direct link to Grant access to additional storage")

To grant your clusters access to additional object storage containers, update the IAM policies on the cluster role.

Each cloud resource has a default cluster role, but you can use cloud IAM mapping to configure rules that assign IAM roles to workloads based on user identity, Anyscale projects, and workload types. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

To configure access to object storage in AWS, Azure, or Google Cloud, see the following pages:

* [Access S3 buckets](/storage/s3.md)
* [Access blob storage and ADLS](/admin/azure/storage.md)
* [Access Google Cloud Storage buckets](/storage/gcs.md)

## Configure block storage defaults[​](#block-storage "Direct link to Configure block storage defaults")

Block storage provides node-local storage at `/mnt/local_storage`. Configuration differs by deployment type.

### VM stack[​](#vm-stack-1 "Direct link to VM stack")

You can configure block storage settings in your compute configuration. Anyscale uses SSD volumes when available on configured instances. For advanced features such as NVMe, you must enable additional settings.

Configuration options vary by cloud provider:

* [AWS compute configuration](/configuration/compute/aws.md#disk-size)
* [Google Cloud compute configuration](/configuration/compute/gcp.md#disk-size)

### Kubernetes stack[​](#kubernetes-stack-1 "Direct link to Kubernetes stack")

Your Kubernetes administrator controls block storage configuration through instance type settings and Helm chart configuration. Anyscale uses ephemeral volumes with the disks configured for your machine types to provide node-local storage for each pod.

## Update CORS settings for default system storage[​](#update-cors "Direct link to Update CORS settings for default system storage")

Anyscale uses CORS for an optimized file viewer experience. New clouds deployed with `anyscale cloud setup` use the required settings by default, but some clouds might have less permissive CORS settings configured. Complete the following steps to update the default system storage for your Anyscale cloud or cloud resource.

important

This command requires Anyscale CLI version 0.26.83 or later. You must be an Anyscale cloud owner to run this command.

This command uses cloud provider credentials stored in your local shell environment. You must have sufficient privileges to update CORS for the default system storage configured for your Anyscale cloud. The following table shows the required permissions:

| Cloud        | Read CORS                                             | Update CORS                                            |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------ |
| AWS          | `s3:GetBucketCors`                                    | `s3:PutBucketCors`                                     |
| Azure        | `Microsoft.Storage/storageAccounts/blobServices/read` | `Microsoft.Storage/storageAccounts/blobServices/write` |
| Google Cloud | `storage.buckets.get`                                 | `storage.buckets.update`                               |

1. Run the following command to authenticate the Anyscale CLI:

   ```
   anyscale login
   ```

2. Use your cloud provider CLI or the authentication pattern of your choosing to authenticate to the cloud provider account containing your default system storage container.

3. Run the following command to update your CORS settings:

   ```
   anyscale cloud update-storage-cors --name <anyscale-cloud-name>
   ```

note

Anyscale attempts to update the CORS settings for all cloud resources in an Anyscale cloud by default. Add `--resource <resource-name>` to your command if you want to only update the storage for a single cloud resource.

Storage accounts that already have the correct configuration don't apply any changes, but the operation might fail if sufficient privileges aren't present for all cloud resources.

See [`anyscale cloud update-storage-cors`](/reference/cloud.md#anyscale-cloud-update-storage-cors).
