# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.databrew_project.dataset.md

---
title: Glue DataBrew Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue DataBrew Project
---

# Glue DataBrew Project

An AWS Glue DataBrew Project is a workspace that lets you organize and manage data preparation tasks. It ties together datasets, transformation recipes, and job runs, allowing you to visually clean and normalize data without writing code. Projects provide an interactive environment where you can apply, test, and refine transformations before running them at scale.

```
aws.databrew_project
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                   | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     | The ID of the Amazon Web Services account that owns the project.                                                                                            |
| create_date        | core | timestamp  | The date and time that the project was created.                                                                                                             |
| created_by         | core | string     | The Amazon Resource Name (ARN) of the user who crated the project.                                                                                          |
| dataset_name       | core | string     | The dataset that the project is to act upon.                                                                                                                |
| last_modified_by   | core | string     | The Amazon Resource Name (ARN) of the user who last modified the project.                                                                                   |
| last_modified_date | core | timestamp  | The last modification date and time for the project.                                                                                                        |
| name               | core | string     | The unique name of a project.                                                                                                                               |
| open_date          | core | timestamp  | The date and time when the project was opened.                                                                                                              |
| opened_by          | core | string     | The Amazon Resource Name (ARN) of the user that opened the project for use.                                                                                 |
| recipe_name        | core | string     | The name of a recipe that will be developed during a project session.                                                                                       |
| resource_arn       | core | string     | The Amazon Resource Name (ARN) for the project.                                                                                                             |
| role_arn           | core | string     | The Amazon Resource Name (ARN) of the role that will be assumed for this project.                                                                           |
| sample             | core | json       | The sample size and sampling type to apply to the data. If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset. |
| tags               | core | hstore_csv |
