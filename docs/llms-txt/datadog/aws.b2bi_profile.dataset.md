# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.b2bi_profile.dataset.md

---
title: B2B Data Interchange Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > B2B Data Interchange Profile
---

# B2B Data Interchange Profile

B2B Data Interchange Profile in AWS B2BI defines the configuration and details of a trading partner's profile used for secure electronic data interchange. It contains information such as identifiers, communication settings, and supported document formats, enabling businesses to exchange data reliably with partners.

```
aws.b2bi_profile
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                      | Description |
| -------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| business_name  | core | string     | Returns the name for the business associated with this profile.                                                                                |
| created_at     | core | timestamp  | Returns a timestamp for creation date and time of the transformer.                                                                             |
| email          | core | string     | Returns the email address associated with this customer profile.                                                                               |
| log_group_name | core | string     | Returns the name of the logging group.                                                                                                         |
| logging        | core | string     | Returns whether or not logging is enabled for this profile.                                                                                    |
| modified_at    | core | timestamp  | Returns a timestamp for last time the profile was modified.                                                                                    |
| name           | core | string     | Returns the name of the profile, used to identify it.                                                                                          |
| phone          | core | string     | Returns the phone number associated with the profile.                                                                                          |
| profile_arn    | core | string     | Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer. |
| profile_id     | core | string     | Returns the unique, system-generated identifier for the profile.                                                                               |
| tags           | core | hstore_csv |
