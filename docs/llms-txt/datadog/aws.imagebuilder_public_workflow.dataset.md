# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_public_workflow.dataset.md

---
title: Image Builder Public Workflow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Image Builder Public Workflow
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.imagebuilder_public_workflow.dataset/index.html
---

# Image Builder Public Workflow

Image Builder Public Workflow in AWS provides details about a publicly shared workflow that can be used to automate image building, testing, and distribution. It allows you to retrieve metadata and configuration information about a workflow, enabling reuse of standardized automation steps for creating and managing machine images across accounts and regions.

```
aws.imagebuilder_public_workflow
```

## Fields

| Title              | ID   | Type   | Data Type                                                                                                                                      | Description |
| ------------------ | ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string |
| account_id         | core | string |
| arn                | core | string | The Amazon Resource Name (ARN) of the workflow resource.                                                                                       |
| change_description | core | string | Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow. |
| data               | core | string | Contains the YAML document content for the workflow.                                                                                           |
| date_created       | core | string | The timestamp when Image Builder created the workflow resource.                                                                                |
| description        | core | string | The description of the workflow.                                                                                                               |
| kms_key_id         | core | string | The KMS key identifier used to encrypt the workflow resource.                                                                                  |
| name               | core | string | The name of the workflow resource.                                                                                                             |
| owner              | core | string | The owner of the workflow resource.                                                                                                            |
| parameters         | core | json   | An array of input parameters that that the image workflow uses to control actions or configure settings.                                       |
| state              | core | json   | Describes the current status of the workflow and the reason for that status.                                                                   |
| tags               | core | hstore |
| type               | core | string | Specifies the image creation stage that the workflow applies to. Image Builder currently supports build and test workflows.                    |
| version            | core | string | The workflow resource version. Workflow resources are immutable. To make a change, you can clone a workflow or create a new version.           |
