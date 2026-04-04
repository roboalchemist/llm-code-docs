# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.location_map.dataset.md

---
title: Location Service Map
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Location Service Map
---

# Location Service Map

AWS Location Service Map is a managed resource that provides customizable map tiles for applications. It allows developers to integrate maps from trusted data providers without managing infrastructure. With this service, you can render maps, control style and appearance, and use them alongside other Location Service features like geocoding, routing, and tracking. It is designed to support location-based applications with secure, scalable, and cost-effective mapping capabilities.

```
aws.location_map
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                    | Description |
| ------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| configuration | core | json       | Specifies the map tile style selected from a partner data provider.                                                                                                          |
| create_time   | core | timestamp  | The timestamp for when the map resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.                                                                            |
| data_source   | core | string     | Specifies the data provider for the associated map tiles.                                                                                                                    |
| description   | core | string     | The optional description for the map resource.                                                                                                                               |
| map_arn       | core | string     | The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all Amazon Web Services. Format example: arn:aws:geo:region:account-id:map/ExampleMap |
| map_name      | core | string     | The map style selected from an available provider.                                                                                                                           |
| pricing_plan  | core | string     | No longer used. Always returns RequestBasedUsage.                                                                                                                            |
| tags          | core | hstore_csv |
| update_time   | core | timestamp  | The timestamp for when the map resource was last update in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.                                                                        |
