# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rum_app_monitor.dataset.md

---
title: CloudWatch RUM App Monitor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudWatch RUM App Monitor
---

# CloudWatch RUM App Monitor

CloudWatch RUM App Monitor is an AWS resource that collects and analyzes real user monitoring data from web applications. It helps track performance, detect errors, and measure user experience in real time. By capturing metrics such as page load times, client-side errors, and user interactions, it provides insights to improve application reliability and responsiveness.

```
aws.rum_app_monitor
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                    | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| app_monitor_configuration   | core | json          | A structure that contains much of the configuration data for the app monitor.                                                                                |
| created                     | core | string        | The date and time that this app monitor was created.                                                                                                         |
| custom_events               | core | json          | Specifies whether this app monitor allows the web client to define and send custom events. For more information about custom events, see Send custom events. |
| data_storage                | core | json          | A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.            |
| deobfuscation_configuration | core | json          | A structure that contains the configuration for how an app monitor can deobfuscate stack traces.                                                             |
| domain                      | core | string        | The top-level internet domain name for which your application has administrative authority.                                                                  |
| domain_list                 | core | array<string> | List the domain names for which your application has administrative authority.                                                                               |
| id                          | core | string        | The unique ID of this app monitor.                                                                                                                           |
| last_modified               | core | string        | The date and time of the most recent changes to this app monitor's configuration.                                                                            |
| name                        | core | string        | The name of the app monitor.                                                                                                                                 |
| state                       | core | string        | The current state of the app monitor.                                                                                                                        |
| tags                        | core | hstore_csv    |
