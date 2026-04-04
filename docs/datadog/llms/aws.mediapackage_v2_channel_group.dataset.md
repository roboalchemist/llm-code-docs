# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_v2_channel_group.dataset.md

---
title: Mediapackage V2 Channel Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage V2 Channel Group
---

# Mediapackage V2 Channel Group

This table represents the mediapackage_v2_channel_group resource from Amazon Web Services.

```
aws.mediapackage_v2_channel_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                   | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) associated with the resource.                                                                                                |
| channel_group_name | core | string     | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. |
| created_at         | core | timestamp  | The date and time the channel group was created.                                                                                                            |
| description        | core | string     | The description for your channel group.                                                                                                                     |
| e_tag              | core | string     | The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.                  |
| egress_domain      | core | string     | The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.        |
| modified_at        | core | timestamp  | The date and time the channel group was modified.                                                                                                           |
| tags               | core | hstore_csv |
