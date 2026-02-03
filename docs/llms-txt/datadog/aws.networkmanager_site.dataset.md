# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_site.dataset.md

---
title: Network Manager Site
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Site
---

# Network Manager Site

A Network Manager Site in AWS represents a physical location, such as a branch office, data center, or other on-premises facility, that is part of a global network managed through AWS Network Manager. It provides metadata about the site, including its name, description, and location details, enabling centralized visibility and management of network resources across multiple regions and environments.

```
aws.networkmanager_site
```

## Fields

| Title             | ID   | Type       | Data Type                                    | Description |
| ----------------- | ---- | ---------- | -------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| created_at        | core | timestamp  | The date and time that the site was created. |
| description       | core | string     | The description of the site.                 |
| global_network_id | core | string     | The ID of the global network.                |
| location          | core | json       | The location of the site.                    |
| site_arn          | core | string     | The Amazon Resource Name (ARN) of the site.  |
| site_id           | core | string     | The ID of the site.                          |
| state             | core | string     | The state of the site.                       |
| tags              | core | hstore_csv |
