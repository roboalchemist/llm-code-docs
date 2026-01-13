# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.identitystore_group.dataset.md

---
title: Identity Store Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Store Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.identitystore_group.dataset/index.html
---

# Identity Store Group

An Identity Store Group in AWS represents a collection of users within the AWS Identity Store service. It is used to organize users into logical groups for easier management of access and permissions across applications and services. Groups simplify administration by allowing policies and roles to be assigned collectively rather than individually to each user.

```
aws.identitystore_group
```

## Fields

| Title             | ID   | Type   | Data Type                                                                                                            | Description |
| ----------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string |
| account_id        | core | string |
| description       | core | string | A string containing a description of the specified group.                                                            |
| external_ids      | core | json   | A list of ExternalId objects that contains the identifiers issued to this resource by an external identity provider. |
| group_id          | core | string | The identifier for a group in the identity store.                                                                    |
| identity_store_id | core | string | The globally unique identifier for the identity store.                                                               |
| tags              | core | hstore |
