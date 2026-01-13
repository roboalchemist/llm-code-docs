# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.identitystore_group_membership.dataset.md

---
title: Identity Store Group Membership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Store Group Membership
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.identitystore_group_membership.dataset/index.html
---

# Identity Store Group Membership

This table represents the Identity Store Group Membership resource from Amazon Web Services.

```
aws.identitystore_group_membership
```

## Fields

| Title             | ID   | Type   | Data Type                                                                                                                                                                               | Description |
| ----------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string |
| account_id        | core | string |
| group_id          | core | string | The identifier for a group in the identity store.                                                                                                                                       |
| identity_store_id | core | string | The globally unique identifier for the identity store.                                                                                                                                  |
| member_id         | core | json   | An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group. |
| membership_id     | core | string | The identifier for a <code>GroupMembership</code> object in an identity store.                                                                                                          |
| tags              | core | hstore |
