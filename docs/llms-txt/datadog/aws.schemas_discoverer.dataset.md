# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.schemas_discoverer.dataset.md

---
title: Schemas Discoverer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Schemas Discoverer
---

# Schemas Discoverer

Schemas Discoverer in AWS is a resource within the EventBridge Schemas service that helps automatically detect and capture schema information from events as they flow through an event bus. It simplifies schema management by discovering event structures without requiring manual definition, making it easier for developers to understand, catalog, and integrate event-driven applications.

```
aws.schemas_discoverer
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                 | Description |
| -------------- | ---- | ---------- | ----------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| cross_account  | core | bool       | The Status if the discoverer will discover schemas from events sent from another account. |
| discoverer_arn | core | string     | The ARN of the discoverer.                                                                |
| discoverer_id  | core | string     | The ID of the discoverer.                                                                 |
| source_arn     | core | string     | The ARN of the event bus.                                                                 |
| state          | core | string     | The state of the discoverer.                                                              |
| tags           | core | hstore_csv |
