# Source: https://docs.anyscale.com/admin/azure/pvc.md

# Configure shared storage with Azure blob PVC for AKS

[View Markdown](/admin/azure/pvc.md)

# Configure shared storage with Azure blob PVC for AKS

This page provides an overview of configuring Azure blob storage as a persistent volume claim (PVC) for Azure Kubernetes Services (AKS) using a Container Storage Interface (CSI) driver for use as shared storage on Anyscale.

note

Configuring shared storage for Anyscale clouds on AKS is optional. All users have full privileges for files and data in shared storage. Shared storage provides a convenient storage location for users to persist files between sessions, but might not fulfill security requirements for some organizations.

To configure access to blob storage or ADLS using more fine-grained permissions, see [Access blob storage and ADLS](/admin/azure/storage.md).

## Anyscale recommendations for PVC configuration[​](#anyscale-recommendations-for-pvc-configuration "Direct link to Anyscale recommendations for PVC configuration")

Azure provides multiple drivers and configuration options for setting up PVC for AKS. While most PVC configurations work with Anyscale once configured for AKS, Anyscale provides the following recommendations when configuring PVC for shared storage:

| Recommendation                                                                   | Reason                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Use Azure blob storage.                                                          | Blob storage is infinitely scalable, affordable, and performant.                                                                                                                                                                                                                                                                                                               |
| Use the same storage account you configured for Anyscale system default storage. | All managed identities you use as Anyscale cluster roles must have the Storage Blob Data Contributor role on this storage account. This is the same role required for setting up the CSI driver and provides the desired privileges for reading and writing data over the PVC mount.                                                                                           |
| Use a dedicated storage container for each Anyscale cloud resource.              | Use a separate blob storage container to avoid granting permissions on production data written by other systems. Anyscale shared storage includes directories for each user and workload, but all users in the cloud have full read and write permission on all directories.If necessary, you can provide read access to this container from other systems.                    |
| Use dynamic provisioning for your storage container.                             | Dynamic provisioning simplifies configuration and ensures that you have a dedicated container for your Anyscale cloud resource.Anyscale doesn't recommend configuring storage containers with production data from other systems as shared storage. Contact [Anyscale support](mailto:support@anyscale.com) if you need help migrating shared storage between cloud resources. |
| Retain your storage container beyond the PVC lifetime.                           | Make sure you set your reclaim policy to retain your storage container. By retaining your container, you can optionally remount the container on a new AKS cluster. Setting the reclaim policy to delete results in data loss if you delete the PVC.                                                                                                                           |
| Configure your connection with `blobfuse2`.                                      | Anyscale designed shared storage to interact with object storage using FUSE protocols. FUSE works well with large data files often seen in ML and AI workloads.                                                                                                                                                                                                                |
| Configure storage mounts with block-cache mode.                                  | Block-cache mode breaks larger files into blocks and uses RAM and disk space for optimized caching and asynchronous uploads.                                                                                                                                                                                                                                                   |

## Configure shared storage for AKS[​](#configure-shared-storage-for-aks "Direct link to Configure shared storage for AKS")

Complete the following steps to configure shared storage for an AKS cloud resource on Anyscale.

### Requirements[​](#requirements "Direct link to Requirements")

This example has the following requirements:

* You have permission to assign roles in the target resource group, such as Role Based Access Control Administrator.

* You have the following CLI tools installed on your local machine:

  <!-- -->

  * `kubectl`
  * Azure CLI
  * Anyscale CLI

### Step 1: Configure your local environment[​](#step-1-configure-your-local-environment "Direct link to Step 1: Configure your local environment")

Run the following commands to authenticate to Azure, your AKS cluster, and Anyscale.

Define the following environment variables describing your AKS cluster:

```
export RESOURCE_GROUP=<resource-group-name>
export AKS_CLUSTER_NAME=<aks-cluster-name>
```

Log in to Anyscale:

```
anyscale login
```

Log in to Azure:

```
az login
```

note

Make sure you select the tenant and subscription that contain your AKS cluster.

Get credentials for your AKS cluster:

```
az aks get-credentials --resource-group "${RESOURCE_GROUP}" --name "${AKS_CLUSTER_NAME}"
```

Run the following command to confirm you've configured `kubectl` for your AKS cluster:

```
kubectl config current-context
```

### Step 2: Enable the CSI driver on AKS[​](#step-2-enable-the-csi-driver-on-aks "Direct link to Step 2: Enable the CSI driver on AKS")

