# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.service_quotas_service_quota.dataset.md

---
title: Service Quotas Service Quota
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Quotas Service Quota
---

# Service Quotas Service Quota

This table represents the Service Quotas Service Quota resource from Amazon Web Services.

```
aws.service_quotas_service_quota
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                       | Description |
| ---------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| adjustable             | core | bool       | Indicates whether the quota value can be increased.                                                                                                                                                             |
| error_reason           | core | json       | The error code and error reason.                                                                                                                                                                                |
| global_quota           | core | bool       | Indicates whether the quota is global.                                                                                                                                                                          |
| period                 | core | json       | The period of time.                                                                                                                                                                                             |
| quota_applied_at_level | core | string     | Specifies at which level of granularity that the quota value is applied.                                                                                                                                        |
| quota_arn              | core | string     | The Amazon Resource Name (ARN) of the quota.                                                                                                                                                                    |
| quota_code             | core | string     | Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want. |
| quota_context          | core | json       | The context for this service quota.                                                                                                                                                                             |
| quota_name             | core | string     | Specifies the quota name.                                                                                                                                                                                       |
| service_code           | core | string     | Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.                                                                     |
| service_name           | core | string     | Specifies the service name.                                                                                                                                                                                     |
| tags                   | core | hstore_csv |
| unit                   | core | string     | The unit of measurement.                                                                                                                                                                                        |
| usage_metric           | core | json       | Information about the measurement.                                                                                                                                                                              |
| value                  | core | float64    | The quota value.                                                                                                                                                                                                |
