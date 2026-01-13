# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iottwinmaker_scene.dataset.md

---
title: IoT TwinMaker Scene
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT TwinMaker Scene
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iottwinmaker_scene.dataset/index.html
---

# IoT TwinMaker Scene

IoT TwinMaker Scene in AWS represents a 3D scene used to visualize digital twins of real-world systems. It allows you to define and manage visual elements, assets, and data connections within a scene, enabling interactive exploration of equipment, facilities, or processes. This resource helps create immersive dashboards that combine sensor data, simulations, and operational context for monitoring and analysis.

```
aws.iottwinmaker_scene
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                     | Description |
| ------------------------ | ---- | ------------- | ----------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| arn                      | core | string        | The ARN of the scene.                                                         |
| capabilities             | core | array<string> | A list of capabilities that the scene uses to render.                         |
| content_location         | core | string        | The relative path that specifies the location of the content definition file. |
| creation_date_time       | core | timestamp     | The date and time when the scene was created.                                 |
| description              | core | string        | The description of the scene.                                                 |
| error                    | core | json          | The SceneResponse error.                                                      |
| generated_scene_metadata | core | hstore        | The generated scene metadata.                                                 |
| scene_id                 | core | string        | The ID of the scene.                                                          |
| scene_metadata           | core | hstore        | The response metadata.                                                        |
| tags                     | core | hstore        |
| update_date_time         | core | timestamp     | The date and time when the scene was last updated.                            |
| workspace_id             | core | string        | The ID of the workspace that contains the scene.                              |
