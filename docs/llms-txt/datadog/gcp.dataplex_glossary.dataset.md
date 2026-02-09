# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_glossary.dataset.md

---
title: Dataplex Glossary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Glossary
---

# Dataplex Glossary

Dataplex Glossary in Google Cloud is a centralized metadata management feature that allows users to define, organize, and manage business terms and their relationships across data assets. It helps ensure consistent data understanding and governance by linking glossary terms to data entities, improving data discovery, compliance, and collaboration across teams.

```
gcp.dataplex_glossary
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| category_count       | core | int64         | Output only. The number of GlossaryCategories in the Glossary.                                                                                                                                                                                |
| create_time          | core | timestamp     | Output only. The time at which the Glossary was created.                                                                                                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. The user-mutable description of the Glossary.                                                                                                                                                                                       |
| etag                 | core | string        | Optional. Needed for resource freshness validation. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| gcp_display_name     | core | string        | Optional. User friendly display name of the Glossary. This is user-mutable. This will be same as the GlossaryId, if not specified.                                                                                                            |
| labels               | core | array<string> | Optional. User-defined labels for the Glossary.                                                                                                                                                                                               |
| name                 | core | string        | Output only. Identifier. The resource name of the Glossary. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| term_count           | core | int64         | Output only. The number of GlossaryTerms in the Glossary.                                                                                                                                                                                     |
| uid                  | core | string        | Output only. System generated unique id for the Glossary. This ID will be different if the Glossary is deleted and re-created with the same name.                                                                                             |
| update_time          | core | timestamp     | Output only. The time at which the Glossary was last updated.                                                                                                                                                                                 |
| zone_id              | core | string        |
