# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_faq.dataset.md

---
title: Amazon Kendra FAQ
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Kendra FAQ
---

# Amazon Kendra FAQ

Amazon Kendra FAQ is a managed resource that represents a Frequently Asked Questions (FAQ) document used by Amazon Kendra to improve search relevance. It stores structured question-and-answer pairs that Kendra indexes to provide direct, accurate responses to user queries. The resource includes details such as FAQ name, status, file location, and associated index.

```
aws.kendra_faq
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                                                                                 | Description |
| ------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| created_at    | core | timestamp  | The Unix timestamp when the FAQ was created.                                                                                                                                                                                              |
| description   | core | string     | The description of the FAQ that you provided when it was created.                                                                                                                                                                         |
| error_message | core | string     | If the Status field is FAILED, the ErrorMessage field contains the reason why the FAQ failed.                                                                                                                                             |
| file_format   | core | string     | The file format used for the FAQ file.                                                                                                                                                                                                    |
| id            | core | string     | The identifier of the FAQ.                                                                                                                                                                                                                |
| index_id      | core | string     | The identifier of the index for the FAQ.                                                                                                                                                                                                  |
| language_code | core | string     | The code for a language. This shows a supported language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see Adding documents in languages other than English. |
| name          | core | string     | The name that you gave the FAQ when it was created.                                                                                                                                                                                       |
| role_arn      | core | string     | The Amazon Resource Name (ARN) of the IAM role that provides access to the S3 bucket containing the FAQ file.                                                                                                                             |
| s3_path       | core | json       | Information required to find a specific file in an Amazon S3 bucket.                                                                                                                                                                      |
| status        | core | string     | The status of the FAQ. It is ready to use when the status is ACTIVE.                                                                                                                                                                      |
| tags          | core | hstore_csv |
| updated_at    | core | timestamp  | The Unix timestamp when the FAQ was last updated.                                                                                                                                                                                         |
