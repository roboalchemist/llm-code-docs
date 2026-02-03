# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appstream_app_block.dataset.md

---
title: AppStream 2.0 App Block
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppStream 2.0 App Block
---

# AppStream 2.0 App Block

An AppStream 2.0 App Block in AWS is a resource that packages applications and their dependencies so they can be streamed to users without installing them on local devices. It allows administrators to manage and update applications centrally, ensuring consistent performance and security. App Blocks are combined with application packages and images to deliver a complete virtualized app experience through AppStream 2.0.

```
aws.appstream_app_block
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| app_block_errors          | core | json       | The errors of the app block.                                                                                                                                                                                                                                                                                                                                        |
| arn                       | core | string     | The ARN of the app block.                                                                                                                                                                                                                                                                                                                                           |
| created_time              | core | timestamp  | The created time of the app block.                                                                                                                                                                                                                                                                                                                                  |
| description               | core | string     | The description of the app block.                                                                                                                                                                                                                                                                                                                                   |
| name                      | core | string     | The name of the app block.                                                                                                                                                                                                                                                                                                                                          |
| packaging_type            | core | string     | The packaging type of the app block.                                                                                                                                                                                                                                                                                                                                |
| post_setup_script_details | core | json       | The post setup script details of the app block. This only applies to app blocks with PackagingType APPSTREAM2.                                                                                                                                                                                                                                                      |
| setup_script_details      | core | json       | The setup script details of the app block. This only applies to app blocks with PackagingType CUSTOM.                                                                                                                                                                                                                                                               |
| source_s3_location        | core | json       | The source S3 location of the app block.                                                                                                                                                                                                                                                                                                                            |
| state                     | core | string     | The state of the app block. An app block with WorkSpaces Applications packaging will be in the INACTIVE state if no application package (VHD) is assigned to it. After an application package (VHD) is created by an app block builder for an app block, it becomes ACTIVE. Custom app blocks are always in the ACTIVE state and no action is required to use them. |
| tags                      | core | hstore_csv |
