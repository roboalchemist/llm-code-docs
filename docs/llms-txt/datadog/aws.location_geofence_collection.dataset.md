# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.location_geofence_collection.dataset.md

---
title: Location Service Geofence Collection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Location Service Geofence Collection
---

# Location Service Geofence Collection

Location Service Geofence Collection in AWS is a resource that stores and manages geofences, which are virtual boundaries defined around geographic areas. It allows applications to track device positions relative to these boundaries and trigger events when devices enter or exit them. This resource is useful for location-based services such as asset tracking, delivery monitoring, and geospatial alerts.

```
aws.location_geofence_collection
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                 | Description |
| ------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| collection_arn           | core | string     | The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all Amazon Web Services. Format example: arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection |
| collection_name          | core | string     | The name of the geofence collection.                                                                                                                                                                                                      |
| create_time              | core | timestamp  | The timestamp for when the geofence resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ                                                                                                                                     |
| description              | core | string     | The optional description for the geofence collection.                                                                                                                                                                                     |
| geofence_count           | core | int64      | The number of geofences in the geofence collection.                                                                                                                                                                                       |
| kms_key_id               | core | string     | A key identifier for an Amazon Web Services KMS customer managed key assigned to the Amazon Location resource                                                                                                                             |
| pricing_plan             | core | string     | No longer used. Always returns RequestBasedUsage.                                                                                                                                                                                         |
| pricing_plan_data_source | core | string     | No longer used. Always returns an empty string.                                                                                                                                                                                           |
| tags                     | core | hstore_csv |
| update_time              | core | timestamp  | The timestamp for when the geofence collection was last updated in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ                                                                                                                              |
