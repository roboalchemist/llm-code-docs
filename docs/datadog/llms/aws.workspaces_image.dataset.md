# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_image.dataset.md

---
title: WorkSpaces Image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkSpaces Image
---

# WorkSpaces Image

An AWS WorkSpaces Image is a custom virtual desktop image that includes the operating system, applications, and settings you define. It allows you to standardize and quickly deploy WorkSpaces with a consistent configuration across your organization. Images can be created from existing WorkSpaces and then used to launch new ones, simplifying management and ensuring uniformity.

```
aws.workspaces_image
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                                                     | Description |
| ---------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| created          | core | timestamp  | The date when the image was created. If the image has been shared, the Amazon Web Services account that the image has been shared with sees the original creation date of the image.                          |
| description      | core | string     | The description of the image.                                                                                                                                                                                 |
| error_code       | core | string     | The error code that is returned for the image.                                                                                                                                                                |
| error_details    | core | json       | Additional details of the error returned for the image, including the possible causes of the errors and troubleshooting information.                                                                          |
| error_message    | core | string     | The text of the error message that is returned for the image.                                                                                                                                                 |
| image_id         | core | string     | The identifier of the image.                                                                                                                                                                                  |
| name             | core | string     | The name of the image.                                                                                                                                                                                        |
| operating_system | core | json       | The operating system that the image is running.                                                                                                                                                               |
| owner_account_id | core | string     | The identifier of the Amazon Web Services account that owns the image.                                                                                                                                        |
| required_tenancy | core | string     | Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to DEDICATED. For more information, see Bring Your Own Windows Desktop Images. |
| state            | core | string     | The status of the image.                                                                                                                                                                                      |
| tags             | core | hstore_csv |
| updates          | core | json       | The updates (if any) that are available for the specified image.                                                                                                                                              |
