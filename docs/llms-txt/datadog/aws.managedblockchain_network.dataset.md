# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.managedblockchain_network.dataset.md

---
title: Managed Blockchain Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Blockchain Network
---

# Managed Blockchain Network

Managed Blockchain Network in AWS represents a blockchain network created and managed through Amazon Managed Blockchain. It provides details about the network such as its framework (like Hyperledger Fabric or Ethereum), status, configuration, and member information. This resource allows organizations to set up and operate scalable blockchain networks without the overhead of managing infrastructure, enabling secure and decentralized applications.

```
aws.managedblockchain_network
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                       | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |
| creation_date             | core | timestamp  | The date and time that the network was created.                                                                                                                                 |
| description               | core | string     | Attributes of the blockchain framework for the network.                                                                                                                         |
| framework                 | core | string     | The blockchain framework that the network uses.                                                                                                                                 |
| framework_attributes      | core | json       | Attributes of the blockchain framework that the network uses.                                                                                                                   |
| framework_version         | core | string     | The version of the blockchain framework that the network uses.                                                                                                                  |
| id                        | core | string     | The unique identifier of the network.                                                                                                                                           |
| name                      | core | string     | The name of the network.                                                                                                                                                        |
| status                    | core | string     | The current status of the network.                                                                                                                                              |
| tags                      | core | hstore_csv |
| voting_policy             | core | json       | The voting rules that the network uses to decide if a proposal is accepted.                                                                                                     |
| vpc_endpoint_service_name | core | string     | The VPC endpoint service name of the VPC endpoint service of the network. Members use the VPC endpoint service name to create a VPC endpoint to access network resources.       |
