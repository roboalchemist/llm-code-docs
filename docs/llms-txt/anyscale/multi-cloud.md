# Source: https://docs.anyscale.com/admin/cloud/multi-cloud.md

# Configure multiple resources for an Anyscale cloud

[View Markdown](/admin/cloud/multi-cloud.md)

# Configure multiple resources for an Anyscale cloud

This page provides an overview of adding multiple resource configurations to an Anyscale cloud. You configure multiple resource configurations so that Anyscale jobs can fall back to using resources in another region or cloud provider when resources in your primary configuration aren't available for your Anyscale clusters.

important

This feature is in beta release.

You can only configure fallback across multiple resources for Anyscale jobs. Fallback isn't supported for workspaces or services.

## Add a cloud resource configuration to an Anyscale cloud[​](#create "Direct link to Add a cloud resource configuration to an Anyscale cloud")

You can add additional cloud resource configurations to any self-hosted Anyscale cloud. See [Cloud API Reference](/reference/cloud.md).

note

Anyscale serverless clouds (also called Anyscale-hosted clouds) are the only clouds that don't support multiple resource configurations.

You must be an owner on an existing Anyscale cloud to add a new resource configuration. Complete the following steps:

1. Define your cloud resource configuration in a YAML file on your local machine, such as the following example saved to `/path/to/cloud-resources.yaml`:

   * AWS EC2
   * Google Cloud Engine
   * EKS
   * GKE
   * AKS

   ```
   name: new-cloud-resource-name
   provider: AWS
   compute_stack: VM
   region: us-west-2
   networking_mode: PUBLIC
   object_storage:
     bucket_name: s3://my-bucket
   aws_config:
     vpc_id: vpc-123
     subnet_ids:
     - subnet-123
     security_group_ids:
     - sg-123
     anyscale_iam_role_id: arn:aws:iam::123456789012:role/anyscale-role-123
     cluster_iam_role_id: arn:aws:iam::123456789012:role/cluster-role-123
     memorydb_cluster_name: my-memorydb-cluster
   ```

   ```
   name: vm-gcp-us-west1
   provider: GCP
   compute_stack: VM
   region: us-west1
   networking_mode: PUBLIC
   object_storage:
     bucket_name: gs://my-bucket-us-west1
   gcp_config:
     project_id: my-project
     provider_name: projects/123456789012/locations/global/workloadIdentityPools/my-pool/providers/my-provider
     vpc_name: my-vpc
     subnet_names:
     - my-subnet-west
     firewall_policy_names:
     - my-firewall-policy
     anyscale_service_account_email: anyscale-sa@my-project.iam.gserviceaccount.com
     cluster_service_account_email: cluster-node-sa@my-project.iam.gserviceaccount.com
     memorystore_instance_name: projects/123456789012/locations/us-west1-b/instances/my-memorystore-west
   ```

   ```
   name: k8s-aws-us-west-2
   provider: AWS
   compute_stack: K8S
   region: us-west-2
   object_storage:
     bucket_name: s3://my-eks-bucket
   kubernetes_config:
     anyscale_operator_iam_identity: arn:aws:iam::123456789012:role/eks-node-role
     zones:
     - us-west-2a
     - us-west-2b
     - us-west-2c
   ```

   ```
   name: k8s-gcp-us-central1
   provider: GCP
   compute_stack: K8S
   region: us-central1
   object_storage:
     bucket_name: gs://my-gke-bucket
   kubernetes_config:
     anyscale_operator_iam_identity: anyscale-operator@my-project.iam.gserviceaccount.com
     zones:
     - us-central1-a
     - us-central1-b
     - us-central1-c
   ```

   ```
   name: k8s-azure-eastus
   provider: AZURE
   compute_stack: K8S
   region: eastus
   object_storage:
     bucket_name: abfss://<container-name>@<storage-account-name>.dfs.core.windows.net
   kubernetes_config:
     zones:
     - eastus-1
     - eastus-2
     - eastus-3
   ```

   For cloud resource config parameters, see [`CloudResource`](/reference/cloud.md#cloudresource).

2. Run the following command to use this YAML config file to create a cloud resource configuration in your existing cloud:

   ```
   anyscale cloud resource create --cloud <cloud-name> --file /path/to/cloud-resources.yaml
   ```

## Update multiple resources for a cloud[​](#update "Direct link to Update multiple resources for a cloud")

You can use the CLI to update the configurations for multiple resources for an Anyscale cloud. You can only modify existing resources this way.

important

The `anyscale cloud update` command expects a resources YAML file formatted as a list of resources, as in the following example:

```
- name: k8s-azure-eastus
  provider: AZURE
  compute_stack: K8S
  region: eastus
  object_storage:
  bucket_name: abfss://<container-name>@<storage-account-name>.dfs.core.windows.net
  kubernetes_config:
    zones:
    - eastus-1
    - eastus-2
    - eastus-3
- name: k8s-azure-westus
  provider: AZURE
  compute_stack: K8S
  region: westus
  object_storage:
    bucket_name: abfss://<container-name>@<storage-account-name>.dfs.core.windows.net
  kubernetes_config:
    zones:
    - westus-1
    - westus-2
    - westus-3
```

Complete the following steps to update resources for a cloud:

1. Save the current cloud configuration as a YAML file using the following CLI command:

   ```
   anyscale cloud get --name <cloud-name> --output /path/to/cloud-resources.yaml
   ```

2. Open the file in your preferred text editor or IDE.

   * You must format your file to match the structure of a cloud resources YAML. Modify the output of `anyscale cloud get` to remove everything except the items under `resources:`.
   * Edit settings for one or more of your resources.
   * Save the file.

3. Run the following CLI command to apply your saved configuration:

   ```
   anyscale cloud update --name <cloud-name> --resources-file /path/to/cloud-resources.yaml
   ```

## Remove a cloud resource configuration from an Anyscale cloud[​](#remove "Direct link to Remove a cloud resource configuration from an Anyscale cloud")

Run the following code to remove a cloud resource configuration from a multi-cloud setup:

```
anyscale cloud resource delete --cloud <cloud-name> --resource <cloud-resource-name>
```

Replace `<cloud-resource-name>` with the name of the cloud resource you want to remove.

## Configure compute configs for multi-resource clouds[​](#compute-config "Direct link to Configure compute configs for multi-resource clouds")

Once you've added multiple cloud resources to an Anyscale cloud, you configure compute configs to specify which resources to use and how to handle fallback between them.

### How compute configs work with multiple resources[​](#how-compute-configs-work-with-multiple-resources "Direct link to How compute configs work with multiple resources")

* The head node and all worker nodes for a cluster must deploy to the same cloud resource.
* A cluster deploys to a single cloud resource at a time.
* When resources aren't available in the primary cloud resource, Anyscale attempts to launch the cluster using the next cloud resource in the configuration.
* You specify which cloud resource each configuration should use with the `cloud_resource` field in each config entry.

### Simple example with auto-selected workers[​](#simple-example "Direct link to Simple example with auto-selected workers")

The following example shows a minimal multi-resource compute config that uses auto-selected worker nodes. When you don't specify a head node, Anyscale uses the default for the cloud resource:

* m5.2xlarge for AWS VMs
* n2-standard-8 for Google Cloud VMs
* Smallest CPU-only instance type for Kubernetes

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: vm-gcp-us-west1
  auto_select_worker_config: true
- cloud_resource: vm-aws-us-west-2
  auto_select_worker_config: true
```

For more information about auto-selected workers, see [Auto-select worker nodes](/configuration/compute.md#auto-select).

### Multi-resource compute config examples[​](#compute-examples "Direct link to Multi-resource compute config examples")

The following examples show compute configurations that correspond to the cloud resource configurations shown in the preceding section. Each example includes head node and worker group definitions for both CPU and GPU workloads.

note

By default, Anyscale prioritizes cloud resources using the `availability` strategy. You can also prioritize resources using the `input_order` strategy. See [Control resource selection strategy](#strategy).

* EC2 multi-region
* GCE multi-region
* EC2 and GCE
* EKS and EC2
* GKE and GCE
* AKS multi-region

Configure fallback between two AWS regions with CPU and GPU worker groups.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: vm-aws-us-west-2
  head_node:
    instance_type: m5.2xlarge
  worker_nodes:
  - instance_type: m5.4xlarge
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: g5.4xlarge
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
- cloud_resource: vm-aws-us-east-1
  head_node:
    instance_type: m5.2xlarge
  worker_nodes:
  - instance_type: m5.4xlarge
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: g5.4xlarge
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
```

Configure fallback between two Google Cloud regions with CPU and GPU worker groups.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: vm-gcp-us-west1
  head_node:
    instance_type: n2-standard-8
  worker_nodes:
  - instance_type: n2-standard-16
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: a2-highgpu-1g
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
- cloud_resource: vm-gcp-us-central1
  head_node:
    instance_type: n2-standard-8
  worker_nodes:
  - instance_type: n2-standard-16
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: a2-highgpu-1g
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
```

Configure cross-cloud fallback between AWS and Google Cloud with CPU and GPU worker groups.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: vm-aws-us-west-2
  head_node:
    instance_type: m5.2xlarge
  worker_nodes:
  - instance_type: m5.4xlarge
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: g5.4xlarge
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
- cloud_resource: vm-gcp-us-west1
  head_node:
    instance_type: n2-standard-8
  worker_nodes:
  - instance_type: n2-standard-16
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: a2-highgpu-1g
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
```

Configure fallback from EKS to AWS EC2 VMs. For Kubernetes deployments, you must define instance types in your cluster's custom instance type configurations.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: k8s-aws-us-west-2
  head_node:
    instance_type: cpu-8-32
  worker_nodes:
  - instance_type: cpu-16-64
    min_nodes: 0
    max_nodes: 10
  - instance_type: gpu-a100-1
    min_nodes: 0
    max_nodes: 5
- cloud_resource: vm-aws-us-west-2
  head_node:
    instance_type: m5.2xlarge
  worker_nodes:
  - instance_type: m5.4xlarge
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: g5.4xlarge
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
```

Configure fallback from GKE to Google Cloud VMs. For Kubernetes deployments, you must define instance types in your cluster's custom instance type configurations.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: k8s-gcp-us-central1
  head_node:
    instance_type: cpu-8-32
  worker_nodes:
  - instance_type: cpu-16-64
    min_nodes: 0
    max_nodes: 10
  - instance_type: gpu-a100-1
    min_nodes: 0
    max_nodes: 5
- cloud_resource: vm-gcp-us-central1
  head_node:
    instance_type: n2-standard-8
  worker_nodes:
  - instance_type: n2-standard-16
    min_nodes: 0
    max_nodes: 10
    market_type: SPOT
  - instance_type: a2-highgpu-1g
    min_nodes: 0
    max_nodes: 5
    market_type: SPOT
```

Configure fallback between two AKS regions. For Kubernetes deployments, you must define instance types in your cluster's custom instance type configurations.

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: k8s-azure-eastus
  head_node:
    instance_type: cpu-8-32
  worker_nodes:
  - instance_type: cpu-16-64
    min_nodes: 0
    max_nodes: 10
  - instance_type: gpu-a100-1
    min_nodes: 0
    max_nodes: 5
- cloud_resource: k8s-azure-westus
  head_node:
    instance_type: cpu-8-32
  worker_nodes:
  - instance_type: cpu-16-64
    min_nodes: 0
    max_nodes: 10
  - instance_type: gpu-a100-1
    min_nodes: 0
    max_nodes: 5
```

### Control resource selection strategy[​](#strategy "Direct link to Control resource selection strategy")

By default, Anyscale uses internal availability scoring to choose which cloud resource to use when launching a cluster. Anyscale bases this scoring on historical success rates for launching instances across different cloud resources and regions. The scoring considers only the resources requested, not the actual contents of your workloads.

You can override this behavior by setting the `cloud_resource_strategy` flag to `input_order`, which attempts to launch clusters using cloud resources in the order they're listed in your compute config.

The following example shows how to configure the resource selection strategy:

```
cloud: my-multi-resource-cloud
configs:
- cloud_resource: vm-gcp-us-west1
  auto_select_worker_config: true
- cloud_resource: vm-aws-us-west-2
  auto_select_worker_config: true
flags:
  min_resources:
    'accelerator_type:A100-40G': 1
  cloud_resource_strategy: input_order
```

#### Available strategies[​](#available-strategies "Direct link to Available strategies")

* **`availability`** (default): Anyscale chooses the cloud resource with the highest availability score from historical launch success rates.
* **`input_order`**: Anyscale attempts to launch clusters using cloud resources in the order specified in the `configs` list.

### Accelerator requirements[​](#accelerators "Direct link to Accelerator requirements")

When using `min_resources` with accelerator types such as `'accelerator_type:A100-40G'`, the specified accelerator must be available in the target cloud resources. For VM deployments, both cloud resources must have instance types with the specified GPU available. For Kubernetes deployments, you must define the accelerator types in your custom instance type configurations.

For more information about accelerator types and auto-selected workers, see [Auto-select worker nodes](/configuration/compute.md#auto-select).

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations exist for multiple resource configurations:

* Only available in Anyscale clouds created using `cloud register`.
* Only jobs support configuration with multiple resources.
* Ray clusters can only launch in one resource at a time for each job.
* No support for task dashboards.
