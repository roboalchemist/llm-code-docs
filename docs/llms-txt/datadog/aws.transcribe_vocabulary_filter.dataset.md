# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transcribe_vocabulary_filter.dataset.md

---
title: Transcribe Vocabulary Filter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transcribe Vocabulary Filter
---

# Transcribe Vocabulary Filter

Transcribe Vocabulary Filter in AWS is a custom word list used with Amazon Transcribe to filter or mask specific terms during speech-to-text transcription. It helps manage sensitive, profane, or unwanted words by replacing them with asterisks or removing them from the transcript. This allows greater control over transcription output for compliance, moderation, or content customization needs.

```
aws.transcribe_vocabulary_filter
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                          | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| download_uri           | core | string     | The Amazon S3 location where the custom vocabulary filter is stored; use this URI to view or download the custom vocabulary filter.                                                                                                |
| language_code          | core | string     | The language code you selected for your custom vocabulary filter.                                                                                                                                                                  |
| last_modified_time     | core | timestamp  | The date and time the specified custom vocabulary filter was last modified. Timestamps are in the format YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC. For example, 2022-05-04T12:32:58.761000-07:00 represents 12:32 PM UTC-7 on May 4, 2022. |
| tags                   | core | hstore_csv |
| vocabulary_filter_name | core | string     | The name of the custom vocabulary filter you requested information about.                                                                                                                                                          |
