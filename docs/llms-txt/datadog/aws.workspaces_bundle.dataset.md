# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_bundle.dataset.md

---
title: WorkSpaces Bundle
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkSpaces Bundle
---

# WorkSpaces Bundle

An AWS WorkSpaces Bundle is a predefined package of compute resources, storage, and software configurations used to create virtual desktops in Amazon WorkSpaces. It defines the hardware specifications such as CPU, memory, and root and user volume sizes, along with the operating system and applications included. Bundles allow you to quickly deploy consistent desktop environments for users.

```
aws.workspaces_bundle
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                         | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| bundle_id         | core | string     | The identifier of the bundle.                                                                                                     |
| bundle_type       | core | string     | The type of WorkSpace bundle.                                                                                                     |
| compute_type      | core | json       | The compute type of the bundle. For more information, see Amazon WorkSpaces Bundles.                                              |
| creation_time     | core | timestamp  | The time when the bundle was created.                                                                                             |
| description       | core | string     | The description of the bundle.                                                                                                    |
| image_id          | core | string     | The identifier of the image that was used to create the bundle.                                                                   |
| last_updated_time | core | timestamp  | The last time that the bundle was updated.                                                                                        |
| name              | core | string     | The name of the bundle.                                                                                                           |
| owner             | core | string     | The owner of the bundle. This is the account identifier of the owner, or AMAZON if the bundle is provided by Amazon Web Services. |
| root_storage      | core | json       | The size of the root volume.                                                                                                      |
| state             | core | string     | The state of the WorkSpace bundle.                                                                                                |
| tags              | core | hstore_csv |
| user_storage      | core | json       | The size of the user volume.                                                                                                      |
