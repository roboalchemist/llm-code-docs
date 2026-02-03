# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_packet_mirroring.dataset.md

---
title: Packet Mirroring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Packet Mirroring
---

# Packet Mirroring

Packet Mirroring in Google Cloud captures network traffic from specified VM instances, forwarding copies of the packets to a collector destination for analysis. It helps with network monitoring, intrusion detection, and troubleshooting by allowing inspection of traffic patterns without affecting production workloads.

```
gcp.compute_packet_mirroring
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| collector_ilb        | core | json          | The Forwarding Rule resource of typeloadBalancingScheme=INTERNAL that will be used as collector for mirrored traffic. The specified forwarding rule must have isMirroringCollector set to true.                                                                                                                                                                                                                                                     |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| enable               | core | string        | Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE.                                                                                                                                                                                                                                                                                |
| filter               | core | json          | Filter for mirrored traffic. If unspecified, all IPv4 traffic is mirrored.                                                                                                                                                                                                                                                                                                                                                                          |
| id                   | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                        |
| kind                 | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#packetMirroring for packet mirrorings.                                                                                                                                                                                                                                                                                                                                               |
| labels               | core | array<string> |
| mirrored_resources   | core | json          | PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.                                                                                                                                                                                                                                                          |
| name                 | core | string        | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| network              | core | json          | Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.                                                                                                                                                                                                                                            |
| organization_id      | core | string        |
| parent               | core | string        |
| priority             | core | int64         | The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535.                                                                                                                                             |
| project_id           | core | string        |
| project_number       | core | string        |
| region               | core | string        | [Output Only] URI of the region where the packetMirroring resides.                                                                                                                                                                                                                                                                                                                                                                                  |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
