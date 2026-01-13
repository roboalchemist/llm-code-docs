# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_source_network.dataset.md

---
title: Elastic Disaster Recovery Source Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery Source
  Network
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.drs_source_network.dataset/index.html
---

# Elastic Disaster Recovery Source Network

Elastic Disaster Recovery Source Network in AWS represents the network configuration of a source environment that is being protected by AWS Elastic Disaster Recovery (DRS). It defines the networking details of the source system, such as subnets and routing, to ensure accurate replication and recovery in the target AWS environment. This resource helps maintain consistent connectivity and network settings during failover or recovery operations.

```
aws.drs_source_network
```

## Fields

| Title                      | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                         | Description |
| -------------------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string |
| account_id                 | core | string |
| arn                        | core | string | The ARN of the Source Network.                                                                                                                                                                                                                                                                                    |
| cfn_stack_name             | core | string | CloudFormation stack name that was deployed for recovering the Source Network.                                                                                                                                                                                                                                    |
| last_recovery              | core | json   | An object containing information regarding the last recovery of the Source Network.                                                                                                                                                                                                                               |
| launched_vpc_id            | core | string | ID of the recovered VPC following Source Network recovery.                                                                                                                                                                                                                                                        |
| replication_status         | core | string | Status of Source Network Replication. Possible values: (a) STOPPED - Source Network is not replicating. (b) IN_PROGRESS - Source Network is being replicated. (c) PROTECTED - Source Network was replicated successfully and is being synchronized for changes. (d) ERROR - Source Network replication has failed |
| replication_status_details | core | string | Error details in case Source Network replication status is ERROR.                                                                                                                                                                                                                                                 |
| source_account_id          | core | string | Account ID containing the VPC protected by the Source Network.                                                                                                                                                                                                                                                    |
| source_network_id          | core | string | Source Network ID.                                                                                                                                                                                                                                                                                                |
| source_region              | core | string | Region containing the VPC protected by the Source Network.                                                                                                                                                                                                                                                        |
| source_vpc_id              | core | string | VPC ID protected by the Source Network.                                                                                                                                                                                                                                                                           |
| tags                       | core | hstore |
