# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_hostreservation.dataset.md

---
title: EC2 Host Reservation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Host Reservation
---

# EC2 Host Reservation

This table represents the EC2 Host Reservation resource from Amazon Web Services.

```
aws.ec2_hostreservation
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                              | Description |
| ------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| count               | core | int64         | The number of Dedicated Hosts the reservation is associated with.                                                                                                      |
| currency_code       | core | string        | The currency in which the <code>upfrontPrice</code> and <code>hourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>. |
| duration            | core | int64         | The length of the reservation's term, specified in seconds. Can be <code>31536000 (1 year)</code> | <code>94608000 (3 years)</code>.                                   |
| end                 | core | timestamp     | The date and time that the reservation ends.                                                                                                                           |
| host_id_set         | core | array<string> | The IDs of the Dedicated Hosts associated with the reservation.                                                                                                        |
| host_reservation_id | core | string        | The ID of the reservation that specifies the associated Dedicated Hosts.                                                                                               |
| hourly_price        | core | string        | The hourly price of the reservation.                                                                                                                                   |
| instance_family     | core | string        | The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation.     |
| offering_id         | core | string        | The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it.                                                           |
| payment_option      | core | string        | The payment option selected for this reservation.                                                                                                                      |
| start               | core | timestamp     | The date and time that the reservation started.                                                                                                                        |
| state               | core | string        | The state of the reservation.                                                                                                                                          |
| tags                | core | hstore_csv    |
| upfront_price       | core | string        | The upfront price of the reservation.                                                                                                                                  |
