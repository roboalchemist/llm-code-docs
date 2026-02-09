# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53profiles_profile.dataset.md

---
title: "Amazon Route\_53 Profile"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Amazon Route\_53 Profile"
---

# Amazon Route 53 Profile

Amazon Route 53 Profile is a configuration resource that defines and manages DNS profiles within Route 53. It allows users to group and apply DNS settings, routing policies, and resolver configurations consistently across multiple domains or accounts. This helps simplify DNS management, improve consistency, and streamline operations in complex environments.

```
aws.route53profiles_profile
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                  | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| arn               | core | string     | The Amazon Resource Name (ARN) of the Profile.                                                             |
| client_token      | core | string     | The ClientToken value that was assigned when the Profile was created.                                      |
| creation_time     | core | timestamp  | The date and time that the Profile was created, in Unix time format and Coordinated Universal Time (UTC).  |
| id                | core | string     | ID of the Profile.                                                                                         |
| modification_time | core | timestamp  | The date and time that the Profile was modified, in Unix time format and Coordinated Universal Time (UTC). |
| name              | core | string     | Name of the Profile.                                                                                       |
| owner_id          | core | string     | Amazon Web Services account ID of the Profile owner.                                                       |
| share_status      | core | string     | Sharing status for the Profile.                                                                            |
| status            | core | string     | The status for the Profile.                                                                                |
| status_message    | core | string     | Status message that includes additiona information about the Profile.                                      |
| tags              | core | hstore_csv |
