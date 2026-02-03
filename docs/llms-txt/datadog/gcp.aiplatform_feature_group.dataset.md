# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.aiplatform_feature_group.dataset.md

---
title: Vertex AI Feature Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vertex AI Feature Group
---

# Vertex AI Feature Group

Vertex AI Feature Group is a managed service in Google Cloud that organizes and stores machine learning features for consistent use across training and serving. It enables centralized feature management, versioning, and sharing, ensuring data consistency and reducing duplication. Feature Groups integrate with Vertex AI Feature Store for scalable, low-latency access to features.

```
gcp.aiplatform_feature_group
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| big_query             | core | json          | Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source. The BigQuery source table or view must have at least one entity ID column and a column named `feature_timestamp`.                                                                                                                                                                                                                                                                                                          |
| create_time           | core | timestamp     | Output only. Timestamp when this FeatureGroup was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| datadog_display_name  | core | string        |
| description           | core | string        | Optional. Description of the FeatureGroup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| etag                  | core | string        | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| labels                | core | array<string> | Optional. The labels with user-defined metadata to organize your FeatureGroup. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureGroup(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| name                  | core | string        | Identifier. Name of the FeatureGroup. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| service_account_email | core | string        | Output only. A Service Account unique to this FeatureGroup. The role bigquery.dataViewer should be granted to this service account to allow Vertex AI Feature Store to access source data while running jobs under this FeatureGroup.                                                                                                                                                                                                                                                                                                                         |
| service_agent_type    | core | string        | Optional. Service agent type used during jobs under a FeatureGroup. By default, the Vertex AI Service Agent is used. When using an IAM Policy to isolate this FeatureGroup within a project, a separate service account should be provisioned by setting this field to `SERVICE_AGENT_TYPE_FEATURE_GROUP`. This will generate a separate service account to access the BigQuery source table.                                                                                                                                                                 |
| tags                  | core | hstore_csv    |
| update_time           | core | timestamp     | Output only. Timestamp when this FeatureGroup was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| zone_id               | core | string        |
