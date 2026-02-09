# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pca_connector_ad_directory_registration.dataset.md

---
title: PCA Connector Active Directory Directory Registration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > PCA Connector Active Directory
  Directory Registration
---

# PCA Connector Active Directory Directory Registration

This table represents the PCA Connector Active Directory Directory Registration resource from Amazon Web Services.

```
aws.pca_connector_ad_directory_registration
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                               | Description |
| ----------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| arn               | core | string     | The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.                                                                 |
| connector_arn     | core | string     | The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.                                                               |
| created_at        | core | timestamp  | The date and time that the template was created.                                                                                                                                                                                                        |
| definition        | core | json       | Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings. |
| directory_id      | core | string     | The identifier of the Active Directory.                                                                                                                                                                                                                 |
| name              | core | string     | Name of the template. The template name must be unique.                                                                                                                                                                                                 |
| object_identifier | core | string     | Object identifier of a template.                                                                                                                                                                                                                        |
| policy_schema     | core | int64      | The template schema version. Template schema versions can be v2, v3, or v4. The template configuration options change based on the template schema version.                                                                                             |
| revision          | core | json       | The revision version of the template. Template updates will increment the minor revision. Re-enrolling all certificate holders will increment the major revision.                                                                                       |
| status            | core | string     | Status of the template. Status can be creating, active, deleting, or failed.                                                                                                                                                                            |
| status_reason     | core | string     | Additional information about the directory registration status if the status is failed.                                                                                                                                                                 |
| tags              | core | hstore_csv |
| updated_at        | core | timestamp  | The date and time that the template was updated.                                                                                                                                                                                                        |
