# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_network_analyzer_configuration.dataset.md

---
title: IoT Wireless Network Analyzer Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > IoT Wireless Network Analyzer
  Configuration
---

# IoT Wireless Network Analyzer Configuration

The IoT Wireless Network Analyzer Configuration in AWS provides details about a network analyzer setup used to monitor and debug wireless device communications. It allows you to define which wireless devices, gateways, and resources are included in the analysis, helping to capture traffic and troubleshoot connectivity or performance issues in IoT wireless networks.

```
aws.iotwireless_network_analyzer_configuration
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                      | Description |
| ----------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| arn               | core | string        | The Amazon Resource Name of the new resource.                                                  |
| description       | core | string        | The description of the new resource.                                                           |
| multicast_groups  | core | array<string> | List of multicast group resources that have been added to the network analyzer configuration.  |
| name              | core | string        | Name of the network analyzer configuration.                                                    |
| tags              | core | hstore_csv    |
| trace_content     | core | json          | Trace content for your wireless devices, gateways, and multicast groups.                       |
| wireless_devices  | core | array<string> | List of wireless device resources that have been added to the network analyzer configuration.  |
| wireless_gateways | core | array<string> | List of wireless gateway resources that have been added to the network analyzer configuration. |
