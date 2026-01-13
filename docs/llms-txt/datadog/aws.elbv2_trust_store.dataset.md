# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elbv2_trust_store.dataset.md

---
title: Elastic Load Balancing Trust Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elastic Load Balancing Trust Store
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elbv2_trust_store.dataset/index.html
---

# Elastic Load Balancing Trust Store

An Elastic Load Balancing Trust Store in AWS is a resource that allows you to manage and store digital certificates used for mutual TLS authentication. It provides a centralized way to configure and maintain trusted certificate authorities, enabling secure communication between clients and your load balancer.

```
aws.elbv2_trust_store
```

## Fields

| Title                     | ID   | Type   | Data Type                                              | Description |
| ------------------------- | ---- | ------ | ------------------------------------------------------ | ----------- |
| _key                      | core | string |
| account_id                | core | string |
| name                      | core | string | The name of the trust store.                           |
| number_of_ca_certificates | core | int64  | The number of ca certificates in the trust store.      |
| status                    | core | string | The current status of the trust store.                 |
| tags                      | core | hstore |
| total_revoked_entries     | core | int64  | The number of revoked certificates in the trust store. |
| trust_store_arn           | core | string | The Amazon Resource Name (ARN) of the trust store.     |
