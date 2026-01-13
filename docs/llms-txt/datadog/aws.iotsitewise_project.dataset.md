# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_project.dataset.md

---
title: IoT SiteWise Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Project
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotsitewise_project.dataset/index.html
---

# IoT SiteWise Project

An IoT SiteWise Project in AWS is a container that lets you organize and manage assets, dashboards, and visualizations for industrial data. It provides a collaborative space where teams can access and analyze equipment and process information collected through IoT SiteWise, enabling better monitoring and decision-making.

```
aws.iotsitewise_project
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                      | Description |
| ------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| portal_id                | core | string    | The ID of the portal that the project is in.                                                                                   |
| project_arn              | core | string    | The ARN of the project, which has the following format. arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId} |
| project_creation_date    | core | timestamp | The date the project was created, in Unix epoch time.                                                                          |
| project_description      | core | string    | The project's description.                                                                                                     |
| project_id               | core | string    | The ID of the project.                                                                                                         |
| project_last_update_date | core | timestamp | The date the project was last updated, in Unix epoch time.                                                                     |
| project_name             | core | string    | The name of the project.                                                                                                       |
| tags                     | core | hstore    |
