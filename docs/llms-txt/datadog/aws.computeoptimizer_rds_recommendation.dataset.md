# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.computeoptimizer_rds_recommendation.dataset.md

---
title: Computeoptimizer RDS Recommendation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Computeoptimizer RDS Recommendation
---

# Computeoptimizer RDS Recommendation

This table represents the Computeoptimizer RDS Recommendation resource from Amazon Web Services.

```
aws.computeoptimizer_rds_recommendation
```

## Fields

| Title                 | ID   | Type       | Data Type | Description |
| --------------------- | ---- | ---------- | --------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| rdsdb_recommendations | core | json       |
| tags                  | core | hstore_csv |
