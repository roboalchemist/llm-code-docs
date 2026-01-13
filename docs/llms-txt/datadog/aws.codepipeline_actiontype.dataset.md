# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codepipeline_actiontype.dataset.md

---
title: CodePipeline Actiontype
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodePipeline Actiontype
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codepipeline_actiontype.dataset/index.html
---

# CodePipeline Actiontype

This table represents the CodePipeline Actiontype resource from Amazon Web Services.

```
aws.codepipeline_actiontype
```

## Fields

| Title                   | ID   | Type   | Data Type                                                                                                                                                                  | Description |
| ----------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string |
| account_id              | core | string |
| description             | core | string | The description for the action type to be updated.                                                                                                                         |
| executor                | core | json   | Information about the executor for an action type that was created with any supported integration model.                                                                   |
| id                      | core | json   | The action category, owner, provider, and version of the action type to be updated.                                                                                        |
| input_artifact_details  | core | json   | Details for the artifacts, such as application files, to be worked on by the action. For example, the minimum and maximum number of input artifacts allowed.               |
| output_artifact_details | core | json   | Details for the output artifacts, such as a built application, that are the result of the action. For example, the minimum and maximum number of output artifacts allowed. |
| permissions             | core | json   | Details identifying the accounts with permissions to use the action type.                                                                                                  |
| properties              | core | json   | The properties of the action type to be updated.                                                                                                                           |
| tags                    | core | hstore |
| urls                    | core | json   | The links associated with the action type to be updated.                                                                                                                   |