Run the following command to enable the Azure blob storage CSI driver on your AKS cluster:

```
az aks update --enable-blob-driver --resource-group "${RESOURCE_GROUP}" --name "${AKS_CLUSTER_NAME}"
```

See [Enable CSI driver on a new or existing AKS cluster](https://learn.microsoft.com/en-us/azure/aks/azure-blob-csi?tabs=NFS#enable-csi-driver-on-a-new-or-existing-aks-cluster) in the Azure docs.

### Step 3: Add credentials to the system-assigned managed identity[​](#step-3-add-credentials-to-the-system-assigned-managed-identity "Direct link to Step 3: Add credentials to the system-assigned managed identity")

In this step, you configure the trust relationship between the managed identity used by your AKS cluster and the storage account. This managed identity creates the container and mounts the PVC using workload identity federation.

note

This step assumes that you deployed your AKS cluster using a system-assigned managed identity. If you're using a user-assigned managed identity, the command might differ slightly.

Configure the following variables describing your Azure environment:

```
export SUBSCRIPTION_ID=<your-azure-subscription-id>
export STORAGE_ACCOUNT_NAME=<your-storage-account-name>
export SCOPE="/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT_NAME}"
```

Run the following command to get the principal ID for the identity used by AKS:

```
AKS_CLUSTER_IDENTITY=$(az aks show \
  --resource-group "${RESOURCE_GROUP}" \
  --name "${AKS_CLUSTER_NAME}" \
  --query "identity.principalId" \
  -o tsv)
```

Run the following command to assign read, write, and container creation privileges to the identity:

```
az role assignment create \
  --assignee "${AKS_CLUSTER_IDENTITY}" \
  --role "Storage Blob Data Contributor" \
  --scope "${SCOPE}"
```

Run the following command so the identity can access storage account keys to mount the container:

```
az role assignment create \
  --assignee "${AKS_CLUSTER_IDENTITY}" \
  --role "Storage Account Key Operator Service Role" \
  --scope "${SCOPE}"
```

### Step 4: Create a storage class[​](#step-4-create-a-storage-class "Direct link to Step 4: Create a storage class")

To dynamically provision a container, you define and create a storage class.

The following is an example YAML configuration that defines a storage class using blobfuse2, workload identity federation, and block-cache. Create a YAML file on your machine with this configuration, replacing the variable placeholders with the names of the storage account and resource group you configure as default system storage for your Anyscale cloud.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: blobfuse-csi

provisioner: blob.csi.azure.com
parameters:
  protocol: fuse2
  storageAccount: <your-storage-account-name>
  resourceGroup: <your-resource-group-name>
  mountWithWorkloadIdentityToken: "true"

mountOptions:
  - -o allow_other
  - --block-cache
  
allowVolumeExpansion: true
reclaimPolicy: Retain
volumeBindingMode: Immediate
```

Run the following command to create the storage class in your AKS cluster:

```
kubectl create -f your-storage-class.yaml
```

### Step 5: Create the PVC[​](#step-5-create-the-pvc "Direct link to Step 5: Create the PVC")

The following is an example YAML configuration that defines a PVC using the storage class you created in your AKS cluster. Create a YAML file on your machine with this configuration.

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: anyscale-shared-fuse
  namespace: anyscale-operator
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 100Gi
  storageClassName: blobfuse-csi
```

Run the following command to create the PVC in your AKS cluster:

```
kubectl create -f your-pvc.yaml
```

### Step 6: Add the PVC to the Anyscale cloud[​](#step-6-add-the-pvc-to-the-anyscale-cloud "Direct link to Step 6: Add the PVC to the Anyscale cloud")

In this step, you update the Anyscale cloud resource configuration to add the PVC as Anyscale shared storage.

Download your current cloud configuration and modify the resources file, then use `anyscale cloud update` to apply the changes. See [Update multiple resources for a cloud](/admin/cloud/multi-cloud.md#update).

The following example shows the structure of a cloud resource with PVC file storage configuration:

```
- name: k8s-azure-eastus
  provider: AZURE
  compute_stack: K8S
  region: eastus
  file_storage:  # Add this section
    persistent_volume_claim: anyscale-shared-fuse
```

## Use shared storage[​](#use-shared-storage "Direct link to Use shared storage")

Once configured, shared storage is available for all new workloads you create on Anyscale. See [Shared storage on Anyscale](/storage/shared.md).
