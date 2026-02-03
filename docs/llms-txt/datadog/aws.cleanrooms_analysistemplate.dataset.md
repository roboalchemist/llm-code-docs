# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_analysistemplate.dataset.md

---
title: Cleanrooms Analysistemplate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cleanrooms Analysistemplate
---

# Cleanrooms Analysistemplate

This table represents the cleanrooms_analysistemplate resource from Amazon Web Services.

```
aws.cleanrooms_analysistemplate
```

## Fields

| Title               | ID   | Type       | Data Type                                                                       | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| analysis_parameters | core | json       | The parameters of the analysis template.                                        |
| arn                 | core | string     | The Amazon Resource Name (ARN) of the analysis template.                        |
| collaboration_arn   | core | string     | The unique ARN for the analysis template's associated collaboration.            |
| collaboration_id    | core | string     | The unique ID for the associated collaboration of the analysis template.        |
| create_time         | core | timestamp  | The time that the analysis template was created.                                |
| description         | core | string     | The description of the analysis template.                                       |
| format              | core | string     | The format of the analysis template.                                            |
| id                  | core | string     | The identifier for the analysis template.                                       |
| membership_arn      | core | string     | The Amazon Resource Name (ARN) of the member who created the analysis template. |
| membership_id       | core | string     | The identifier of a member who created the analysis template.                   |
| name                | core | string     | The name of the analysis template.                                              |
| schema              | core | json       | The entire schema object.                                                       |
| source_metadata     | core | json       | The source metadata for the analysis template.                                  |
| tags                | core | hstore_csv |
| update_time         | core | timestamp  | The time that the analysis template was last updated.                           |
| validations         | core | json       | Information about the validations performed on the analysis template.           |
