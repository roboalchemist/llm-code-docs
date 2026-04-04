# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_topic.dataset.md

---
title: QuickSight Topic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Topic
---

# QuickSight Topic

QuickSight Topic in AWS is a semantic layer that allows users to define business-friendly terms and concepts for their data in Amazon QuickSight. It enables natural language queries by mapping technical data fields into intuitive topics, making it easier for business users to explore and analyze data without needing deep technical knowledge.

```
aws.quicksight_topic
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                             | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| arn        | core | string     | The Amazon Resource Name (ARN) of the topic.                                                                                          |
| request_id | core | string     | The Amazon Web Services request ID for this operation.                                                                                |
| status     | core | int64      | The HTTP status of the request.                                                                                                       |
| tags       | core | hstore_csv |
| topic      | core | json       | The definition of a topic.                                                                                                            |
| topic_id   | core | string     | The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account. |
