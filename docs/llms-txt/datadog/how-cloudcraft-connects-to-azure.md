# Source: https://docs.datadoghq.com/cloudcraft/faq/how-cloudcraft-connects-to-azure.md

---
title: How does Cloudcraft connect to my Azure account?
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > FAQ > How does Cloudcraft connect to my Azure
  account?
---

# How does Cloudcraft connect to my Azure account?

Cloudcraft connects to your Azure account using the IAM role created in your Azure subscription. This role allows Cloudcraft to communicate with Microsoft's public API and query the metadata that describes your infrastructure. The discovery process is read-only and does not require opening up your network or connecting directly to your infrastructure.

Here's how the process works:

1. Cloudcraft makes several API requests to [every supported Azure component](https://docs.datadoghq.com/cloudcraft/faq/supported-azure-components/).
1. The results are correlated to reverse engineer your infrastructure into an architecture diagram.
1. This process is repeated every time you run a scan to ensure your diagram is up-to-date.

The only exception to the read-only rule is when an AKS Cluster is discovered. In this case, you have the option to connect Cloudcraft directly to the cluster through Kubernetes' native APIs for complete workload and pod discovery. For more information, see [Connect an Azure AKS Cluster with Cloudcraft](https://docs.datadoghq.com/cloudcraft/getting-started/connect-an-azure-aks-cluster-with-cloudcraft/).

Cloudcraft is committed to ensuring the security of your data and has implemented rigorous security processes and controls as part of its SOC2 compliance program. To learn more about Cloudcraft's security measures, visit the [security page](https://www.cloudcraft.co/security).
