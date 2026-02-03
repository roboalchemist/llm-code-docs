# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.availability_zone.dataset.md

---
title: Availability Zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Availability Zone
---

# Availability Zone

This table represents the Availability Zone resource from Amazon Web Services.

```
aws.availability_zone
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                                                                            | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| availability_zone_arn | core | string     |
| group_name            | core | string     | For Availability Zones, this parameter has the same value as the Region name. For Local Zones, the name of the associated group, for example <code>us-west-2-lax-1</code>. For Wavelength Zones, the name of the associated group, for example <code>us-east-1-wl1-bos-wlz-1</code>. |
| messages              | core | json       | Any messages about the Availability Zone, Local Zone, or Wavelength Zone.                                                                                                                                                                                                            |
| network_border_group  | core | string     | The name of the network border group.                                                                                                                                                                                                                                                |
| opt_in_status         | core | string     | For Availability Zones, this parameter always has the value of <code>opt-in-not-required</code>. For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are <code>opted-in</code>, and <code>not-opted-in</code>.                            |
| parent_zone_id        | core | string     | The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.                                                                                                                                                               |
| parent_zone_name      | core | string     | The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.                                                                                                                                                             |
| region_name           | core | string     | The name of the Region.                                                                                                                                                                                                                                                              |
| state                 | core | string     | The state of the Availability Zone, Local Zone, or Wavelength Zone. This value is always <code>available</code>.                                                                                                                                                                     |
| tags                  | core | hstore_csv |
| zone_id               | core | string     | The ID of the Availability Zone, Local Zone, or Wavelength Zone.                                                                                                                                                                                                                     |
| zone_name             | core | string     | The name of the Availability Zone, Local Zone, or Wavelength Zone.                                                                                                                                                                                                                   |
| zone_type             | core | string     | The type of zone. The valid values are <code>availability-zone</code>, <code>local-zone</code>, and <code>wavelength-zone</code>.                                                                                                                                                    |
