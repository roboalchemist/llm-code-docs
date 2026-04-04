# Source: https://docs.datadoghq.com/cloudcraft/getting-started/connect-an-azure-aks-cluster-with-cloudcraft.md

---
title: Connect an Azure AKS Cluster with Cloudcraft
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Connect an Azure AKS
  Cluster with Cloudcraft
---

# Connect an Azure AKS Cluster with Cloudcraft

By scanning your Azure AKS clusters, Cloudcraft allows you to generate system architecture diagrams to help visualize your deployed workloads and pods.

Cloudcraft uses Azure's Kubernetes Service Cluster User Role, and requires no special software or agent to look inside your clusters.

{% alert level="info" %}
The ability to scan Azure AKS clusters and Azure accounts is only available to Cloudcraft Pro subscribers. Refer to [Cloudcraft's pricing page](https://www.cloudcraft.co/pricing) for more information.
{% /alert %}

## Prerequisites{% #prerequisites %}

Before connecting your Azure AKS clusters with Cloudcraft, you must connect your Azure account and generate diagrams that include your clusters. For more information, see [Connect your Azure account with Cloudcraft](https://docs.datadoghq.com/cloudcraft/getting-started/connect-azure-account-with-cloudcraft/).

## Authorizing the Cloudcraft IAM user for view-only access{% #authorizing-the-cloudcraft-iam-user-for-view-only-access %}

Start by opening a blueprint with an existing Azure AKS cluster, or using the **Auto Layout** feature to generate a new blueprint.

With your Azure environment mapped into a blueprint, select the Azure AKS cluster that you wish to scan, and click the **Enable cluster scanning** button that appears in the component toolbar.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-an-azure-aks-cluster-with-cloudcraft/enable-cluster-scanning.615d0211a5e8da3d6e73fd816ddb45ab.png?auto=format"
   alt="Interactive Cloudcraft diagram showing an Azure AKS cluster with enable cluster scanning button highlighted." /%}

The next screen provides step-by-step instructions to complete in Azure.

1. Click the first link to open your Azure Subscriptions page, then click **Access control (IAM)** on the left sidebar.
1. Click **Add** and select **Add role assignment**.
1. Search for and select **Azure Kubernetes Service Cluster User Role**, then click **Next**.
1. Click **Select members**.
1. Search for the IAM user that you want to grant access to your Azure AKS clusterâusually named cloudcraftâand click **Select**.
1. Click **Review + assign** twice to complete the process.

## Testing access to the cluster{% #testing-access-to-the-cluster %}

To test that Cloudcraft can access to the cluster, click **Test cluster access** at the bottom of the **Enable Kubernetes Cluster Scanning** screen.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-an-azure-aks-cluster-with-cloudcraft/test-cluster-access.74bc93bd9adebcc54e83e61c2fe5b2d3.png?auto=format"
   alt="Screenshot of Cloudcraft Enable Kubernetes Cluster Scanning interface with instructions and Test Cluster Access button." /%}
