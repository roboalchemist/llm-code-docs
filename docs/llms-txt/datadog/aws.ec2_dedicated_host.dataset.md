# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_dedicated_host.dataset.md

---
title: EC2 Dedicated Host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Dedicated Host
---

# EC2 Dedicated Host

This table represents the EC2 Dedicated Host resource from Amazon Web Services.

```
aws.ec2_dedicated_host
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                  | Description |
| --------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| account_id                              | core | string     |
| allocation_time                         | core | timestamp  | The time that the Dedicated Host was allocated.                                                                                                                                                                                                                                                            |
| allows_multiple_instance_types          | core | string     | Indicates whether the Dedicated Host supports multiple instance types of the same instance family. If the value is <code>on</code>, the Dedicated Host supports multiple instance types in the instance family. If the value is <code>off</code>, the Dedicated Host supports a single instance type only. |
| asset_id                                | core | string     | The ID of the Outpost hardware asset on which the Dedicated Host is allocated.                                                                                                                                                                                                                             |
| auto_placement                          | core | string     | Whether auto-placement is on or off.                                                                                                                                                                                                                                                                       |
| availability_zone                       | core | string     | The Availability Zone of the Dedicated Host.                                                                                                                                                                                                                                                               |
| availability_zone_id                    | core | string     | The ID of the Availability Zone in which the Dedicated Host is allocated.                                                                                                                                                                                                                                  |
| available_capacity                      | core | json       | Information about the instances running on the Dedicated Host.                                                                                                                                                                                                                                             |
| client_token                            | core | string     | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.                                                            |
| host_arn                                | core | string     |
| host_id                                 | core | string     | The ID of the Dedicated Host.                                                                                                                                                                                                                                                                              |
| host_maintenance                        | core | string     | Indicates whether host maintenance is enabled or disabled for the Dedicated Host.                                                                                                                                                                                                                          |
| host_properties                         | core | json       | The hardware specifications of the Dedicated Host.                                                                                                                                                                                                                                                         |
| host_recovery                           | core | string     | Indicates whether host recovery is enabled or disabled for the Dedicated Host.                                                                                                                                                                                                                             |
| host_reservation_id                     | core | string     | The reservation ID of the Dedicated Host. This returns a <code>null</code> response if the Dedicated Host doesn't have an associated reservation.                                                                                                                                                          |
| instances                               | core | json       | The IDs and instance type that are currently running on the Dedicated Host.                                                                                                                                                                                                                                |
| member_of_service_linked_resource_group | core | bool       | Indicates whether the Dedicated Host is in a host resource group. If <b>memberOfServiceLinkedResourceGroup</b> is <code>true</code>, the host is in a host resource group; otherwise, it is not.                                                                                                           |
| outpost_arn                             | core | string     | The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which the Dedicated Host is allocated.                                                                                                                                                                                                |
| owner_id                                | core | string     | The ID of the Amazon Web Services account that owns the Dedicated Host.                                                                                                                                                                                                                                    |
| release_time                            | core | timestamp  | The time that the Dedicated Host was released.                                                                                                                                                                                                                                                             |
| state                                   | core | string     | The Dedicated Host's state.                                                                                                                                                                                                                                                                                |
| tags                                    | core | hstore_csv |
