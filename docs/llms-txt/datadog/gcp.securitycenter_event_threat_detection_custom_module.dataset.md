# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.securitycenter_event_threat_detection_custom_module.dataset.md

---
title: Event Threat Detection Custom Module
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Threat Detection Custom Module
---

# Event Threat Detection Custom Module

Event Threat Detection Custom Module in Google Cloud allows users to create and manage custom detection rules for identifying security threats within their environment. It extends the built-in Event Threat Detection service by enabling organizations to define their own logic for detecting suspicious activity based on logs and events. This helps tailor threat detection to specific security needs and compliance requirements.

```
gcp.securitycenter_event_threat_detection_custom_module
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestor_module      | core | string        | Output only. The closest ancestor module that this module inherits the enablement state from. The format is the same as the EventThreatDetectionCustomModule resource name.                                                                                                                                                          |
| ancestors            | core | array<string> |
| cloud_provider       | core | string        | The cloud provider of the custom module.                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | The description for the module.                                                                                                                                                                                                                                                                                                      |
| enablement_state     | core | string        | The state of enablement for the module at the given level of the hierarchy.                                                                                                                                                                                                                                                          |
| gcp_display_name     | core | string        | The human readable name to be displayed for the module.                                                                                                                                                                                                                                                                              |
| labels               | core | array<string> |
| last_editor          | core | string        | Output only. The editor the module was last updated by.                                                                                                                                                                                                                                                                              |
| name                 | core | string        | Immutable. The resource name of the Event Threat Detection custom module. Its format is: * `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`. * `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`. * `projects/{project}/eventThreatDetectionSettings/customModules/{module}`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Type for the module. e.g. CONFIGURABLE_BAD_IP.                                                                                                                                                                                                                                                                                       |
| update_time          | core | timestamp     | Output only. The time the module was last updated.                                                                                                                                                                                                                                                                                   |
| zone_id              | core | string        |
