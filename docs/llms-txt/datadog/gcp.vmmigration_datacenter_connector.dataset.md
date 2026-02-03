# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_datacenter_connector.dataset.md

---
title: DatacenterConnector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DatacenterConnector
---

# DatacenterConnector

DatacenterConnector in Google Cloud is a component used to connect on-premises environments with Google Cloud for migration purposes. It enables communication between local workloads and Google's migration services, allowing data and virtual machines to be discovered, replicated, and moved to the cloud securely.

```
gcp.vmmigration_datacenter_connector
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                | Description |
| -------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| ancestors                        | core | array<string> |
| appliance_infrastructure_version | core | string        | Output only. Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance. |
| appliance_software_version       | core | string        | Output only. Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance.                                             |
| available_versions               | core | json          | Output only. The available versions for updating this appliance.                                                                                                                         |
| bucket                           | core | string        | Output only. The communication channel between the datacenter connector and Google Cloud.                                                                                                |
| create_time                      | core | timestamp     | Output only. The time the connector was created (as an API call, not when it was actually installed).                                                                                    |
| datadog_display_name             | core | string        |
| error                            | core | json          | Output only. Provides details on the state of the Datacenter Connector in case of an error.                                                                                              |
| labels                           | core | array<string> |
| name                             | core | string        | Output only. The connector's name.                                                                                                                                                       |
| organization_id                  | core | string        |
| parent                           | core | string        |
| project_id                       | core | string        |
| project_number                   | core | string        |
| region_id                        | core | string        |
| registration_id                  | core | string        | Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.         |
| resource_name                    | core | string        |
| service_account                  | core | string        | The service account to use in the connector when communicating with the cloud.                                                                                                           |
| state                            | core | string        | Output only. State of the DatacenterConnector, as determined by the health checks.                                                                                                       |
| state_time                       | core | timestamp     | Output only. The time the state was last set.                                                                                                                                            |
| tags                             | core | hstore_csv    |
| update_time                      | core | timestamp     | Output only. The last time the connector was updated with an API call.                                                                                                                   |
| upgrade_status                   | core | json          | Output only. The status of the current / last upgradeAppliance operation.                                                                                                                |
| version                          | core | string        | The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.                                           |
| zone_id                          | core | string        |
