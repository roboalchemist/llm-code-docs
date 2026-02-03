# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.securityhub_finding_aggregator.dataset.md

---
title: Security Hub Finding Aggregator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Hub Finding Aggregator
---

# Security Hub Finding Aggregator

Security Hub Finding Aggregator in AWS collects and centralizes security findings from multiple regions into a single region. This allows you to manage and analyze findings across your AWS environment more efficiently, providing a unified view of security issues. It helps streamline compliance checks, threat detection, and response by reducing the need to review findings region by region.

```
aws.securityhub_finding_aggregator
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                | Description |
| -------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| finding_aggregation_region | core | string        | The home Region. Findings generated in linked Regions are replicated and sent to the home Region.                        |
| finding_aggregator_arn     | core | string        | The ARN of the finding aggregator.                                                                                       |
| region_linking_mode        | core | string        | Indicates whether to link all Regions, all Regions except for a list of excluded Regions, or a list of included Regions. |
| regions                    | core | array<string> | The list of excluded Regions or included Regions.                                                                        |
| tags                       | core | hstore_csv    |
