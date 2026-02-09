# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transcribe_medical_vocabulary.dataset.md

---
title: Transcribe Medical Vocabulary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transcribe Medical Vocabulary
---

# Transcribe Medical Vocabulary

Transcribe Medical Vocabulary in AWS allows you to manage custom medical vocabularies used with Amazon Transcribe Medical. These vocabularies help improve the accuracy of speech-to-text transcriptions for medical terms, drug names, procedures, and other domain-specific language. The resource provides details about a vocabulary's status, creation time, and content, enabling healthcare applications to generate more precise transcripts tailored to clinical and medical use cases.

```
aws.transcribe_medical_vocabulary
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                           | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| download_uri       | core | string     | The Amazon S3 location where the specified custom medical vocabulary is stored; use this URI to view or download the custom vocabulary.                                                                                             |
| failure_reason     | core | string     | If VocabularyState is FAILED, FailureReason contains information about why the custom medical vocabulary request failed. See also: Common Errors.                                                                                   |
| language_code      | core | string     | The language code you selected for your custom medical vocabulary. US English (en-US) is the only language supported with Amazon Transcribe Medical.                                                                                |
| last_modified_time | core | timestamp  | The date and time the specified custom medical vocabulary was last modified. Timestamps are in the format YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC. For example, 2022-05-04T12:32:58.761000-07:00 represents 12:32 PM UTC-7 on May 4, 2022. |
| tags               | core | hstore_csv |
| vocabulary_name    | core | string     | The name of the custom medical vocabulary you requested information about.                                                                                                                                                          |
| vocabulary_state   | core | string     | The processing state of your custom medical vocabulary. If the state is READY, you can use the custom vocabulary in a StartMedicalTranscriptionJob request.                                                                         |
