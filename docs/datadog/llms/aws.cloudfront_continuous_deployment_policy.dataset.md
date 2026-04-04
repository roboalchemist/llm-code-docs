# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_continuous_deployment_policy.dataset.md

---
title: CloudFront Continuous Deployment Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > CloudFront Continuous Deployment
  Policy
---

# CloudFront Continuous Deployment Policy

A CloudFront Continuous Deployment Policy in AWS defines how traffic is safely shifted between two CloudFront distributions, typically a primary and a staging distribution. It allows controlled testing of configuration changes or new features by gradually routing a percentage of viewer requests to the staging distribution. This helps validate updates in real-world conditions without impacting all users at once, reducing risk and enabling safer rollouts.

```
aws.cloudfront_continuous_deployment_policy
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                           | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| continuous_deployment_policy | core | json       | A continuous deployment policy.                                                     |
| e_tag                        | core | string     | The version identifier for the current version of the continuous deployment policy. |
| tags                         | core | hstore_csv |
