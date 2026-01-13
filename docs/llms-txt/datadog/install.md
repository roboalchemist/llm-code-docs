# Source: https://docs.datadoghq.com/cloudprem/install.md

---
title: Install CloudPrem
description: Learn how to deploy CloudPrem on various platforms and environments
breadcrumbs: Docs > CloudPrem > Install CloudPrem
source_url: https://docs.datadoghq.com/install/index.html
---

# Install CloudPrem

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

CloudPrem can be deployed in various environments, from cloud-managed Kubernetes services to bare metal servers. The provided installation instructions are specific to **Kubernetes distributions**.

## Prerequisites{% #prerequisites %}

### Kubernetes cluster requirements{% #kubernetes-cluster-requirements %}

| Requirement                        | Details                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kubernetes Version**             | 1.25 or higher                                                                                                                              |
| **Recommended Platforms**          | - AWS EKS- Google GKE- Azure AKS- Self-managed Kubernetes (Nginx controller)                                                                |
| **Metadata Storage**               | PostgreSQL database                                                                                                                         |
| **Recommended PostgreSQL Options** | - AWS: RDS PostgreSQL- GCP: Cloud SQL for PostgreSQL- Azure: Azure Database for PostgreSQL- Self-hosted: PostgreSQL with persistent storage |

### Object storage{% #object-storage %}

CloudPrem supports the following object storage types:

- Amazon S3
- Google Cloud Storage (GCS)
- Azure Blob Storage
- MinIO
- Ceph Object Storage
- Any S3-compatible storage

## Cloud-managed Kubernetes{% #cloud-managed-kubernetes %}

- [Install on AWS EKS](https://docs.datadoghq.com/cloudprem/install/aws_eks/)
- [Install on Azure AKS](https://docs.datadoghq.com/cloudprem/install/azure_aks/)
- [Install locally with Docker for testing](https://docs.datadoghq.com/cloudprem/install/docker/)
