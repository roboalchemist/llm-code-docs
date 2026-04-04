# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.translate_terminology.dataset.md

---
title: Translate Terminology
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Translate Terminology
---

# Translate Terminology

AWS Translate Terminology is a feature of Amazon Translate that allows you to manage and retrieve custom terminology resources. A terminology is a collection of user-defined terms that ensures consistent and accurate translations for domain-specific vocabulary. The GetTerminologyResponse provides details about a stored terminology, including its metadata and file content, enabling you to integrate specialized vocabulary into your translation workflows.

```
aws.translate_terminology
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| auxiliary_data_location   | core | json       | The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a terminology resource. The location is returned as a presigned URL to that has a 30-minute expiration.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| tags                      | core | hstore_csv |
| terminology_data_location | core | json       | The Amazon S3 location of the most recent custom terminology input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration. Amazon Translate doesn't scan all input files for the risk of CSV injection attacks. CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it. Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator. |
| terminology_properties    | core | json       | The properties of the custom terminology being retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
