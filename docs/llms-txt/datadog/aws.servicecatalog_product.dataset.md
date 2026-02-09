# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicecatalog_product.dataset.md

---
title: Service Catalog Product
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Catalog Product
---

# Service Catalog Product

Service Catalog Product in AWS represents a managed product that can be created, described, and provisioned through AWS Service Catalog. It allows administrators to define and manage collections of IT services, such as virtual machines, databases, or applications, that are approved for use within an organization. This resource provides details about the product, including its metadata, versions, and provisioning artifacts, enabling users to discover and launch products in a controlled and compliant manner.

```
aws.servicecatalog_product
```

## Fields

| Title                  | ID   | Type       | Data Type                                                               | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| budgets                | core | json       | Information about the associated budgets.                               |
| launch_paths           | core | json       | Information about the associated launch paths.                          |
| product_view_summary   | core | json       | Summary information about the product view.                             |
| provisioning_artifacts | core | json       | Information about the provisioning artifacts for the specified product. |
| tags                   | core | hstore_csv |
