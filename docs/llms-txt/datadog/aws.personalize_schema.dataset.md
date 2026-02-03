# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_schema.dataset.md

---
title: Personalize Schema
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Schema
---

# Personalize Schema

Personalize Schema in AWS defines the structure of your dataset for Amazon Personalize. It specifies the format, fields, and data types that describe user interactions, items, or user metadata. Schemas ensure that the data you import into Personalize is consistent and interpretable by the service, enabling accurate training of recommendation models.

```
aws.personalize_schema
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                        | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The date and time (in Unix time) that the schema was created.                    |
| domain                 | core | string     | The domain of a schema that you created for a dataset in a Domain dataset group. |
| last_updated_date_time | core | timestamp  | The date and time (in Unix time) that the schema was last updated.               |
| name                   | core | string     | The name of the schema.                                                          |
| schema                 | core | string     | The schema.                                                                      |
| schema_arn             | core | string     | The Amazon Resource Name (ARN) of the schema.                                    |
| tags                   | core | hstore_csv |
