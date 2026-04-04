# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_service.dataset.md

---
title: VPC Lattice Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Service
---

# VPC Lattice Service

This table represents the VPC Lattice Service resource from Amazon Web Services.

```
aws.vpc_lattice_service
```

## Fields

| Title              | ID   | Type       | Data Type                                                                | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) of the service.                           |
| auth_type          | core | string     | The type of IAM policy.                                                  |
| certificate_arn    | core | string     | The Amazon Resource Name (ARN) of the certificate.                       |
| created_at         | core | timestamp  | The date and time that the service was created, in ISO-8601 format.      |
| custom_domain_name | core | string     | The custom domain name of the service.                                   |
| dns_entry          | core | json       | The DNS name of the service.                                             |
| failure_code       | core | string     | The failure code.                                                        |
| failure_message    | core | string     | The failure message.                                                     |
| id                 | core | string     | The ID of the service.                                                   |
| last_updated_at    | core | timestamp  | The date and time that the service was last updated, in ISO-8601 format. |
| name               | core | string     | The name of the service.                                                 |
| status             | core | string     | The status of the service.                                               |
| tags               | core | hstore_csv |
