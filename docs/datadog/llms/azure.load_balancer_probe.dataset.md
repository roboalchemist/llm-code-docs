# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.load_balancer_probe.dataset.md

---
title: Load Balancer Probe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Load Balancer Probe
---

# Load Balancer Probe

This table represents the Load Balancer Probe resource from Microsoft Azure.

```gdscript3
azure.load_balancer_probe
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string     |
| etag                 | core | string     | A unique read-only string that changes whenever the resource is updated.                                                                                                                                                                                                                                     |
| id                   | core | string     | Resource ID.                                                                                                                                                                                                                                                                                                 |
| interval_in_seconds  | core | int64      | The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5. |
| load_balancing_rules | core | json       | The load balancer rules that use this probe.                                                                                                                                                                                                                                                                 |
| location             | core | string     |
| name                 | core | string     | The name of the resource that is unique within the set of probes used by the load balancer. This name can be used to access the resource.                                                                                                                                                                    |
| number_of_probes     | core | int64      | The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.                                                                     |
| port                 | core | int64      | The port for communicating the probe. Possible values range from 1 to 65535, inclusive.                                                                                                                                                                                                                      |
| protocol             | core | string     | The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful.                                                                     |
| provisioning_state   | core | string     | The provisioning state of the probe resource.                                                                                                                                                                                                                                                                |
| request_path         | core | string     | The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value.                                                                                                                                               |
| resource_group       | core | string     |
| subscription_id      | core | string     |
| subscription_name    | core | string     |
| tags                 | core | hstore_csv |
| type                 | core | string     | Type of the resource.                                                                                                                                                                                                                                                                                        |
