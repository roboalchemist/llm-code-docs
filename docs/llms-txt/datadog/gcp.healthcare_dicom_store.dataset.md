# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.healthcare_dicom_store.dataset.md

---
title: Cloud Healthcare API DICOM store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Healthcare API DICOM store
---

# Cloud Healthcare API DICOM store

A Cloud Healthcare API DICOM store in Google Cloud is a managed service for storing, managing, and accessing medical imaging data in the DICOM format. It enables secure storage, retrieval, and sharing of medical images such as X-rays, MRIs, and CT scans. The service integrates with healthcare systems and supports compliance with healthcare data standards and privacy regulations.

```
gcp.healthcare_dicom_store
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| labels               | core | array<string> | User-supplied key-value pairs used to organize DICOM stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| name                 | core | string        | Identifier. Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.                                                                                                                                                                                                                                                                                                                                                    |
| notification_config  | core | json          | Optional. Notification destination for new DICOM instances. Supplied by the client.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| notification_configs | core | json          | Optional. Specifies where and whether to send notifications upon changes to a DICOM store.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| stream_configs       | core | json          | Optional. A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.                                                                                              |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
