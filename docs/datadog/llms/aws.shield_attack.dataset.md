# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.shield_attack.dataset.md

---
title: Shield Attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Shield Attack
---

# Shield Attack

AWS Shield Attack represents details about a Distributed Denial of Service (DDoS) attack detected by AWS Shield. It provides information such as the attack's start and end time, vectors used, and resources targeted. This helps users analyze the nature and impact of the attack for better mitigation and response.

```
aws.shield_attack
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                  | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| attack_counters   | core | json       | List of counters that describe the attack for the specified time period.                                                                                                                                                                                                   |
| attack_id         | core | string     | The unique identifier (ID) of the attack.                                                                                                                                                                                                                                  |
| attack_properties | core | json       | The array of objects that provide details of the Shield event. For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see Shield metrics and alarms in the WAF Developer Guide. |
| end_time          | core | timestamp  | The time the attack ended, in Unix time in seconds.                                                                                                                                                                                                                        |
| mitigations       | core | json       | List of mitigation actions taken for the attack.                                                                                                                                                                                                                           |
| resource_arn      | core | string     | The ARN (Amazon Resource Name) of the resource that was attacked.                                                                                                                                                                                                          |
| start_time        | core | timestamp  | The time the attack started, in Unix time in seconds.                                                                                                                                                                                                                      |
| sub_resources     | core | json       | If applicable, additional detail about the resource being attacked, for example, IP address or URL.                                                                                                                                                                        |
| tags              | core | hstore_csv |
