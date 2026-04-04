# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.managedblockchain_accessor.dataset.md

---
title: Managed Blockchain Accessor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Blockchain Accessor
---

# Managed Blockchain Accessor

Managed Blockchain Accessor in AWS is a resource that provides the necessary credentials and configuration for a member to interact with a blockchain network. It acts as a secure access point, enabling applications to connect to the network without directly managing cryptographic materials. This simplifies integration and ensures secure communication with the blockchain.

```
aws.managedblockchain_accessor
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                                    | Description |
| ------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| arn           | core | string     | The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.             |
| billing_token | core | string     | The billing token is a property of the Accessor. Use this token to when making calls to the blockchain network. The billing token is used to track your accessor token for billing requests. |
| creation_date | core | timestamp  | The creation date and time of the accessor.                                                                                                                                                  |
| id            | core | string     | The unique identifier of the accessor.                                                                                                                                                       |
| network_type  | core | string     | The blockchain network that the Accessor token is created for.                                                                                                                               |
| status        | core | string     | The current status of the accessor.                                                                                                                                                          |
| tags          | core | hstore_csv |
| type          | core | string     | The type of the accessor. Currently, accessor type is restricted to BILLING_TOKEN.                                                                                                           |
