# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.network_capture_filter.dataset.md

---
title: Capture Filter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Capture Filter
---

# Capture Filter

A Capture Filter in Oracle Cloud Infrastructure (OCI) is a virtual network resource that defines rules to include or exclude specific types of traffic for packet capture. It allows you to control which network packets are mirrored when using a VCN traffic mirroring session. By specifying criteria such as source and destination IP addresses, ports, and protocols, Capture Filters help reduce data volume and focus analysis on relevant traffic, improving performance and efficiency in network monitoring and troubleshooting.

```
oci.network_capture_filter
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                          | Description |
| ----------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| cloud_account_id              | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                              |
| cloud_account_name            | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                                  |
| cloud_provider                | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                                    |
| cloud_tags                    | core | hstore     |
| compartment_id                | core | string     | The value to assign to the compartment_id property of this CaptureFilter.                                                                                                                                                                                                                          |
| created_at                    | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                                           |
| filter_type                   | core | string     | The value to assign to the filter_type property of this CaptureFilter. Allowed values for this property are: "VTAP", "FLOWLOG", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.                                                        |
| flow_log_capture_filter_rules | core | json       | The value to assign to the flow_log_capture_filter_rules property of this CaptureFilter.                                                                                                                                                                                                           |
| freeform_tags                 | core | hstore     | The value to assign to the freeform_tags property of this CaptureFilter.                                                                                                                                                                                                                           |
| id                            | core | string     | The value to assign to the id property of this CaptureFilter.                                                                                                                                                                                                                                      |
| lifecycle_state               | core | string     | The value to assign to the lifecycle_state property of this CaptureFilter. Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name                          | core | string     | The name of this resource.                                                                                                                                                                                                                                                                         |
| region_id                     | core | string     | The region this resource resides within.                                                                                                                                                                                                                                                           |
| resource_type                 | core | string     | The name of the resource type.                                                                                                                                                                                                                                                                     |
| tags                          | core | hstore_csv |
| time_created                  | core | timestamp  | The value to assign to the time_created property of this CaptureFilter.                                                                                                                                                                                                                            |
| updated_at                    | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                             |
| vtap_capture_filter_rules     | core | json       | The value to assign to the vtap_capture_filter_rules property of this CaptureFilter.                                                                                                                                                                                                               |
| zone_id                       | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                             |
