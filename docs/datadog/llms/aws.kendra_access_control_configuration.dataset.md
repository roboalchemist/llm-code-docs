# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_access_control_configuration.dataset.md

---
title: Amazon Kendra Access Control Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Amazon Kendra Access Control
  Configuration
---

# Amazon Kendra Access Control Configuration

Amazon Kendra Access Control Configuration defines how access permissions are managed for a Kendra index. It specifies which users or groups can view or search specific documents based on identity or group membership. This configuration helps enforce fine-grained access control, ensuring that search results are filtered according to user permissions and organizational security policies.

```
aws.kendra_access_control_configuration
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                                                                                                                                          | Description |
| -------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| access_control_list              | core | json       | Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents. |
| account_id                       | core | string     |
| description                      | core | string     | The description for the access control configuration.                                                                                                                                                                              |
| error_message                    | core | string     | The error message containing details if there are issues processing the access control configuration.                                                                                                                              |
| hierarchical_access_control_list | core | json       | The list of principal lists that define the hierarchy for which documents users should have access to.                                                                                                                             |
| name                             | core | string     | The name for the access control configuration.                                                                                                                                                                                     |
| tags                             | core | hstore_csv |
