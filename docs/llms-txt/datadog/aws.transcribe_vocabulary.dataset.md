# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transcribe_vocabulary.dataset.md

---
title: Custom Vocabulary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Custom Vocabulary
---

# Custom Vocabulary

Custom Vocabulary in AWS Transcribe allows you to define domain-specific terms, unique product names, or uncommon words to improve the accuracy of speech-to-text transcriptions. By creating and managing custom vocabularies, you can ensure that specialized terminology is recognized correctly during transcription jobs. This resource is part of the Transcribe service and is retrieved through the GetVocabularyResponse API.

```
aws.transcribe_vocabulary
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                   | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| download_uri       | core | string     | The Amazon S3 location where the custom vocabulary is stored; use this URI to view or download the custom vocabulary.                                                                                                       |
| failure_reason     | core | string     | If VocabularyState is FAILED, FailureReason contains information about why the custom vocabulary request failed. See also: Common Errors.                                                                                   |
| language_code      | core | string     | The language code you selected for your custom vocabulary.                                                                                                                                                                  |
| last_modified_time | core | timestamp  | The date and time the specified custom vocabulary was last modified. Timestamps are in the format YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC. For example, 2022-05-04T12:32:58.761000-07:00 represents 12:32 PM UTC-7 on May 4, 2022. |
| tags               | core | hstore_csv |
| vocabulary_name    | core | string     | The name of the custom vocabulary you requested information about.                                                                                                                                                          |
| vocabulary_state   | core | string     | The processing state of your custom vocabulary. If the state is READY, you can use the custom vocabulary in a StartTranscriptionJob request.                                                                                |
