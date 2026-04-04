# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.macie2_allow_list.dataset.md

---
title: Macie Allow List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Macie Allow List
---

# Macie Allow List

Macie Allow List in AWS is a resource that defines a set of text or patterns that Amazon Macie should ignore when scanning data for sensitive information. It helps reduce false positives by excluding known safe values, such as test data, dummy identifiers, or common strings that are not sensitive. This allows Macie to focus on identifying truly sensitive data and improves the accuracy of findings.

```
aws.macie2_allow_list
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                                                                                                                                        | Description |
| ----------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name (ARN) of the allow list.                                                                                                                                                                                                |
| created_at  | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie.                                                                                                                                         |
| criteria    | core | json       | The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression (regex) that defines a text pattern to ignore. |
| description | core | string     | The custom description of the allow list.                                                                                                                                                                                                        |
| id          | core | string     | The unique identifier for the allow list.                                                                                                                                                                                                        |
| name        | core | string     | The custom name of the allow list.                                                                                                                                                                                                               |
| status      | core | json       | The current status of the allow list, which indicates whether Amazon Macie can access and use the list's criteria.                                                                                                                               |
| tags        | core | hstore_csv |
| updated_at  | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, when the allow list's settings were most recently changed in Amazon Macie.                                                                                                               |
