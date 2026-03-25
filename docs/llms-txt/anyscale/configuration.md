# Source: https://docs.anyscale.com/configuration.md

# Define a Ray cluster

[View Markdown](/configuration.md)

# Define a Ray cluster

This page provides an overview of how you define a Ray cluster on Anyscale. When you launch a workspace, job, or service, Anyscale deploys a Ray cluster using cloud resources according to your cluster definition. Because workspaces, jobs, and services rely on the same basic constructs for defining clusters, you can move between stages in your development lifecycle by updating a handful of configurations.

The following diagram highlights the core concepts in this model:

![A diagram of how Anyscale products combine to define a Ray cluster on cloud resources](/assets/images/config-1b18c71f21a7416d7a7ff929ac0069d2.png)

## How to define a cluster on Anyscale[​](#how-to-define "Direct link to How to define a cluster on Anyscale")

A cluster definition consists of the following two components:

* A [*container image*](#container-image) specifies the compute environment deployed to each node. It includes package requirements, dependencies, and environmental variables.
* A [*compute config*](#compute-config) specifies the number and type of Ray nodes to deploy, as well as instructions about scaling and various cloud-specific configuration options.

The Anyscale console provides user interfaces for the following:

* Creating custom container images.
* Defining custom compute configs.
* Configuring and managing workspaces.
* Monitoring and terminating jobs and services.

The CLI and SDK provide commands for defining, managing, and deploying all the configurations related to workspaces, jobs, and services.

You use the CLI or SDK to define clusters when submitting jobs and deploying services.

Workspaces, jobs, and services each have additional options and parameters to further customize clusters for an application.

### Minimum required configuration for Anyscale workspace[​](#minimum-config "Direct link to Minimum required configuration for Anyscale workspace")

When you use the Anyscale console to define a workspace, Anyscale configures default values for the following settings:

| Setting          | Default value                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------- |
| Container image  | Latest stable slim Anyscale base image. Uses the most recent Ray, Python, and CUDA versions. |
| Head node        | `8CPU-32GB` Must specify for Kubernetes deployments.                                         |
| Auto termination | Terminate the workspace after 120 minutes of inactivity.                                     |

Anyscale recommends the following additional configurations for new users:

| Setting      | Recommended configuration                                                                                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name         | (Required) You must give your workspace a unique name.                                                                                                                                                                                                                                                     |
| Worker nodes | Enable **Auto-select nodes** to let Anyscale dynamically scale your cluster based on your workload.<br /><br />For exploratory development on smaller data, consider adding a single worker node that autoscales between `0` and `1` nodes. Select GPU-enabled instance type if your workload requires it. |

## Container image[​](#container-image "Direct link to Container image")

The container image defines the standardized package of dependencies and code that Anyscale deploys as containerized Ray nodes in a cluster. See [What is a container image?](/container-image.md).

Anyscale provides a selection of base images for each version of Ray. To review available images and installed libraries, see [Anyscale base images](/reference/base-images.md).

If you're using Anyscale workspaces for interactive development, you can iterate on the environment in your container image using workspace dependency features. See [Dependency management on Anyscale](/dependency-management.md).

If you're submitting a job or deploying a service, Anyscale recommends building and using a custom image. Custom images use standard Dockerfile syntax to allow you to extend Anyscale-provided base images to include your own environmental variables, package dependencies, and other configurations. See [Custom images on Anyscale](/container-image/custom-image.md).

## Compute configuration[​](#compute-config "Direct link to Compute configuration")

The compute config defines the number and type of nodes that Anyscale adds to the Ray cluster. You use the compute config to specify settings such as the following:

* The size of the head node.
* The number of CPUs and GPUs in the cluster.
* The size and type of worker nodes.
* Whether to use spot instances.
* The minimum and maximum number of nodes for scaling.

Compute configs are specific to an Anyscale cloud. The Anyscale cloud determines where the Ray cluster deploys (for example, AWS, Google Cloud, AKS, or Kubernetes), the default permissions assumed by the cluster in that ecosystem, and defaults for other settings such as networking and storage. You can optionally use the compute config to specify advanced configurations including custom networking or IAM roles.

The console only shows compute configs for the active Anyscale cloud. You can use the console to define a new compute config for the active cloud. If you're using the CLI or SDK, you can either specify an Anyscale cloud in your compute config or name a previously defined compute config in a specified cloud.

note

The Anyscale console provides human-friendly names for node configuration when working with clouds hosted on AWS or Google Cloud virtual machines. These map back to virtual machine instances.

For example, the **8CPU-32GB** instance type maps to a `m5.2xlarge` machine on AWS or a `n2-standard-8` machine on Google Cloud.

Anyscale clouds deployed on Kubernetes use pods instead of virtual machines as worker nodes, and Kubernetes admins configure instance type names while using Helm charts while deploying the Anyscale operator.

You can use the same compute config for multiple jobs, services, and workspaces. To learn more about compute configs, see [Compute configurations](/configuration/compute.md).

## Cluster storage[​](#cluster-storage "Direct link to Cluster storage")

Workspaces, jobs, and services use the same basic model for cluster storage. Anyscale cloud admins configure the default storage permissions and configurations used when deploying clusters.

Anyscale configures and deploys the following storage assets each time a cluster starts:

* Ephemeral block storage local to each machine in your cluster.
* Ephemeral storage for sharing files across nodes in the cluster.
* Default object storage configured by Anyscale for persisting files between workloads.
* Shared storage available to all users in a cloud.
* Shared storage available to all clusters launched by a user.

To learn more about these different types of storage, see [Storage overview](/storage.md).

## Grant access to cloud provider resources[​](#iam "Direct link to Grant access to cloud provider resources")

Anyscale recommends configuring access to resources in your cloud provider to add persistent object storage and secret management to your cluster, as shown in the following table.

note

You must have sufficient privileges in your cloud provider account to configure the required permissions.

|                       | AWS                                    | Google Cloud                               | Azure                                                         |
| --------------------- | -------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| **Object storage**    | [S3](/storage/s3.md)                   | [GCS](/storage/gcs.md)                     | [Access blob storage and ADLS](/admin/azure/storage.md)       |
| **Secret management** | [AWS Secrets Manager](/secrets/aws.md) | [Secret Manager](/secrets/google-cloud.md) | [Use secrets from Azure Key Vault](/admin/azure/key-vault.md) |
