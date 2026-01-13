# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.databrew_dataset.dataset.md

---
title: Glue DataBrew Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue DataBrew Dataset
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.databrew_dataset.dataset/index.html
---

# Glue DataBrew Dataset

Glue DataBrew Dataset is a resource in AWS Glue DataBrew that defines the data you want to prepare and transform. It represents a collection of data from sources such as Amazon S3, Amazon Redshift, or other supported data stores. The dataset acts as the input for DataBrew projects, enabling users to visually clean, normalize, and enrich data without writing code.

```
aws.databrew_dataset
```

## Fields

| Title              | ID   | Type      | Data Type                                                                                       | Description |
| ------------------ | ---- | --------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string    |
| account_id         | core | string    | The ID of the Amazon Web Services account that owns the dataset.                                |
| create_date        | core | timestamp | The date and time that the dataset was created.                                                 |
| created_by         | core | string    | The Amazon Resource Name (ARN) of the user who created the dataset.                             |
| format             | core | string    | The file format of a dataset that is created from an Amazon S3 file or folder.                  |
| format_options     | core | json      | A set of options that define how DataBrew interprets the data in the dataset.                   |
| input              | core | json      | Information on how DataBrew can find the dataset, in either the Glue Data Catalog or Amazon S3. |
| last_modified_by   | core | string    | The Amazon Resource Name (ARN) of the user who last modified the dataset.                       |
| last_modified_date | core | timestamp | The last modification date and time of the dataset.                                             |
| name               | core | string    | The unique name of the dataset.                                                                 |
| path_options       | core | json      | A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.         |
| resource_arn       | core | string    | The unique Amazon Resource Name (ARN) for the dataset.                                          |
| tags               | core | hstore    |
