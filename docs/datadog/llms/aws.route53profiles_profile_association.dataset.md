# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53profiles_profile_association.dataset.md

---
title: Route 53 Profiles Profile Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Profiles Profile
  Association
---

# Route 53 Profiles Profile Association

Associates a Route 53 Profiles profile with a specific AWS resource, such as a VPC. This enables the resource to use the DNS settings, configurations, and policies defined in the associated profile, simplifying DNS management and ensuring consistent behavior across multiple resources.

```
aws.route53profiles_profile_association
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                              | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| creation_time     | core | timestamp  | The date and time that the Profile association was created, in Unix time format and Coordinated Universal Time (UTC).  |
| id                | core | string     | ID of the Profile association.                                                                                         |
| modification_time | core | timestamp  | The date and time that the Profile association was modified, in Unix time format and Coordinated Universal Time (UTC). |
| name              | core | string     | Name of the Profile association.                                                                                       |
| owner_id          | core | string     | Amazon Web Services account ID of the Profile association owner.                                                       |
| profile_id        | core | string     | ID of the Profile.                                                                                                     |
| resource_id       | core | string     | The Amazon Resource Name (ARN) of the VPC.                                                                             |
| status            | core | string     | Status of the Profile association.                                                                                     |
| status_message    | core | string     | Additional information about the Profile association.                                                                  |
| tags              | core | hstore_csv |
