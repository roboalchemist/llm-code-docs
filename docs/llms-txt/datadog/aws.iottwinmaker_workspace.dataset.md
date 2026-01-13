# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iottwinmaker_workspace.dataset.md

---
title: IoT TwinMaker Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT TwinMaker Workspace
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iottwinmaker_workspace.dataset/index.html
---

# IoT TwinMaker Workspace

AWS IoT TwinMaker Workspace is a container for digital twin data and configurations. It provides the environment where you can integrate data sources, define 3D scenes, and manage entities that represent real-world systems. Workspaces serve as the foundation for building and visualizing digital twins, enabling you to model physical environments and monitor them in real time.

```
aws.iottwinmaker_workspace
```

## Fields

| Title              | ID   | Type          | Data Type                                                                          | Description |
| ------------------ | ---- | ------------- | ---------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| arn                | core | string        | The ARN of the workspace.                                                          |
| creation_date_time | core | timestamp     | The date and time when the workspace was created.                                  |
| description        | core | string        | The description of the workspace.                                                  |
| linked_services    | core | array<string> | A list of services that are linked to the workspace.                               |
| role               | core | string        | The ARN of the execution role associated with the workspace.                       |
| s3_location        | core | string        | The ARN of the S3 bucket where resources associated with the workspace are stored. |
| tags               | core | hstore        |
| update_date_time   | core | timestamp     | The date and time when the workspace was last updated.                             |
| workspace_id       | core | string        | The ID of the workspace.                                                           |
