# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_workflow.dataset.md

---
title: AWS HealthOmics Workflow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Workflow
---

# AWS HealthOmics Workflow

AWS HealthOmics Workflow is a managed service that enables users to create, run, and manage bioinformatics workflows for analyzing omics data such as genomics, transcriptomics, and proteomics. It supports standard workflow languages and integrates with AWS storage and compute services to scale analyses efficiently.

```
aws.omics_workflow
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                               | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| accelerators       | core | string     | The computational accelerator specified to run the workflow.                                            |
| account_id         | core | string     |
| arn                | core | string     | The workflow's ARN.                                                                                     |
| creation_time      | core | timestamp  | When the workflow was created.                                                                          |
| definition         | core | string     | The workflow's definition.                                                                              |
| description        | core | string     | The workflow's description.                                                                             |
| digest             | core | string     | The workflow's digest.                                                                                  |
| engine             | core | string     | The workflow's engine.                                                                                  |
| id                 | core | string     | The workflow's ID.                                                                                      |
| main               | core | string     | The path of the main definition file for the workflow.                                                  |
| metadata           | core | hstore     | Gets metadata for the workflow.                                                                         |
| name               | core | string     | The workflow's name.                                                                                    |
| parameter_template | core | string     | The workflow's parameter template.                                                                      |
| status             | core | string     | The workflow's status.                                                                                  |
| status_message     | core | string     | The workflow's status message.                                                                          |
| storage_capacity   | core | int64      | The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. |
| storage_type       | core | string     | The default storage type for runs using this workflow.                                                  |
| tags               | core | hstore_csv |
| type               | core | string     | The workflow's type.                                                                                    |
| uuid               | core | string     | The universally unique identifier (UUID) value for this workflow.                                       |
