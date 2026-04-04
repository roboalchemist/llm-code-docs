# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_certificate.dataset.md

---
title: Lightsail Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Certificate
---

# Lightsail Certificate

Lightsail Certificate in AWS is a managed SSL/TLS certificate used with Amazon Lightsail resources, such as load balancers and distributions, to enable secure HTTPS connections. It simplifies certificate creation, validation, and renewal, allowing developers to protect their applications without managing complex certificate infrastructure.

```
aws.lightsail_certificate
```

## Fields

| Title              | ID   | Type       | Data Type                                          | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| certificate_arn    | core | string     | The Amazon Resource Name (ARN) of the certificate. |
| certificate_detail | core | json       | An object that describes a certificate in detail.  |
| certificate_name   | core | string     | The name of the certificate.                       |
| domain_name        | core | string     | The domain name of the certificate.                |
| tags               | core | hstore_csv |
