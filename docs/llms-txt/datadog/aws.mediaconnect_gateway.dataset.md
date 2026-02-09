# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconnect_gateway.dataset.md

---
title: Elemental MediaConnect Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaConnect Gateway
---

# Elemental MediaConnect Gateway

Elemental MediaConnect Gateway is an AWS resource that enables secure and reliable transport of live video between on-premises networks and the AWS Cloud. It acts as a bridge, allowing video workflows to extend beyond the cloud into local environments, supporting hybrid video distribution and contribution use cases.

```
aws.mediaconnect_gateway
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                                                                                                                     | Description |
| ------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| egress_cidr_blocks | core | array<string> | The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. |
| gateway_arn        | core | string        | The Amazon Resource Name (ARN) of the gateway.                                                                                                                                                                                                |
| gateway_messages   | core | json          | Messages with information about the gateway.                                                                                                                                                                                                  |
| gateway_state      | core | string        | The current status of the gateway.                                                                                                                                                                                                            |
| name               | core | string        | The name of the gateway. This name can not be modified after the gateway is created.                                                                                                                                                          |
| networks           | core | json          | The list of networks in the gateway.                                                                                                                                                                                                          |
| tags               | core | hstore_csv    |
