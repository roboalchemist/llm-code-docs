# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3outposts_outpost.dataset.md

---
title: Outposts Outpost
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Outposts Outpost
---

# Outposts Outpost

Outposts Outpost is an AWS resource that represents a physical rack of AWS infrastructure deployed at a customer site. It extends AWS services, infrastructure, and operating models to on-premises locations, allowing workloads to run locally while seamlessly integrating with the AWS cloud. This resource provides consistent APIs, tools, and services across environments, enabling low-latency applications, local data processing, and compliance with data residency requirements.

```
aws.s3outposts_outpost
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                           | Description |
| ----------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| capacity_in_bytes | core | int64      | The Amazon S3 capacity of the outpost in bytes.                                                                     |
| outpost_arn       | core | string     | Specifies the unique Amazon Resource Name (ARN) for the outpost.                                                    |
| outpost_id        | core | string     | Specifies the unique identifier for the outpost.                                                                    |
| owner_id          | core | string     | Returns the Amazon Web Services account ID of the outpost owner. Useful for comparing owned versus shared outposts. |
| s3_outpost_arn    | core | string     | Specifies the unique S3 on Outposts ARN for use with Resource Access Manager (RAM).                                 |
| tags              | core | hstore_csv |
