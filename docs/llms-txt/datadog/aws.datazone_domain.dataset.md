# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datazone_domain.dataset.md

---
title: DataZone Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataZone Domain
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datazone_domain.dataset/index.html
---

# DataZone Domain

An AWS DataZone Domain is a logical boundary within AWS DataZone that organizes and governs data assets, projects, and users. It provides a centralized environment where administrators can manage access, metadata, and policies for data sharing and collaboration. Domains help ensure secure and compliant data usage across teams and applications.

```
aws.datazone_domain
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                    | Description |
| --------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| arn                   | core | string    | The ARN of the specified Amazon DataZone domain.                                                                                                             |
| created_at            | core | timestamp | The timestamp of when the Amazon DataZone domain was created.                                                                                                |
| description           | core | string    | The description of the Amazon DataZone domain.                                                                                                               |
| domain_execution_role | core | string    | The domain execution role with which the Amazon DataZone domain is created.                                                                                  |
| domain_version        | core | string    | The version of the domain.                                                                                                                                   |
| id                    | core | string    | The identifier of the specified Amazon DataZone domain.                                                                                                      |
| kms_key_identifier    | core | string    | The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. |
| last_updated_at       | core | timestamp | The timestamp of when the Amazon DataZone domain was last updated.                                                                                           |
| name                  | core | string    | The name of the Amazon DataZone domain.                                                                                                                      |
| portal_url            | core | string    | The URL of the data portal for this Amazon DataZone domain.                                                                                                  |
| root_domain_unit_id   | core | string    | The ID of the root domain in Amazon Datazone.                                                                                                                |
| service_role          | core | string    | The service role of the domain.                                                                                                                              |
| single_sign_on        | core | json      | The single sing-on option of the specified Amazon DataZone domain.                                                                                           |
| status                | core | string    | The status of the specified Amazon DataZone domain.                                                                                                          |
| tags                  | core | hstore    |
