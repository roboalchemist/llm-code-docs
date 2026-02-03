# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_thesaurus.dataset.md

---
title: Amazon Kendra Thesaurus
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Kendra Thesaurus
---

# Amazon Kendra Thesaurus

Amazon Kendra Thesaurus is a feature that allows you to define synonyms and related terms to improve search relevance in Kendra indexes. By using a thesaurus, Kendra can understand different ways users express the same concept, returning more accurate and comprehensive search results. It helps enhance natural language understanding and user experience in enterprise search applications.

```
aws.kendra_thesaurus
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_at         | core | timestamp  | The Unix timestamp when the thesaurus was created.                                                                                                                                                                                                                                                                                                   |
| description        | core | string     | The thesaurus description.                                                                                                                                                                                                                                                                                                                           |
| error_message      | core | string     | When the Status field value is FAILED, the ErrorMessage field provides more information.                                                                                                                                                                                                                                                             |
| file_size_bytes    | core | int64      | The size of the thesaurus file in bytes.                                                                                                                                                                                                                                                                                                             |
| id                 | core | string     | The identifier of the thesaurus.                                                                                                                                                                                                                                                                                                                     |
| index_id           | core | string     | The identifier of the index for the thesaurus.                                                                                                                                                                                                                                                                                                       |
| name               | core | string     | The thesaurus name.                                                                                                                                                                                                                                                                                                                                  |
| role_arn           | core | string     | An IAM role that gives Amazon Kendra permissions to access thesaurus file specified in SourceS3Path.                                                                                                                                                                                                                                                 |
| source_s3_path     | core | json       | Information required to find a specific file in an Amazon S3 bucket.                                                                                                                                                                                                                                                                                 |
| status             | core | string     | The current status of the thesaurus. When the value is ACTIVE, queries are able to use the thesaurus. If the Status field value is FAILED, the ErrorMessage field provides more information. If the status is ACTIVE_BUT_UPDATE_FAILED, it means that Amazon Kendra could not ingest the new thesaurus file. The old thesaurus file is still active. |
| synonym_rule_count | core | int64      | The number of synonym rules in the thesaurus file.                                                                                                                                                                                                                                                                                                   |
| tags               | core | hstore_csv |
| term_count         | core | int64      | The number of unique terms in the thesaurus file. For example, the synonyms a,b,c and a=>d, the term count would be 4.                                                                                                                                                                                                                               |
| updated_at         | core | timestamp  | The Unix timestamp when the thesaurus was last updated.                                                                                                                                                                                                                                                                                              |
