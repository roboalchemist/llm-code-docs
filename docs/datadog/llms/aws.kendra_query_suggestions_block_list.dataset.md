# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_query_suggestions_block_list.dataset.md

---
title: Amazon Kendra Query Suggestions Block List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Amazon Kendra Query Suggestions
  Block List
---

# Amazon Kendra Query Suggestions Block List

Amazon Kendra Query Suggestions Block List is a resource that defines a list of words or phrases that should be excluded from query suggestions in an Amazon Kendra index. It helps control and filter out inappropriate, irrelevant, or sensitive terms from being suggested to users, improving the quality and compliance of search experiences.

```
aws.kendra_query_suggestions_block_list
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                                                                    | Description |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| created_at      | core | timestamp  | The Unix timestamp when a block list for query suggestions was created.                                                                                                                                                                                      |
| description     | core | string     | The description for the block list.                                                                                                                                                                                                                          |
| error_message   | core | string     | The error message containing details if there are issues processing the block list.                                                                                                                                                                          |
| file_size_bytes | core | int64      | The current size of the block list text file in S3.                                                                                                                                                                                                          |
| id              | core | string     | The identifier of the block list.                                                                                                                                                                                                                            |
| index_id        | core | string     | The identifier of the index for the block list.                                                                                                                                                                                                              |
| item_count      | core | int64      | The current number of valid, non-empty words or phrases in the block list text file.                                                                                                                                                                         |
| name            | core | string     | The name of the block list.                                                                                                                                                                                                                                  |
| role_arn        | core | string     | The IAM (Identity and Access Management) role used by Amazon Kendra to access the block list text file in S3. The role needs S3 read permissions to your file in S3 and needs to give STS (Security Token Service) assume role permissions to Amazon Kendra. |
| source_s3_path  | core | json       | Shows the current S3 path to your block list text file in your S3 bucket. Each block word or phrase should be on a separate line in a text file. For information on the current quota limits for block lists, see Quotas for Amazon Kendra.                  |
| status          | core | string     | The current status of the block list. When the value is ACTIVE, the block list is ready for use.                                                                                                                                                             |
| tags            | core | hstore_csv |
| updated_at      | core | timestamp  | The Unix timestamp when a block list for query suggestions was last updated.                                                                                                                                                                                 |
