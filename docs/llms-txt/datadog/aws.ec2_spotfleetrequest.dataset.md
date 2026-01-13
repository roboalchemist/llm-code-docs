# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_spotfleetrequest.dataset.md

---
title: EC2 Spot Fleet Request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Spot Fleet Request
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_spotfleetrequest.dataset/index.html
---

# EC2 Spot Fleet Request

This table represents the EC2 Spot Fleet Request resource from Amazon Web Services.

```
aws.ec2_spotfleetrequest
```

## Fields

| Title                     | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| activity_status           | core | string    | The progress of the Spot Fleet request. If there is an error, the status is <code>error</code>. After all requests are placed, the status is <code>pending_fulfillment</code>. If the size of the fleet is equal to or greater than its target capacity, the status is <code>fulfilled</code>. If the size of the fleet is decreased, the status is <code>pending_termination</code> while Spot Instances are terminating. |
| create_time               | core | timestamp | The creation date and time of the request.                                                                                                                                                                                                                                                                                                                                                                                 |
| spot_fleet_request_config | core | json      | The configuration of the Spot Fleet request.                                                                                                                                                                                                                                                                                                                                                                               |
| spot_fleet_request_id     | core | string    | The ID of the Spot Fleet request.                                                                                                                                                                                                                                                                                                                                                                                          |
| spot_fleet_request_state  | core | string    | The state of the Spot Fleet request.                                                                                                                                                                                                                                                                                                                                                                                       |
| tags                      | core | hstore    |
