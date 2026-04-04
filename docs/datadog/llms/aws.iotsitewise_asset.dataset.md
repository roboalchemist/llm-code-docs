# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_asset.dataset.md

---
title: IoT SiteWise Asset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Asset
---

# IoT SiteWise Asset

An IoT SiteWise Asset in AWS represents a digital model of a physical device, process, or piece of equipment. It defines the structure, measurements, metrics, and relationships of industrial assets, enabling you to collect, organize, and analyze data from industrial operations. Assets can be composed of other assets, allowing hierarchical modeling of complex systems.

```
aws.iotsitewise_asset
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                                           | Description |
| ------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| asset_arn                       | core | string     | The ARN of the asset, which has the following format. arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}                                                                            |
| asset_composite_model_summaries | core | json       | The list of the immediate child custom composite model summaries for the asset.                                                                                                                     |
| asset_composite_models          | core | json       | The composite models for the asset.                                                                                                                                                                 |
| asset_creation_date             | core | timestamp  | The date the asset was created, in Unix epoch time.                                                                                                                                                 |
| asset_description               | core | string     | A description for the asset.                                                                                                                                                                        |
| asset_external_id               | core | string     | The external ID of the asset, if any.                                                                                                                                                               |
| asset_hierarchies               | core | json       | A list of asset hierarchies that each contain a hierarchyId. A hierarchy specifies allowed parent/child asset relationships.                                                                        |
| asset_id                        | core | string     | The ID of the asset, in UUID format.                                                                                                                                                                |
| asset_last_update_date          | core | timestamp  | The date the asset was last updated, in Unix epoch time.                                                                                                                                            |
| asset_model_id                  | core | string     | The ID of the asset model that was used to create the asset.                                                                                                                                        |
| asset_name                      | core | string     | The name of the asset.                                                                                                                                                                              |
| asset_properties                | core | json       | The list of asset properties for the asset. This object doesn't include properties that you define in composite models. You can find composite model properties in the assetCompositeModels object. |
| asset_status                    | core | json       | The current status of the asset, which contains a state and any error message.                                                                                                                      |
| tags                            | core | hstore_csv |
