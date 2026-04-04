# Source: https://docs.anyscale.com/reference/cloud.md

# Source: https://docs.anyscale.com/archive/ref/cloud.md

# Source: https://docs.anyscale.com/admin/cloud.md

# Introduction to Anyscale clouds

[View Markdown](/admin/cloud.md)

# Introduction to Anyscale clouds

This page provides an overview of Anyscale clouds and how to configure cloud resources for different environments.

## What is an Anyscale cloud?[​](#what-is-an-anyscale-cloud "Direct link to What is an Anyscale cloud?")

An Anyscale cloud abstracts the resources and infrastructure necessary for managing Anyscale clusters. An Anyscale cloud is a logical entity that connects the Anyscale control plane with cloud resources in your AWS account, Google Cloud project, or Kubernetes cluster. When you configure cloud resources for an Anyscale cloud, you create a trust relationship between the Anyscale control plane and resources in your cloud provider environment.

note

Cloud resources include both the infrastructure you configure during initial setup (VPCs, IAM roles, storage) and additional resources Anyscale deploys on your behalf (MemoryDB for fault tolerance, EC2 instances for Ray clusters). All of these resources reside in your cloud provider account as part of the data plane.

Anyscale clouds sit between your Anyscale organization and projects in the platform hierarchy. Your organization can contain one or many Anyscale clouds. Organization admins and cloud owners can manage which users can access an Anyscale cloud. See [Anyscale organization overview](/get-started/org-overview.md) and [Cloud roles](/administration/organization/permissions.md#cloud-roles).

An Anyscale cloud performs the following functions:

* Maintains information on where and how to start clusters.
* Deploys Ray clusters in your AWS, Google Cloud, or Kubernetes environments.
* Defines the collection of resources necessary to manage Anyscale clusters.
* Provides isolated environments of resources for users within your organization.

note

Your organization might have received an Anyscale-hosted cloud during initial onboarding or platform evaluation. See [Anyscale-hosted clouds](#serverless).

## Types of cloud resource configurations[​](#cloud-types "Direct link to Types of cloud resource configurations")

You configure an Anyscale cloud to deploy Ray clusters using either virtual machines or Kubernetes. The following table shows the options for each configuration:

| Compute stack    | Configuration options                                                                                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Virtual machines | **•** AWS<br />**•** Google Cloud<br />**•** Serverless Anyscale clouds (Anyscale-hosted clouds)                                                                                                                      |
| Kubernetes       | **•** Amazon Elastic Kubernetes Service (EKS)<br />**•** Google Kubernetes Engine (GKE)<br />**•** Azure Kubernetes Service (AKS)<br />**•** Any Kubernetes cluster with configured network access, including on-prem |

Anyscale supports the following options for configuring cloud resources:

| Option                                  | Description                                                                                                                                                                                                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anyscale-managed resource configuration | Use `anyscale cloud setup` to let Anyscale configure resources and permissions in your AWS or Google Cloud account. Only available for clouds that use virtual machines.                                                                                             |
| Customer-defined resource configuration | Use `anyscale cloud register` to create a trust relationship between Anyscale and resources you've configured in your cloud environment or Kubernetes cluster. Available for AWS and Google Cloud configurations, and required for deploying Anyscale on Kubernetes. |

## How should you configure your Anyscale cloud?[​](#configure "Direct link to How should you configure your Anyscale cloud?")

You should choose the configuration type that meets the needs of your organization. The following table describes the different configuration types in order of increasing complexity:

| Configuration type                                             | Details                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Serverless Anyscale (Anyscale-hosted) cloud                    | Default for new organizations. Provides a fully managed cloud experience. Good for initial product exploration and for customers who prefer not to manage any cloud configurations.                                                                                                                                                                     |
| Anyscale-managed resource configuration                        | A simpler way to configure AWS or Google Cloud resources for Anyscale. Use this method to let Anyscale automatically configure the necessary resources in your cloud provider account.                                                                                                                                                                  |
| Customer-defined resource configuration on AWS or Google Cloud | Recommended for most use cases, unless you prefer to work on Kubernetes. This provides the greatest customization and includes support for custom networking.                                                                                                                                                                                           |
| Kubernetes deployment                                          | Use Kubernetes when you have established Kubernetes infrastructure that you want to leverage for Ray workloads on Anyscale. When deploying Anyscale on Kubernetes, you install the Anyscale operator in your cluster. When possible, use first-party offerings from cloud providers such as GKE, AKS, and EKS for the best Anyscale product experience. |

important

Deploying Anyscale on Kubernetes requires custom configuration for your environment. Contact [Anyscale support](mailto:support@anyscale.com) for assistance deploying the Anyscale operator on Kubernetes.

## Anyscale-hosted clouds[​](#serverless "Direct link to Anyscale-hosted clouds")

Some organizations have special clouds known as *Anyscale-hosted* or *serverless* clouds. In this model, Anyscale manages all of the underlying infrastructure and storage used in your workloads.

Anyscale recommends serverless clouds primarily for users that are familiarizing themselves with the platform or trying out Ray for the first time.

Generally speaking, you can interact with serverless clouds the same way you would with self-hosted clouds, just without the need to worry about configuring underlying cloud infrastructure.

Some users might prefer to use serverless clouds to eliminate cloud configuration complexities. Review the [Anyscale pricing page](https://www.anyscale.com/pricing) to estimate costs for your workloads.

Contact [Anyscale support](mailto:support@anyscale.com) if you're having trouble with a serverless Anyscale cloud or need access to the following features on a serverless cloud:

* GPU compute instances.
* A serverless cloud running on Google Cloud.
* Custom cloud storage for data retention.

important

Anyscale provides temporary object storage as scratch storage on Anyscale-hosted clouds. `$ANYSCALE_ARTIFACT_STORAGE` retains data for up to 90 days from the date of creation. Anyscale removes all user data within a maximum of 120 days following account deactivation. Anyscale-hosted clouds may retain logs for up to 2 years. Users can request deletion of their Anyscale-hosted cloud account by contacting [Anyscale support](mailto:support@anyscale.com).

## Cloud hibernation[​](#hibernate "Direct link to Cloud hibernation")

An Anyscale cloud hibernates after one week without activity such as the following:

* Running workloads with workspaces, jobs, or services.
* Creating a compute configuration.
* Accessing the Grafana dashboard.

Submit a workload to wake the cloud. It takes at least a minute to wake a cloud, but might take up to ten minutes.

note

The API returns a `599` status code when you launch a workload on a hibernated cloud. You might see error messages such as `HibernationException: Failed to Start Cluster`.

Contact [Anyscale support](mailto:support@anyscale.com) if your cloud fails to recover from hibernation.

If cloud hibernation is preventing you from running infrequent workloads on Anyscale, talk to your account representative or Anyscale support.
