# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.b2bi_partnership.dataset.md

---
title: B2B Data Interchange Partnership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > B2B Data Interchange Partnership
---

# B2B Data Interchange Partnership

B2B Data Interchange Partnership in AWS B2BI represents the configuration and relationship between two trading partners for secure electronic data exchange. It defines how partners connect, authenticate, and exchange business documents such as purchase orders or invoices. This resource helps organizations automate and manage partner integrations without building custom data exchange solutions.

```
aws.b2bi_partnership
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                      | Description |
| ------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| capabilities       | core | array<string> | Returns one or more capabilities associated with this partnership.                                                                             |
| capability_options | core | json          | Contains the details for an Outbound EDI capability.                                                                                           |
| created_at         | core | timestamp     | Returns a timestamp for creation date and time of the partnership.                                                                             |
| email              | core | string        | Returns the email address associated with this trading partner.                                                                                |
| modified_at        | core | timestamp     | Returns a timestamp that identifies the most recent date and time that the partnership was modified.                                           |
| name               | core | string        | Returns the display name of the partnership                                                                                                    |
| partnership_arn    | core | string        | Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer. |
| partnership_id     | core | string        | Returns the unique, system-generated identifier for a partnership.                                                                             |
| phone              | core | string        | Returns the phone number associated with the partnership.                                                                                      |
| profile_id         | core | string        | Returns the unique, system-generated identifier for the profile connected to this partnership.                                                 |
| tags               | core | hstore_csv    |
| trading_partner_id | core | string        | Returns the unique identifier for the partner for this partnership.                                                                            |
