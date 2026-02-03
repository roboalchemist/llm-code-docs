# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.application_signals_slo.dataset.md

---
title: Application Signals Slo
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Application Signals Slo
---

# Application Signals Slo

This table represents the application_signals_slo resource from Amazon Web Services.

```gdscript3
aws.application_signals_slo
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                        | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| arn                      | core | string     | The ARN of this SLO.                                                                                                                                                                                                                             |
| burn_rate_configurations | core | json       | Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO. |
| created_time             | core | timestamp  | The date and time that this SLO was created. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.                                                            |
| description              | core | string     | The description that you created for this SLO.                                                                                                                                                                                                   |
| evaluation_type          | core | string     | Displays whether this is a period-based SLO or a request-based SLO.                                                                                                                                                                              |
| goal                     | core | json       |
| last_updated_time        | core | timestamp  | The time that this SLO was most recently updated. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.                                                       |
| metric_source_type       | core | string     | Displays the SLI metric source type for this SLO. Supported types are: <ul> <li> Service operation </li> <li> Service dependency </li> <li> CloudWatch metric </li> </ul>                                                                        |
| name                     | core | string     | The name of this SLO.                                                                                                                                                                                                                            |
| request_based_sli        | core | json       | A structure containing information about the performance metric that this SLO monitors, if this is a request-based SLO.                                                                                                                          |
| sli                      | core | json       | A structure containing information about the performance metric that this SLO monitors, if this is a period-based SLO.                                                                                                                           |
| tags                     | core | hstore_csv |
