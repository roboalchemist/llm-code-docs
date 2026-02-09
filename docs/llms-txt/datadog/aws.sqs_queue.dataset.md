# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sqs_queue.dataset.md

---
title: SQS Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SQS Queue
---

# SQS Queue

An SQS Queue in AWS is a fully managed message queuing service that enables decoupling and scaling of distributed systems, microservices, and serverless applications. It allows components to communicate asynchronously by sending, storing, and receiving messages reliably at scale.

```
aws.sqs_queue
```

## Fields

| Title                                      | ID   | Type       | Data Type             | Description |
| ------------------------------------------ | ---- | ---------- | --------------------- | ----------- |
| _key                                       | core | string     |
| account_id                                 | core | string     |
| all                                        | core | string     |
| approximate_number_of_messages             | core | int64      |
| approximate_number_of_messages_delayed     | core | int64      |
| approximate_number_of_messages_not_visible | core | int64      |
| content_based_deduplication                | core | string     |
| created_timestamp                          | core | string     |
| deduplication_scope                        | core | string     |
| delay_seconds                              | core | int64      |
| fifo_queue                                 | core | string     |
| fifo_throughput_limit                      | core | string     |
| kms_data_key_reuse_period_seconds          | core | string     |
| kms_master_key_id                          | core | string     |
| last_modified_timestamp                    | core | string     |
| maximum_message_size                       | core | string     |
| message_retention_period                   | core | string     |
| policies                                   | core | json       |
| policy                                     | core | string     |
| queue_arn                                  | core | string     |
| queue_url                                  | core | string     | The URL of the queue. |
| receive_message_wait_time_seconds          | core | int64      |
| redrive_allow_policy                       | core | string     |
| redrive_policy                             | core | string     |
| sqs_managed_sse_enabled                    | core | bool       |
| tags                                       | core | hstore_csv |
| visibility_timeout                         | core | int64      |
