# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_idnamespaceassociation.dataset.md

---
title: Cleanrooms Idnamespaceassociation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cleanrooms Idnamespaceassociation
---

# Cleanrooms Idnamespaceassociation

This table represents the cleanrooms_idnamespaceassociation resource from Amazon Web Services.

```
aws.cleanrooms_idnamespaceassociation
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                        | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| arn                        | core | string     | The Amazon Resource Name (ARN) of the ID namespace association.                                  |
| collaboration_arn          | core | string     | The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association. |
| collaboration_id           | core | string     | The unique identifier of the collaboration that contains this ID namespace association.          |
| create_time                | core | timestamp  | The time at which the ID namespace association was created.                                      |
| description                | core | string     | The description of the ID namespace association.                                                 |
| id                         | core | string     | The unique identifier for this ID namespace association.                                         |
| id_mapping_config          | core | json       | The configuration settings for the ID mapping table.                                             |
| input_reference_config     | core | json       | The input reference configuration for the ID namespace association.                              |
| input_reference_properties | core | json       | The input reference properties for the ID namespace association.                                 |
| membership_arn             | core | string     | The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.     |
| membership_id              | core | string     | The unique identifier of the membership resource for this ID namespace association.              |
| name                       | core | string     | The name of this ID namespace association.                                                       |
| tags                       | core | hstore_csv |
| update_time                | core | timestamp  | The most recent time at which the ID namespace association was updated.                          |
