# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_rule.dataset.md

---
title: Fraud Detector Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Rule
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_rule.dataset/index.html
---

# Fraud Detector Rule

This table represents the Fraud Detector Rule resource from Amazon Web Services.

```
aws.frauddetector_rule
```

## Fields

| Title             | ID   | Type          | Data Type                                        | Description |
| ----------------- | ---- | ------------- | ------------------------------------------------ | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| arn               | core | string        | The rule ARN.                                    |
| created_time      | core | string        | The timestamp of when the rule was created.      |
| description       | core | string        | The rule description.                            |
| detector_id       | core | string        | The detector for which the rule is associated.   |
| expression        | core | string        | The rule expression.                             |
| language          | core | string        | The rule language.                               |
| last_updated_time | core | string        | Timestamp of the last time the rule was updated. |
| outcomes          | core | array<string> | The rule outcomes.                               |
| rule_id           | core | string        | The rule ID.                                     |
| rule_version      | core | string        | The rule version.                                |
| tags              | core | hstore        |
