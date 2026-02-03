# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_policy.dataset.md

---
title: IoT Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Policy
---

# IoT Policy

An AWS IoT Policy defines permissions for devices, users, or applications interacting with the AWS IoT Core service. It specifies which IoT actions are allowed or denied and under what conditions, using a JSON-based policy document. These policies are attached to IoT identities such as certificates or Cognito identities, enabling secure communication and controlled access to IoT resources.

```
aws.iot_policy
```

## Fields

| Title              | ID   | Type       | Data Type                                    | Description |
| ------------------ | ---- | ---------- | -------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| creation_date      | core | timestamp  | The date the policy was created.             |
| default_version_id | core | string     | The default policy version ID.               |
| generation_id      | core | string     | The generation ID of the policy.             |
| last_modified_date | core | timestamp  | The date the policy was last modified.       |
| policy_arn         | core | string     | The policy ARN.                              |
| policy_document    | core | string     | The JSON document that describes the policy. |
| policy_name        | core | string     | The policy name.                             |
| tags               | core | hstore_csv |
