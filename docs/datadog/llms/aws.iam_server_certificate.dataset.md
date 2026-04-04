# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_server_certificate.dataset.md

---
title: IAM Server Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Server Certificate
---

# IAM Server Certificate

An IAM Server Certificate in AWS is a resource that stores SSL/TLS certificates and their associated private keys for use with AWS services. It allows you to manage and deploy certificates to secure communication between clients and AWS resources such as Elastic Load Balancers or CloudFront distributions.

```
aws.iam_server_certificate
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                     | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see IAM identifiers in the IAM User Guide. |
| expiration              | core | timestamp  | The date on which the certificate is set to expire.                                                                                                                           |
| path                    | core | string     | The path to the server certificate. For more information about paths, see IAM identifiers in the IAM User Guide.                                                              |
| server_certificate_id   | core | string     | The stable and unique string identifying the server certificate. For more information about IDs, see IAM identifiers in the IAM User Guide.                                   |
| server_certificate_name | core | string     | The name that identifies the server certificate.                                                                                                                              |
| tags                    | core | hstore_csv |
| upload_date             | core | timestamp  | The date when the server certificate was uploaded.                                                                                                                            |
