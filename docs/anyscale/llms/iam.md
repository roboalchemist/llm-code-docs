# Source: https://docs.anyscale.com/iam.md

# IAM on Anyscale

[View Markdown](/iam.md)

# IAM on Anyscale

When you deploy an Anyscale cloud, you configure identity and access management (IAM) roles and settings that govern how Anyscale manages infrastructure and how your workloads access resources in your cloud provider account.

## Kubernetes vs. virtual machine IAM models[​](#architecture "Direct link to Kubernetes vs. virtual machine IAM models")

Anyscale uses different IAM models depending on your compute stack.

**Kubernetes deployments**: The Anyscale control plane doesn't have direct access to your cloud provider IAM. Instead, you deploy the *Anyscale operator* to your Kubernetes cluster. The control plane sends instructions to the operator, and the operator uses its own IAM permissions to create and manage Pods in your cluster. This architecture provides full separation between the Anyscale control plane and your data plane.

**Virtual machine deployments**: The Anyscale control plane assumes a cross-account IAM role in your cloud provider account to directly manage virtual machine infrastructure.

## IAM terminology by cloud provider[​](#terminology "Direct link to IAM terminology by cloud provider")

Each cloud provider uses different terminology for IAM. The following table provides an overview:

| Cloud provider | Compute stack          | Infrastructure management IAM                                                                        | Cluster IAM                                                                        |
| -------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| AWS            | Kubernetes (EKS)       | Anyscale operator Kubernetes service account annotated with an AWS IAM role.                         | Kubernetes service account annotated with an AWS IAM role.                         |
| AWS            | Virtual machines (EC2) | Cross-account IAM role assumed by Anyscale control plane.                                            | Instance profile.                                                                  |
| Google Cloud   | Kubernetes (GKE)       | Anyscale operator Kubernetes service account annotated with a Google Cloud service account.          | Kubernetes service account annotated with a Google Cloud service account.          |
| Google Cloud   | Virtual machines (GCE) | Service account assumed by Anyscale control plane.                                                   | Service account.                                                                   |
| Azure          | Kubernetes (AKS)       | Anyscale operator Kubernetes service account annotated with an Azure user-assigned managed identity. | Kubernetes service account annotated with an Azure user-assigned managed identity. |

## How does Anyscale use IAM?[​](#how-it-works "Direct link to How does Anyscale use IAM?")

When you deploy a job, service, or workspace, Anyscale uses two categories of IAM:

* *Infrastructure management IAM* grants permissions to create and manage Ray cluster infrastructure. For Kubernetes, this is the Anyscale operator's IAM role. For VMs, this is the cross-account role assumed by the Anyscale control plane.
* *Cluster IAM* grants your Ray applications access to resources in your cloud provider account, such as object storage buckets.

Anyscale provides the following options for altering the permissions available to developers and applications running on Ray clusters:

