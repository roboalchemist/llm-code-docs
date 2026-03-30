# Source: https://northflank.com/docs/v1/application/bring-your-own-cloud/coreweave-on-northflank.md

# CoreWeave on Northflank

You can integrate your CoreWeave account to create and manage clusters using Northflank.

> [!note] 
> 
- Spot instances are not available on CoreWeave clusters.
- Builds with local cache are not supported on CoreWeave clusters.

## Add your CoreWeave account to Northflank

Navigate to `Cloud → Provider links → Create provider link` and select CoreWeave as the provider. Or use the direct link:

> [!note] 
> [Click here](https://app.northflank.com/s/account/cloud/integrations/new/coreweave) to create a new CoreWeave integration.
Copy your CoreWeave access token into the `API key` field and create the provider link. If you don't have a CoreWeave access token, you can create it in the [CoreWeave console](https://console.coreweave.com/tokens).

![Create a new provider link](https://assets.northflank.com/documentation/v1/application/bring-your-own-cloud/coreweave/integration-new.png)

You can now configure and deploy new clusters in your CoreWeave account.

Note: You can edit the integration at any time to update the API key, if required.

## Check your quotas

To successfully deploy a cluster on CoreWeave using Northflank you must have the required resources available to your account.

You can view your account quota and request new quota from the [CoreWeave console](https://console.coreweave.com/organization/quotas). In order to provision a cluster, you will require a cluster resource and the desired number of instances available in your desired zone.

Learn more on the [CoreWeave documentation on quotas](https://docs.coreweave.com/docs/products/cks/clusters/quotas).

## Create a cluster

Navigate to `Cloud → Clusters → Create cluster` and select CoreWeave as the provider. Or use the direct link:

> [!note] 
> [Click here](https://app.northflank.com/s/account/cloud/clusters/new/coreweave) to create a new CoreWeave cluster.
Enter a name for the cluster or generate one randomly. Choose your integration credentials. Select the region and the zone to deploy in.

![Create a new cluster](https://assets.northflank.com/documentation/v1/application/bring-your-own-cloud/coreweave/cluster-new.png)

### Network configuration

Choose `New VPC` if you would like a new VPC with default settings to be created for your cluster.

Choose `Re-use VPC` if you have an existing VPC that you would like to place the new cluster in. Choose one of the available VPCs for your chosen zone from the drop-down selector, and then choose the prefixes to use for pods, services, and load balancers from the VPCs available prefixes. Load balancers can use multiple prefixes. The same prefix cannot be used more than once and prefixes cannot overlap.

![Re-use an existing VPC](https://assets.northflank.com/documentation/v1/application/bring-your-own-cloud/coreweave/cluster-vpc.png)

### Node pool configuration

You can now configure the node pools for your cluster. Node pools can also be added, deleted, and updated after creating your cluster. Click add node pool to add another pool. Node types which are not available in your chosen zone will be grayed out in the selection box.

![Create a nodepool for your cluster](https://assets.northflank.com/documentation/v1/application/bring-your-own-cloud/coreweave/cluster-nodepool.png)

> [!note] Minimum cluster requirements
> Each cluster requires at least one node pool, and a combined minimum of 4 vCPU and 8GB memory across all node pools.

Each node can schedule up to 256 pods (minus system pods). The actual number of pods per node will usually be limited by resource requests and [request modifiers](configure-your-cluster#configure-resources) for smaller nodes.

See [deploy and scale node pools](deploy-and-scale-node-pools) for more information on configuring nodes and node pools.

CoreWeave:

- Does not support spot instances.

- Does not support autoscaling.

- Does not support choosing the node's disk size and type. Instead, each node comes with a predefined disk (usually a few TBs).

### Configure advanced options

After adding your initial node pools, you can configure advanced options for the cluster, such as build infrastructure and resource request modifiers.

When you create the cluster, Northflank will begin installing system components in the node pools according to their capacity. Provisioning a node pool can take up to 20-30 minutes.

## Next steps

- [Configure your Kubernetes cluster: Manage your clusters on other cloud providers using Northflank.](/v1/application/bring-your-own-cloud/configure-your-cluster)
- [Deploy node pools: Configure and deploy node pools on a Kubernetes cluster with Northflank.](/v1/application/bring-your-own-cloud/deploy-and-scale-node-pools)
- [Deploy workloads to your cluster: Deploy services, jobs, and addons to your own cluster, and configure workloads to schedule on specific node pools.](/v1/application/bring-your-own-cloud/deploy-workloads-to-your-cluster)
- [Run GPU workloads: Deploy GPU workloads on Northflank for AI, machine learning, HPC workloads, and other tasks.](/v1/application/gpu-workloads/gpus-on-northflank)
