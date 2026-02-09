# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_network.dataset.md

---
title: Elemental MediaLive Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Network
---

# Elemental MediaLive Network

AWS Elemental MediaLive Network represents the network configuration and connectivity details used by MediaLive channels and inputs. It defines how live video streams are transmitted between MediaLive resources, including input attachments, output destinations, and VPC interfaces. This resource helps manage secure, reliable, and scalable live video workflows within AWS infrastructure.

```
aws.medialive_network
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| arn                    | core | string        | The ARN of this Network. It is automatically assigned when the Network is created.                                                                                                                                                                                                                                                                                      |
| associated_cluster_ids | core | array<string> | Placeholder documentation for __listOf__string                                                                                                                                                                                                                                                                                                                          |
| id                     | core | string        | The ID of the Network. Unique in the AWS account. The ID is the resource-id portion of the ARN.                                                                                                                                                                                                                                                                         |
| ip_pools               | core | json          | An array of IpPools in your organization's network that identify a collection of IP addresses in your organization's network that are reserved for use in MediaLive Anywhere. MediaLive Anywhere uses these IP addresses for Push inputs (in both Bridge and NAT networks) and for output destinations (only in Bridge networks). Each IpPool specifies one CIDR block. |
| name                   | core | string        | The name that you specified for this Network.                                                                                                                                                                                                                                                                                                                           |
| routes                 | core | json          | An array of routes that MediaLive Anywhere needs to know about in order to route encoding traffic.                                                                                                                                                                                                                                                                      |
| state                  | core | string        | The current state of the Network. Only MediaLive Anywhere can change the state.                                                                                                                                                                                                                                                                                         |
| tags                   | core | hstore_csv    |
