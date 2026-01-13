# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iottwinmaker_component_type.dataset.md

---
title: IoT TwinMaker Component Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT TwinMaker Component Type
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iottwinmaker_component_type.dataset/index.html
---

# IoT TwinMaker Component Type

IoT TwinMaker Component Type in AWS defines reusable building blocks that represent the behavior, properties, and data of components within a digital twin. It allows you to model real-world entities by specifying schemas, functions, and data connectors that can be applied across multiple digital twin models. This helps standardize how different systems and devices are represented, making it easier to build, manage, and scale digital twin applications.

```
aws.iottwinmaker_component_type
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                     | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| arn                       | core | string        | The ARN of the component type.                                                                                                                |
| component_type_id         | core | string        | The ID of the component type.                                                                                                                 |
| component_type_name       | core | string        | The component type name.                                                                                                                      |
| composite_component_types | core | string        | This is an object that maps strings to compositeComponentTypes of the componentType. CompositeComponentType is referenced by componentTypeId. |
| creation_date_time        | core | timestamp     | The date and time when the component type was created.                                                                                        |
| description               | core | string        | The description of the component type.                                                                                                        |
| extends_from              | core | array<string> | The name of the parent component type that this component type extends.                                                                       |
| functions                 | core | string        | An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.                 |
| is_abstract               | core | bool          | A Boolean value that specifies whether the component type is abstract.                                                                        |
| is_schema_initialized     | core | bool          | A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.                   |
| is_singleton              | core | bool          | A Boolean value that specifies whether an entity can have more than one component of this type.                                               |
| property_definitions      | core | string        | An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.      |
| property_groups           | core | string        | The maximum number of results to return at one time. The default is 25. Valid Range: Minimum value of 1. Maximum value of 250.                |
| status                    | core | json          | The current status of the component type.                                                                                                     |
| sync_source               | core | string        | The syncSource of the SyncJob, if this entity was created by a SyncJob.                                                                       |
| tags                      | core | hstore        |
| update_date_time          | core | timestamp     | The date and time when the component was last updated.                                                                                        |
| workspace_id              | core | string        | The ID of the workspace that contains the component type.                                                                                     |
