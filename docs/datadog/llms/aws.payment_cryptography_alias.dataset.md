# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.payment_cryptography_alias.dataset.md

---
title: Payment Cryptography Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Payment Cryptography Alias
---

# Payment Cryptography Alias

This table represents the Payment Cryptography Alias resource from Amazon Web Services.

```
aws.payment_cryptography_alias
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                     | Description |
| ---------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| alias_name | core | string     | A friendly name that you can use to refer to a key. The value must begin with <code>alias/</code>. <important> Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output. </important> |
| key_arn    | core | string     | The <code>KeyARN</code> of the key associated with the alias.                                                                                                                                                                                                                 |
| tags       | core | hstore_csv |
