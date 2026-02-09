# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_reservation.dataset.md

---
title: Elemental MediaLive Reservation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Reservation
---

# Elemental MediaLive Reservation

Elemental MediaLive Reservation in AWS represents a commitment to use specific MediaLive resources, such as encoding capacity, at a discounted rate compared to on-demand pricing. Reservations help reduce costs for predictable, long-term live video streaming workloads by securing dedicated capacity for channels or inputs.

```
aws.medialive_reservation
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                             | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567'           |
| count                  | core | int64      | Number of reserved resources                                                                          |
| currency_code          | core | string     | Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'                            |
| duration               | core | int64      | Lease duration, e.g. '12'                                                                             |
| duration_units         | core | string     | Units for duration, e.g. 'MONTHS'                                                                     |
| end                    | core | string     | Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00'                      |
| fixed_price            | core | float64    | One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering                      |
| name                   | core | string     | User specified reservation name                                                                       |
| offering_description   | core | string     | Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)' |
| offering_id            | core | string     | Unique offering ID, e.g. '87654321'                                                                   |
| offering_type          | core | string     | Offering type, e.g. 'NO_UPFRONT'                                                                      |
| region                 | core | string     | AWS region, e.g. 'us-west-2'                                                                          |
| renewal_settings       | core | json       | Renewal settings for the reservation                                                                  |
| reservation_id         | core | string     | Unique reservation ID, e.g. '1234567'                                                                 |
| resource_specification | core | json       | Resource configuration details                                                                        |
| start                  | core | string     | Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00'                    |
| state                  | core | string     | Current state of reservation, e.g. 'ACTIVE'                                                           |
| tags                   | core | hstore_csv |
| usage_price            | core | float64    | Recurring usage charge for each reserved resource, e.g. '157.0'                                       |
