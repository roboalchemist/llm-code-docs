# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_offering.dataset.md

---
title: Elemental MediaLive Offering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Offering
---

# Elemental MediaLive Offering

Elemental MediaLive Offering in AWS represents a reserved capacity purchase option for MediaLive channels. It allows customers to commit to a specific amount of channel capacity for a defined term, typically at a discounted rate compared to on-demand pricing. This helps optimize costs for predictable, long-term live video streaming workloads.

```
aws.medialive_offering
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                             | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321'                |
| currency_code          | core | string     | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'                            |
| duration               | core | int64      | Lease duration, e.g. '12'                                                                             |
| duration_units         | core | string     | Units for duration, e.g. 'MONTHS'                                                                     |
| fixed_price            | core | float64    | One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering                      |
| offering_description   | core | string     | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offering_id            | core | string     | Unique offering ID, e.g. '87654321'                                                                   |
| offering_type          | core | string     | Offering type, e.g. 'NO_UPFRONT'                                                                      |
| region                 | core | string     | AWS region, e.g. 'us-west-2'                                                                          |
| resource_specification | core | json       | Resource configuration details                                                                        |
| tags                   | core | hstore_csv |
| usage_price            | core | float64    | Recurring usage charge for each reserved resource, e.g. '157.0'                                       |
