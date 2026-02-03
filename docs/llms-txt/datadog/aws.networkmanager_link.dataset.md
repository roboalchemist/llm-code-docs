# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_link.dataset.md

---
title: Network Manager Link
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Link
---

# Network Manager Link

Network Manager Link in AWS represents a connection between a customer's on-premises network and AWS, or between different network sites. It defines the characteristics of the link such as bandwidth, provider, and type, and is used within AWS Network Manager to model and monitor global network topology.

```
aws.networkmanager_link
```

## Fields

| Title             | ID   | Type       | Data Type                                    | Description |
| ----------------- | ---- | ---------- | -------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| bandwidth         | core | json       | The bandwidth for the link.                  |
| created_at        | core | timestamp  | The date and time that the link was created. |
| description       | core | string     | The description of the link.                 |
| global_network_id | core | string     | The ID of the global network.                |
| link_arn          | core | string     | The Amazon Resource Name (ARN) of the link.  |
| link_id           | core | string     | The ID of the link.                          |
| provider          | core | string     | The provider of the link.                    |
| site_id           | core | string     | The ID of the site.                          |
| state             | core | string     | The state of the link.                       |
| tags              | core | hstore_csv |
| type              | core | string     | The type of the link.                        |
