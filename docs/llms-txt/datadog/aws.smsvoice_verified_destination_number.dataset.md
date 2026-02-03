# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_verified_destination_number.dataset.md

---
title: Pinpoint SMS and Voice Verified Destination Number
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Pinpoint SMS and Voice Verified
  Destination Number
---

# Pinpoint SMS and Voice Verified Destination Number

A Pinpoint SMS and Voice Verified Destination Number in AWS represents a phone number that has been validated for use with Amazon Pinpoint SMS and Voice services. Verification ensures that the number is authorized to receive messages or calls, helping prevent misuse and ensuring compliance with messaging regulations.

```
aws.smsvoice_verified_destination_number
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                 | Description |
| ------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| created_timestamp               | core | timestamp  | The time when the destination phone number was created, in UNIX epoch time format.                                                                                        |
| destination_phone_number        | core | string     | The verified destination phone number, in E.164 format.                                                                                                                   |
| status                          | core | string     | The status of the verified destination phone number. PENDING: The phone number hasn't been verified yet. VERIFIED: The phone number is verified and can receive messages. |
| tags                            | core | hstore_csv |
| verified_destination_number_arn | core | string     | The Amazon Resource Name (ARN) for the verified destination phone number.                                                                                                 |
| verified_destination_number_id  | core | string     | The unique identifier for the verified destination phone number.                                                                                                          |
