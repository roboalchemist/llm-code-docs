# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_input_security_group.dataset.md

---
title: Elemental MediaLive Input Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elemental MediaLive Input Security
  Group
---

# Elemental MediaLive Input Security Group

An Elemental MediaLive Input Security Group in AWS defines a set of rules that control which IP addresses are allowed to push live video content into a MediaLive input. It acts as a virtual firewall for live video sources, ensuring that only trusted IP ranges can send streams to your channel inputs. This helps secure live video workflows by preventing unauthorized access to your broadcast streams.

```
aws.medialive_input_security_group
```

## Fields

| Title           | ID   | Type          | Data Type                                                     | Description |
| --------------- | ---- | ------------- | ------------------------------------------------------------- | ----------- |
| _key            | core | string        |
| account_id      | core | string        |
| arn             | core | string        | Unique ARN of Input Security Group                            |
| id              | core | string        | The Id of the Input Security Group                            |
| inputs          | core | array<string> | The list of inputs currently using this Input Security Group. |
| state           | core | string        | The current state of the Input Security Group.                |
| tags            | core | hstore_csv    |
| whitelist_rules | core | json          | Whitelist rules and their sync status                         |
