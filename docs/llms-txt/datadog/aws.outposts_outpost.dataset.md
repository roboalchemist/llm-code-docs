# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.outposts_outpost.dataset.md

---
title: AWS Outpost
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Outpost
---

# AWS Outpost

AWS Outpost is a fully managed service that extends AWS infrastructure, services, APIs, and tools to on-premises locations. It allows users to run AWS compute, storage, and other services locally while maintaining seamless integration with the AWS cloud for a consistent hybrid experience.

```
aws.outposts_outpost
```

## Fields

| Title             | ID   | Type       | Data Type                                                | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| capacity_in_bytes | core | int64      |
| outpost_arn       | core | string     | The Amazon Resource Name (ARN) of the Outpost.           |
| outpost_id        | core | string     | The ID of the Outpost.                                   |
| owner_id          | core | string     | The Amazon Web Services account ID of the Outpost owner. |
| s3_outpost_arn    | core | string     |
| tags              | core | hstore_csv |
