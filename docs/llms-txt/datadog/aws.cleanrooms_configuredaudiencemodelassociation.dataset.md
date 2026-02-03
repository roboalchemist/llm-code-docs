# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_configuredaudiencemodelassociation.dataset.md

---
title: Cleanrooms Configuredaudiencemodelassociation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Cleanrooms
  Configuredaudiencemodelassociation
---

# Cleanrooms Configuredaudiencemodelassociation

This table represents the cleanrooms_configuredaudiencemodelassociation resource from Amazon Web Services.

```
aws.cleanrooms_configuredaudiencemodelassociation
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                       | Description |
| ----------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| arn                           | core | string     | The Amazon Resource Name (ARN) of the configured audience model association.                                                                                                                                                                                                                                                                                    |
| collaboration_arn             | core | string     | The Amazon Resource Name (ARN) of the collaboration that contains this configured audience model association.                                                                                                                                                                                                                                                   |
| collaboration_id              | core | string     | A unique identifier of the collaboration that contains this configured audience model association.                                                                                                                                                                                                                                                              |
| configured_audience_model_arn | core | string     | The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.                                                                                                                                                                                                                                   |
| create_time                   | core | timestamp  | The time at which the configured audience model association was created.                                                                                                                                                                                                                                                                                        |
| description                   | core | string     | The description of the configured audience model association.                                                                                                                                                                                                                                                                                                   |
| id                            | core | string     | A unique identifier of the configured audience model association.                                                                                                                                                                                                                                                                                               |
| manage_resource_policies      | core | bool       | When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration. |
| membership_arn                | core | string     | The Amazon Resource Name (ARN) of the membership that contains this configured audience model association.                                                                                                                                                                                                                                                      |
| membership_id                 | core | string     | A unique identifier for the membership that contains this configured audience model association.                                                                                                                                                                                                                                                                |
| name                          | core | string     | The name of the configured audience model association.                                                                                                                                                                                                                                                                                                          |
| tags                          | core | hstore_csv |
| update_time                   | core | timestamp  | The most recent time at which the configured audience model association was updated.                                                                                                                                                                                                                                                                            |
