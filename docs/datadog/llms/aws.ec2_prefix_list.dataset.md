# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_prefix_list.dataset.md

---
title: EC2 Prefix List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Prefix List
---

# EC2 Prefix List

This table represents the EC2 Prefix List resource from Amazon Web Services.

```
aws.ec2_prefix_list
```

## Fields

| Title            | ID   | Type       | Data Type                                           | Description |
| ---------------- | ---- | ---------- | --------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| address_family   | core | string     | The IP address version.                             |
| entries          | core | json       | Information about the prefix list entries.          |
| max_entries      | core | int64      | The maximum number of entries for the prefix list.  |
| owner_id         | core | string     | The ID of the owner of the prefix list.             |
| prefix_list_arn  | core | string     | The Amazon Resource Name (ARN) for the prefix list. |
| prefix_list_id   | core | string     | The ID of the prefix list.                          |
| prefix_list_name | core | string     | The name of the prefix list.                        |
| state            | core | string     | The current state of the prefix list.               |
| state_message    | core | string     | The state message.                                  |
| tags             | core | hstore_csv |
| version          | core | int64      | The version of the prefix list.                     |
