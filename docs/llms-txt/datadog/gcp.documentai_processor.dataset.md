# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.documentai_processor.dataset.md

---
title: Document AI Processor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Document AI Processor
---

# Document AI Processor

Document AI Processor is a managed Google Cloud service that uses machine learning to extract, classify, and structure information from documents. It supports various document types such as invoices, receipts, and forms, enabling automated data capture and analysis. The processor can be customized or use pre-trained models to streamline document workflows and integrate with other GCP services for scalable document processing.

```
gcp.documentai_processor
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                            | Description |
| ------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| create_time               | core | timestamp     | Output only. The time the processor was created.                                                                                     |
| datadog_display_name      | core | string        |
| default_processor_version | core | string        | The default processor version.                                                                                                       |
| gcp_display_name          | core | string        | The display name of the processor.                                                                                                   |
| kms_key_name              | core | string        | The [KMS key](https://cloud.google.com/security-key-management) used for encryption and decryption in CMEK scenarios.                |
| labels                    | core | array<string> |
| name                      | core | string        | Output only. Immutable. The resource name of the processor. Format: `projects/{project}/locations/{location}/processors/{processor}` |
| organization_id           | core | string        |
| parent                    | core | string        |
| process_endpoint          | core | string        | Output only. Immutable. The http endpoint that can be called to invoke processing.                                                   |
| processor_version_aliases | core | json          | Output only. The processor version aliases.                                                                                          |
| project_id                | core | string        |
| project_number            | core | string        |
| region_id                 | core | string        |
| resource_name             | core | string        |
| satisfies_pzi             | core | bool          | Output only. Reserved for future use.                                                                                                |
| satisfies_pzs             | core | bool          | Output only. Reserved for future use.                                                                                                |
| state                     | core | string        | Output only. The state of the processor.                                                                                             |
| tags                      | core | hstore_csv    |
| type                      | core | string        | The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`. To get a list of processor types, see FetchProcessorTypes.        |
| zone_id                   | core | string        |
