# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amp_scraper.dataset.md

---
title: Managed Service for Prometheus Scraper
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Managed Service for Prometheus
  Scraper
---

# Managed Service for Prometheus Scraper

Managed Service for Prometheus Scraper in AWS is a fully managed component that collects metrics from your workloads and infrastructure using Prometheus-compatible scraping. It eliminates the need to run and maintain your own Prometheus servers, providing scalable and reliable metric ingestion directly into Amazon Managed Service for Prometheus. This allows you to monitor applications with minimal operational overhead.

```
aws.amp_scraper
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| alias                | core | string     | (Optional) A name associated with the scraper.                                                                                                                                                                                        |
| arn                  | core | string     | The Amazon Resource Name (ARN) of the scraper. For example, arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34.                                                                                         |
| created_at           | core | timestamp  | The date and time that the scraper was created.                                                                                                                                                                                       |
| destination          | core | json       | The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.                                                                                                                                                     |
| last_modified_at     | core | timestamp  | The date and time that the scraper was last modified.                                                                                                                                                                                 |
| role_arn             | core | string     | The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf. For example, arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example. |
| role_configuration   | core | json       | This structure displays information about the IAM roles used for cross-account scraping configuration.                                                                                                                                |
| scrape_configuration | core | json       | The configuration in use by the scraper.                                                                                                                                                                                              |
| scraper_id           | core | string     | The ID of the scraper. For example, s-example1-1234-abcd-5678-ef9012abcd34.                                                                                                                                                           |
| status               | core | json       | A structure that contains the current status of the scraper.                                                                                                                                                                          |
| status_reason        | core | string     | If there is a failure, the reason for the failure.                                                                                                                                                                                    |
| tags                 | core | hstore_csv |