* Update the permissions in the default IAM role used by your Ray clusters. See [Default role for Ray clusters](#clusters).
* Use cloud IAM mapping to set permissions based on project, user, or cluster type. See [Cloud IAM mapping](#mapping).
* Specify an IAM role for your cluster in the advanced setting of your compute config. See [Override default role with compute config](#config).

## Infrastructure management IAM[​](#infra-iam "Direct link to Infrastructure management IAM")

Infrastructure management IAM grants permissions to create and manage Ray cluster resources in your cloud provider account.

### Kubernetes deployments: Anyscale operator IAM[​](#operator-iam "Direct link to Kubernetes deployments: Anyscale operator IAM")

For Kubernetes deployments, the Anyscale operator runs in your Kubernetes cluster and manages all infrastructure on behalf of the Anyscale control plane. The operator uses a Kubernetes service account that maps to a cloud provider IAM identity.

The Anyscale control plane sends instructions to the operator over a secure channel, but the control plane never directly accesses your cloud provider IAM. The operator interprets these instructions and uses its own IAM permissions to:

* Create and delete Pods for Ray nodes.
* Read and write to your default object storage bucket.
* Manage other Kubernetes resources such as services and ingresses.

For cloud provider-specific details on configuring the Anyscale operator IAM, see the following:

* [Configure IAM roles for clusters on Anyscale on EKS](/iam/eks.md)
* [Configure service accounts for clusters on Anyscale on GKE](/iam/gke.md)
* [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md)

### Virtual machine deployments: Cross-account IAM[​](#cross-account-iam "Direct link to Virtual machine deployments: Cross-account IAM")

For virtual machine deployments on AWS and Google Cloud, you configure a trust relationship between your cloud provider account and the Anyscale control plane. This trust relationship allows the Anyscale control plane to assume an IAM role in your cloud provider account and directly manage infrastructure.

The Anyscale control plane uses this role to perform actions such as launching virtual machines and storing artifacts in your cloud object storage. When deploying a workspace, service, or job, Anyscale attaches a separate cluster IAM role with more restricted permissions. See [Default role for Ray clusters](#clusters).

important

Your cross-account IAM role must have permissions to attach IAM roles to your virtual machines.

Whether you use `anyscale cloud setup` or `anyscale cloud register`, you can customize some permissions in this role after deploying your cloud. Disabling default configurations might remove some Anyscale features. For assistance restricting default IAM permissions, contact [Anyscale support](mailto:support@anyscale.com).

## Default role for Ray clusters[​](#clusters "Direct link to Default role for Ray clusters")

Anyscale attaches an IAM role to each node in your Ray cluster to allow the node to interact with other infrastructure in your cloud provider account. At minimum, your default role must have access to the default object storage location configured during your cloud deployment.

### Kubernetes deployments[​](#clusters-k8s "Direct link to Kubernetes deployments")

For Kubernetes deployments, you annotate Kubernetes service accounts to map them to cloud provider IAM identities. When the Anyscale operator deploys a new cluster or autoscales to add worker nodes, the Pods use this service account and assume the associated IAM identity to gain access to resources in your cloud provider account.

You must define a Kubernetes service account for each unique set of IAM permissions you want to assign to a given user, workload, or project through cloud IAM mapping.

For cloud provider-specific details on creating and annotating service accounts, see the following:

* [Configure IAM roles for clusters on Anyscale on EKS](/iam/eks.md)
* [Configure service accounts for clusters on Anyscale on GKE](/iam/gke.md)
* [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md)

### Virtual machine deployments[​](#clusters-vm "Direct link to Virtual machine deployments")

For virtual machine deployments, the permissions configured for your default role might vary depending on how you deployed your Anyscale cloud.

You can optionally add additional permissions to the default IAM role to make additional resources available to all Ray clusters deployed in your Anyscale cloud. See [Manage AWS IAM roles for Anyscale clusters](/iam/aws.md) or [Manage Google Cloud service accounts for Anyscale clusters](/iam/google-cloud.md).

## Cloud IAM mapping[​](#mapping "Direct link to Cloud IAM mapping")

Anyscale cloud owners can configure cloud IAM mapping rules.

Cloud IAM mapping allows you to set the default IAM role attached to Ray clusters based on any combination of the following:

* Workload type (job, service, or workspace).
* Project name.
* User identity (includes Anyscale service accounts).

For example, you can use cloud IAM mapping to configure read-only permissions to production data for workspaces in a project used for interactive development, and then grant read and write permissions on that production data for a service account that launches production Anyscale jobs.

For Kubernetes deployments, cloud IAM mapping specifies a Kubernetes service account name. You must pre-configure these service accounts with annotations that map them to cloud provider IAM identities.

See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

## Override default role with compute config[​](#config "Direct link to Override default role with compute config")

You can directly specify an IAM role in the advanced configurations section of your compute config to override the default IAM role.

* For AWS, see [Subnets, security groups, and instance IAM role](/configuration/compute/aws.md#iam).
* For Google Cloud, see [Subnets and service accounts](/configuration/compute/gcp.md#iam).

note

In some advanced use cases, such as deploying multiple applications to an Anyscale service, you might assign different IAM roles to worker node groups.

For most applications, Anyscale recommends using a single IAM role for all nodes in your cluster.
