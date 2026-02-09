# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_instance.dataset.md

---
title: Connect Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Instance
---

# Connect Instance

An AWS Connect Instance is a cloud-based contact center resource that provides the core environment for running Amazon Connect. It defines the instance where you configure users, routing, telephony, and integrations. Each instance is isolated, allowing you to manage contact flows, queues, and reporting independently.

```
aws.connect_instance
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| instance                  | core | json       | The name of the instance.                                                                                                                                                                                                                                                                                                                                                   |
| replication_configuration | core | json       | Status information about the replication process. This field is included only when you are using the ReplicateInstance API to replicate an Amazon Connect instance across Amazon Web Services Regions. For information about replicating Amazon Connect instances, see Create a replica of your existing Amazon Connect instance in the Amazon Connect Administrator Guide. |
| tags                      | core | hstore_csv |
