# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_certificate.dataset.md

---
title: DMS Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Certificate
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dms_certificate.dataset/index.html
---

# DMS Certificate

DMS Certificate in AWS Database Migration Service is a managed resource that stores Secure Sockets Layer (SSL) certificates used to encrypt connections between replication instances and database endpoints. It ensures secure communication during data migration by validating the identity of servers and protecting data in transit.

```
aws.dms_certificate
```

## Fields

| Title                     | ID   | Type      | Data Type                                                                                                                                                                                                     | Description |
| ------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| certificate_arn           | core | string    | The Amazon Resource Name (ARN) for the certificate.                                                                                                                                                           |
| certificate_creation_date | core | timestamp | The date that the certificate was created.                                                                                                                                                                    |
| certificate_identifier    | core | string    | A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens. |
| certificate_owner         | core | string    | The owner of the certificate.                                                                                                                                                                                 |
| certificate_pem           | core | string    | The contents of a .pem file, which contains an X.509 certificate.                                                                                                                                             |
| key_length                | core | int64     | The key length of the cryptographic algorithm being used.                                                                                                                                                     |
| signing_algorithm         | core | string    | The signing algorithm for the certificate.                                                                                                                                                                    |
| tags                      | core | hstore    |
| valid_from_date           | core | timestamp | The beginning date that the certificate is valid.                                                                                                                                                             |
| valid_to_date             | core | timestamp | The final date that the certificate is valid.                                                                                                                                                                 |
