# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.verifiedpermissions_policy.dataset.md

---
title: Verified Permissions Policy Item
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Verified Permissions Policy Item
---

# Verified Permissions Policy Item

An AWS Verified Permissions Policy Item represents an individual policy statement within the Verified Permissions service. It defines rules that determine whether specific actions are allowed or denied for given principals on particular resources. These policy items are used to build fine-grained, centralized access control decisions, enabling applications to enforce consistent authorization logic across services and resources.

```
aws.verifiedpermissions_policy
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                               | Description |
| ----------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| actions           | core | json       | The action that a policy permits or forbids. For example, {"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}. |
| created_date      | core | timestamp  | The date and time the policy was created.                                                                                                                                                               |
| definition        | core | json       | The policy definition of an item in the list of policies returned.                                                                                                                                      |
| effect            | core | string     | The effect of the decision that a policy returns to an authorization request. For example, "effect": "Permit".                                                                                          |
| last_updated_date | core | timestamp  | The date and time the policy was most recently updated.                                                                                                                                                 |
| policy_id         | core | string     | The identifier of the policy you want information about.                                                                                                                                                |
| policy_store_id   | core | string     | The identifier of the policy store where the policy you want information about is stored.                                                                                                               |
| policy_type       | core | string     | The type of the policy. This is one of the following values: STATIC TEMPLATE_LINKED                                                                                                                     |
| principal         | core | json       | The principal associated with the policy.                                                                                                                                                               |
| resource          | core | json       | The resource associated with the policy.                                                                                                                                                                |
| tags              | core | hstore_csv |
