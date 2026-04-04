# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.network_devices.dataset.md

---
title: Network Devices
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Devices
---

# Network Devices

The Network Devices dataset provides metadata and status information about all network devices discovered and monitored through Datadog's Network Device Monitoring (NDM). Each device is uniquely identified and enriched with details such as vendor, device type, location, IP address, and operational health. This dataset enables network and infrastructure teams to track device inventory, assess connectivity and reachability, and monitor the overall health of routers, switches, firewalls, and other critical devices across their environments.

```
dd.network_devices
```

## Fields

| Title                 | ID            | Type | Data Type | Description                                                                                                                                                                                   |
| --------------------- | ------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device Identifier     | device_id     | core | string    | A unique internal identifier assigned to each network device by Datadog. Used to correlate and distinguish devices across monitoring data.                                                    |
| SNMP System Object ID | sys_object_id | core | string    | The SNMP sysObjectID for the device, identifying the vendor and device family/model. Useful for mapping devices to profiles and vendor-specific metadata.                                     |
| Device Name           | name          | core | string    | The name of the device as discovered (e.g., hostname or sysName for SNMP devices).                                                                                                            |
| Namespace             | namespace     | core | string    | A logical grouping or environment identifier (e.g., tenant, cluster, or configuration domain) used to isolate and scope devices.                                                              |
| Device Description    | description   | core | string    | The system description for the device (sysDescr in SNMP), typically containing vendor-provided details about hardware, OS, version, and build information.                                    |
| Device Status         | status        | core | string    | The high-level health status of the device as reported by Datadog.                                                                                                                            |
| Ping Reachability     | ping_status   | core | string    | Status of ICMP ping checks to the device. Indicates if the device is responding to network pings.                                                                                             |
| SNMP Profile          | profile       | core | string    | The Datadog NDM profile applied to the device, typically derived from its vendor and model (e.g., cisco-router, juniper-switch). Profiles determine which metrics and metadata are collected. |
| Vendor                | vendor        | core | string    | The manufacturer or provider of the device (e.g., Cisco, Juniper, Palo Alto Networks).                                                                                                        |
| Subnet                | subnet        | core | string    | The IP subnet (in CIDR notation) associated with the device. Useful for network segmentation and inventory grouping.                                                                          |
| IP Address            | ip_address    | core | string    | The primary IPv4 address used by Datadog to monitor the device.                                                                                                                               |
| Device Type           | device_type   | core | string    | The functional category of the device (e.g., router, switch, firewall, load balancer).                                                                                                        |
| Location              | location      | core | string    | A logical or physical location identifier for the device (e.g., datacenter, site, or region). May be derived from configuration or tagging.                                                   |
| Model                 | model         | core | string    | The model type of the device.                                                                                                                                                                 |
| Tags                  | tags          | core | hstore    | Key-value metadata tags associated with the device. Tags provide flexible categorization (e.g., environment, owner team, role).                                                               |
| Agent Host            | agent_host    | tag  | string    | The hostname of the Datadog Agent responsible for collecting SNMP data from the network device.                                                                                               |
| Agent Version         | agent_version | tag  | string    | The version of the Datadog Agent running the SNMP check that monitors the device.                                                                                                             |
