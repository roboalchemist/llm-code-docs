# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.location_place_index.dataset.md

---
title: Location Place Index
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Location Place Index
---

# Location Place Index

Location Place Index in AWS is part of the Amazon Location Service. It provides geocoding and reverse geocoding capabilities, allowing you to convert addresses into geographic coordinates and vice versa. This resource helps applications search for places, validate addresses, and display location-based information on maps.

```
aws.location_place_index
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                       | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| create_time               | core | timestamp  | The timestamp for when the place index resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.                                                                                       |
| data_source               | core | string     | The data provider of geospatial data. Values can be one of the following: Esri Grab Here For more information about data providers, see Amazon Location Service data providers.                 |
| data_source_configuration | core | json       | The specified data storage option for requesting Places.                                                                                                                                        |
| description               | core | string     | The optional description for the place index resource.                                                                                                                                          |
| index_arn                 | core | string     | The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across Amazon Web Services. Format example: arn:aws:geo:region:account-id:place-index/ExamplePlaceIndex |
| index_name                | core | string     | The name of the place index resource being described.                                                                                                                                           |
| pricing_plan              | core | string     | No longer used. Always returns RequestBasedUsage.                                                                                                                                               |
| tags                      | core | hstore_csv |
| update_time               | core | timestamp  | The timestamp for when the place index resource was last updated in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.                                                                                  |
