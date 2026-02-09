# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.contactcenterinsights_issue_model.dataset.md

---
title: Contact Center AI Insights Issue Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Contact Center AI Insights Issue
  Model
---

# Contact Center AI Insights Issue Model

Contact Center AI Insights Issue Model in Google Cloud is a machine learning model that identifies and categorizes recurring issues from customer interactions. It analyzes conversation transcripts to detect patterns, helping contact centers understand common customer problems and improve service quality. The model can be trained on historical data and used to generate insights for operational optimization.

```
gcp.contactcenterinsights_issue_model
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                  | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time at which this issue model was created.                                                               |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | The representative name for the issue model.                                                                               |
| input_data_config    | core | json          | Configs for the input data that used to create the issue model.                                                            |
| issue_count          | core | int64         | Output only. Number of issues in this issue model.                                                                         |
| labels               | core | array<string> |
| language_code        | core | string        | Language of the model.                                                                                                     |
| model_type           | core | string        | Type of the model.                                                                                                         |
| name                 | core | string        | Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issue_model} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the model.                                                                                           |
| tags                 | core | hstore_csv    |
| training_stats       | core | json          | Output only. Immutable. The issue model's label statistics on its training data.                                           |
| update_time          | core | timestamp     | Output only. The most recent time at which the issue model was updated.                                                    |
| zone_id              | core | string        |
