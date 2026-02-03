# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_certificateprovider.dataset.md

---
title: Iot Certificateprovider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Certificateprovider
---

# Iot Certificateprovider

This table represents the iot_certificateprovider resource from Amazon Web Services.

```
aws.iot_certificateprovider
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                     | Description |
| ------------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| account_default_for_operations | core | array<string> | A list of the operations that the certificate provider will use to generate certificates. Valid value: <code>CreateCertificateFromCsr</code>. |
| account_id                     | core | string        |
| certificate_provider_arn       | core | string        | The ARN of the certificate provider.                                                                                                          |
| certificate_provider_name      | core | string        | The name of the certificate provider.                                                                                                         |
| creation_date                  | core | timestamp     | The date-time string that indicates when the certificate provider was created.                                                                |
| lambda_function_arn            | core | string        | The Lambda function ARN that's associated with the certificate provider.                                                                      |
| last_modified_date             | core | timestamp     | The date-time string that indicates when the certificate provider was last updated.                                                           |
| tags                           | core | hstore_csv    |
