# Source: https://northflank.com/docs/v1/application/bring-your-own-cloud/create-custom-resource-plans.md

# Create custom resource plans

You can create custom resource plans for your team to use on clusters in your [own cloud provider accounts](use-other-cloud-providers-with-northflank).

These plans allow you to define your own CPU and memory limits for builds and deployments. Plan limits represent the maximum CPU and memory a container will be able to use on the node it is deployed on. CPU is defined in vCPU, with 1 vCPU corresponding to 1000 [millicore](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu). Memory is defined in MB.

You can create plans that can be used with builds only, deployments only, or both builds and deployments. You may want to create build plans with higher resource limits to build quickly, but not allow persistent deployments to be deployed with these resource limits.

You can combine custom plans with [node pool labels and tags](deploy-workloads-to-your-cluster) to manage which node pools your workloads are deployed to.

> [!note] 
> [Click here](https://app.northflank.com/s/account/cloud/custom-plans/new) to create a new custom plan.

## Northflank resource configuration

You can select the Northflank configuration type to set CPU and memory limits only in your custom plan.

Resource requests will be determined by the configuration of the cluster that workloads with this plan are deployed to. They will request the percentage of the limit set in the plan according to the [request modifiers on the cluster](configure-your-cluster#configure-resources).

## Kubernetes resource configuration

You can select the Kubernetes configuration type to set both requests and limits in your custom plan.

The request defines the minimum resources a workload requires to deploy to a node, while the limit sets the maximum resources a workload will potentially use if there is available capacity on a node.

You can enable unbounded CPU to remove the CPU limit, and workloads using the plan will be able to use as much vCPU that they require, up to the maximum available capacity on the node. This could exhaust the capacity of specific node pools, or your entire cluster, if you have many unbounded workloads deployed simultaneously and/or persistently.

## Next steps

- [Deploy node pools: Configure and deploy node pools on a Kubernetes cluster with Northflank.](/v1/application/bring-your-own-cloud/deploy-and-scale-node-pools)
- [Deploy workloads to your cluster: Deploy services, jobs, and addons to your own cluster, and configure workloads to schedule on specific node pools.](/v1/application/bring-your-own-cloud/deploy-workloads-to-your-cluster)
- [Tag your workloads and resources: Create tags to assign to your Northflank workloads and resources to help keep track of them.](/v1/application/release/tag-workloads-and-resources)
- [Configure your Kubernetes cluster: Manage your clusters on other cloud providers using Northflank.](/v1/application/bring-your-own-cloud/configure-your-cluster)
