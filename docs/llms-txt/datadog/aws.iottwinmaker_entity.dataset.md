# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iottwinmaker_entity.dataset.md

---
title: IoT TwinMaker Entity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT TwinMaker Entity
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iottwinmaker_entity.dataset/index.html
---

# IoT TwinMaker Entity

IoT TwinMaker Entity in AWS represents a digital twin component that models real-world systems, such as equipment, processes, or environments. An entity can include properties, components, and relationships that define its behavior and connections to other entities. It allows users to build a virtual representation of physical assets, enabling monitoring, simulation, and analysis within IoT TwinMaker applications.

```
aws.iottwinmaker_entity
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                                 | Description |
| --------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| are_all_components_returned | core | bool      | This flag notes whether all components are returned in the API response. The maximum number of components returned is 30. |
| arn                         | core | string    | The ARN of the entity.                                                                                                    |
| components                  | core | string    | An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.    |
| creation_date_time          | core | timestamp | The date and time when the entity was created.                                                                            |
| description                 | core | string    | The description of the entity.                                                                                            |
| entity_id                   | core | string    | The ID of the entity.                                                                                                     |
| entity_name                 | core | string    | The name of the entity.                                                                                                   |
| has_child_entities          | core | bool      | A Boolean value that specifies whether the entity has associated child entities.                                          |
| parent_entity_id            | core | string    | The ID of the parent entity for this entity.                                                                              |
| status                      | core | json      | The current status of the entity.                                                                                         |
| sync_source                 | core | string    | The syncSource of the sync job, if this entity was created by a sync job.                                                 |
| tags                        | core | hstore    |
| update_date_time            | core | timestamp | The date and time when the entity was last updated.                                                                       |
| workspace_id                | core | string    | The ID of the workspace.                                                                                                  |
