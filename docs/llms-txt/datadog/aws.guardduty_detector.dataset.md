# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.guardduty_detector.dataset.md

---
title: GuardDuty Detector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GuardDuty Detector
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.guardduty_detector.dataset/index.html
---

# GuardDuty Detector

GuardDuty Detector is the core resource in Amazon GuardDuty that represents an enabled instance of the threat detection service. It continuously monitors AWS accounts, workloads, and data for malicious or unauthorized activity. A detector must be created and enabled in each region where you want GuardDuty to analyze logs and generate findings.

```
aws.guardduty_detector
```

## Fields

| Title                        | ID   | Type   | Data Type                                                           | Description |
| ---------------------------- | ---- | ------ | ------------------------------------------------------------------- | ----------- |
| _key                         | core | string |
| account_id                   | core | string |
| coverage_statistics          | core | json   | Represents the count aggregated by the statusCode and resourceType. |
| created_at                   | core | string | The timestamp of when the detector was created.                     |
| data_sources                 | core | json   | Describes which data sources are enabled for the detector.          |
| features                     | core | json   | Describes the features that have been enabled for the detector.     |
| finding_publishing_frequency | core | string | The publishing frequency of the finding.                            |
| service_role                 | core | string | The GuardDuty service role.                                         |
| status                       | core | string | The detector status.                                                |
| tags                         | core | hstore |
| updated_at                   | core | string | The last-updated timestamp for the detector.                        |
