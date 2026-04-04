# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resourceexplorer2_index.dataset.md

---
title: Resource Explorer Index
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Explorer Index
---

# Resource Explorer Index

Resource Explorer Index in AWS provides information about the index used by AWS Resource Explorer to organize and search resources across an account and Regions. It helps identify whether the index is local or aggregator, its state, and the Region where it is created. This resource is essential for enabling efficient resource discovery and search within AWS environments.

```
aws.resourceexplorer2_index
```

## Fields

| Title            | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                | Description |
| ---------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| arn              | core | string        | The Amazon resource name (ARN) of the index.                                                                                                                                                                                                                                                                             |
| created_at       | core | timestamp     | The date and time when the index was originally created.                                                                                                                                                                                                                                                                 |
| last_updated_at  | core | timestamp     | The date and time when the index was last updated.                                                                                                                                                                                                                                                                       |
| replicating_from | core | array<string> | This response value is present only if this index is Type=AGGREGATOR. A list of the Amazon Web Services Regions that replicate their content to the index in this Region.                                                                                                                                                |
| replicating_to   | core | array<string> | This response value is present only if this index is Type=LOCAL. The Amazon Web Services Region that contains the aggregator index, if one exists. If an aggregator index does exist then the Region in which you called this operation replicates its index information to the Region specified in this response value. |
| state            | core | string        | The current state of the index in this Amazon Web Services Region.                                                                                                                                                                                                                                                       |
| tags             | core | hstore_csv    |
| type             | core | string        | The type of the index in this Region. For information about the aggregator index and how it differs from a local index, see Turning on cross-Region search by creating an aggregator index.                                                                                                                              |
