# Source: https://docs.anyscale.com/configuration/compute.md

# Compute configuration on Anyscale

[View Markdown](/configuration/compute.md)

# Compute configuration on Anyscale

A compute configuration defines the resources Anyscale uses to launch a Ray cluster for a workspace, job, or service.

You use the compute config to define the shape of the cluster. The *shape* of a cluster reflects the instance types used for the head node and worker nodes, as well as the number of worker nodes. Anyscale cluster support heterogeneous compute, meaning you can define worker nodes using different instance types, including CPUs and GPUs.

You use *worker groups* to configure a collection of worker nodes. All worker nodes launched from a worker group use the same instance type and configurations. You configure cluster scaling at the worker group level, but can also set a global maximum for CPUs and GPUs for your cluster.

The Anyscale compute config is a superset of the [Ray cluster YAML configuration file](https://docs.ray.io/en/latest/cluster/vms/references/ray-cluster-configuration.html).

Anyscale scopes compute configs at the Anyscale cloud level. If you need to replicate a compute config to another cloud, you can use the CLI to download the YAML and use it to create a new compute config. See [Compute Config API Reference](/reference/compute-config-api.md).

Available configurations vary based on where you deploy your Anyscale cloud. See the following pages for cloud-specific details:

* [Compute configurations for AWS](/configuration/compute/aws.md)
* [Compute configuration options for Google Cloud](/configuration/compute/gcp.md)
* [Compute configuration options for Kubernetes](/configuration/compute/kubernetes.md)
* [Advanced settings for compute configs on Anyscale](/configuration/compute/advanced.md)

You can also define compute requirements directly using declarative syntax instead of selecting from predefined instance types. See [Declarative compute configs](/configuration/compute/declarative.md).

note

Serverless clouds (also called Anyscale-hosted clouds) don't support advanced configurations passed through to the underlying infrastructure. You can still configure Ray and Anyscale features such as scheduling priority.

## Compute config settings overview[​](#settings-overview "Direct link to Compute config settings overview")

You specify compute configs for the head node, worker nodes, and cluster-wide.

The following sections provide a high-level overview of configuration options in the Anyscale console. You can also specify these options when creating a compute config using the CLI or SDK, or as part of the cluster configuration for your workspace, service, or job. See [Compute Config Models](/reference/compute-config-api.md#compute-config-models).

note

When you launch Ray clusters from the Anyscale CLI, you can use the `--compute-config` flag to specify a compute config already registered to your Anyscale cloud. To specify a compute config directly with YAML, use the `compute_config` option in the [workspace config](/reference/workspaces.md#workspaceconfig), [job config](/reference/job-api.md#jobconfig), or [service config](/reference/service-api.md#serviceconfig).

Anyscale provides tools to create and manage compute configs scoped to an Anyscale cloud deployment. You can also directly specify your compute config when defining a new cluster. See [Create or version a compute config](/configuration/compute/create.md).

### Node config[​](#node "Direct link to Node config")

The following settings are common to all nodes in your cluster. Use these options to configure your head node or worker groups.

| Setting             | Description                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance type**   | The virtual machine instance type used for the node.<br /><br />Instance types are specific to the cloud. The Anyscale console uses shorthand for instance types to highlight the size CPU and GPU on the instance. |
| **Instance config** | Node-specific configurations that override cluster-wide configurations. These settings are cloud-specific and passed to the cloud provider to further customize the virtual machine.                                |
| **Ray config**      | Specify custom resource rules to control how Ray schedules tasks and actors on your nodes.                                                                                                                          |

### Worker nodes scaling config[​](#scaling "Direct link to Worker nodes scaling config")

Use the following settings to control scaling behaviors for worker groups:

| Setting         | Description                                                                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Autoscaling** | Enable autoscaling to allow Ray to dynamically scale your cluster between the specified minimum and maximum number of nodes. If you disable autoscaling, your cluster deploys with the specified number of nodes. |
| **Scale with**  | Specify how you want Anyscale to use spot instances when adding nodes to the cluster. Choose from **Spot instances**, **On-demand instances**, or **Spot first, fall back to on-demand**.                         |

### Cluster config advanced settings[​](#cluster "Direct link to Cluster config advanced settings")

Use the following settings to configure cluster-wide behavior:

| Setting                       | Description                                                                                                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Region**                    | The region used to deploy your cluster. Maps to the region of your Anyscale cloud.                                                                                                                     |
| **Allowed zones**             | The zones within the specified region that Anyscale searches for available compute.                                                                                                                    |
| **Enable cross-zone scaling** | Enable this option to allow Anyscale to scale your cluster by adding nodes across multiple available zones.                                                                                            |
| **Maximum CPUs**              | Specify the total limit for the number of CPUs that Anyscale can add to your cluster across all worker groups.                                                                                         |
| **Maximum GPUs**              | Specify the total limit for the number of GPUs that Anyscale can add to your cluster across all worker groups.                                                                                         |
| **Instance config**           | Cluster-wide configurations passed to the cloud provider and used while deploying all nodes. If you specify settings at both the cluster and node level, the node config overrides the cluster config. |
| **Advanced features**         | Additional cluster-wide settings for Ray or Anyscale settings.                                                                                                                                         |

warning

You can set the **Instance config** field at either the cluster or node level.

If you configure any settings in the **Instance config** field at the node level, that node ignores any cluster-wide configurations you specified using this field. Anyscale makes no attempt to merge **Instance config** settings at the node and cluster level.

## Auto-select worker nodes[​](#auto-select "Direct link to Auto-select worker nodes")

Enable **Advanced settings > Auto-select worker nodes** in your compute config to allow the Anyscale autoscaler to dynamically choose instances based on instance cost, availability, and requested resources.

When you run Ray applications with this feature enabled, Anyscale respects accelerator types specified in your Ray code. Anyscale doesn't support all accelerator types supported on Ray. You use short-form names to specify GPU and TPU [accelerator types](https://docs.ray.io/en/latest/ray-core/scheduling/accelerators.html#accelerator-types) in your Ray code.

If you define your compute config with YAML, you must explicitly enable the option `auto_select_worker_config`, as in the following example:

```
head_node:
    instance_type: m5.2xlarge
auto_select_worker_config: true
```

## Configure availability zones[​](#availability-zones "Direct link to Configure availability zones")

You can customize how Anyscale searches availability zones within your cloud region for deploying nodes in your cluster. You can specify zones in the **Advanced settings > Allowed zones** field.

By default, Anyscale searches all availability zones within the region for specified instances when deploying nodes. Anyscale deploys nodes with the following behavior during cluster initialization or auto-scaling events:

* Anyscale deploys the head node for your cluster in a zone.
* Anyscale attempts to deploy worker nodes in the same zone as the head node.
* If resources aren't available in that zone, Anyscale attempts to deploy worker nodes in another zone.

By default, Anyscale deploys all worker nodes to the same zone. Anyscale doesn't guarantee the head node deploys to the same zone as worker nodes.

If you select **Enable cross-zone scaling**, Anyscale can deploy worker nodes to different availability zones in your cloud region. Workloads with heavy inter-node communication can experience slowdown when workers deploy to different zones, and incur network transfer costs for data moving between zones.

Some instances types might not be available in all availability zones. To avoid possible errors during autoscaling events, Anyscale recommends excluding zones that don't support all instance types used in your compute config.

## Supported instance types[​](#supported-types "Direct link to Supported instance types")

Anyscale supports a wide variety of instance types for Anyscale clouds deployed on Google Cloud and AWS virtual machines. Access to accelerators such as GPUs and TPUs varies by cloud provider and region. For a full list, see [Supported Machine Types](https://www.anyscale.com/pricing-detail#supported-machine-types).

For Anyscale clouds deployed to Kubernetes, including AKS, EKS, and GKE, a Kubernetes admin configures what instance types are available using the Helm chart for the Anyscale operator.

Cloud admins define and manage instance types for machine pools. Anyscale recommends configuring machine pools for use with GPU-intensive applications to secure accelerators in cloud provider regions with limited GPU availability. See [Share compute resources with Anyscale machine pools](/machine-pools.md).

### Node sizing guidelines[​](#sizing-recs "Direct link to Node sizing guidelines")

Each Ray workload has different requirements for cluster shape, but all Ray workloads share some common requirements.

Ray reserves CPU cores and system memory for running Ray system processes. The head node requires additional system resources to run the Global Control Service. As workloads scale in size, outbound bandwidth for the head node might become a limiting factor.

Anyscale recommends the following when selecting machine types for nodes in your cluster:

| Node type    | Recommendations                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Head node    | - Use an instance type with at least 8 vCPUs and 32 GB of RAM.<br />- Don't use a GPU instance when deploying a multi-node cluster.                                         |
| Worker nodes | - Use an instance type with at least 4 vCPUs and 16 GB of RAM.<br />- Consider scaling up machine size before scaling out number of nodes to limit internode communication. |

Anyscale workspaces run Jupyter and VS Code servers on the head node in addition to Ray system processes.

Anyscale automatically disables head node scheduling for multi-node clusters. You can deploy a single node cluster by defining a compute config without any worker nodes (don't enable auto-select worker nodes). Anyscale automatically configures single node clusters to use head node scheduling. Anyscale recommends single node clusters for development and testing.

note

If you need a GPU during development, you can define a cluster with a single GPU as the head node. As you move to a multi-node configuration, update your head node to be CPU-only and move your GPUs to worker nodes.
