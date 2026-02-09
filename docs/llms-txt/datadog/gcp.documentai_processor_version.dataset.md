# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.documentai_processor_version.dataset.md

---
title: Document AI Processor Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Document AI Processor Version
---

# Document AI Processor Version

A Document AI Processor Version in Google Cloud represents a specific release of a Document AI processor model. Each version defines the model's capabilities, accuracy, and supported document types. It allows users to manage and upgrade their document processing workflows while maintaining compatibility and performance consistency across different versions.

```
gcp.documentai_processor_version
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                              | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time the processor version was created.                                                                                                               |
| datadog_display_name | core | string        |
| deprecation_info     | core | json          | Output only. If set, information about the eventual deprecation of this version.                                                                                       |
| document_schema      | core | json          | Output only. The schema of the processor version. Describes the output.                                                                                                |
| gcp_display_name     | core | string        | The display name of the processor version.                                                                                                                             |
| gen_ai_model_info    | core | json          | Output only. Information about Generative AI model-based processor versions.                                                                                           |
| google_managed       | core | bool          | Output only. Denotes that this `ProcessorVersion` is managed by Google.                                                                                                |
| kms_key_name         | core | string        | Output only. The KMS key name used for encryption.                                                                                                                     |
| kms_key_version_name | core | string        | Output only. The KMS key version with which data is encrypted.                                                                                                         |
| labels               | core | array<string> |
| latest_evaluation    | core | json          | Output only. The most recently invoked evaluation for the processor version.                                                                                           |
| model_type           | core | string        | Output only. The model type of this processor version.                                                                                                                 |
| name                 | core | string        | Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                  |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                  |
| state                | core | string        | Output only. The state of the processor version.                                                                                                                       |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
