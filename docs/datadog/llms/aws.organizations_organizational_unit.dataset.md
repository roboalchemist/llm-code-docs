# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.organizations_organizational_unit.dataset.md

---
title: Organizational Unit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Organizational Unit
---

# Organizational Unit

An Organizational Unit in AWS Organizations is a container used to group accounts within an organization. It helps structure accounts into a hierarchy, making it easier to apply policies, manage permissions, and organize resources according to business or security needs.

```
aws.organizations_organizational_unit
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| arn        | core | string     | The Amazon Resource Name (ARN) of this OU. For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the Amazon Web Services Service Authorization Reference.                                                                                                                                                                        |
| id         | core | string     | The unique identifier (ID) associated with this OU. The ID is unique to the organization only. The regex pattern for an organizational unit ID string requires "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits. |
| name       | core | string     | The friendly name of this OU. The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.                                                                                                                                                                                                                 |
| tags       | core | hstore_csv |
