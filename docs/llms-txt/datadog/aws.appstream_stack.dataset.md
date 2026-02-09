# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appstream_stack.dataset.md

---
title: AppStream 2.0 Stack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppStream 2.0 Stack
---

# AppStream 2.0 Stack

An AppStream 2.0 Stack in AWS defines the configuration for delivering applications or desktops to users. It specifies settings such as user access policies, storage options, and application settings, and connects to fleets of streaming instances. Stacks provide the user-facing environment where applications are launched and managed.

```
aws.appstream_stack
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                          | Description |
| ----------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| access_endpoints              | core | json          | The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.                                |
| account_id                    | core | string        |
| application_settings          | core | json          | The persistent application settings for users of the stack.                                                                                                                                        |
| arn                           | core | string        | The ARN of the stack.                                                                                                                                                                              |
| created_time                  | core | timestamp     | The time the stack was created.                                                                                                                                                                    |
| description                   | core | string        | The description to display.                                                                                                                                                                        |
| embed_host_domains            | core | array<string> | The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions. |
| feedback_url                  | core | string        | The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.                                                          |
| name                          | core | string        | The name of the stack.                                                                                                                                                                             |
| redirect_url                  | core | string        | The URL that users are redirected to after their streaming session ends.                                                                                                                           |
| stack_errors                  | core | json          | The errors for the stack.                                                                                                                                                                          |
| storage_connectors            | core | json          | The storage connectors to enable.                                                                                                                                                                  |
| streaming_experience_settings | core | json          | The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.                                                       |
| tags                          | core | hstore_csv    |
| user_settings                 | core | json          | The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.                                                                          |
