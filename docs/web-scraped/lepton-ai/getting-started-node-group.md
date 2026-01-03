# Source: https://docs.nvidia.com/dgx-cloud/lepton/get-started/node-group

Toggle Menu

Menu

[](/dgx-cloud/lepton/)

Get Started

  * [Introduction](/dgx-cloud/lepton/get-started/)
  * [Endpoint](/dgx-cloud/lepton/get-started/endpoint/)
  * [Dev Pod](/dgx-cloud/lepton/get-started/dev-pod/)
  * [Batch Job](/dgx-cloud/lepton/get-started/batch-job/)
  * [Node Group](/dgx-cloud/lepton/get-started/node-group/)
  * [Workspace](/dgx-cloud/lepton/get-started/workspace/)



Compute

  * Bring Your Own Compute



Features

  * Endpoints
  * Dev Pods
  * Batch Jobs
  * Nodes
  * Clusters
  * Utilities
  * Workspace



Examples

  * Batch Job
  * Connections
  * Dev Pod
  * Endpoint
  * Fine Tuning
  * Raycluster



Reference

  * CLI
  * [Python SDK Reference](/dgx-cloud/lepton/reference/api/)
  * Workload Identity
  * Limits
  * [Support](/dgx-cloud/lepton/reference/support/)



# Node Group

Copy page

Learn how to create and manage node groups on DGX Cloud Lepton.

A node group is a dedicated set of nodes of a specific GPU type. Node groups let you group multiple nodes for a given workload. There are two types of node groups:

  * **BYOC Node Group** : Uses your own compute resources.
  * **Lepton Managed Node Group** : All resources are managed by DGX Cloud Lepton.



Lepton Managed Node Groups will be created by your Technical Account Manager(TAM) for you to use.

## Create a BYOC Node Group

Bring Your Own Compute (BYOC) allows you to bring your own compute resources to DGX Cloud Lepton. This is useful if you have existing resources you want to use with DGX Cloud Lepton. Follow the steps on the [Create BYOC Node Group page](/dgx-cloud/lepton/compute/bring-your-own-compute/create-byoc/) to get started.

## Use a Node Group

Once the node group is available, you can view its details on the [node group list page](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/node-groups/list).

By default, a new node group is empty. To add capacity, [bring your own compute](/dgx-cloud/lepton/compute/bring-your-own-compute/add-machines/) by clicking **Add Machines** under the **Nodes** tab.

### Create Workloads

After adding machines to the node group, you can create workloads from the node group using available nodes. When creating a workload, select the node group in the **Resource** pane to view the GPU types available in that group.

![use-node-group](/dgx-cloud/lepton/_next/static/media/use-node-group.69ecc77b.png)

## Next Steps

  * [Bring Your Own Compute](/dgx-cloud/lepton/compute/bring-your-own-compute/)



[Batch Job](/dgx-cloud/lepton/get-started/batch-job/)[Workspace](/dgx-cloud/lepton/get-started/workspace/)

Create a BYOC Node Group

Use a Node Group

Next Steps

[](/dgx-cloud/lepton/)

### Corporate Info

  * [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)
  * [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/)
  * [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
  * [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/)



### NVIDIA Developer

  * [Developer Home](https://developer.nvidia.com/)
  * [Blog](https://blogs.nvidia.com/)



### Resources

  * [Contact Us](https://www.nvidia.com/en-us/contact/)
  * [Developer Program](https://developer.nvidia.com/developer-program)



Copyright @ 2025, NVIDIA Corporation.
