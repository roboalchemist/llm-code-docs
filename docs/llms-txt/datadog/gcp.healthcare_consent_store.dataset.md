# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.healthcare_consent_store.dataset.md

---
title: Cloud Healthcare API Consent Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Healthcare API Consent Store
---

# Cloud Healthcare API Consent Store

Cloud Healthcare API Consent Store is a Google Cloud resource that manages patient consent policies for healthcare data access and sharing. It allows organizations to define, store, and enforce consent directives in compliance with privacy regulations. The Consent Store integrates with other Cloud Healthcare API components to control data access based on patient permissions.

```
gcp.healthcare_consent_store
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| ancestors                       | core | array<string> |
| datadog_display_name            | core | string        |
| default_consent_ttl             | core | string        | Optional. Default time to live for Consents created in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| enable_consent_create_on_update | core | bool          | Optional. If `true`, UpdateConsent creates the Consent if it does not already exist. If unspecified, defaults to `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| labels                          | core | array<string> | Optional. User-supplied key-value pairs used to organize consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62}. Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}. No more than 64 labels can be associated with a given store. For more information: https://cloud.google.com/healthcare/docs/how-tos/labeling-resources |
| name                            | core | string        | Identifier. Resource name of the consent store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}`. Cannot be changed after creation.                                                                                                                                                                                                                                                                                                                                                                                                      |
| organization_id                 | core | string        |
| parent                          | core | string        |
| project_id                      | core | string        |
| project_number                  | core | string        |
| region_id                       | core | string        |
| resource_name                   | core | string        |
| tags                            | core | hstore_csv    |
| zone_id                         | core | string        |
