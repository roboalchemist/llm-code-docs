# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appstream_application.dataset.md

---
title: AppStream 2.0 Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppStream 2.0 Application
---

# AppStream 2.0 Application

An AppStream 2.0 Application in AWS represents a software application that can be streamed to users through AppStream 2.0 fleets and stacks. It defines the application's launch configuration, including the executable path, display name, and icon, allowing users to access and run the application securely without installing it locally.

```
aws.appstream_application
```

## Fields

| Title             | ID   | Type          | Data Type                                                                    | Description |
| ----------------- | ---- | ------------- | ---------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| app_block_arn     | core | string        | The app block ARN of the application.                                        |
| arn               | core | string        | The ARN of the application.                                                  |
| created_time      | core | timestamp     | The time at which the application was created within the app block.          |
| description       | core | string        | The description of the application.                                          |
| enabled           | core | bool          | If there is a problem, the application can be disabled after image creation. |
| icon_s3_location  | core | json          | The S3 location of the application icon.                                     |
| icon_url          | core | string        | The URL for the application icon. This URL might be time-limited.            |
| instance_families | core | array<string> | The instance families for the application.                                   |
| launch_parameters | core | string        | The arguments that are passed to the application at launch.                  |
| launch_path       | core | string        | The path to the application executable in the instance.                      |
| metadata          | core | hstore        | Additional attributes that describe the application.                         |
| name              | core | string        | The name of the application.                                                 |
| platforms         | core | array<string> | The platforms on which the application can run.                              |
| tags              | core | hstore_csv    |
| working_directory | core | string        | The working directory for the application.                                   |
