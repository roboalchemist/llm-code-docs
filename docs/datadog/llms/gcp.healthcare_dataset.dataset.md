# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.healthcare_dataset.dataset.md

---
title: Cloud Healthcare API Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Healthcare API Dataset
---

# Cloud Healthcare API Dataset

A Cloud Healthcare API Dataset in Google Cloud is a container for healthcare data that supports multiple data formats such as FHIR, HL7v2, and DICOM. It provides a secure and compliant environment for storing, managing, and accessing medical information. The dataset serves as the top-level resource for organizing healthcare data stores and enables integration with analytics, AI, and interoperability tools within Google Cloud.

```
gcp.healthcare_dataset
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| encryption_spec      | core | json          | Optional. Customer-managed encryption key spec for a Dataset. If set, this Dataset and all of its sub-resources will be secured by this key. If empty, the Dataset is secured by the default Google encryption key.                                                       |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. Resource name of the dataset, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`.                                                                                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Whether the dataset satisfies zone isolation.                                                                                                                                                                                                                |
| satisfies_pzs        | core | bool          | Output only. Whether the dataset satisfies zone separation.                                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| time_zone            | core | string        | Optional. The default timezone used by this dataset. Must be a either a valid IANA time zone name such as "America/New_York" or empty, which defaults to UTC. This is used for parsing times in resources, such as HL7 messages, where no explicit timezone is specified. |
| zone_id              | core | string        |
