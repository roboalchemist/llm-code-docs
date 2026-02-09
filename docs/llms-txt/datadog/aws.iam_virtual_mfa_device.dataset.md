# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_virtual_mfa_device.dataset.md

---
title: IAM Virtual MFA device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Virtual MFA device
---

# IAM Virtual MFA device

An IAM Virtual MFA device in AWS is a software-based multi-factor authentication option that generates time-based one-time passwords. It can be configured on a user's smartphone or other compatible device using an authenticator app. This adds an extra layer of security to AWS accounts by requiring both a password and the MFA code during sign-in.

```
aws.iam_virtual_mfa_device
```

## Fields

| Title         | ID   | Type       | Data Type                                                      | Description |
| ------------- | ---- | ---------- | -------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| enable_date   | core | timestamp  | The date and time on which the virtual MFA device was enabled. |
| serial_number | core | string     | The serial number associated with VirtualMFADevice.            |
| tags          | core | hstore_csv |
| user          | core | json       | The IAM user associated with this virtual MFA device.          |
