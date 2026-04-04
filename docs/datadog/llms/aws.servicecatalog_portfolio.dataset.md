# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicecatalog_portfolio.dataset.md

---
title: Service Catalog Portfolio
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Catalog Portfolio
---

# Service Catalog Portfolio

An AWS Service Catalog Portfolio is a collection of approved products that helps organizations manage and govern cloud resources. It allows administrators to organize products, control access, and apply compliance rules, while enabling end users to quickly deploy pre-approved solutions. Portfolios can be shared across accounts and regions to standardize deployments.

```
aws.servicecatalog_portfolio
```

## Fields

| Title            | ID   | Type       | Data Type                                                       | Description |
| ---------------- | ---- | ---------- | --------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| budgets          | core | json       | Information about the associated budgets.                       |
| portfolio_detail | core | json       | Information about the portfolio.                                |
| tag_options      | core | json       | Information about the TagOptions associated with the portfolio. |
| tags             | core | hstore_csv |
