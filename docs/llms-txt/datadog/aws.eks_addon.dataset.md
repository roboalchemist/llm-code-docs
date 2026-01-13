# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_addon.dataset.md

---
title: EKS Add-on
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Add-on
source_url: https://docs.datadoghq.com/data_directory/aws/aws.eks_addon.dataset/index.html
---

# EKS Add-on

EKS Add-on in AWS is a managed extension that simplifies the installation and lifecycle management of operational software for Amazon Elastic Kubernetes Service clusters. It allows you to deploy and keep critical Kubernetes components, such as networking or observability tools, up to date with minimal effort.

```
aws.eks_addon
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                 | Description |
| ------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| addon_arn                 | core | string        | The Amazon Resource Name (ARN) of the add-on.                                                                                                                                                                                                                             |
| addon_name                | core | string        | The name of the add-on.                                                                                                                                                                                                                                                   |
| addon_version             | core | string        | The version of the add-on.                                                                                                                                                                                                                                                |
| cluster_name              | core | string        | The name of your cluster.                                                                                                                                                                                                                                                 |
| configuration_values      | core | string        | The configuration values that you provided.                                                                                                                                                                                                                               |
| created_at                | core | timestamp     | The Unix epoch timestamp at object creation.                                                                                                                                                                                                                              |
| health                    | core | json          | An object that represents the health of the add-on.                                                                                                                                                                                                                       |
| marketplace_information   | core | json          | Information about an Amazon EKS add-on from the Amazon Web Services Marketplace.                                                                                                                                                                                          |
| modified_at               | core | timestamp     | The Unix epoch timestamp for the last modification to the object.                                                                                                                                                                                                         |
| owner                     | core | string        | The owner of the add-on.                                                                                                                                                                                                                                                  |
| pod_identity_associations | core | array<string> | An array of EKS Pod Identity associations owned by the add-on. Each association maps a role to a service account in a namespace in the cluster. For more information, see Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity in the Amazon EKS User Guide. |
| publisher                 | core | string        | The publisher of the add-on.                                                                                                                                                                                                                                              |
| service_account_role_arn  | core | string        | The Amazon Resource Name (ARN) of the IAM role that's bound to the Kubernetes ServiceAccount object that the add-on uses.                                                                                                                                                 |
| status                    | core | string        | The status of the add-on.                                                                                                                                                                                                                                                 |
| tags                      | core | hstore        |
